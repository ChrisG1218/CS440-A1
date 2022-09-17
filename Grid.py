import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_HEIGHT = 1000
WINDOW_WIDTH = 1000
ROWS = 400 #1000 
COLS = 300 #500 
BLOCKSIZE = 100 # 10

def main():
    global SCREEN
    randomBlockedSet = randomBlocked(ROWS, COLS, BLOCKSIZE) ## Check these numbers and make sure they match drawGrid
    randomStart = randomVertex(ROWS, COLS, BLOCKSIZE)
    randomEnd = randomVertex(ROWS, COLS, BLOCKSIZE)
    
    # ensuring end point is different than start point
    while (randomEnd==randomStart):
        randomEnd = randomVertex(ROWS, COLS, BLOCKSIZE)
    print(randomBlockedSet)
    print(randomStart)
    print(randomEnd)

    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    SCREEN.fill(WHITE)
    run = True
    i = 0
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        drawGrid(randomBlockedSet, randomStart, randomEnd)
        pygame.display.update()

def randomBlocked(rows, cols, blockSize): 
    blocked = set()
    numCells = int((rows/blockSize * cols/blockSize) * 0.1)
    for i in range(numCells): 
        randX = random.randrange(0, rows, blockSize)
        randY = random.randrange(0, cols, blockSize)
        pair = (randX, randY)
        blocked.add(pair)
    return blocked

def randomVertex(rows, cols, blockSize):
    randX = random.randrange(0, rows, blockSize)
    randY = random.randrange(0, cols, blockSize)
    pair = (randY, randX)
    return pair

def drawGrid(randomBlockedSet, randomStart, randomEnd):
    # print(randomBlockedSet)
    for y in range(0, COLS, BLOCKSIZE):
        for x in range(0, ROWS, BLOCKSIZE):
            rect = pygame.Rect(y, x, BLOCKSIZE, BLOCKSIZE)
            if((x, y) in randomBlockedSet):
                pygame.draw.rect(SCREEN, BLACK, rect)
            else: 
                pygame.draw.rect(SCREEN, BLACK, rect, 1)
            pygame.draw.line(SCREEN, BLACK, (y ,x), (y + BLOCKSIZE, x + BLOCKSIZE))
            pygame.draw.line(SCREEN, BLACK, (y + BLOCKSIZE, x), (y, x + BLOCKSIZE))
    
    #(r, g, b) is color, (x, y) is center, R is radius and w is the thickness of the circle border.
    pygame.draw.circle(SCREEN, (0,255,0), randomStart, 5, 5)
    pygame.draw.circle(SCREEN, (255,0,0), randomEnd, 5, 5) 


def drawLine(start, end): 
    pygame.draw.line(SCREEN, (0, 0, 255), start, end)

main()