from flask import Flask, request, jsonify
from faker import Faker
import requests

app = Flask(__name__)
fake = Faker()

@app.route('/requirements')
def requirements():
    file = open("requirements.txt")
    return file.read()

@app.route('/users_generate')
def users_generate():
    try:

        count = int(request.args.get('count', 100))
        people = [{'name': fake.name(), 'email': fake.email()} for i in range(count)]

        return jsonify(people)

    except ValueError:
        return jsonify({'error': 'Некоректне значення параметра "count"'}), 400

@app.route('/mean')
def mean():
    file = open("hw.csv")
    return file.read()

@app.route('/space')
def space():
    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)
    data = response.json()
    number = data["number"]
    return str(number)

if __name__ == '__main__':
    app.run(debug=True)