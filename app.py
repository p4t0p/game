from flask import Flask, escape, request, jsonify
from chess.figure import Figure
from chess.game import Game

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/game', methods=['POST'])
def game():
    """
        Создание новой игры
    """
    new_game = Game()
    return jsonify(new_game.to_json())


@app.route('/move', methods=['POST'])
def move():
    """
        Сделать шаг игроком
    """

    return jsonify({})


if __name__ == '__main__':
    app.run(port=8080,debug=True)
