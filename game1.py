def main():
	#Acessing library to use
	import random
	import pygame
	import time
	#starting pygame
	pygame.init()
	#pygame.display.set_caption('Game 1')
	
	#defining certain variables to use
	screen = pygame.display.set_mode((500, 400)) #add a screen of defined pixels to use in game
	pygame.display.set_caption('Game 1')
	image_file = 'wall3.jpg'
	done = False
	is_blue = True
	whileplaying=True
	x = 220
	y = 170
	score = 0
	dx=20
	zy=20
	block=['','','','','','','','','','','','','','','','','','']
	dy=['','','','','','','','','','','','','']
	#crash_sound = pygame.mixer.Sound("crash.wav")
	
	# defining random variables for the position of blocks
	for i in range(1,6):
	    dy[i] = random.randint(50,200)
	for i in range(6,13):
	    dy[i] = random.randint(200,500)
	for i in range (1,15):
	    block[i] =random.randint(1,350)
	#pygame.mixer.music.load('music1.wav')
	#pygame.mixer.music.play(-1)
	#Defining several variables to use in screen dispaly 
	background = pygame.image.load(image_file).convert()
	clock = pygame.time.Clock()
	font = pygame.font.Font(pygame.font.get_default_font(), 18)
	font1 = pygame.font.Font(pygame.font.get_default_font(),13)
	font3 = pygame.font.Font(pygame.font.get_default_font(),25)
	font4 = pygame.font.Font(pygame.font.get_default_font(),13)
	text_surface = font.render('Collided', True, pygame.Color(0,255,0))
	screen_text1=font1.render('WELCOME',True,pygame.Color(0,200,0))
	screen_text2=font1.render('Rules:Move the block to the same coloured block ,you will get 5 points ',True,pygame.Color(0,0,200))
	screen_text3=font4.render('Collision with dissimilar result in minus 5.Dont make 5 collission.',True,pygame.Color(200,0,0))
	screen_text4=font1.render('Change the color of your block by pressing UP or DOWN KEY',True,pygame.Color(0,0,200))
	quit_text1=font3.render('OOPS!!!',True,pygame.Color(0,0,255))
	quit_text2=font3.render('YOU HAVE TO RERUN THE PROGRAM',True,pygame.Color(0,0,255))
	quit_text3=font3.render(f'YOUR SCORE= '+ str(score),True,pygame.Color(0,0,255))
	quit_text4 = font3.render('PRESS ENTER KEY TO RESTART',True,pygame.Color(0,255,20))
	def final(color,x):
	    
	    for i in range(6,13):
	        dy[i] = -100
	    for i in range (1,15):
	        block[i] =-100
	    x=-100
	    y=0
	    dx=0
	    color=(40,45,50)
	    screen.fill(pygame.Color(40,45,50))
	    screen.blit(quit_text3,(150,150))
	    screen.blit(quit_text1,(200,200))
	    screen.blit(quit_text2,(10,250))
	    screen.blit(quit_text4,(0,0))
	    return x
	def condition(score,dx,dy,zy):
	    
	    if color == (255 , 0, 0) :
	        if rect.colliderect(rect1):
	            score+=5
	            screen.blit(text_surface, dest=(0,0))
	            pygame.time.wait(5) #dx=dx+20
	            block[1]=random.randint(1,400)
	            dy[1]=random.randint(50,380)
	        if rect.colliderect(rect2):
	            score-=5
	            screen.blit(text_surface, dest=(0,0))
	            dx=dx+5
	            zy=zy+5
	            dy[2]=random.randint(50,380)
	            block[2] =random.randint(1,350)
	 #               pygame.mixer.Sound.play(crash_sound)
	        if rect.colliderect(rect3):
	            score+=5
	            screen.blit(text_surface, dest=(0,0))
	            pygame.time.wait(5) #dx= dx+20
	            block[3]=random.randint(1,400)
	            dy[3]=random.randint(50,380)
	        if rect.colliderect(rect4):
	            score-=5
	            screen.blit(text_surface, dest=(0,0))
	            dx=dx+5
	            zy=zy+5
	            dy[4]=random.randint(50,380)
	            block[4]=random.randint(1,400)
	        if rect.colliderect(rect5):
	            score+=5
	            screen.blit(text_surface, dest=(0,0))
	            #dx=dx+20
	            dy[5]=random.randint(50,380)
	            block[5]=random.randint(1,400)
	        if rect.colliderect(rect6):
	            score-=5
	            screen.blit(text_surface, dest=(0,0))
	            dx=dx+5
	            zy=zy+5
	            dy[6]=random.randint(50,380)
	            block[6]=random.randint(1,400)
	        if rect.colliderect(rect7):
	            score+=5
	            screen.blit(text_surface, dest=(0,0))
	            #dx=dx+20
	            dy[7]=random.randint(50,380)
	            block[7]=random.randint(1,400)
	        if rect.colliderect(rect8):
	            score-=5
	            screen.blit(text_surface, dest=(0,0))
	            dx=dx+5
	            zy=zy+5
	            dy[8]=random.randint(50,380)
	            block[8]=random.randint(1,400)
	        if rect.colliderect(rect9):
	            score+=5
	            screen.blit(text_surface, dest=(0,0))
	                #dx=dx+20
	            dy[9]=random.randint(50,380)
	            block[9]=random.randint(1,400)
	        if rect.colliderect(rect10):
	            score-=5
	            screen.blit(text_surface, dest=(0,0))
	            dx=dx+5
	            zy=zy+5
	            dy[10]=random.randint(50,380)
	            block[10]=random.randint(1,400)
	        if rect.colliderect(rect11):
	            score+=5
	            screen.blit(text_surface, dest=(0,0))
	            #dx=dx+20
	            dy[11]=random.randint(50,380)
	            block[11]=random.randint(1,400)
	        if rect.colliderect(rect12):
	            score-=5
	            screen.blit(text_surface, dest=(0,0))
	            dx=dx+5
	            zy=zy+5
	            dy[12]=random.randint(50,380)
	            block[12]=random.randint(1,400)
	    if color == (0 , 0, 255) :
	        
	        if rect.colliderect(rect1):
	            score = score-5
	            screen.blit(text_surface, dest=(0,0))
	            dx=dx+5
	            zy=zy+5
	            dy[1]=random.randint(50,380)
	            block[1]=random.randint(1,400)
	        if rect.colliderect(rect2):
	            score = score+5
	            screen.blit(text_surface, dest=(0,0))
	              #dx=dx+20
	            dy[2]=random.randint(50,380)
	            block[2]=random.randint(1,400)
	        if rect.colliderect(rect3):
	            score-=5
	            screen.blit(text_surface, dest=(0,0))
	            dx= dx+5
	            zy=zy+5
	            dy[3]=random.randint(50,380)
	            block[3]=random.randint(1,400)
	        if rect.colliderect(rect4):
	            score+=5
	            screen.blit(text_surface, dest=(0,0))
	            #dx=dx+20
	            dy[4]=random.randint(50,380)
	            block[4]=random.randint(1,400)
	        if rect.colliderect(rect5):
	            score-=5
	            screen.blit(text_surface, dest=(0,0))
	            dx=dx+5
	            zy=zy+5
	            dy[5]=random.randint(50,380)
	            block[5]=random.randint(1,400)
	        if rect.colliderect(rect6):
	            score+=5
	            screen.blit(text_surface, dest=(0,0))
	              #dx=dx+20
	            dy[6]=random.randint(50,380)
	            block[6]=random.randint(1,400)
	        if rect.colliderect(rect7):
	            score-=5
	            screen.blit(text_surface, dest=(0,0))
	            dx=dx+5
	            zy=zy+5
	            dy[7]=random.randint(50,380)
	            block[7]=random.randint(1,400)
	        if rect.colliderect(rect8):
	            score+=5
	            screen.blit(text_surface, dest=(0,0))
	                #dx=dx+20
	            dy[8]=random.randint(50,380)
	            block[8]=random.randint(1,400)
	        if rect.colliderect(rect9):
	            score-=5
	            screen.blit(text_surface, dest=(0,0))
	            dx=dx+5
	            zy=zy+5
	            dy[9]=random.randint(50,380)
	            block[9]=random.randint(1,400)
	        if rect.colliderect(rect10):
	            score+=5
	            screen.blit(text_surface, dest=(0,0))
	             #dx=dx+20
	            dy[10]=random.randint(50,380)
	            block[10]=random.randint(1,400)
	        if rect.colliderect(rect11):
	            score-=5
	            screen.blit(text_surface, dest=(0,0))
	            dx=dx+5
	            zy=zy+5
	            dy[11]=random.randint(50,380)
	            block[11]=random.randint(1,400)
	        if rect.colliderect(rect12):
	            score+=5
	            screen.blit(text_surface, dest=(0,0))
	            #dx=dx+20
	            dy[12]=random.randint(50,380)
	            block[12]=random.randint(1,400)
	    return score,dx,dy,zy
	
	
	#starting the game loop. Contains the part which should run continuously
	while not done:
	        for event in pygame.event.get():
	                if event.type == pygame.QUIT:
	                        quit()
	                if event.type == pygame.KEYDOWN and (event.key == pygame.K_UP or event.key == pygame.K_DOWN):
	                        is_blue = not is_blue
	                if event.type == pygame.KEYDOWN and (event.key == pygame.K_RETURN):
	                    whileplaying =True
	                    main()
	        pressed = pygame.key.get_pressed()
	        if pressed[pygame.K_w]: y -=2
	        if pressed[pygame.K_s]: y += 2
	        if pressed[pygame.K_a]: x -= 2
	        if pressed[pygame.K_d]: x += 2
	        if y<=50: y=50
	        if x<=0: x=0
	        if x>=500-dx: x=500-dx
	        if y>=400-zy: y=400-zy
	
	        screen.blit(background,(0,0))
	
	        screen.blit(screen_text1,(200,0))
	        screen.blit(screen_text2,(0,12))
	        screen.blit(screen_text3,(0,24))
	        screen.blit(screen_text4,(0,36))
	        if is_blue: color = (0, 0, 255)
	        else: color = (255, 0, 0)
	
	#Setting endcondition of gameplay
	        quit_text3=font3.render(f'YOUR SCORE= '+ str(score),True,pygame.Color(0,0,255))
	        area=dx*zy
	        
	
	            
	        
	        if area>= 2025:
	            screen.fill(pygame.Color(40,45,50))
	            whileplaying=False
	            x=final(color,x)
	            
	            
	            
	# Defining a player block
	        rect = pygame.draw.rect(screen, color, pygame.Rect(x, y, dx, zy))
	
	#Defining random blocks for gameplay
	        rect1 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(block[1], dy[1], 20, 20))
	        rect3 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(block[3], dy[3], 20, 20))
	        rect2 = pygame.draw.rect(screen, (0, 0, 255), pygame.Rect((block[2]), dy[2], 20, 20))
	        rect4 = pygame.draw.rect(screen, (0, 0, 255), pygame.Rect((block[4]), dy[4], 20, 20))
	        rect5 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect((block[5]), dy[5], 20, 20))
	        rect6 = pygame.draw.rect(screen, (0, 0, 250), pygame.Rect((block[6]) ,dy[6] , 20, 20))
	        rect7 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect((block[7]), dy[7], 20, 20))
	        rect8 = pygame.draw.rect(screen, (0, 0, 255), pygame.Rect((block[8]), dy[8], 20, 20))
	        rect10 = pygame.draw.rect(screen, (0, 0, 255), pygame.Rect((block[10]), dy[10], 20, 20))
	        rect9 = pygame.draw.rect(screen, (250, 0, 0), pygame.Rect((block[9]), dy[9], 20, 20))
	        rect12 = pygame.draw.rect(screen, (0, 0, 255), pygame.Rect((block[12]), dy[12], 20, 20))
	        rect11 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect((block[11]), dy[11], 20, 20))
	
	        score_text = font.render(f'score ='+str(score), True,pygame.Color(100,0,0))
	        screen.blit(score_text, dest=(390,35))
	
	        if (whileplaying):
	            score,dx,dy,zy=condition(score,dx,dy,zy)
	            condition(score,dx,dy,zy)
	
	#Setting up so that game gat updated
	        pygame.display.flip()
	        clock.tick(60)
	
main()
