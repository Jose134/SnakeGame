from graphics import *

framerate = 5.0
scl = 20 #Size of the grid's square
gridSize = 32 #Amount of squares in the grid
win = GraphWin("Snake Game", gridSize*scl + 1, gridSize*scl + 1)

grid = [[0 for x in range(gridSize)] for y in range(gridSize)]

for i in range(gridSize):
    for j in range(gridSize):
        grid[i][j] = Rectangle(Point(i*scl, j*scl), Point(i*scl + scl, j*scl + scl))
        grid[i][j].setFill("black")
        grid[i][j].setFill(color_rgb(40, 40, 40))
        grid[i][j].draw(win)

class SnakePart:
    def __init__ (self, pos):
        self.pos = pos
        self.graphic = Rectangle(Point(self.pos.x*scl, self.pos.y*scl), Point(self.pos.x*scl + scl, self.pos.y*scl + scl))

        self.graphic.setFill(color_rgb(200, 200, 200))
        self.graphic.draw(win)

class Snake:
    def __init__ (self, x, y, length):
        self.x = x
        self.y = y
        self.tail = []
        
        self.lastTail = Point(x - length, y)
        self.prevHead = Point(x, y)
        self.eat = False

        self.headGraph = Rectangle(Point(x*scl, y*scl), Point(x*scl + scl, y*scl + scl))
        self.headGraph.setFill("red")
        self.headGraph.draw(win)

        for i in range(1, length + 1):
            pos = Point(x - i, y)
            self.tail.append(SnakePart(pos))
        
    def move (self, dirX, dirY):
        #saves head and tail position
        self.prevHead = Point(self.x, self.y)
        if (self.eat):
            self.lastTail = self.tail[len(self.tail) - 1]
            square = Rectangle(Point(self.prevHead.x*scl, self.prevHead.y*scl), Point(self.prevHead.x*scl+scl, self.prevHead.y*scl+scl))
            square.setFill(color_rgb(200, 200, 200))
            square.draw(win)
            
            self.eat = False
        else:        
            self.lastTail = self.tail.pop()

        #moves tail to head and adds dirX and dirY to the head position
        self.tail.insert(0, Point(self.x, self.y))
        self.x += dirX
        self.y += dirY

        #moves the graphics
        self.headGraph.move(dirX*scl, dirY*scl)


def update ():
    while True:
        #Input
        global playerDirX, playerDirY
        key = win.checkKey()
        
        if (key == "w"):
            playerDirX = 0
            playerDirY = -1
        elif (key == "a"):
            playerDirX = -1
            playerDirY = 0
        elif (key == "s"):
            playerDirX = 0
            playerDirY = 1
        elif (key == "d"):
            playerDirX = 1
            playerDirY = 0
 
        player.move(playerDirX, playerDirY)
        
        #Tail Collision
        for i in range(len(player.tail)):
            if ((player.x == player.tail[i].pos.x) and (player.y == player.tail[i].pos.y)):
                player.tail = [0]

        #Food Collision
        if (player.x == food.x and player.y == food.y):
            player.eat = True

        draw()
        time.sleep(1/framerate)


def draw ():
    #Draws the head
    head = Rectangle(Point(player.x*scl, player.y*scl), Point(player.x*scl + scl, player.y*scl + scl))
    head.setFill("red")
    #head.draw(win)

    #Draws the tail
    for i in range(len(player.tail)):
        tail = Rectangle(Point(player.tail[i].x*scl, player.tail[i].y*scl), Point(player.tail[i].x*scl + scl, player.tail[i].y*scl + scl))
        tail.setFill(color_rgb(200, 200, 200))
        #tail.draw(win)

    #Draws the food
    foodRect = Rectangle(Point(food.x*scl, food.y*scl), Point(food.x*scl + scl, food.y*scl + scl))
    foodRect.setFill("green")
    foodRect.draw(win)

lastKey = ""

player = Snake(gridSize/2, gridSize/2, 3)
playerDirX = 1
playerDirY = 0

food = Point(10, 10)

update()
