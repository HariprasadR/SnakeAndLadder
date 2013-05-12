import pygame, pygbutton, sys
from pygame.locals import *
import random
FPS = 30
WINDOWWIDTH = 380
WINDOWHEIGHT = 350

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)


def main():
    windowBgColor = WHITE

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    size = width, height = 600,500
    speed = [0, 0]
    black = 0, 0, 0
    DISPLAYSURFACE = pygame.display.set_mode(size)
    ball = pygame.image.load("ladderssnakesboardgamescreenshot.jpg")
    pygame.display.set_caption('snake and ladder game')
    ballrect = ball.get_rect()


    # buttons that change the button text color
    bpl1 = pygbutton.PygButton((470, 100, 120, 45), 'PL1 BLACK')
    bpl4 = pygbutton.PygButton((470, 150, 120, 45), 'PL2 RED')
    bpl2 = pygbutton.PygButton((500, 210, 85, 45), 'play')
    bpl3 = pygbutton.PygButton((500, 310, 85, 45), 'NO')

    FgButtons = (bpl3, bpl2, bpl1, bpl4)

    while True: # main game loop
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            
            buttonFgColor = None
            if 'click' in bpl2.handleEvent(event):
                buttonFgColor = BLUE
		value = 0
		value1 = 0

		if value < 100 :
			if value1 < 100:	
				LEFT = 1 
				running = 1
				screen = pygame.display.set_mode((600, 500))
				while running:
					event = pygame.event.poll()
					if event.type == pygame.QUIT:
						running = 0
			     		elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
		     	     			num= random.randint(1,6)
						num1 = random.randint(1,6)
						print ('player1 number is')
						print(num)
						value += num
						print ('player1 in the position ')
						print(value)
						if value == 24:
							print("you r going back to 1")
							value = 1
							DISPLAYSURFACE.blit(ball, ballrect)
							pygame.draw.rect(screen, BLACK, [11,425, 20, 20], 2)
							pygame.display.flip()


						elif value == 55:
							print("you r going back to 13")
							value = 13
							DISPLAYSURFACE.blit(ball, ballrect)
							pygame.draw.rect(screen, BLACK, [325, 380, 20, 20], 2)
							pygame.display.flip()


						elif value == 71:
							print("you r going back to 29")
							value = 29
							DISPLAYSURFACE.blit(ball, ballrect)
							pygame.draw.rect(screen, BLACK, [370, 335, 20, 20], 2)
							pygame.display.flip()


						elif value == 88:
							print("you r going back to 67")
							value = 67
							DISPLAYSURFACE.blit(ball, ballrect)
							pygame.draw.rect(screen, BLACK, [280, 150, 20, 20], 2)
							pygame.display.flip()


						elif value == 99:	
							print("you r going back to 6")
							value = 6
							DISPLAYSURFACE.blit(ball, ballrect)
							pygame.draw.rect(screen, BLACK, [235, 425, 20, 20], 2)
							pygame.display.flip()


						if value == 8:
							print("congrates you r jumping to 31")
							value = 31
							DISPLAYSURFACE.blit(ball, ballrect)
							pygame.draw.rect(screen, BLACK, [415, 290, 20, 20], 2)
							pygame.display.flip()



						elif value == 15:
							print("congrates you r jumping to 97")
							value = 97
							DISPLAYSURFACE.blit(ball, ballrect)
							pygame.draw.rect(screen, BLACK, [145, 11, 20, 20], 2)
							pygame.display.flip()


						elif value == 42:
							print("congrates you r jumping to 81")
							value = 81
							DISPLAYSURFACE.blit(ball, ballrect)
							pygame.draw.rect(screen, BLACK, [11, 60, 20, 20], 2)
							pygame.display.flip()

						elif value == 66:
							print("congrates you r jumping to 87")
							value = 87
							DISPLAYSURFACE.blit(ball, ballrect)
							pygame.draw.rect(screen, BLACK, [280, 60, 20, 20], 2)
							pygame.display.flip()

						elif value >100:
							value = value - num
							
				
						print ('playr2 your number is')
						print(num1)
						value1 += num1
						print ('player2 r in the position ')
						print(value1)
						if value1 == 24:
							print("you r going back to 1")
							value1 = 1
							DISPLAYSURFACE.blit(ball, ballrect)
							pygame.draw.rect(screen, RED, [11,425, 20, 20], 2)
							pygame.display.flip()
						elif value1 == 55:
							print("you r going back to 13")
							value1 = 13
							DISPLAYSURFACE.blit(ball, ballrect)
							pygame.draw.rect(screen, RED, [325, 380, 20, 20], 2)
							pygame.display.flip()


						elif value1 == 71:
							value1 = 29
							print("you r going back to 29")
							DISPLAYSURFACE.blit(ball, ballrect)
							pygame.draw.rect(screen, RED, [370, 335, 20, 20], 2)
							pygame.display.flip()

						elif value1 == 88:
							print("you r going back to 67")
							value1 = 67
							DISPLAYSURFACE.blit(ball, ballrect)
							pygame.draw.rect(screen, RED, [280, 150, 20, 20], 2)
							pygame.display.flip()


						elif value1 == 99:	
							print("you r going back to 6")
							value1 = 6
							DISPLAYSURFACE.blit(ball, ballrect)
							pygame.draw.rect(screen, RED, [235, 425, 20, 20], 2)
							pygame.display.flip()


						if value1 == 8:
							print("congrates you r jumping to 31")
							value1 = 31
							DISPLAYSURFACE.blit(ball, ballrect)
							pygame.draw.rect(screen, RED, [415, 290, 20, 20], 2)
							pygame.display.flip()

						elif value1 == 15:
							print("congrates you r jumping to 97")
							value1 = 97
							DISPLAYSURFACE.blit(ball, ballrect)
							pygame.draw.rect(screen, RED, [145, 11, 20, 20], 2)
							pygame.display.flip()


						elif value1 == 42:
							print("congrates you r jumping to 81")
							value1 = 81	
							DISPLAYSURFACE.blit(ball, ballrect)
							pygame.draw.rect(screen, RED, [11, 60, 20, 20], 2)
							pygame.display.flip()

						elif value1 == 66:
							print("congrates you r jumping to 87")
							value1 = 87
							DISPLAYSURFACE.blit(ball, ballrect)
							pygame.draw.rect(screen, RED, [280, 60, 20, 20], 2)
							pygame.display.flip()
						elif value1 >100:
							value1 = value1 - num1
							
			
						if value == 100:
							print('player1 win')
							print('if you want to play again, click yes else click no')
							break
						
						elif value1 == 100:
							print('player2 win')
							print('you want to play again, click yes else click no')
							break
						
            if 'click' in bpl3.handleEvent(event):
		pygame.quit()
		sys.exit()
		break
				
	
            				
            if buttonFgColor is not None:
                for b in FgButtons:
                    b.fgcolor = buttonFgColor
            DISPLAYSURFACE.fill(black)
	    DISPLAYSURFACE.blit(ball, ballrect)

        for b in FgButtons:
            b.draw(DISPLAYSURFACE)
	    
            

        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    main()
