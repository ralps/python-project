from math import sqrt
#class definition

class Point:
    def __init__(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y
    def __str__(self):
        return"({},{})" .format(self.x, self.y)   
    def distance_from_origin(self):
        d = sqrt(self.x ** 2 + self.y ** 2)
        return d
    def __eq__(self, p):
        return self.x == p.x and self.y == p.y
    def __add__(self, q):
        r = Point(self.x + q.x, self.y + q.y)
        return r
    def __sub__(self, q):
        r = Point(self.x - q.x, self.y - q.y)
        return r
    
        
"__name__" == "__main__"

#object instantiation
p = Point()
print("p.x={}, p.y={}".format(p.x, p.y))
print("p.x={}".format (p))

p = Point(x=3.4, y=5.6)
print("p.x={}, p.y={}".format(p.x, p.y))
print("p.x={}".format (p))
a = Point(3,4)
b = Point(3,4)
print (a + b)
print (a-b)

p = Point(3,4)
q = Point(1,2)
print (p+q)
print (p-q)
