from .figure import Figure
from .moves import moves


def is_check(field, color):
    field = field.copy()
    
    king_coords = {'x': None, 'y': None}
    opposite_figures = []
    
    for x in range(8):
        for y in range(8):
            fig = field[y][x]

            if fig != None and fig.color != color:
                opposite_figures.append(fig)

            if fig != None and fig.kind == 'king' and fig.color == color:
                king_coords['x'] = x
                king_coords['y'] = y
                
    for fig in opposite_figures:
        figure_move = moves.get(fig.kind)
        
        try:
            figure_move(field, fig, king_coords)
            return True
        except:
            pass
        
    return False

def create_new_game_field():
    field = [
        [None for i in range(8)] for j in range(8)
    ]

    field[1] = [Figure('pawn', 1, i, 'black') for i in range(8)]
    field[6] = [Figure('pawn', 6, i, 'white') for i in range(8)]

    field[0][0] = Figure('rook', 0, 0, 'black')
    field[0][7] = Figure('rook', 0, 7, 'black')

    field[0][1] = Figure('knight', 0, 1, 'black')
    field[0][6] = Figure('knight', 0, 6, 'black')

    field[0][5] = Figure('bishop', 0, 5, 'black')
    field[0][2] = Figure('bishop', 0, 2, 'black')

    field[0][3] = Figure('king', 0, 3, 'black')
    field[0][4] = Figure('queen', 0, 4, 'black')

    field[7][0] = Figure('rook', 7, 0, 'white')
    field[7][7] = Figure('rook', 7, 7, 'white')

    field[7][1] = Figure('knight',7,1,'white')
    field[7][6] = Figure('knight',7,6,'white')

    field[7][2] = Figure('bishop',7,2,'white')
    field[7][5] = Figure('bishop',7,5,'white')

    field[7][3] = Figure('king',7,3,'white')
    field[7][4] = Figure('queen',7,4,'white')

    return field


class Game():
    def __init__(self, field = None, params = None):
        if field is None:
            self.field = create_new_game_field()
        else:
            f = []
            for i in field:
                row = []
                for cell in i:
                    if cell is None:
                        row.append(None)
                    else:
                        figure = Figure(cell['kind'], cell['y'], cell['x'], cell['color'], cell['is_moved'])
                        row.append(figure)
                f.append(row)
            self.field = f

        if params is None:
            self.params = {
                'turn': 'white',
                'eaten': [],
                'check': None,
            }
        else:
            self.params = params

    def move(self, move):
        from_x = move['from']['x']
        from_y = move['from']['y']

        figure = self.field[from_y][from_x]

        if figure is None:
            raise Exception("Not figure")
        if figure.color != self.params['turn']:
            raise Exception(f'Not {figure.color}\'s turn')


        figure_move = moves.get(figure.kind)
        field, new_eaten = figure_move(self.field, figure, move['to'])

        color = 'white' if self.params['turn'] == 'black' else 'black'
        self.field = field
        self.params = {
            'eaten': self.params['eaten'] + [f.to_json() for f in new_eaten],
            'turn': color,
            'check': is_check(self.field, color)
        }

    def to_json(self):
        d = []
        for i in self.field:
            row = []
            for j in i:
                if j is None:
                    row.append(j)
                else:
                    row.append(j.to_json())
            d.append(row)

        return {
            'field': d,
            'eaten': self.params['eaten'],
            'turn': self.params['turn'],
            'check': self.params['check'],
        }