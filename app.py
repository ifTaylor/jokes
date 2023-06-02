from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)
jokes = []

def fetch_joke():
    url = "https://official-joke-api.appspot.com/jokes/random"
    response = requests.get(url)
    joke = response.json()
    return joke["setup"], joke["punchline"]

@app.route('/')
def index():
    return render_template('index.html', jokes=jokes)

@app.route('/joke', methods=['POST'])
def get_joke():
    setup, punchline = fetch_joke()
    joke = {'setup': setup, 'punchline': punchline, 'revealed': False}
    jokes.append(joke)
    return jsonify(joke)

if __name__ == '__main__':
    app.run(debug=True)
