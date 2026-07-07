from flask import Flask, render_template
from random import randint

app = Flask(__name__)
number = randint(0, 9)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/<int:num>')
def about(num : int):
    if num == number:
        return render_template('winner.html')
    elif num > number:
        return render_template('upper.html')
    elif num < number:
        return render_template('lower.html')
    else:
        return None

if __name__ == '__main__':
    app.run(debug=True)