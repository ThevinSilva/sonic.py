import pygame as pg
import math
from animation_engine import *
from Hedgehog_Engine import *
from zone import Zone
from sensor import *
from collisions import *
from camera import *

def main():
    fps = 60; size = (320*4 ,224*4)
    pg.init()
    screen = pg.display.set_mode(size)
    spin_start = False
    jump_lock = False
    background = pg.image.load('tiles.png')
    #flag for the main game-loop

    #subject to change when running cycles get introduced
    clock = pg.time.Clock()
    player = sonic('jump_',Zone(640, 448).sonic_hitbox()[0:2],1,4,'right')
    all_sprites = pg.sprite.Group()
    all_sprites.add(player)
    pg.init()
    zone = Zone(player.rect.x, player.rect.y)
    right_lock = False; left_lock = False; spinmode =False
    tile(Zone(640, 448).screen)
    # block(Zone(640, 448).screen)
    ramp(Zone(640, 448).screen)
    X_pos = 1000
    floor = 8009
    Camera = camera(1280, 896)
    Engine = engine()
    while True:
        Camera.update(Engine.gsp)
        tiles = [ (n[1] * 64  - Camera.offset()[0], n[0] * 64 - Camera.offset()[1]) for n in tile.floor_tiles]
        # blocks = [ (n[1] * 64  - Camera.offset()[0], n[0] * 64 - Camera.offset()[1]) for n in block.block_tiles]
        ramps = [ (n[1] * 64  - Camera.offset()[0] , n[0] * 64 - Camera.offset()[1]) for n in ramp.ramp_tiles]
        sensor_lines = {'bottom_left': sensor_A(640, 448, player),
                        'bottom_right' : sensor_B(640, 448, player),
                        'mid_left' : sensor_C(640,448,player),
                        'mid_right' : sensor_D(640, 448, player),
                        'top_left': sensor_E(640,448,player),
                        'top_right' : sensor_F(640, 448, player)}
        button = None
        dt = clock.tick(fps)/1000
        Engine.direction = player.direction_returner

        ''' Loop that checks first '''
        keys = pg.key.get_pressed()
        if keys[pg.K_a] and not keys[pg.K_s]:
            if not left_lock:
                Engine.movement = 'left'
        elif keys[pg.K_d] and not keys[pg.K_s]:
            if not right_lock:
                Engine.movement = 'right'
        else:
            Engine.movement = 'None'

        '''note implement A variable jump system that requires holding the button and a lot more effort'''
        if keys[pg.K_w]:
            button = 'look_up'



        if keys.count(1) == 0:
            jump_lock = False
        else:
            spinmode = False

        if keys[pg.K_SPACE] and Engine.onGround == True and not keys[pg.K_s] and jump_lock == False:
            Engine.movement = 'jump'
        if keys[pg.K_s] and Engine.onGround == True:
            if player.velocity.x != 0:
                Engine.movement = 'roll'
            else:
                button = 'look_down'
            jump_lock = True
            for event in pg.event.get():
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    # smoke trails
                    spin_start = True
                    Engine.movement = 'spin_charge'
                if event.type == pg.KEYUP:
                    if spin_start and event.key == pg.K_s and Engine.onGround == True and jump_lock == True:
                        Engine.movement = 'spin_dash'
                        spinmode = True
                        spin_start = False
                        Engine.spin_rev = 0

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()



        if spin_start:
            button = 'spin'

        sensor_lines['mid_left'].floor_mode()
        sensor_lines['mid_right'].floor_mode()

        print(f'movement: {Engine.gsp}')
        Camera.velocity.x, Camera.velocity.y = Engine.gsp, Engine.ysp
        player.velocity.x , player.velocity.y = Engine.gsp, Engine.ysp


        ''' collision detection using sensor lines '''

        if pushing_left(sensor_lines,tiles,Camera,Engine) != None:
            button = pushing_left(sensor_lines, tiles, Camera, Engine)

        if pushing_right(sensor_lines, tiles, Camera, Engine) != None:
            button = pushing_right(sensor_lines,tiles,Camera, Engine)

        fall = falling(sensor_lines, tiles,player,Engine,ramps,zone.screen,ramp,Camera.offset(),Camera)

        if fall != None:
            floor = fall['floor']
            sonic.angle = fall['angle']
            # Engine.angle = fall['angle']
            # Engine.xsp = Engine.gsp * math.cos(fall['angle'])
            # Engine.ysp = Engine.gsp * - math.sin(fall['angle'])



        ''' animation '''
        screen.fill((0, 0, 0))
        # screen.blit(background,(0,0))
        [screen.blit(pg.image.load('tile.png'), n) for n in tiles]
        [screen.blit(pg.image.load('slope_45.png'), n ) for n in ramps]
        screen.blit(pg.image.load('active_tile.png'),( floor,X_pos))
        player.refresh(dt,button,spinmode)
        all_sprites.draw(screen)
        [sensor_lines.get(n).draw(screen) for n in sensor_lines]
        pg.display.update()


if __name__ == '__main__':
    main()
