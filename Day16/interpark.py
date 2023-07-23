from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/abc', methods=['POST'])
def abc():
    URL = request.form['URL']
    response = requests.post(URL, json={
        "encryptedParamString": "RKRXsFwP3HpLSncgnf4aJ9Ij0dP+gakW5qBh0ZDSTZDGrb6r4EFWMbZczFZBECtjV2ALOfU4zxY/T4k2QYEtsLlq6/e99+2nBduy8OSa+GFgZyRAK7dzoZJHh6uLj2ssNtfVpW+Vl8aIy4k0Iu1aD5Q/qpLEplrkR4KBNuOEoGVO2fEHO5ARMBRS1u/+z14hrnPULfs4fVxYD/bV+IyF1lQRbgQAP7iU0+3uc1fc3f7ygX5dfn9rwfucpuDMw2S5xgpAw8ayj88+ule02j/H3hxHA/mihF53nlR+t5+XWNzYbS+PkEz+SuFsAXU0kN1Zq16Q5EPUpgO80RCyrNU7TQ==",
        "c1": "3",
        "c2": "2",
        "c3": "1",
        "c4": "6"
    })
    data = response.json()
    print(data['data']['availableSlotSize'])
    return render_template('home.html')

if __name__ == "__main__":
    app.run(port=3000)

