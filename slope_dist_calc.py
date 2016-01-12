from __future__ import division

class Line(object):

    def __init__(self,coor1,coor2):
        self.x1=coor1[1]
        self.x2=coor2[1]
        self.y1=coor1[0]
        self.y2=coor2[0]
    
    def distance(self):
        from math import sqrt
        return sqrt((self.x2-self.x1)**2 + (self.y2-self.y1)**2)
    
    def slope(self):
        return (self.x1-self.x2)/(self.y1-self.y2)
        
def start():

    x1 = int(raw_input("Please enter the x coordinate of the first point:  "))
    y1 = int(raw_input("Please enter the y coordinate of the first point:  "))
    x2 = int(raw_input("Please enter the x coordinate of the second point:  "))
    y2 = int(raw_input("Please enter the y coordinate of the second point:  "))
    
    li = Line([x1,y1],[x2,y2])
    print "Distance: ", li.distance()
    print "Slope: ", li.slope()
    
start()