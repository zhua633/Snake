import pygame
import time

#Initiates pygame
pygame.init()

#Defining variables
width=400
height=400
speed=10

blue=(0,0,255)
red=(255,0,0)
white=(255,255,255)
black=(0,0,0)

x=width/2
y=height/2
snake=[x,y,10,10]


#Creates an instance of the calss and returns it.
#Sets window size to be 400 x 300
dis=pygame.display.set_mode((width,width))
pygame.display.set_caption('Snake')

game_over=False

#Function print_screen() prints a message on screen
def print_screen(message,color):
    message=pygame.font.SysFont(None, 50).render(message,True,color)
    message_center=(
        (width-message.get_width())/2,
        (height-message.get_height())/2
    )
    dis.blit(message,message_center)


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

    if x>width or x<0 or y>height or y<0:
        game_over=True

    snake=[x,y,10,10]

    #Fill up the entire screen
    dis.fill(black)

    #Draw a new dot at current position
    pygame.draw.rect(dis,red,snake)
    pygame.display.update()

    clock.tick(speed)

print_screen("Defeat",red)
pygame.display.update()
time.sleep(2)

pygame.quit()
quit()

