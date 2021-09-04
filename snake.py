import pygame

#Initiates pygame
pygame.init()

#Defining variables
width=400

blue=(0,0,255)
red=(255,0,0)
white=(255,255,255)
black=(0,0,0)

x=width/2
y=width/2
snake=[x,y,10,10]


#Creates an instance of the calss and returns it.
#Sets window size to be 400 x 300
dis=pygame.display.set_mode((width,width))
pygame.display.set_caption('Snake')

game_over=False

#Starts clock
clock=pygame.time.Clock()

while not game_over:
    #Gets events from the queue
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                x=x-10
            if event.key==pygame.K_RIGHT:
                x=x+10
            if event.key==pygame.K_UP:
                y=y-10
            if event.key==pygame.K_DOWN:
                y=y+10

    snake=[x,y,10,10]
    #Fill up the entire screen
    dis.fill(black)
    #Draw a new dot at current position
    pygame.draw.rect(dis,red,snake)
    pygame.display.update()

    clock.tick(10)

pygame.quit()
quit()

