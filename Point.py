'''
use this class as an object for each individual point on a Chart object
x = x value
y = y value (usually a price value)

'''

class Point:
    def __init__(self, selfX = 0, selfY = 0):
        self.x = selfX #x coordinate of the point. defaults to 0
        self.y = selfY #y coordinate of the point. defaults to 0. generally used as a "Value" component. (ex. price)