class Figure():
    def __init__(self, kind, y, x, color):
        self.kind = kind
        self.x = x
        self.y = y
        self.color = color

    def to_json(self):
        return {
            'x': self.x,
            'y': self.y,
            'color': self.color,
            'kind': self.kind,
        }