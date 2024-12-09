from flask import Flask
import random

random_number = random.randint(1, 9)

app = Flask(__name__)

gess_number = 0
@app.route('/')
def index():
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">')


@app.route('/<int:number>')
def verification(number):
    if number < random_number:
        return ('<h1>Its so low!!</h1>'
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">')
    elif number > random_number:
        return ('<h1>Its so high!!</h1>'
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">')
    elif number == random_number:
        return ('<h1>You find me!!</h1>'
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">')
    else:
        return "<h1>number out of the range</h1>"



if __name__ == "__main__":
    app.run(debug=True)