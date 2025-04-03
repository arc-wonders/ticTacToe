@app.route('/move', methods=['POST'])
def move():
    data = request.get_json()
    board = data["board"]
    row, col = get_best_move(board)
    return jsonify({"row": row, "col": col})