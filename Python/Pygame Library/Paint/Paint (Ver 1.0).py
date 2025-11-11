import pygame

pygame.init()

Display_Width = 800
Display_Height = 600

White = (255,255,255)
Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0,255)

MyDisplay = pygame.display.set_mode((Display_Width,Display_Height))

pygame.display.set_caption('Paint')

clock = pygame.time.Clock()

def Rectangle(x,y,Width,Height,Color):
    #Rect = pygame.Rect(x,y,Width,Height)
    #pygame.draw.rect(MyDisplay,Color,Rect)
    
    #pygame.draw.rect(MyDisplay,Color,[x,y,Width,Height])
    pygame.draw.rect(MyDisplay,Color,[x,y,Width,Height],2)

def Circle(x,y,r,Width,Color):
    pygame.draw.circle(MyDisplay,Color,(x,y),r,Width)

def Line(x1,y1,x2,y2,Width,Color):
    pygame.draw.line(MyDisplay,Color,(x1,y1),(x2,y2),Width)

Rect_Select = pygame.Rect(25,25,20,10)
Line_Select = pygame.Rect(25,45,20,10)
Circle_Select = pygame.Rect(25,65,20,10)

IsRunning = True

Rect_Active = False
Line_Active = False
Circle_Active = False

MyDisplay.fill(White)

while IsRunning:
    
    Rectangle(25,25,20,10,Red)
    Line(25,45,45,55,2,Green)
    Circle(35,70,10,1,Blue)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            IsRunning = False
        
        # ----------------- Draw rectangle  -----------------
        if event.type == pygame.MOUSEBUTTONDOWN and not Rect_Active:
            if Rect_Select.collidepoint(event.pos):
                Rect_Active = True
                Line_Active = False
                Circle_Active = False

        if event.type == pygame.MOUSEBUTTONDOWN and Rect_Active:
            x,y = event.pos
            Width = Height = 0
        elif event.type == pygame.MOUSEMOTION and Rect_Active:
            if x > 50 and y > 80 :
                Previous_Width = Width
                Previous_Heigth = Height
                Width = event.pos[0] - x
                Height = event.pos[1] - y  
                Rectangle(x,y,Previous_Width,Previous_Heigth,White)
                Rectangle(x,y,Width,Height,Red)                    
        elif event.type == pygame.MOUSEBUTTONUP and Rect_Active:
            if x > 50 and y > 80 :
                Rectangle(x,y,Width,Height,Red)
                x = y = Width = Height = 0

        # ----------------- Draw line  -----------------
        if event.type == pygame.MOUSEBUTTONDOWN and not Line_Active:
            if Line_Select.collidepoint(event.pos):
                Line_Active = True
                Rect_Active = False
                Circle_Active = False
     
        if event.type == pygame.MOUSEBUTTONDOWN and Line_Active:
            x1,y1 = event.pos
            x2 = 0
            y2 = 0
        elif event.type == pygame.MOUSEMOTION and Line_Active:
            if x1 > 50 and y1 > 80:        
                Previous_x2 = x2
                Previous_y2 = y2
                x2,y2 = event.pos
                Line(x1,y1,Previous_x2,Previous_y2,2,White)
                Line(x1,y1,x2,y2,2,Green)
        elif event.type == pygame.MOUSEBUTTONUP and Line_Active:
            if x1 > 50 and y1 > 80 :
                Line(x1,y1,x2,y2,2,Green)
                x1 = y1 = x2 = y2 = 0

        # ----------------- Draw circle  -----------------
        if event.type == pygame.MOUSEBUTTONDOWN and not Circle_Active:
            if Circle_Select.collidepoint(event.pos):
                Circle_Active = True
                Line_Active = False
                Rect_Active = False
     
        if event.type == pygame.MOUSEBUTTONDOWN and Circle_Active:
            X_Center,Y_Center = event.pos
            r = 1
        elif event.type == pygame.MOUSEMOTION and Circle_Active:
            if X_Center > 50 and Y_Center > 80:        
                Previous_r = r
                r = abs(event.pos[0] - X_Center)
                Circle(X_Center,Y_Center,Previous_r,1,White)             
                Circle(X_Center,Y_Center,r,1,Blue)             
        elif event.type == pygame.MOUSEBUTTONUP and Circle_Active:
            if X_Center > 50 and Y_Center > 80:        
                Circle(X_Center,Y_Center,r,1,Blue)             
                X_Center = Y_Center = 0

        pygame.display.update()
        clock.tick(120)

pygame.quit()
quit()