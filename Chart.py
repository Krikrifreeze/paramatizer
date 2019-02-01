'''
use the class for each specific chart. (ex. 1 chart for ticker symbol, 1 chart for indicator, etc)


Chart(pointList)
    creates a chart Object.
    pointList = an array of points.

'''

from Point import *

class Chart:
    def __init__(self, pL = None):
        self.pointList = pL
    def getSize(self):
        return len(self.pointList)
    def getPoint(self,index):
        return self.pointList[index]

chart = Chart([Point(),Point(2,3),Point(2)])

for i in range( chart.getSize() ):
    print(chart.getPoint(i).y)