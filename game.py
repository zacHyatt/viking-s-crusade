# Primes.cpp
# By Zachary Hyatt
# Copyright 2024
#  my First py Game © 2024 by Zachary Hyatt is licensed under CC BY-NC-SA 4.0
import pygame
import random
import py_compile
py_compile.compile ('game.py')
# pygame setup
pygame.init()
Running = True
Screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
dt = 0
player_img = pygame.image.load('./craftpix-891165-assassin-mage-viking-free-pixel-art-game-heroes/PNG/Knight/knight.png')
player_right = pygame.transform.scale(player_img,(200,200))
player_left = pygame.transform.flip(player_right, True, False)
player_updated = player_right
background_img = pygame.image.load('./craftpix-net-776320-free-pixel-art-fantasy-2d-battlegrounds/PNG/Battleground1/Bright/Battleground1.png')
background_updated = pygame.transform.scale(background_img, (1920,1080))
enemy_list = []
enemy_img = pygame.image.load('./craftpix-net-281834-free-chaos-monsters-32x32-icon-pack/PNG/Transperent/Icon28.png')
enemy_updated = pygame.transform.scale(enemy_img,(100,100))
SPAWNENEMY = pygame.USEREVENT+1
pygame.time.set_timer(SPAWNENEMY,10)

def load_images(path):
	"""
	Loads all images in directory. The directory must only contain images.

	Args:
		path: The relative or absolute path to the directory to load images from.

	Returns:
		List of images.
	"""
	images = []
	for file_name in os.listdir(path):
		image = pygame.image.load(path + os.sep + file_name).convert()
		images.append(image)
	return images

class Player:
	def __init__(self):
		self.ypos = 372
		self.xpos = 0
		self.height = 200
		self.width = 200
		self.playerUpdated = player_updated
	def create_player(self):
		Playerss = pygame.Rect(self.xpos,self.ypos,self.height,self.width)
		Screen.blit(player_updated, (Playerss.x, Playerss.y))

sizee = random.randint(10,40)
randomX = random.randint(0,700)

class Enemy:
	def __init__(self):
		self.recycle()   # set the position & size initially

	def recycle( self ):
		# start or re-start an enemy position
		self.size = random.randint(10,40)
		self.xval = random.randint(50,1850)
		self.yval = random.randint(500,1000)             # off the screen-top
		self.rect = pygame.Rect( self.xval, self.yval, self.size, self.size )

	def draw( self, screen ):

		Screen.blit(enemy_updated, (self.xval, self.yval))

	def create_enemy(self):
		global enemy_list
		new_enemy = Enemy()               # create a new Enemy
		enemy_list.append( new_enemy )    # add it to the list


Player = Player()
Enemys = Enemy()
while Running:
	keys = pygame.key.get_pressed()
	Screen.fill((0,0,0))
	Screen.blit(background_updated, (0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			Running = False
		if keys[pygame.K_w]:
			if Player.ypos>372:
				Player.ypos -= 300 * dt
		if keys[pygame.K_a]:
			Player.xpos -= 300 * dt
			if Player.xpos<-256:
				Player.xpos = 1920
			player_updated = player_left
		if keys[pygame.K_s]:
			if Player.ypos<900:
				Player.ypos += 300 * dt
		if keys[pygame.K_d]:
			Player.xpos += 300 * dt
			if Player.xpos>1920:
				Player.xpos = -100
			player_updated = player_right

		if event.type == SPAWNENEMY:
			if len(enemy_list)<10:
				Enemys.create_enemy()
	for enemy in enemy_list:
		enemy.draw( Screen )
		if ( enemy.yval < 600 ):          # TODO - don't use a fixed size
			enemy.recycle()               # move back to top
	print(Player.ypos)

	Player.create_player()
	dt = clock.tick(60) / 1000
	pygame.display.update()

