import pygame
import time
import random

#Initiates pygame
pygame.init()

#Defining variables
width=100
height=100
speed=60

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

#Creates an instance of the calss and returns it.
#Sets window size to be 400 x 300
dis=pygame.display.set_mode((width,width))
pygame.display.set_caption('Snake')

def snake(snake_list):
    for n in snake_list:
        pygame.draw.rect(dis,red,[n[0],n[1],10,10])

#Function print_screen() prints a message on screen
def print_screen(message,color):
    message=pygame.font.SysFont(None, 10).render(message,True,color)
    message_center=(
        (width-message.get_width())/2,
        (height-message.get_height())/2
    )
    dis.blit(message,message_center)

#Starts clock
clock=pygame.time.Clock()

def game():
    game_over=False
    game_quit=False

    x=width/2
    y=height/2
    snake_list=[]
    snake_len=1

    foodx=round(random.randrange(0,(width-10)/10)*10)
    foody=round(random.randrange(0,(height-10)/10)*10)
    food=[foodx,foody,10,10]

    while not game_over:

        while game_quit:
            dis.fill(black)
            print_screen("Defeat, press Q to quit or R to play again",red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        game_over=True
                        game_quit=False
                    if event.key==pygame.K_r:
                        game()

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
            game_quit=True

        #Fill up the entire screen
        dis.fill(black)
        pygame.draw.rect(dis,white,food)

        #Draw a new dot at current position
        snake_list.append([x,y])
        if len(snake_list)>snake_len:
            del snake_list[0]

        for n in snake_list[:-1]:
            if x==snake_list[0]:
                game_quit=True
        
        snake(snake_list)
        pygame.display.update()

        if x==foodx and y==foody:
                foodx=round(random.randrange(0,(width-10)/10)*10)
                foody=round(random.randrange(0,(height-10)/10)*10)
                food=[foodx,foody,10,10]
                snake_len+=1

        clock.tick(speed)

    pygame.quit()
    quit()

game()

