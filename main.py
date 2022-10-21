import pygame
from pygame.locals import *
import random

pygame.init()
var = 0
screen_width = 360
screen_height = 568


# defining the surface to draw on and update
surf = surf2 = pygame.display.set_mode((screen_width, screen_height))

tempColor = (255, 255, 255)
grid = [[(255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255)], [(255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255)], [(255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255)], [(255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255)], [(255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255)], [(255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255)], [(255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255)], [(255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255)], [(255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255)], [(255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255)], [], []]
pegGrid = [[(50, 50, 50), (50, 50, 50), (50, 50, 50), (50, 50, 50)], [(50, 50, 50), (50, 50, 50), (50, 50, 50), (50, 50, 50)], [(50, 50, 50), (50, 50, 50), (50, 50, 50), (50, 50, 50)], [(50, 50, 50), (50, 50, 50), (50, 50, 50), (50, 50, 50)], [(50, 50, 50), (50, 50, 50), (50, 50, 50), (50, 50, 50)], [(50, 50, 50), (50, 50, 50), (50, 50, 50), (50, 50, 50)], [(50, 50, 50), (50, 50, 50), (50, 50, 50), (50, 50, 50)], [(50, 50, 50), (50, 50, 50), (50, 50, 50), (50, 50, 50)], [(50, 50, 50), (50, 50, 50), (50, 50, 50), (50, 50, 50)], [(50, 50, 50), (50, 50, 50), (50, 50, 50), (50, 50, 50)], [(50, 50, 50), (50, 50, 50), (50, 50, 50), (50, 50, 50)]]
gridButtonList = [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
revealAnswer = [False, True]

gameOn = [True]

round = 0

answer = [random.randint(1,8), random.randint(1,8), random.randint(1,8), random.randint(1,8)]

def duplicateCheck(listP):
  for i in range(len(listP)):
    for j in range(len(listP) - i - 1):
      if listP[i] == listP[i + j + 1]:
        return True
      else:
        continue
  
  return False

# makes sure that there are no duplicates in the answer
while duplicateCheck(answer):
  answer = [random.randint(1,8), random.randint(1,8), random.randint(1,8), random.randint(1,8)]

def convertToColor(val):
  if val == 1:
    return (255, 0, 0)
  elif val == 2:
    return (0, 255, 0)
  elif val == 3:
    return (0, 0, 255)
  elif val == 4:
    return (255, 255, 0)
  elif val == 5:
    return (185, 107, 50)
  elif val == 6:
    return (255, 127, 0)
  elif val == 7:
    return (127, 127, 127)
  elif val == 8:
    return (255, 0, 255)
    
for i in range(len(answer)):
  answer[i] = convertToColor(answer[i])
print(answer) # for fast debugging

# class for buttons :D
class button():
  def __init__(self, color, x, y, width, height, text = ""):
    self.color = color
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.text = text
  
  def draw(self, surf2, outline = None):
    if outline:
      pygame.draw.rect(surf2, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)
    
    pygame.draw.rect(surf2, self.color, (self.x, self.y, self.width, self.height), 0)

      # writing text
    if self.text != "":
      font = pygame.font.SysFont('comicsans', 20)
      text = font.render(self.text, 1, (0, 0, 0))
      surf2.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))
    
  def hover(self, pos): 
    if pos[0] > self.x and pos[0] < self.x + self.width and pos[1] > self.y and pos[1] < self.y + self.height:
      return True
    else:
      return False

# drawing the main board for mastermind
def draw_circles(x1, y1, circle_size, separation):
  for i in range(10):
    for j in range(4):
      color = grid[i][j]
      pygame.draw.circle(surf, color, (x1, y1), circle_size)
      x1 += separation
    x1 += -separation * 4
    y1 += -separation - 5

# drawing the smaller judgement circles to the side of each main circle
def draw_small(x1, y1, circle_size):
  for i in range(10):
    for j in range(2):
      for k in range(2):
        color = pegGrid[i][j * 2 + k]
        pygame.draw.circle(surf, color, (x1, y1), circle_size - 10)
        x1 += 15
      x1 += -30
      y1 += 15
    y1 += -70

def sus_circles(x1, y1, circle_size, reveal = False):
  if reveal == False:
    for i in range(4):
      pygame.draw.circle(surf, (25, 25, 25), (x1, y1), circle_size + 5)
      x1 += 50
  elif reveal == True:
    for i in range(4):
      color = answer[i]
      pygame.draw.circle(surf, color, (x1, y1), circle_size + 5)
      x1 += 50
  
# setting up vars, building screen etc
def main():
  pygame.init()

  pygame.display.set_caption("Mastermind")

# defining buttons (and color) :D
curColor = (25, 25, 25)
redButton = button((255, 0, 0), 50, 470, 35, 35)
greenButton = button((0, 255, 0), 95, 470, 35, 35)
blueButton = button((0, 0, 255), 140, 470, 35, 35)
yellowButton = button((255, 255, 0), 185, 470, 35, 35)
brownButton = button((185, 107, 50), 50, 515, 35, 35)
orangeButton = button((255, 127, 0), 95, 515, 35, 35)
grayButton = button((127, 127, 127), 140, 515, 35, 35)
purpleButton = button((255, 0, 255), 185, 515, 35, 35)
checkButton2 = button((255, 215, 0), 235, 425, 100, 30, "Check")
pygame.draw.rect(surf2, curColor, (260, 470, 60, 60), 0)
pygame.display.update()

def checkButton():
  for i in grid[round]:
    if i == (255, 255, 255):
      return False
  
  return True
    
