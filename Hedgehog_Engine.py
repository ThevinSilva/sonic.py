import math

class engine:
    # constants
    posy = 896/2
    posx = 1280 / 2
    grv = 0.21875 * 4
    rollfrc = 0.0234375 * 4
    rolldec = 0.125 * 4
    slp = 0.125 * 4
    frc = 0.046875 * 4

    def __init__(self):
        self._onGround = True
        self._gsp = 0
        self._xsp = 0
        self._ysp = 0
        self._direction = 'right'
        self._angle= 0
        self._spin_rev = 0
        self._roll= True
        self._movement = None

    @property
    def movement(self): return self._movement

    @movement.setter
    def movement(self, val):
        self._movement = val

        if self._movement == 'roll':
            print('semi success')
            self.roll = True

        if self._movement == "right":
            print('shit number 2')
            self.right()
        elif self._movement == "left":
            self.left()
        elif self._movement != "right" or self._movement != 'left':
            self.gsp = self.gsp - (min(abs(self.gsp), engine.frc) * self.sign(self.gsp))
            print('friction')
            if  self.roll == True:
                self.gsp = self.gsp - (min(abs(self.gsp), self.rollfrc) * self.sign(self.gsp))


        if self._movement == "jump":
            self.jump(True)
        if self._movement == "end_jump":
            self.jump(False)

        self.spin_rev -= ((self.spin_rev // 0.25) / 1280)
        if self._movement =='spin_charge':
            if self.spin_rev < 48:
                self.spin_rev += 8
        if self._movement == 'spin_dash':
            if self.direction == 'right':
                self.gsp = 32 + (math.floor(self.spin_rev) / 8)
            if self.direction == 'left':
                self.gsp = - 32 - (math.floor(self.spin_rev) / 8)

    @property
    def onGround(self): return self._onGround

    @onGround.setter
    def onGround(self, val): self._onGround = val

    @property
    def xsp(self): return self._xsp

    @xsp.setter
    def xsp(self, val):
        self._xsp = self.gsp * math.cos(self._angle)
        self._xsp = val

    @property
    def gsp(self): return self._gsp

    @gsp.setter
    def gsp(self, val): self._gsp = val

    @property
    def ysp(self): return self._ysp

    @ysp.setter
    def ysp(self, val):
        self._ysp = val

    @property
    def direction(self): return self._direction

    @direction.setter
    def direction(self, val):self._direction = val

    @property
    def angle(self): return self._angle

    @angle.setter
    def angle(self, val): self._angle= val

    @property
    def spin_rev(self):
        return self._spin_rev

    @spin_rev.setter
    def spin_rev(self, val):
        self._spin_rev = val

    @property
    def roll(self):
        return self._roll

    @roll.setter
    def roll(self, val):
        self._roll= val

    @staticmethod
    def sign(data):
        if data > 0:
            return 1
        elif data < 0:
            return -1
        else:
            return 0

    def left(self):
        self.acc = 0.046875 * 4
        self.dec = 0.5 * 4
        self.top = 6 * 4

        if self.gsp > 0:
            self.gsp -= self.dec
            if self.gsp <= 0:
                self.gsp = - 0.5 * 4

        elif self.gsp > -self.top:
            self.gsp -= self.acc
            if self.gsp <= -self.top:
                self.gsp = -self.top

    def right(self):
        self.acc = 0.046875 * 4
        self.dec = 0.5 * 4
        self.top = 6 * 4
        print('shit')
        if self.gsp < 0:
            self.gsp += self.dec
            if self.gsp >= 0:
                self.gsp = 0.5 * 4

        elif self.gsp < self.top:
            self.gsp += self.acc
            if self.gsp >= self.top:
                self.gsp = self.top


    def jump(self, state):
        self.state = state
        self.jmp = 6.5 * 4
        if self.state:
            self.ysp = - self.jmp
            if self.ysp > (16 * 4):
                self.ysp = 16 * 4
            if (self.ysp < 0) and self.ysp > - 4 * 4:
                self.xsp -= ((self.xsp // 0.125 * 4) / 896)


Engine = engine()
# for n in range(7):
# print(Engine.gsp)
# Engine.movement = 'right'
# print(Engine.gsp)
