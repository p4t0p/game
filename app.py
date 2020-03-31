from flask import Flask, escape, request, jsonify
from flask_cors import CORS

import traceback

from chess.figure import Figure
from chess.game import Game

app = Flask(__name__)

CORS(app)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/game', methods=['POST'])
def game():
    """
        New Game
    """

    new_game = Game()
    return jsonify(new_game.to_json())


@app.route('/move', methods=['POST'])
def move():
    """
        Player Move
    """

    try:
        game = Game(request.json['field'], request.json['turn'], request.json['eaten'])
        game.move(request.json['move'])
        
        return jsonify(game.to_json())
    except Exception as e:
        # traceback.print_exception(e)
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(port=8080,debug=True)
