from flask import Flask
from decorators import h1_tag
app = Flask(__name__)
name2 = ''
@app.route('/')
@h1_tag
def hello():
    return "Hello World"

@app.route('/bye')
def bye():
    return "Bye baka"

@app.route("/username/<name>")
def helo(name):
    return f"Hello {name}"


if __name__ == "__main__":
    app.run(debug=True)