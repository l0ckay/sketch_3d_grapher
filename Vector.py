class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        # Add two vectors together
        return Vector2(self.x + other.x, self.y+other.y)
    
    def __mul__(self,scalar):
        # Multiply a vector by a scalar
        return Vector2(self.x*scalar, self.y*scalar)
    
    def __rmul__(self, other):
        # Multiply a scalar by a vector
        return self.__mul__(other)
    
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)


    
class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        # Add two vectors together
        return Vector3(self.x + other.x, self.y+other.y, self.z+other.z)
    
    def __mul__(self,scalar):
        # Multiply a vector by a scalar
        return Vector3(self.x*scalar, self.y*scalar, self.z*scalar)
    
    def __rmul__(self, other):
        # Multiply a scalar by a vector
        return self.__mul__(other)
    
    def __str__(self):
        return "({0},{1},{2})".format(self.x,self.y,self.z)

    def toScreen(self, x_proj, y_proj, z_proj):
        return self.x * x_proj + self.y * y_proj + self.z * z_proj
    
    def drawLine(self, other, x_proj, y_proj, z_proj):
        p1 = self.toScreen(x_proj, y_proj, z_proj)
        p2 = other.toScreen(x_proj, y_proj, z_proj)
        line(p1.x,p1.y,p2.x,p2.y)
