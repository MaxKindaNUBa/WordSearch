from flask import Flask, request, jsonify
from wordSearchGen import Puzzle

app = Flask(__name__)


@app.route("/")
def home():
    return "Home"


@app.route("/get-puzzle/")
def get_user():
    def get_boolean(str):
        if str=="true":
            return True
        elif str=="false":
            return False

    data = {}

    rows = int(request.args.get("rows"))
    cols = int(request.args.get("cols"))
    words = request.args.get("words")
    words = words.split(',')
    inv = get_boolean(request.args.get("inv"))
    spaces = get_boolean(request.args.get("spaces"))
    chars = get_boolean(request.args.get("chars"))
    mixCase = get_boolean(request.args.get("mixCase"))
    answers = get_boolean(request.args.get("answers"))

    data["rows"]=rows
    data["cols"]=cols
    data["words"] = words
    data["invExists"] = inv
    data["spaces"] = spaces
    data["chars"] = chars
    data["mixCase"] = mixCase
    data["answers"] = answers

    print(data)
    puzzle = Puzzle(rows,cols,words,invExist=inv,emptySpaces=spaces,crazyChars=chars,mixCasing=mixCase,answersOnly=answers)
    puzzle.generate_grid()
    data["puzzle"] = puzzle.grid

    return jsonify(data),200


if __name__ == "__main__":
    app.run(debug=True,port=7853)



