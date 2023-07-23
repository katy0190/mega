from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/login')
def login():
    url = 'https://nid.naver.com/oauth2.0/authorize?client_id=LbhUlOMfKMr22x1jk0Yw&redirect_uri=http://127.0.0.1:3000/success&response_type=code'
    return redirect(url)



if __name__ == "__main__":
    app.run(port=3000)

