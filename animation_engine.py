import pygame
pygame.init()
screen = pygame.display.set_mode((320 * 4, 224 * 4))
clock = pygame.time.Clock()
fps = 60

# print(render_buffer('idle_',1,4))

class sonic(pygame.sprite.Sprite):
    frames = []
    angle = 0
    def __init__(self,name,position,start, end, direction):
        super(sonic, self).__init__()
        self.name = name
        self.start = start
        self.end = end
        self.direction = direction
        self.position = position

        #hitbox
        self.rect = pygame.Rect((self.position), (192,260))                                                             # CHANGE SUCH THAT THE HITBOX CHANGES SIZE WHEN SPIN DASHING
        sonic.frames = self.render_buffer(self.name, self.start, self.end, sonic.angle)


        if self.direction == 'right':
            sonic.frames = sonic.frames

        else:
            sonic.frames = [pygame.transform.flip(frame, True, False) for frame in sonic.frames]
            # sonic.angle = 180 - sonic.angle

        # requirements for animation to work
        # dependencies for the refresh function
        self.index = 0
        self.image = sonic.frames[self.index]  # 'image' is the current image of the animation.
        self.animation_time = 0.075
        self.current_time = 0
        self.velocity = pygame.math.Vector2(0,0)

    @property
    def direction_returner(self):
        return self.direction

    @direction_returner.setter
    def direction_returner(self,direction):
        self.direction = direction

    @staticmethod
    def rot_center(image, angle):
        '''
        rotate an image while keeping its center and size

        link - http://www.pygame.org/wiki/RotateCenter?parent=CookBook%22here%22

        :param image:
        :param angle:
        :return:
        '''

        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image

    def render_buffer(self, name, start, end, angle):
        frames = [self.rot_center(pygame.image.load(name + str(i) + '.png'), angle) for i in range(start, end)]
        return frames

    def refresh(self,dt,button,spinmode):
        self.button = button
        self.spinmode = spinmode

        if self.direction != 'right' :
            sonic.angle = - sonic.angle

        ''' jumping'''

        if (self.velocity.x > 0 and self.velocity.y != 0) or self.velocity.y != 0:
            sonic('jump_', self.position, 1, 4, 'right')
        elif self.velocity.x < 0 and self.velocity.y != 0:
            sonic('jump_', self.position, 1, 4, 'left')

        ''' spinning '''
        if self.spinmode == True:
            if self.velocity.x > 0:
                sonic('spin_', self.position, 1,2,'right')
            if self.velocity.x < 0:
                sonic('spin_', self.position, 1, 2, 'left')



        ''' right '''

        #running normal right
        if self.velocity.x > 0 and self.velocity.y == 0:  # Use the right images if sprite is moving right.
            self.direction = 'right'
            sonic('run_', self.position, 3,9, 'right')
        #up stare
        elif self.button == 'look_up' and self.direction == 'right' and self.velocity.y == 0 :
            sonic('idle_', self.position, 3, 4, 'right')
        #down stare
        elif self.button == 'look_down' and self.direction == 'right' and self.velocity.y == 0 :
            sonic('idle_', self.position, 6, 7, 'right')
        #spin_right
        elif self.button == 'spin' and self.direction == 'right' and self.velocity.y == 0 :
            sonic('spin_', self.position, 3, 7, 'right')
        #idle left
        elif self.direction == 'right' and self.velocity.x == 0 and self.velocity.y == 0:
            sonic('idle_', self.position,1,2, 'right')
        # border animation



        ''' left movement'''
        # running normal right
        if self.velocity.x < 0 and self.velocity.y == 0:
            self.direction = 'left'
            sonic('run_', self.position, 3, 9, 'left')
        # up stare
        elif self.button == 'look_up' and self.direction == 'left' and self.velocity.y == 0 :
            sonic('idle_', self.position, 3, 4, 'left')
        # down stare
        elif self.button == 'look_down'and self.direction == 'left' and self.velocity.y == 0:
            sonic('idle_', self.position, 6, 7, 'left')
        # spin_right
        elif self.button == 'spin' and self.direction == 'left' and self.velocity.y == 0 :
            sonic('spin_', self.position, 3, 7, 'left')
        # idle left
        elif self.direction == 'left' and self.velocity.x == 0 and self.velocity.y == 0:
            sonic('idle_', self.position, 1, 2, 'left')


        ''' high speed(peel out/ spinning legs) - right '''

        if 16 < self.velocity.x < 24:
            sonic('run_', self.position, 9, 12, 'right')

        if self.velocity.x >= 24:
            sonic('run_', self.position, 13, 16, 'right')

        ''' high speed(peel out/ spinning legs) - left '''

        if  -24 < self.velocity.x < -16:
            sonic('run_', self.position, 9, 12, 'left')
        if self.velocity.x <= -24:
            sonic('run_', self.position, 13,16,'left')

        '''Border animations currently not functional '''

        if self.button == 'border_left' and self.direction == 'right' and self.velocity.y == 0:
            sonic('idle_', self.position, 7, 15, 'right')
            #border animation
        if self.button == 'border_right'and self.direction == 'left' and self.velocity.y == 0:
            sonic('idle_', self.position,7,15,'left')

        if self.button == 'push_left' and self.direction == 'left' and self.velocity.y == 0:
            sonic('idle_', self.position, 16, 19, 'left')
        if self.button == 'push_right' and self.direction == 'right' and self.velocity.y == 0:
            sonic('idle_', self.position, 16, 19, 'right')

        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(sonic.frames)
            self.image = sonic.frames[self.index]

    def refresh_all(self, dt):
        self.refresh(dt)

class tile(pygame.sprite.Sprite):
    '''
        return rectangles with location
    '''
    floor_tiles = []

    def __init__(self, zone):
        super(tile, self).__init__()
        self.zone = zone
        # self.zone = surface
        for x in range(len(zone)): # use set() to improve complexity
            for y in range(len(zone[x])):
                if self.zone[x][y] == 'floor':
                    self.floor_tiles.append([x,y])

class ramp(pygame.sprite.Sprite):

    ramp_tiles = []
    mask = pygame.mask.from_surface(pygame.image.load('slope_45.png')).outline(16)

    def __init__(self, zone):
        super(ramp, self).__init__()
        self.zone = zone
        for x in range(len(zone)):
            for y in range(len(zone[x])):
                if isinstance(self.zone[x][y],int):
                    self.ramp_tiles.append([x, y])



#pygame.image.load("tile.png")







