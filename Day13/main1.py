from flask import Flask, render_template, request
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://xodus0118:@xodus0118.nr0cb6s.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['test']
collection = db['CGV']
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/subway')
def subway():
    return render_template('subway.html')

@app.route('/abc',methods=['POST'])
def abc():
    menu = request.form['menu']
    kcal = request.form['kcal']
    # ingredient = request.form['ingredient']
    collection.insert_one({"name": menu, "kcal": kcal})

    return f'너가 만든 메뉴: {menu} {kcal} '


if __name__ == "__main__":
    app.run(port=3000)
