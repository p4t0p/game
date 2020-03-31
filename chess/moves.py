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

        if abs(v_diff) == 1 and abs(h_diff) == 1:
            eaten = [move_to_fig]
            field[_to['y']][_to['x']] = figure_after_move
            field[figure.y][figure.x] = None
        else:
            raise Exception('Invalid move')

    return field, eaten

def rook_move(field, figure, _to):
    is_vertical = figure.x == _to['x']
    is_straight= figure.y == _to['y']
    eaten = []

    h_direction = 1 if _to['x'] - figure.x > 0 else -1
    v_direction = 1 if _to['y'] - figure.y > 0 else -1

    if is_straight:
        for x in range(figure.x + h_direction, _to['x'], h_direction):
            if field[figure.y][x] is not None:
                raise Exception('Invalid move')
    elif is_vertical:
        for y in range(figure.y + v_direction, _to['y'], v_direction):
            if field[y][figure.x] is not None:
                raise Exception('Invalid move')        
    else:
         raise Exception('Invalid move')
    
       
    move_to_fig = field[_to['y']][_to['x']]

    if move_to_fig is not None:
        if move_to_fig.color == figure.color:
            raise Exception('Invalid move')
        eaten = [move_to_fig]
    
    field[figure.y][figure.x] = None
    field[_to['y']][_to['x']] = Figure('rook', _to['y'], _to['x'], figure.color)
    
    return field, eaten


def knight_move(field, figure, _to):
    to_fig = field[_to['y']][_to['x']]

    eaten = []

    v_diff = abs(_to['y'] - figure.y) 
    h_diff = abs(_to['x'] - figure.x) 
    
                 
    is_valid = v_diff==2 and h_diff==1 or v_diff==1 and h_diff==2
    
    if not is_valid:
        raise Exception('Invalid move')
        
    if to_fig is not None:
        if to_fig.color == figure.color:
            raise Exception('Invalid move')
        eaten = [to_fig]
    
    field[figure.y][figure.x] = None
    field[_to['y']][_to['x']] = Figure('knight', _to['y'], _to['x'], figure.color)
    
    return field,eaten

def bishop_move(field, figure, _to):
    eaten = []
    to_fig = field[_to['y']][_to['x']]

    h_diff = _to['x'] - figure.x
    v_diff = _to['y'] - figure.y
    
    h_d = 1 if _to['x'] - figure.x > 0 else -1
    v_d = 1 if _to['y'] - figure.y > 0 else -1


    if abs(v_diff) - abs(h_diff) != 0:
        raise Exception('Inavalid move')

    if to_fig is not None:
        if to_fig.color == figure.color:
            raise Exception('Invalid move')
        eaten = [to_fig]
     
    h_range = range(figure.x + h_d, _to['x'], h_d) # [1,2,3] x - координаты
    v_range = range(figure.y + v_d, _to['y'], v_d) # [1,2,3] y - координаты
    
    
    index = 0;
    while index < len(h_range):
        x = h_range[index]
        y = v_range[index]
        if field[y][x] is not None:
            raise Exception('invalid move')
        index +=1
        
        
    
        
    field[figure.y][figure.x] = None
    field[_to['y']][_to['x']] = Figure('bishop', _to['y'], _to['x'], figure.color)
    
    return field,eaten
        
    pass

def queen_move(field, figure, _to):
    eaten = []
    to_fig = field[_to['y']][_to['x']]
    h_diff = _to['x'] - figure.x
    v_diff = _to['y'] - figure.y
   
    is_vertical = figure.x == _to['x']
    is_straight= figure.y == _to['y']
    is_diagonal = abs(v_diff) - abs(h_diff) == 0
    

    if is_vertical or is_straight or is_diagonal:
        h_d = 1 if _to['x'] - figure.x > 0 else -1
        v_d = 1 if _to['y'] - figure.y > 0 else -1
        h_range = range(figure.x + h_d, _to['x'], h_d)
        v_range = range(figure.y + v_d, _to['y'], v_d) 

        index = 0;
        while index < max(len(h_range), len(v_range)):
            x = figure.x if len(h_range) == 0 else h_range[index]
            y = figure.y if len(v_range) == 0 else v_range[index]
            if field[y][x] is not None:
                raise Exception ('invalid move')
            index +=1
    else:
        raise Exception('Invalid move')
        
    if to_fig is not None:
        if to_fig.color == figure.color:
            raise Exception('Invalid move')
        eaten = [to_fig]
        
    field[figure.y][figure.x] = None
    field[_to['y']][_to['x']] = Figure('queen', _to['y'], _to['x'], figure.color)
    
    return field,eaten

def king_move(field, figure, _to):
    is_horizontal = figure.x == _to['x']
    is_vertical = figure.y == _to['y']
    to_fig = field[_to['y']][_to['x']]
    eaten = []
    
    v_diff = abs(_to['y'] - figure.y) 
    h_diff = abs(_to['x'] - figure.x)
    
    if not (v_diff <=1 and h_diff <=1):
        raise Exception('Invalid move')

    if to_fig is not None:
        if to_fig.color == figure.color:
            raise Exception('Invalid move')
        eaten = [to_fig]
    
    field[figure.y][figure.x] = None
    field[_to['y']][_to['x']] = Figure('king', _to['y'], _to['x'], figure.color)
    
    return field,eaten

moves = {
    'pawn': pawn_move,
    'rook': rook_move,
    'knight': knight_move,
    'bishop': bishop_move,
    'queen': queen_move,
    'king': king_move,
}