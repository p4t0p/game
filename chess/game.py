from .figure import Figure

class Game():
    def __init__(self):
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
        
        field[0][3] = Figure('queen', 0, 3, 'black')
        field[0][4] = Figure('king', 0, 4, 'black')
        
                             
        field[7][0] = Figure('rook', 7, 0, 'white')
        field[7][7] = Figure('rook', 7, 7, 'white')

        field[7][1] = Figure('knight',7,1,'white')
        field[7][6] = Figure('knight',7,6,'white')
        
        field[7][2] = Figure('bishop',7,2,'white')
        field[7][5] = Figure('bishop',7,5,'white')
        field[7][3] = Figure('queen',7,3,'white')
        field[7][4] = Figure('king',7,4,'white')
                
        
        self.field = field
        self.turn = 'white'
        self.eaten = []

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
        
        return {'field':d, 'eaten':self.eaten, 'turn':self.turn}