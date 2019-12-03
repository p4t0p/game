from flask import Flask, escape, request, jsonify
from chess.figure import Figure
app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'
    
@app.route('/game')
def game():
    data = [
        {'figure': 'pawn', 'x': 1, 'y': 2, 'color': 'white'},
        {'figure': 'pawn', 'x': 1, 'y': 3, 'color': 'black'},
    ]
    pawn = Figure(2,2,'black')
    return jsonify(pawn.to_dict())
    
    




if __name__ == '__main__':
    app.run(port=8080,debug=True)
