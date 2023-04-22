import requests
from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_meme')
def get_meme():
    response = requests.get('https://api.imgflip.com/get_memes')
    memes = response.json()['data']['memes']
    meme = memes[random.randint(0, len(memes)-1)]
    return jsonify({'url': meme['url'], 'caption': meme['name']})

if __name__ == '__main__':
    app.run(debug=True)
