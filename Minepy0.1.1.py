from ursina import *
from ursina import texture
from ursina.prefabs.first_person_controller import FirstPersonController
from random import randint

app = Ursina()


grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture = load_texture('assets/dirt_block.png')
sky_texture = load_texture('assets/skybox.png')
arm_texture = load_texture('assets/arm_texture.png')
punch_sound = Audio('assets/punch_sound',loop = False, autoplay= False)
block_pick = 1
bm = "none"
world_size = randint(10,20)
block_selected = Text(text="block:"+" "+bm, color=color.black, scale=1.3, x= -0.88, y= 0.48)
fps_label = Text(text="FPS:", color=color.black, scale=1.4, x= 0.8, y= 0.5)

is_fullscreen = True
window.title = 'MinePy 0.1.1'
window.borderless = True
window.fullscreen = is_fullscreen
window.exit_button.visible = False
window.fps_counter.enabled = True


def update():
    global block_pick
    global bm
    global block_selected

    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()

    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4
    if held_keys['escape']: quit()
    if block_pick == 1:
        destroy(block_selected)
        bm = "Grass"
        block_selected = Text(text="block:"+" "+bm, color=color.black, scale=1.3, x= -0.88, y= 0.48)
    if block_pick == 2:
        destroy(block_selected)
        bm = "Stone"
        block_selected = Text(text="block:"+" "+bm, color=color.black, scale=1.3, x= -0.88, y= 0.48)
    if block_pick == 3:
        destroy(block_selected)
        bm = "Brick"
        block_selected = Text(text="block:"+" "+bm, color=color.black, scale=1.3, x= -0.88, y= 0.48)
    if block_pick == 4:
        destroy(block_selected)
        bm = "Dirt"
        block_selected = Text(text="block:"+" "+bm, color=color.black, scale=1.3, x= -0.88, y= 0.48)


class Voxel(Button):
    def __init__(self, position = (0,0,0), texture = grass_texture):
        super().__init__(
            parent = scene,
            position = position,
            model = 'assets/block',
            origin_y = 0.5,
            texture= texture,
            color = color.color(0,0, random.uniform(0.9,1)),
            #highlight_color = color.lime,
            scale = 0.5)

    def input(self,key):
        if self.hovered:
            if key == 'right mouse down':
                punch_sound.play()
                if block_pick == 1:
                    voxel = Voxel(position = self.position + mouse.normal, texture = grass_texture)
                elif block_pick == 2:
                    voxel = Voxel(position = self.position + mouse.normal, texture = stone_texture)
                elif block_pick == 3:
                    voxel = Voxel(position = self.position + mouse.normal, texture = brick_texture)
                elif block_pick == 4:
                    voxel = Voxel(position = self.position + mouse.normal, texture = dirt_texture)
            
            if key == 'left mouse down':
                punch_sound.play()
                destroy(self)

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = sky_texture,
            scale = 150,
            double_sided = True
        )

class Hand(Entity):
    def __init__(self):
        super().__init__(
        parent = camera.ui,
        model = 'assets/arm',
        texture = arm_texture,
        scale = 0.2,
        rotation = Vec3(150,-10,0),
        position = Vec2(0.4,-0.6)
        )
    def active(self):
        self.rotation = Vec3(150,-10,0)
        self.position = Vec2(0.3,-0.5)
    def passive(self):
        self.position = Vec2(0.4,-0.6)

for z in range(world_size):
    for x in range(world_size):
        voxel = Voxel(position = (x,0,z))

player = FirstPersonController()
sky = Sky()
hand = Hand()

app.run()
