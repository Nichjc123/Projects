import pygame
import time
import random
#Simple mouse accuracy game/test using pygame libary 

pygame.init()

WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

#Colors
GREY = (211,211,211)
RED = (255,0,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (255,255,0)
BLUE = (0,0,255)

#score counter
score = 0

#Difficulty modifier
difficulty = []

#sounds
targSound = pygame.mixer.Sound('arrow.wav')

#Main function
def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    #Main menu
    def menu():
        running = True
        #Initializing font and on screen text for main menu
        font3 = pygame.font.SysFont('comicsans', 40)
        introText = '60SEC TO CLICK THE TARGETS, PICK A DIFFICULTY:'
        ezText = 'EASY'
        medText = 'MEDIUM'
        hardText = 'HARD'

        while running:
            WIN.fill(BLACK)
            #Drawing rect for buttons
            EASYrect = pygame.draw.rect(WIN, BLUE, (150,50,450,150))
            MEDrect = pygame.draw.rect(WIN, BLUE, (150,250,450,150))
            HARDrect = pygame.draw.rect(WIN, BLUE, (150,450,450,150))

            #Drawing text to screen
            WIN.blit(font3.render(introText, False, WHITE), (10,10))
            WIN.blit(font3.render(ezText, True, WHITE), (340, 115))
            WIN.blit(font3.render(medText, True, WHITE), (325, 315))
            WIN.blit(font3.render(hardText, True, WHITE), (340, 515))

            pygame.display.update()
            for event in pygame.event.get():
                #QUITTING
                if event.type == pygame.QUIT:
                    running = False
                
                #Clicking on buttons and assigning the difficulty to list 
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if EASYrect.collidepoint(pos):
                        difficulty.append('easy')
                        running = False
                    if MEDrect.collidepoint(pos):
                        difficulty.append('medium')
                        running = False
                    if HARDrect.collidepoint(pos):
                        difficulty.append('hard')
                        running = False
        pygame.display.update()

    def crosshairs():
        #Crosshair drawing in center of screen
        C_WIDTH = 75
        C_HEIGHT = 10
        pygame.draw.rect(WIN, GREY, (375-(C_WIDTH//2), 375-(C_HEIGHT//2), C_WIDTH, C_HEIGHT), 0)
        pygame.draw.rect(WIN, GREY, (375-(C_HEIGHT//2), 375-(C_WIDTH//2), C_HEIGHT, C_WIDTH), 0)
    
    def draw():
        #Function to draw targets with a width scailing based off of difficulty 
        global square
        TARGx = random.randint(100, 700)
        TARGy = random.randint(100, 700)
        TARGcol = RED
        if difficulty[0] == 'easy':
            TARGwidth = random.randint(20,30)

        if difficulty[0] == 'medium':
            TARGwidth = random.randint(10,20)
            
        if difficulty[0] == 'hard':
            TARGwidth = random.randint(5,15)
        #Drawing target
        square = pygame.draw.rect(WIN, TARGcol, (TARGx,TARGy,TARGwidth,TARGwidth), 0)
        pygame.display.update()

    def redraw_window():
        #Score and crosshairs being drawn
        scoreTEXT = 'score: ' + str(score)
        crosshairs()
        WIN.blit(font.render(scoreTEXT, True, WHITE), (550,10))
        pygame.display.update()
    
    def hit():
        #Hit the target
        global score
        targSound.play()
        #Adding to the score
        score += 1
        #Drawing the crosshairs and another target and resetting the mouse position
        WIN.fill(BLACK)
        crosshairs()
        draw()
        mouseX = (round(WIDTH//2))
        mouseY = (round(HEIGHT//2))
        
            
        pygame.mouse.set_pos([mouseX,mouseY])
    #Start menu
    menu()

    #game window reset
    WIN.fill(BLACK)

    #initial target
    draw()

    #Timer values
    counter, text = 5, '5'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)

    #Fonts 
    font = pygame.font.SysFont('Consolas', 30)
    font2 = pygame.font.SysFont('comicsans', 45)

    #Cover to layer between timer to not have the numbers overlap
    cover = pygame.surface.Surface((100,100)).convert()
    cover.fill(BLACK)

    #Timer text
    timer = 'TIME: '
    while run:
        redraw_window()
        
        for event in pygame.event.get():
            #Timer that ticks based off user event
            if event.type == pygame.USEREVENT:
                counter -= 1 
                text = str(counter).rjust(3) if counter > 0 else ''
            else:
            #Drawing cover, 'Timer' title and seconds counter
                WIN.blit(cover, (0,0))
                WIN.blit(font.render(timer, True, WHITE), (10,10))
                WIN.blit(font.render(text, True, WHITE), (32,48))
            #Updating dislpay
                pygame.display.flip()
                clock.tick(FPS)
            
            #Quitting
            if event.type == pygame.QUIT:
                run = False
                
            #Coliding with button
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if square.collidepoint(pos):
                    hit()
            
            #Running out of time
            if counter == 0:
                gameOverTEXT1 = 'WELL FOUGHT GAMER'
                gameOverTEXT2 = 'YOUR SCORE WAS: ' + str(score)
                WIN.blit(font2.render(gameOverTEXT1, True, YELLOW), (50,100))
                WIN.blit(font2.render(gameOverTEXT2, True, YELLOW), (50,200))
                time.sleep(3)
                run = False 

        pygame.display.update()

if __name__== '__main__':
    main()

pygame.quit()