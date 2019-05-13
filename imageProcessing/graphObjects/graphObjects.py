class Node:
    """
       Used to compute the undirectionnal weighted graphs
       Contains:
       x : the abcisse of the pixel in the picture
       y : the ordonnée of the pixel in the picture
       magnitude : the approximation of the gradient magnitude of the pixel
       direction : the approximation of the gradient direction of the pixel
    """
    def __init__(self, x, y, magnitude, direction):
        self.x = x
        self.y = y
        self.magnitude = magnitude
        self.direction = direction
        self.component_index = 0

    def __repr__(self):
        return "(x:" + str(self.x) +\
               ", y:" + str(self.y) +\
               ")" + ", magnitude: ," + str(self.magnitude) +\
               "direction: " + str(self.direction)


