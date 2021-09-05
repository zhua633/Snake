import pygame
import random

#Initiate pygame
pygame.init()

#Defining variables
width=200
height=200
speed=10

white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
blue = (50, 153, 213)

#Creates an instance of the calss and returns it.
#Sets window size to be 400 x 300
dis=pygame.display.set_mode((width,width))
pygame.display.set_caption('Snake')

def show_score(score):
    surf=pygame.font.SysFont(None, 20).render('Score:'+str(score),True,red)
    dis.blit(surf,surf.get_rect())

def snake(snake_list):
    for n in snake_list:
        pygame.draw.rect(dis,red,[n[0],n[1],10,10])

#Function print_screen() prints a message on screen
def print_screen(message,color):
    message=pygame.font.SysFont(None, 20).render(message,True,color)
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
    score=0

    x=width/2
    y=height/2
    snake_list=[]
    snake_len=1

    dx=0
    dy=0
    
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
                    dx=-10
                    dy=0
                elif event.key==pygame.K_RIGHT:
                    dx=10
                    dy=0
                elif event.key==pygame.K_UP:
                    dx=0
                    dy=-10
                elif event.key==pygame.K_DOWN:
                    dx=0
                    dy=+10
        
        if x>width-1 or x<1 or y>height-1 or y<1:
            game_quit=True

        x+=dx
        y+=dy
        #Fill up the entire screen
        dis.fill(black)
        pygame.draw.rect(dis,white,food)
        snake_head=[]
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        if len(snake_list)>snake_len:
            del snake_list[0]

        for n in snake_list[:-1]:
            if n==snake_head:
                game_quit=True

        show_score(score)
        snake(snake_list)
        pygame.display.update()

        if x==foodx and y==foody:
                foodx=round(random.randrange(0,(width-10)/10)*10)
                foody=round(random.randrange(0,(height-10)/10)*10)
                food=[foodx,foody,10,10]
                score+=1
                snake_len+=1         

        clock.tick(speed)

    pygame.quit()
    quit()


game()

