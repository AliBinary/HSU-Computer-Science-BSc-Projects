import pygame
from pygame.locals import *
from math import sqrt, floor

pygame.init()
Display_Width = 800
Display_Height = 600

White = (255, 255, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)

MyDisplay = pygame.display.set_mode((Display_Width, Display_Height))
pygame.display.set_caption('Paint')
clock = pygame.time.Clock()

#################################################################
#                            Menu                            
#################################################################
def Menu():
    global  Rect_Select, Line_Select, Circle_Select, Eraser_Select, MyDisplay
    Rect_Select = pygame.Rect(25,25,20,10)
    Line_Select = pygame.Rect(25,45,20,10)
    Circle_Select = pygame.Rect(25,65,20,10)
    Eraser_Select = pygame.Rect(25,95,20,10)
    pygame.draw.rect(MyDisplay, Red, [25,25,20,10], 2)
    pygame.draw.line(MyDisplay,Green,(25,45),(45,55),2)
    pygame.draw.circle(MyDisplay,Blue,(35,70),10,1)

    EraserImg = pygame.image.load("Eraser.png")
    MyDisplay.blit(EraserImg,(25,95))

#################################################################
#                            Rectangle                            
#################################################################
Rect_top_left = (0, 0)
Rect_Size = (0, 0)
Drawing_Rect = False
Rect_List = []

def Rectangle(event):
    global Rect_Active, Drawing_Rect, Rect_top_left, Rect_Size, Rect_List

    if event.type == MOUSEBUTTONDOWN:
        Rect_top_left = event.pos
        Rect_Size = 0, 0
        Drawing_Rect = True

    elif event.type == MOUSEBUTTONUP:
        Rect_bottom_right = event.pos
        Rect_Size = Rect_bottom_right[0]-Rect_top_left[0], Rect_bottom_right[1]-Rect_top_left[1]
        Rect = pygame.Rect(Rect_top_left, Rect_Size)
        if Rect_Active and Rect_top_left[0] > 50 and Rect_top_left[1] > 115:
            Rect_List.append(Rect)    
        Drawing_Rect = False

    elif event.type == MOUSEMOTION and Drawing_Rect:
        Rect_bottom_right = event.pos
        Rect_Size = Rect_bottom_right[0]-Rect_top_left[0], Rect_bottom_right[1]-Rect_top_left[1]
#################################################################
#                            Line
#################################################################
Line_Start_Point = (0, 0)
Line_End_Point = (0, 0)
Drawing_Line = False
Line_List = []

def Line(event):
    global Line_Active, Drawing_Line, Line_Start_Point_Point, Line_End_Point, Line_List

    if event.type == MOUSEBUTTONDOWN:
        Line_Start_Point_Point = event.pos
        Line_End_Point = Line_Start_Point_Point
        Drawing_Line = True

    elif event.type == MOUSEBUTTONUP:
        Line_End_Point = event.pos
        if Line_Active and Line_Start_Point_Point[0] > 50 and Line_Start_Point_Point[1] > 115:
            Line_List.append([Line_Start_Point_Point,Line_End_Point])
        Drawing_Line = False

    elif event.type == MOUSEMOTION and Drawing_Line:
        Line_End_Point = event.pos

#################################################################
#                            Circle
#################################################################
Circle_Center = (0, 0)
Circle_Radius = 1
Drawing_Circle = False
Circle_List = []

def Circle(event):
    global Circle_Active, Drawing_Circle, Circle_Center, Circle_Radius, Circle_List

    if event.type == MOUSEBUTTONDOWN:
        Circle_Center = event.pos
        Circle_Radius = 3
        Drawing_Circle = True

    elif event.type == MOUSEBUTTONUP:
        Circle_Radius = floor(sqrt((event.pos[0] - Circle_Center[0]) **2  +
                              (event.pos[1] - Circle_Center[1]) **2 ))  + 3

        if Circle_Active and Circle_Center[0] > 50 and Circle_Center[1] > 115:
            Circle_List.append([Circle_Center,Circle_Radius])
        Drawing_Circle = False

    elif event.type == MOUSEMOTION and Drawing_Circle:
        Circle_Radius = floor(sqrt((event.pos[0] - Circle_Center[0]) **2  +
                              (event.pos[1] - Circle_Center[1]) **2 )) + 3
#################################################################
#                            Eraser
#################################################################
Eraser_Center = (0, 0)
Eraser_Radius = 10
Erasing = False
Eraser_List = []

def Eraser(event):
    global Eraser_Active, Eraser_Center, Eraser_Radius, Eraser_List

    if event.type == MOUSEMOTION:
        Eraser_Center = event.pos
        Eraser_Radius = 4
        if Eraser_Active and Eraser_Center[0] > 50 and Eraser_Center[1] > 115:
            Eraser_List.append(Eraser_Center)
#################################################################

IsRunning = True
Rect_Active = Line_Active = Circle_Active = Eraser_Active = False

while IsRunning:
    
    MyDisplay.fill(White)
    Menu()

    for rect in Rect_List:
        pygame.draw.rect(MyDisplay, Red, rect, 2)

    for line in Line_List:
        pygame.draw.line(MyDisplay, Green, line[0], line[1], 2)

    for circle in Circle_List:
        pygame.draw.circle(MyDisplay, Blue, circle[0], circle[1], 2)

    for eraser in Eraser_List:
        pygame.draw.circle(MyDisplay, White, eraser, Eraser_Radius, Eraser_Radius)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            IsRunning = False
        
        if Rect_Select.collidepoint(pygame.mouse.get_pos()) or Line_Select.collidepoint(pygame.mouse.get_pos()) or Circle_Select.collidepoint(pygame.mouse.get_pos()) or Eraser_Select.collidepoint(pygame.mouse.get_pos()):            

            pygame.mouse.set_cursor(*pygame.cursors.tri_left) #arrow, diamond, broken_x, tri_left, tri_right
        else:
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
                                                   
        if event.type == MOUSEBUTTONDOWN and not Rect_Active:
            if Rect_Select.collidepoint(event.pos):
                Rect_Active = True
                Line_Active = Circle_Active = Eraser_Active = False

        if event.type == MOUSEBUTTONDOWN and not Line_Active:
            if Line_Select.collidepoint(event.pos):
                Line_Active = True
                Rect_Active = Circle_Active = Eraser_Active = False

        if event.type == MOUSEBUTTONDOWN and not Circle_Active:
            if Circle_Select.collidepoint(event.pos):
                Circle_Active = True
                Line_Active = Rect_Active = Eraser_Active = False

        if event.type == MOUSEBUTTONDOWN and not Eraser_Active:
            if Eraser_Select.collidepoint(event.pos):
                Eraser_Active = True
                Line_Active = Circle_Active = Rect_Active = False

        Rectangle(event)
        Line(event)
        Circle(event)
        Eraser(event)
        
    if Rect_Active and Rect_top_left[0] > 50 and Rect_top_left[1] > 115:
        pygame.draw.rect(MyDisplay, Red, (Rect_top_left, Rect_Size), 2)

    if Line_Active and Line_Start_Point[0] > 50 and Line_Start_Point[1] > 115:
        pygame.draw.line(MyDisplay,Green,Line_Start_Point,Line_End_Point,2)

    if Circle_Active and Circle_Center[0] > 50 and Circle_Center[1] > 115:
        pygame.draw.circle(MyDisplay,Blue,Circle_Center,Circle_Radius,2)

    if Eraser_Active and Eraser_Center[0] > 50 and Eraser_Center[1] > 115:
        pygame.draw.circle(MyDisplay,White,Eraser_Center,Eraser_Radius,Eraser_Radius)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()