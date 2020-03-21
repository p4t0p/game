from .figure import Figure

def pawn_move(field, figure, _to):
    is_straight = figure.x == _to['x']
    move_to_fig = field[_to['y']][_to['x']]
    eaten = []

    v_diff = _to['y'] - figure.y # разница вертикальная
    h_diff = _to['x'] - figure.x # разница горизонтальная

    step_one, step_two = (1, 2) if figure.color == 'black' else (-1, -2)

    figure_after_move = Figure('pawn', _to['y'], _to['x'], figure.color)
    if is_straight:
        if move_to_fig is not None:
            raise Exception('Field is not empty')

        if ((figure.y == 1 or figure.y == 6) and v_diff == step_two) or v_diff == step_one:
            field[_to['y']][_to['x']] = figure_after_move
            field[figure.y][figure.x] = None

            # Если пешка дошла до края, то превращаем ее в королеву
            if _to['y'] in [0, 7]:
                figure = Figure('queen', _to['y'], _to['x'], figure.color)
        else:
            raise Exception('Invalid move')
    else:
        if move_to_fig is None or move_to_fig.color == figure.color:
            raise Exception('Invalid move')

        if v_diff == 1 and abs(h_diff) == 1:
            eaten = move_to_fig
            field[_to['y']][_to['x']] = figure_after_move
            field[figure.y][figure.x] = None

    return field, [eaten]

def rook_move(field, figure, _to):
    is_straight = figure.x == _to['x']
    is_vertical = fugure.y == to['y']
    eaten = []

    v_diff = _to['y'] - figure.y 
    h_diff = _to['x'] - figure.x 

    if is_straight:
        if move_to_fig is not None :
            raise Exception('Field is not empty')

    if is_vertical:
        if move_to_fig is not None:
            raise Exception('Field is not empty')

    pass

def knight_move(field, figure, _to):
    is_vertical = figure.y == to['y']
    is_horisonta = figure.x == to['x']
    if 
def bishop_move(field, figure, _to):
    pass

def queen_move(field, figure, _to):
    pass

def king_move(field, figure, _to):
    pass

moves = {
    'pawn': pawn_move,
    'rook': rook_move,
    'knight': knight_move,
    'bishop': bishop_move,
    'queen': queen_move,
    'king': king_move,
}