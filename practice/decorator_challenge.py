from flask import Flask

app = Flask(__name__)

def make_bold(func):
    def inner(*args, **kwargs):
        output = func(*args, **kwargs)
        return f'<b>{output}</b>'
    return inner

def make_emphasis(func):
    def inner(*args, **kwargs):
        output = func(*args, **kwargs)
        return f'<em>{output}</em>'
    return inner

def make_underline(func):
    def inner(*args, **kwargs):
        output = func(*args, **kwargs)
        return f'<u>{output}</u>'
    return inner

def make_dynamic(func):
    def inner(name , tag):
        output = func(name)
        return f'<{tag}>{output}</{tag}>'
    return inner

@app.route('/')
@make_bold
@make_emphasis
@make_underline
def home():
    return 'Hii'

@app.route('/user/<name>/<type_en>')
def greet(name,type_en):
    return f'Hello {name}!'


if __name__ == '__main__':
    app.run(debug=True)
