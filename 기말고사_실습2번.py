class Point:
    x=0
    y=0
    def __init__(self,X,Y):
        self.x = X;
        self.y = Y;
    def distance(self,other):
        distance = ((self.x-other.x)**2 + (self.y-other.y)**2)**(1/2)
        return distance
    def __add__(self,other):
        self.x += other.x;
        self.y += other.y;
        return self.x,self.y

p1 = Point(10,10)
p2 = Point(40,50)

print(p1.distance(p2))
print(p1+p2);
