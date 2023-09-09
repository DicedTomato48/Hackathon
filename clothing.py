class Clothing:
    
    # need to remove optional argument
    def __init__(self, colour=None, clothing_type=None):
        self.colour = colour
        self.clothing_type = clothing_type
