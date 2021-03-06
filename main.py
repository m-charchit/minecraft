from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
# creating complex shapes
# class Test_cube(Entity):
# 	def __init__(self):
# 		super().__init__(
# 			model = "cube",
# 			color = color.white,
# 			texture = "white_cube",
# 			rotation = Vec3(45,45,45) # three params x,y,z rotation
# 			)

# # create button
# class test_btn(Button):
# 	def __init__(self):
# 		super().__init__(
# 			parent = scene,
# 			model = "cube",
# 			texture = "brick",
# 			color = color.blue,
# 			highlight_color = color.red,
# 			pressed_color = color.green
# 			)
# 	def input(self,key):
# 		if self.hovered:
# 			if key == "left mouse down":
# 				print("hi")



# # create a instance of the game
# # this function will be called by ursina 
# def update():
# 	if held_keys['a']:
# 		block.x -= 2 * time.dt

# app = Ursina()

# block = Entity(model="quad", color=color.red, scale=(1,4),position=(3,2))

# #creating a texture
# sans_texture = load_texture("assets/Sans.png")
# sans = Entity(model="quad",texture=sans_texture)

# # test_c = Test_cube()
# test_but = test_btn()










app = Ursina()

window.title = "mincraft"        # The window title
window.borderless = False 
window.fullscreen = False              # Show a border         # Do not go Fullscreen
window.exit_button.visible = False      # Do not show the in-game red X that loses the window
window.fps_counter.enabled = True 

grass_texture = load_texture("assets/grass_block.png")
stone_texture = load_texture("assets/stone_block.png")
brick_texture = load_texture("assets/brick_block.png")
dirt_texture = load_texture("assets/dirt_block.png")
sky_texture = load_texture("assets/skybox.png")
arm_texture = load_texture("assets/arm_texture.png")
sound = Audio("assets/punch_sound",loop=False,autoplay=False)
block_pick = 1

def update():
	global block_pick
	if held_keys['left mouse'] or held_keys['right mouse']:
		hand.active()
	else:
		hand.passive()
	if held_keys['1']: block_pick = 1
	if held_keys['2']: block_pick = 2
	if held_keys['3']: block_pick = 3
	if held_keys['4']: block_pick = 4

class Voxel(Button):
	def __init__(self,position = (0,0,0),texture=grass_texture):
		super().__init__(
			parent= scene,
			position=position,
			model = "assets/block",
			origin_y = 0.5,
			texture = texture,
			color = color.color(0,0,random.uniform(0.9,1)),
			# highlight_color =  color.lime,
			scale = 0.5,
			)

	def input(self,key):
		if self.hovered:
			if key == 'left mouse down':
				sound.play()
				if block_pick == 1: voxel = Voxel(position=self.position + mouse.normal , texture=grass_texture)
				if block_pick == 2: voxel = Voxel(position=self.position + mouse.normal , texture=dirt_texture)
				if block_pick == 3: voxel = Voxel(position=self.position + mouse.normal , texture=brick_texture)
				if block_pick == 4: voxel = Voxel(position=self.position + mouse.normal , texture=stone_texture)
			if key == "right mouse down":
				destroy(self)
				sound.play()


class sky(Entity):
	def __init__(self):
		super().__init__(
			parent = scene,
			model = "sphere",
			texture = sky_texture,
			scale = 100,
			double_sided = True,
			)

class hand(Entity):
	def __init__(self):
		super().__init__(
			parent = camera.ui,
			model = "assets/arm",
			texture = arm_texture,
			scale = 0.2,
			rotation =  Vec3(150,-10,0),
			position = Vec2(0.4,-0.6)

			)
	def active(self):
		self.position = Vec2(0.4,-0.6)
	def passive(self):
		self.position =  Vec2(0.4,-0.7)

# voxel = Voxel()

for c in range(15):
	for r in range(15):
		voxel = Voxel(position = (r,0,c))

# make the first first_person_controller
player  = FirstPersonController()
sky = sky()
hand = hand()
# camera.position = Vec3(1,1,0)



app.run()