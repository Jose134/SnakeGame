from graphics import *

framerate = 10
scl = 20 #Size of the grid's square
gridSize = 32 #Amount of squares in the grid
win = GraphWin("Snake Game", gridSize*scl + 1, gridSize*scl + 1)

class Snake:
    def __init__ (self, x, y, length):
        self.x = x
        self.y = y
        self.tail = []

        for i in range(1, length + 1):
            self.tail.append(Point(x - i, y))

    def move (dirX, dirY):
        x += dirX
        y += dirY

def update ():
    while True:
        draw()
        time.sleep(1/framerate)


def draw ():
    #Draws the grid
    for i in range(gridSize):
        for j in range(gridSize):
            gridSquare = Rectangle(Point(i*scl, j*scl), Point(i*scl + scl, j*scl + scl))
            gridSquare.setOutline(color_rgb(40, 40, 40))
            gridSquare.setFill("black")
            gridSquare.draw(win)

    #Draws the snake's head
    headPos = Point(player.x * scl, player.y * scl)
    head = Rectangle(headPos, Point(headPos.x + scl, headPos.y + scl))
    head.setFill("red")
    head.draw(win)

    #Draws the snake's body
    for i in range(len(player.tail)):
        tailPos = Point(player.tail[i].x * scl, player.tail[i].y * scl)
        tail = Rectangle(tailPos, Point(tailPos.x + scl, tailPos.y + scl))
        tail.setFill(color_rgb(200, 200, 200))
        tail.draw(win)
    

player = Snake(gridSize / 2, gridSize / 2, 3)
update()
