'''
use the class for each specific chart. (ex. 1 chart for ticker symbol, 1 chart for indicator, etc)

CONSIDER MAKING A POINT OBJECT.

Chart(xVals,yVals)

    xVals = list of x values for each coordinate (please sort before)
    yVals = list of y values for each coordinate (please sort before)

    ex. aapl = plotData([1,2,3],[4,5,6])

chart.getSinglePoint(ID)
    returns a tuple with an x & y that can be used for plotting on charts

    ID = the data number. (first point, second point, etc)

chart.getAllPoints()
    returns a list of tuples of every x and y in the object.

chart.size returns the number of "points" in the object.
    ex. sma = plotdata([1,2,3],[4,5,6])
    sma.size = 3

chart.changeVal(axis,ID,newVal)
    changes a value. ya know
'''

#import Point

class Chart:
    def __init__(self, xVals, yVals): #the lengths of xVals and yVals must be the same
        self.vals = [] #a 2D array that stores MUTABLE x's and y's
        self.vals.append(xVals) #add the x value array
        self.vals.append(yVals) #add the y value array

        self.size = len(self.vals[0]) #the number of actual x&y pairs in the object.

    def getSinglePoint(self,ID): #returns a single tuple of the corresponding x and y's.
        return (self.vals[0][ID], self.vals[1][ID])

    def getAllPoints(self): #returns a list of tuples for every x and y.
        coords = []
        for i in range(self.size): #append to a local blank list every tuple of x&y
            coords.append(self.getSinglePoint(i))
        return coords

    def changeVal(self,axis,ID,newVal): #changes a value in the 2D Array
        if axis == 'x': self.vals[0][ID] = newVal
        elif axis == 'y': self.vals[1][ID] = newVal


datapoint = Chart([1,2,3],[4,5,6])

print(datapoint.getSinglePoint(0))
print("changing...")
datapoint.changeVal('y',0,1)
print(datapoint.getSinglePoint(0))
print("heres all points")
print(datapoint.getAllPoints())