def gridButtonCreate(x1, y1, i, j):
  newButton = button((0, 0, 0), x1, y1, 30, 30)
  gridButtonList[i][j] = newButton

def updatePegs(row):
  # row = grid[round]

  correct = 0
  tempList = [[False, False, False, False], [False, False, False, False]] # used or not used

  for i in range(4):
    if row[i] == answer[i]:
      correct = correct + 1
      tempList[0][i] = True
      tempList[1][i] = True
  
  close = 0

  for i in range(4):
    for j in range(4):
      if i != j:
        if tempList[0][i] == False and tempList[1][j] == False:
          if row[j] == answer[i]:
            tempList[0][i] = True
            tempList[1][j] = True
            close = close + 1

  for i in range(4):
    color = (100, 100, 100)

    if i < correct:
      color = (255, 0, 0)
    elif i < correct + close:
      color = (255, 255, 255)
    
    pegGrid[round][i] = color
  
  # print(str(correct) + ", " + str(close))
  
  if correct == 4:
    print("You Win!")
    revealAnswer[0] = True
    sus_circles(55, 30, 15, revealAnswer[0])

def updateScreen():
  x1 = 60
  y1 = 425
  separation = 35
  circle_size = 15

  if round == 10 and revealAnswer[1] and not revealAnswer[0]:
    revealAnswer[0] = True
    print("You lose!")
    sus_circles(55, 30, circle_size, revealAnswer[0])
    revealAnswer[1] = False

  # a temporary marker to mark the coordinates for the hidden buttons underneath the circles
  for i in range(10):
    for j in range(4):
      gridButtonCreate(x1, y1, i, j)
      pygame.draw.rect(surf2, (0, 0, 0), (x1, y1, 30, 30), 0)
      x1 += 35
    x1 += -140
    y1 += -40
  x1 = 75
  y1 = 440
  draw_circles(x1, y1, circle_size, separation)
  x1 = 210
  y1 = 432.5
  draw_small(x1, y1, circle_size)
  x1 = 55
  y1 = 30
  
  sus_circles(x1, y1, circle_size, revealAnswer[0])
  
  pygame.display.update()
  redButton.draw(surf2, (0, 0, 0))
  greenButton.draw(surf2, (0, 0, 0))
  blueButton.draw(surf2, (0, 0, 0))
  yellowButton.draw(surf2, (0, 0, 0))
  brownButton.draw(surf2, (0, 0, 0))
  orangeButton.draw(surf2, (0, 0, 0))
  grayButton.draw(surf2, (0, 0, 0))
  purpleButton.draw(surf2, (0, 0, 0))
  pygame.draw.rect(surf2, curColor, (260, 470, 60, 60), 0)
  
  if checkButton() and revealAnswer[1]:
    checkButton2.draw(surf2, (0, 0, 0))

main()

while True:
  sus_circles(55, 35, 15, revealAnswer[0])
  pygame.init()
  updateScreen()
  pygame.display.update()
  for event in pygame.event.get():

    pos = pygame.mouse.get_pos()

    if event.type == MOUSEBUTTONDOWN:
      if redButton.hover(pos):
        curColor = (255, 0, 0) 
      
      if greenButton.hover(pos):
        curColor = (0, 255, 0)
      
      if blueButton.hover(pos):
        curColor = (0, 0, 255) 
      
      if yellowButton.hover(pos):
        curColor = (255, 255, 0) 
      
      if brownButton.hover(pos):
        curColor = (185, 107, 50)
      
      if orangeButton.hover(pos):
        curColor = (255, 127, 0)

      if grayButton.hover(pos):
        curColor = (127, 127, 127)
        
      if purpleButton.hover(pos):
        curColor = (255, 0, 255)
      
      if checkButton2.hover(pos):
        if checkButton():
          if revealAnswer[1]:
            updatePegs(grid[round])
          checkButton2.color = (50, 50, 50)
          checkButton2.draw(surf2, (0, 0, 0))

          if revealAnswer[1]:
            round = round + 1
          
      for i in range(len(gridButtonList)):
        for j in range(len(gridButtonList[i])):
          if gridButtonList[i][j].hover(pos):
            if curColor != (25, 25, 25) and i == round:
              grid[i][j] = curColor

    if event.type == pygame.MOUSEMOTION:
      if redButton.hover(pos):
        redButton.color = (255, 50, 50)
      else:
        redButton.color = (255, 0, 0) 
      
      if greenButton.hover(pos):
        greenButton.color = (0, 205, 0)
      else:
        greenButton.color = (0, 255, 0) 
      
      if blueButton.hover(pos):
        blueButton.color = (50, 50, 255)
      else:
        blueButton.color = (0, 0, 255) 
      
      if yellowButton.hover(pos):
        yellowButton.color = (205, 205, 0)
      else:
        yellowButton.color = (255, 255, 0) 
      
      if brownButton.hover(pos):
        brownButton.color = (235, 157, 100)
      else:
        brownButton.color = (185, 107, 50) 
      
      if orangeButton.hover(pos):
        orangeButton.color = (255, 177, 50)
      else:
        orangeButton.color = (255, 127, 0) 
      
      if grayButton.hover(pos):
        grayButton.color = (177, 177, 177)
      else:
        grayButton.color = (127, 127, 127) 
      
      if purpleButton.hover(pos):
        purpleButton.color = (255, 50, 255)
      else:
        purpleButton.color = (255, 0, 255) 
      
      if checkButton2.hover(pos):
        checkButton2.color = (200, 160, 0)
      else:
        checkButton2.color = (255, 215, 0)

