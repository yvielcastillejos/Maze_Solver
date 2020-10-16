import pygame
from test import*


S_WIDTH = len(test[0])*50
S_HEIGHT = len(test)*50

GRIDSIZE = 50
GRID_WIDTH =  S_WIDTH/GRIDSIZE
GRID_HEIGHT = S_HEIGHT / GRIDSIZE


def game():
   # initialize pygame
   pygame.init()
   clock = pygame.time.Clock()
   screen = pygame.display.set_mode(size = (S_WIDTH, S_HEIGHT), flags = 0) #,depth = 32)
   surface = pygame.Surface(screen.get_size())

   # convert the pixel format so its faster
   surface = surface.convert()
   # draw the checkered background
   start1, end1 = drawgrid(surface, screen)
   myfont = pygame.font.SysFont("fontname", 20)
   start_end = pygame.font.SysFont("fontname", 70)
   j = len(shortest)-1
   i = 0
   while True:
        # initialize to 10 frames per second
        clock.tick(10)
        start1, end1 = drawgrid(surface, screen)
        event()
        if j>= i:
            path = shortest[j]
            j = j-1
            drawline(surface, path)
        if j <= 0:
            drawshortest(surface, shortest, start1, end1)
        # handle events
        # Once action transpires, update and refresh the screen & surface
        screen.blit(surface, (0,0))
        text1 = myfont.render("Breadth First Search", 1, (0,0,0))
        screen.blit(text1, (5,10))
        text2 = start_end.render("S", 1, (0,0,0))
        screen.blit(text2, (start1[0]*GRIDSIZE,start1[1]*GRIDSIZE))
        text3 = start_end.render("E", 1, (0,0,0))
        screen.blit(text3, (end1[0]*GRIDSIZE,end1[1]*GRIDSIZE))
        pygame.display.update()
   return

def drawgrid(surface, screen):
   clr1 = (242, 250, 204)
   clr2 = (144, 179, 244)
   for y in range(0, int(GRID_HEIGHT)):
       for x in range(int(GRID_WIDTH)):
          # make a checkered background
              # Size of a rectangle and position
              r = pygame.Rect((GRIDSIZE*x, GRIDSIZE*y),(GRIDSIZE, GRIDSIZE))
              # draw the rectangle on surface at position r with size defined in r
              pygame.draw.rect(surface, (174, 30, 45), r)
   # Now draw the walls
   for y in range(0, len(test)):
       for x in range(0,len(test[0])):
           if test[y][x] == "#":
               r = pygame.Rect((GRIDSIZE*x, GRIDSIZE*y),(GRIDSIZE, GRIDSIZE))
               pygame.draw.rect(surface, (65, 68, 77), r)
               pygame.draw.rect(surface, (255, 255, 255), r, 1)
           if test[y][x] == "S":
               start0 = (x,y)
           if test[y][x] == "E":
               end0 = (x,y)
   return start0, end0

def event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if (event.key == Q):
                pygame.quit()
                sys.exit()

    return

def drawline(surface,path):
   r = pygame.Rect((GRIDSIZE*path[1], GRIDSIZE*path[0]),(GRIDSIZE, GRIDSIZE))
   pygame.draw.rect(surface, (134, 249, 148), r)
   return

def drawshortest(surface, shortest, start, end):
   r = pygame.Rect((GRIDSIZE*start[0], GRIDSIZE*start[1]),(GRIDSIZE, GRIDSIZE))
   pygame.draw.rect(surface, (134, 249, 148), r)
   for path in shortest:
       r = pygame.Rect((GRIDSIZE*path[1], GRIDSIZE*path[0]),(GRIDSIZE, GRIDSIZE))
       pygame.draw.rect(surface, (134, 249, 148), r)
   return
game()
