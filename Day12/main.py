from flask import Flask, render_template, request
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import Movie

uri = "mongodb+srv://xodus0118:비밀번호@xodus0118.nr0cb6s.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['test']
collection = db['CGV']


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/abc')
def abc():
    return render_template('abc.html')

@app.route('/show')
def show():
    return render_template('show.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['movie_name']
    location = request.form['location']
    time = request.form['time']
    rank = request.form['rank']
    newMovie = Movie.Movie(name, location, time, rank)
    collection.insert_one(newMovie.__dict__)
    print(f"{name} {location} {time} {rank} 가져옴")
    return f'영화 이름: {name}'


@app.route('/find', methods=['POST'])
def find():
    name = request.form['movie_name']
    data = collection.find_one({'name':name})
    print(data['name'])
    return render_template('show.html', name=data['name'], location=data['location'], time=data['time'], rank=data['rank'])
    # return f'{data}'



if __name__== "__main__":
    app.run(port=3000)

