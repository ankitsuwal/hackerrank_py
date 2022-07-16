from cgi import print_directory


class MyPoint():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return "({0}, {1})".format(self.x, self.y)
    
    # overloading + oprator
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return MyPoint(x, y)
    
    # overloading < operator
    def __lt__(self, other): 
        selfmag = (self.x ** 2) + (self.y ** 2)
        othermag = (other.x ** 2) + (other.y ** 2)
        return selfmag < othermag
    
p1 = MyPoint(1,2)
p2 = MyPoint(4,5)
p3 = MyPoint(9, 8)
print(p1)
print(p2)        
print(p3)
print()
print(p1 + p2)
print(p3 < p2)