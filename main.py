from graphics import *

framerate = 5
scl = 20 #Size of the grid's square
gridSize = 32 #Amount of squares in the grid
win = GraphWin("Snake Game", gridSize*scl + 1, gridSize*scl + 1)

class Snake:
    def __init__ (self, x, y, length):
        self.x = x
        self.y = y
        self.tail = []
        self.lastTail = Point(x - length, y)
        self.prevHead = Point(x, y)

        for i in range(1, length + 1):
            pos = Point(x - i, y)
            self.tail.append(pos)
            square = Rectangle(Point(pos.x*scl, pos.y*scl), Point(pos.x*scl + scl, pos.y*scl + scl))
            square.setFill(color_rgb(200, 200, 200))
            square.draw(win)

    def move (self, dirX, dirY):
        #saves head and tail position
        self.prevHead = Point(self.x, self.y)
        self.lastTail = self.tail.pop()
        
        #moves tail to head and adds dirX and dirY to the head position
        self.tail.insert(0, Point(self.x, self.y))
        self.x += dirX
        self.y += dirY

        #redraws the snake
        self.draw()

    def draw (self):
        #Fills the last tail position with a grid square
        gridFill = Rectangle(Point(self.lastTail.x*scl, self.lastTail.y*scl), Point(self.lastTail.x*scl + scl, self.lastTail.y*scl + scl))
        gridFill.setFill("black")
        gridFill.setOutline(color_rgb(40, 40, 40))
        gridFill.draw(win)

        #Draws the head
        head = Rectangle(Point(self.x*scl, self.y*scl), Point(self.x*scl + scl, self.y*scl + scl))
        head.setFill("red")
        head.draw(win)

        #Draws the last tail moved
        tail = Rectangle(Point(self.prevHead.x*scl, self.prevHead.y*scl), Point(self.prevHead.x*scl + scl, self.prevHead.y*scl + scl))
        tail.setFill(color_rgb(200, 200, 200))
        tail.draw(win)

def update ():
    while True:
        player.move(1, 0)
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
    
    #Draws the head
    head = Rectangle(Point(player.x * scl, player.y * scl), Point(player.x*scl + scl, player.y*scl + scl))
    head.setFill("red")
    head.draw(win)

    #Draws the tail
    for i in range(len(player.tail)):
        tail = Rectangle(Point(player.tail[i].x*scl, player.tail[i].y*scl), Point(player.tail[i].x*scl + scl, player.tail[i].y*scl + scl))
        tail.setFill(color_rgb(200, 200, 200))
        tail.draw(win)



player = Snake(gridSize/2, gridSize/2, 3)
update()
