import pygame

WIDTH = 750
HEIGHT = 750
FPS = 60
BLOCK_WIDTH = 10
DELTA_T = 1/10

gravity = 10
velocity = 10
floor_friction = 1
vel_x = 0
vel_y = 0
acc_x = 0
acc_y = gravity


def update_position(block):
	global vel_y, vel_x, acc_y, acc_x
	# floor friction
	# if (acc_x > 0):
	# 	acc_x-= floor_friction
	# if (acc_x < 0):
	# 	acc_x+= floor_friction


	vel_x += acc_x*DELTA_T
	vel_y += acc_y*DELTA_T

	# ensure we stay on screen vertically
	if block.y > HEIGHT - BLOCK_WIDTH: 
		# sitting on the ground
		block.y = HEIGHT - BLOCK_WIDTH
	elif block.y < BLOCK_WIDTH:
		block.y = BLOCK_WIDTH
		vel_y*=-1
	else:
		# falling	
		block.y += vel_y * DELTA_T

	# ensure we stay on the screen horizontally
	if block.x > WIDTH - BLOCK_WIDTH: 
		# against the right side
		block.x = WIDTH - BLOCK_WIDTH
		vel_x*=-1
		# acc_x*=-1
		acc_x /= 10
		print(f"acc_x: {acc_x}")
	elif block.x < BLOCK_WIDTH:
		# against the left side
		block.x =  BLOCK_WIDTH
		vel_x*=-1
		# acc_x*=-1
		acc_x /= 10
		print(f"acc_x: {acc_x}")
	else:
		block.x += vel_x * DELTA_T

	if keys_pressed[pygame.K_a]:
		acc_x = -5
	if keys_pressed[pygame.K_d]:
		acc_x = 5
	if keys_pressed[pygame.K_SPACE]:
		vel_y = -110


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
block_image = pygame.Surface((BLOCK_WIDTH, BLOCK_WIDTH))
block_image.fill("green")
block_rect = block_image.get_rect(topleft=(WIDTH/2,0))


clock = pygame.time.Clock()
time = 0
prev_x = None
current_x = None
while True:
	prev_x = block_rect.x
	keys_pressed = pygame.key.get_pressed()
	clock.tick(FPS)
	# time+= 1/60
	# print("Time is: ", time)
	WIN.fill("black")
	WIN.blit(block_image, (block_rect.x, block_rect.y))
	update_position(block_rect)
	pygame.display.update()
	current_x = block_rect.x
	print(current_x-prev_x)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()
		if event.type == pygame.KEYDOWN:
			if keys_pressed[pygame.K_SPACE]:
				pass