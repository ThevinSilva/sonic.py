import pygame
'''collision routines'''

def move(camera,player,floor):
    # player.rect.move_ip(0, floor - (player.rect.y + 192))
    camera.rect.move_ip(0, floor - (player.rect.y + 192))
def get_rect(obj):
    return pygame.Rect(obj[0], obj[1], 64, 64)

def col_det(sensor,_list):

    for i in _list:
        if get_rect(i).colliderect(sensor):
            return i
    else:
        return None

def ramp_detection(sensor_lines,ramps,engine,player,ramp,offset):
        y_pos = col_det(sensor_lines['bottom_right'], ramps)[1] + 64
        index = int(round((sensor_lines['bottom_right'].rect.x - col_det(sensor_lines['bottom_right'], ramps)[0]) / 5))
        return y_pos - sorted([n[1] for n in ramp.mask])[index] + 4

# bug test patch the glitching
def pushing_left(sensor_lines,tiles,player,engine):
    if col_det(sensor_lines['mid_left'],tiles) != None and \
                    col_det(sensor_lines['bottom_left'],tiles)!= None:
        if engine.gsp < 0:
            engine.gsp = 0
        return 'push_left'

def pushing_right(sensor_lines,tiles,camera,engine):
    if col_det(sensor_lines['mid_right'], tiles) != None and \
                    col_det(sensor_lines['bottom_right'],tiles) != None:
        if engine.gsp > 0:
            engine.gsp = 0
        return 'push_right'


def falling(sensor_lines,tiles ,player,engine,ramps,zone, ramp, offset,camera):
    # ramp(uneven terrain) detection
    angle = 0
    if col_det(sensor_lines['top_right'], tiles) != None and col_det(sensor_lines['top_right'], tiles) == None:
        engine.ysp = 0
        ceilling = col_det(sensor_lines['top_right'], tiles)[1]
        move(camera, player, ceilling - 64)
    elif col_det(sensor_lines['top_right'], tiles) == None and col_det(sensor_lines['top_right'], tiles) != None:
        engine.ysp = 0
        ceilling = col_det(sensor_lines['top_left'], tiles)[1]
        move(camera, player, ceilling - 64)


    if col_det(sensor_lines['bottom_right'], ramps) != None:
        floor = ramp_detection(sensor_lines,ramps,engine,player,ramp,offset)
        X_pos = col_det(sensor_lines['bottom_right'], ramps)[0]
        angle = zone[round((col_det(sensor_lines['bottom_right'], ramps)[1] + offset[1])/64) ]\
            [round((col_det(sensor_lines['bottom_right'], ramps)[0] + offset[0])/64)]
        move(camera,player, floor)
        engine.onGround = True
        engine.ysp = 0


        return {'floor': floor, 'x_pos': X_pos, 'angle': angle}
    if col_det(sensor_lines['bottom_right'],tiles) != None and col_det(sensor_lines['bottom_left'],tiles) != None:
        floor = col_det(sensor_lines['bottom_right'], tiles)[1]
        X_pos = col_det(sensor_lines['bottom_right'], tiles)[0]
        engine.ysp = 0
        engine.onGround = True
        move(camera,player, floor)

        return {'floor': floor, 'x_pos': X_pos, 'angle': angle}

    #left sensor
    # bottom_left_sense on
    elif col_det(sensor_lines['bottom_right'],tiles) == None and col_det(sensor_lines['bottom_left'],tiles) != None:
        floor = col_det(sensor_lines['bottom_left'], tiles)[1]
        X_pos = col_det(sensor_lines['bottom_left'], tiles)[0]
        engine.ysp = 0
        engine.onGround = True
        move(camera,player, floor)

        # if (player.rect.centerx -32 ) >= (col_det(sensor_lines['bottom_left'], tiles.floor_tiles)[1]) + 64:
        #     button = 'border_left'
        return {'floor': floor, 'x_pos': X_pos, 'angle': angle}
    #right sensor
    # bottom_right_sense on
    elif col_det(sensor_lines['bottom_left'], tiles) == None and col_det(sensor_lines['bottom_right'], tiles) != None:
        floor = col_det(sensor_lines['bottom_right'], tiles)[1]
        X_pos = col_det(sensor_lines['bottom_right'], tiles)[0]
        engine.ysp = 0
        engine.onGround = True
        move(camera,player,floor)

        # if (player.rect.centerx -32) <= (col_det(sensor_lines['bottom_right'], tiles.floor_tiles)[1]):
        #     button = 'border_right'
        return {'floor': floor, 'x_pos': X_pos, 'angle': angle}
    else:
        engine.ysp += engine.grv
        engine.onGround = False
        return


