from flask import Flask
from flask import request
from closest import Closest

app = Flask(__name__)


@app.route("/")
def closest():
    search = request.args.get('search')
    min_length = 999999
    word = ''

    closest_inst = Closest()
    with open("random.txt", "r") as file:
        lines = file.readlines()
        for text in lines:
            distance = closest_inst.levenshtein_distance(search, text)
            if min_length > distance:
                word = text
                min_length = distance

    print min_length
    print word

    return word


@app.route("/generate")
def generate():
    closest_inst = Closest()
    closest_inst.generate_random_words()

if __name__ == '__main__':
    app.run(debug=True)
