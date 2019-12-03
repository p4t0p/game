class Figure():
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
    
    def to_dict(self):
        return {'x':self.x, 'y':self.y ,'color':self.color}
        
