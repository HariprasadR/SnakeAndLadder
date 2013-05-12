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
    b1 = pygbutton.PygButton((11, 11, 45, 45), '100')
    b2 = pygbutton.PygButton((11, 60, 45, 45), 'st42-81')
    b3 = pygbutton.PygButton((11, 110, 45, 45), '80')
    b4 = pygbutton.PygButton((11, 160, 45, 45), '61')
    b5 = pygbutton.PygButton((11, 210, 45, 45), '60')
    b6 = pygbutton.PygButton((11, 260, 45, 45), '41')
    b7 = pygbutton.PygButton((11, 310, 45, 45), '40')
    b8 = pygbutton.PygButton((11, 360, 45, 45), '21')
    b9 = pygbutton.PygButton((11, 410, 45, 45), '20')
    b10 = pygbutton.PygButton((11, 460, 45, 45), 'sn24-1')
    b11 = pygbutton.PygButton((61,11, 45, 45), 'sn99-6')
    b12 = pygbutton.PygButton((61, 60, 45, 45), '82')
    b13 = pygbutton.PygButton((61, 110, 45, 45), '79')
    b14 = pygbutton.PygButton((61, 160, 45, 45), '62')
    b15 = pygbutton.PygButton((61, 210, 45, 45), '59')
    b16 = pygbutton.PygButton((61, 260, 45, 45), 'st42-81')
    b17 = pygbutton.PygButton((61, 310, 45, 45), '39')
    b18 = pygbutton.PygButton((61, 360, 45, 45), '22')
    b19 = pygbutton.PygButton((61, 410, 45, 45), '19')
    b20 = pygbutton.PygButton((61, 460, 45, 45), '2')
    b21 = pygbutton.PygButton((111, 11, 45, 45), '98')
    b22 = pygbutton.PygButton((111, 60, 45, 45), '83')
    b23 = pygbutton.PygButton((111, 110, 45, 45), '78')
    b24 = pygbutton.PygButton((111, 160, 45, 45), '63')
    b25 = pygbutton.PygButton((111, 210, 45, 45), '58')
    b26 = pygbutton.PygButton((111, 260, 45, 45), '43')
    b27 = pygbutton.PygButton((111, 310, 45, 45), '38')
    b28 = pygbutton.PygButton((111, 360, 45, 45), '23')
    b29 = pygbutton.PygButton((111, 410, 45, 45), '18')
    b30 = pygbutton.PygButton((111, 460, 45, 45), '3')
    b31 = pygbutton.PygButton((161, 11, 45, 45), 'st15-97')
    b32 = pygbutton.PygButton((161, 60, 45, 45), '84')
    b33 = pygbutton.PygButton((161, 110, 45, 45), '77')
    b34 = pygbutton.PygButton((161, 160, 45, 45), '64')
    b35 = pygbutton.PygButton((161, 210, 45, 45), '57')
    b36 = pygbutton.PygButton((161, 260, 45, 45), '44')
    b37 = pygbutton.PygButton((161, 310, 45, 45), '37')
    b38 = pygbutton.PygButton((161, 360, 45, 45), 'sn24-1')
    b39 = pygbutton.PygButton((161, 410, 45, 45), '17')
    b40 = pygbutton.PygButton((161, 460, 45, 45), '4')
    b41 = pygbutton.PygButton((211, 11, 45, 45), '96')
    b42 = pygbutton.PygButton((211, 60, 45, 45), '85')
    b43 = pygbutton.PygButton((211, 110, 45, 45), '76')
    b44 = pygbutton.PygButton((211, 160, 45, 45), '65')
    b45 = pygbutton.PygButton((211, 210, 45, 45), '56')
    b46 = pygbutton.PygButton((211, 260, 45, 45), '45')
    b47 = pygbutton.PygButton((211, 310, 45, 45), '36')
    b48 = pygbutton.PygButton((211, 360, 45, 45), '25')
    b49 = pygbutton.PygButton((211, 410, 45, 45), '16')
    b50 = pygbutton.PygButton((211, 460, 45, 45), '5')
    b51 = pygbutton.PygButton((261, 11, 45, 45), '95')
    b52 = pygbutton.PygButton((261, 60, 45, 45), '86')
    b53 = pygbutton.PygButton((261, 110, 45, 45), '75')
    b54 = pygbutton.PygButton((261, 160, 45, 45), 'st66-87')
    b55 = pygbutton.PygButton((261, 210, 45, 45), 'sn55-13')
    b56 = pygbutton.PygButton((261, 260, 45, 45), '46')
    b57 = pygbutton.PygButton((261, 310, 45, 45), '35')
    b58 = pygbutton.PygButton((261, 360, 45, 45), '26')
    b59 = pygbutton.PygButton((261, 410, 45, 45), '15')
    b60 = pygbutton.PygButton((261, 460, 45, 45), 'sn99-6')
    b61 = pygbutton.PygButton((311, 11, 45, 45), '94')
    b62 = pygbutton.PygButton((311, 60, 45, 45), 'st66-87')
    b63 = pygbutton.PygButton((311, 110, 45, 45), '74')
    b64 = pygbutton.PygButton((311, 160, 45, 45), 'sn88-67')
    b65 = pygbutton.PygButton((311, 210, 45, 45), '54')
    b66 = pygbutton.PygButton((311, 260, 45, 45), '47')
    b67 = pygbutton.PygButton((311, 310, 45, 45), '34')
    b68 = pygbutton.PygButton((311, 360, 45, 45), '27')
    b69 = pygbutton.PygButton((311, 410, 45, 45), '14')
    b70 = pygbutton.PygButton((311, 460, 45, 45), '7')
    b71 = pygbutton.PygButton((361, 11, 45, 45), '93')
    b72 = pygbutton.PygButton((361, 60, 45, 45), 'sn88-67')
    b73 = pygbutton.PygButton((361, 110, 45, 45), '73')
    b74 = pygbutton.PygButton((361, 160, 45, 45), '68')
    b75 = pygbutton.PygButton((361, 210, 45, 45), '53')
    b76 = pygbutton.PygButton((361, 260, 45, 45), '48')
    b77 = pygbutton.PygButton((361, 310, 45, 45), '33')
    b78 = pygbutton.PygButton((361, 360, 45, 45), '28')
    b79 = pygbutton.PygButton((361, 410, 45, 45), 'sn55-13')
    b80 = pygbutton.PygButton((361, 460, 45, 45), 'st8-31')
    b81 = pygbutton.PygButton((411, 11, 45, 45), '92')
    b82 = pygbutton.PygButton((411, 60, 45, 45), '89')
    b83 = pygbutton.PygButton((411, 110, 45, 45), '72')
    b84 = pygbutton.PygButton((411, 160, 45, 45), '69')
    b85 = pygbutton.PygButton((411, 210, 45, 45), '52')
    b86 = pygbutton.PygButton((411, 260, 45, 45), '49')
    b87 = pygbutton.PygButton((411, 310, 45, 45), '32')
    b88 = pygbutton.PygButton((411, 360, 45, 45), 'sn71-29')
    b89 = pygbutton.PygButton((411, 410, 45, 45), '12')
    b90 = pygbutton.PygButton((411, 460, 45, 45), '9')
    b91 = pygbutton.PygButton((461, 11, 45, 45), '91')
    b92 = pygbutton.PygButton((461, 60, 45, 45), '90')
    b93 = pygbutton.PygButton((461, 110, 45, 45), 'sn71-29')
    b94 = pygbutton.PygButton((461, 160, 45, 45), '70')
    b95 = pygbutton.PygButton((461, 210, 45, 45), '51')
    b96 = pygbutton.PygButton((461, 260, 45, 45), '50')
    b97 = pygbutton.PygButton((461, 310, 45, 45), 'st8-31')
    b98 = pygbutton.PygButton((461, 360, 45, 45), '30')
    b99 = pygbutton.PygButton((461, 410, 45, 45), '11')
    b100 = pygbutton.PygButton((461, 460, 45, 45), '10')
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
