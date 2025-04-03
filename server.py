from flask import Flask, request, jsonify, render_template
from ai import get_best_move

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/move', methods=['POST'])
def move():
    data = request.get_json()
    board = data["board"]
    row, col = get_best_move(board)
    return jsonify({"row": row, "col": col})



if __name__ == '__main__':
    app.run(debug=True)
