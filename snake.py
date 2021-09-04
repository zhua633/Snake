import pygame

#Initiates pygame
pygame.init()

#Creates an instance of the calss and returns it.
#Sets window size to be 400 x 300
dis=pygame.display.set_mode((400,300))
pygame.display.update()
pygame.display.set_caption('Snake')

game_over=False
while not game_over:
    #Gets events from the queue
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True


pygame.quit()
quit()

