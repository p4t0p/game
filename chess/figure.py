class Figure():
    def __init__(self, kind, y, x, color, is_moved = False):
        self.kind = kind
        self.x = x
        self.y = y
        self.color = color
        self.is_moved = is_moved

    def to_json(self):
        return {
            'x': self.x,
            'y': self.y,
            'color': self.color,
            'kind': self.kind,
            'is_moved': self.is_moved,
        }