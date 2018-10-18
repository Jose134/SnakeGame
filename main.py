from graphics import *

framerate = 10
scl = 20 #Size of the grid's square
gridSize = 32 #Amount of squares in the grid
win = GraphWin("Snake Game", gridSize*scl + 1, gridSize*scl + 1)

def update ():
    while True:
        draw()
        time.sleep(1/framerate)


def draw ():
    for i in range(gridSize):
        for j in range(gridSize):
            gridSquare = Rectangle(Point(i*scl, j*scl), Point(i*scl + scl, j*scl + scl))
            gridSquare.setOutline("white")
            gridSquare.setFill("black")
            gridSquare.draw(win)
    

update()
