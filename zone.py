import math
import csv

''' data structure for the level'''

class Zone:
    screen_height = 224 * 4
    screen_width = 320 * 4

    def __init__(self,posx,posy):
        self.posx, self.posy= posx, posy
        self.Y_plane = int(math.ceil(((self.posy + 192) /Zone.screen_height)*14))
        self.X_plane = int(math.ceil(((self.posx +  64)/Zone.screen_width)*20))
    @property
    def screen(self):
        self._screen = data = list(csv.reader(open('level.csv')))
        for n,val_x in enumerate(data):
            for i,val_y in enumerate(val_x):
                if val_y == '':
                    self._screen[n][i] = None
                elif 47 < ord(str(val_y)[0]) < 58:
                    self._screen[n][i] = int(self._screen[n][i])
        print(f'{self.Y_plane} , {self.X_plane}')
        return self._screen



    def sonic_hitbox(self):
        self.floor = False
        self.right = -100000
        self.left = 1280

        ''' event handler incase player leaves bounds '''
        try:
            ''' representation on the console of where game objects are located'''

            self.screen[self.Y_plane - 1][self.X_plane] = "sonic"
            print(f'{self.Y_plane} , {self.X_plane}')
            for n in range(14):
                print(f"{self.screen[n]}\n")

        except IndexError:
            if self.Y_plane > 14:
                self.posy = Zone.screen_height
                self.Y_plane = 14
            if self.X_plane > 20:
                self.posx = Zone.screen_width - 128
                self.X_plane = 20
        return self.posx ,self.posy,{ 'floor' : self.floor, 'right' :self.right, 'left' : self.left}

