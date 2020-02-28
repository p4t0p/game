class Figure():
    def __init__(self, kind, x, y, color):
        self.kind = kind
        self.x = x
        self.y = y
        self.color = color

    def to_dict(self):
        return {
            'x': self.x,
            'y': self.y,
            'color': self.color,
            'kind': self.kind,
        }

