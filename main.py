import pyxel
import random

Hi = 150
Wi = 150
score = 50

class balloon:

    def __init__(self):

        pyxel.image(0).load(0, 0, "./assets/Sprite-0001.png")
        self.x = random.randrange(0, 145)
        self.y = random.randrange(0, Hi)

        self.alive = True

    def updata(self):
        self.y = (self.y - 0.5) % Hi

        if self.chleckd() == True:
            self.remove()


    def chleckd(self):
        if pyxel.mouse_x < self.x or pyxel.mouse_x > self.x + 10:
            return False

        if pyxel.mouse_y < self.y or pyxel.mouse_y > self.y + 10:
            return False

        return True

    def remove(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            self.alive = False


class App:
    def __init__(self):
        pyxel.init(Hi, Wi)

        self.balloon = [balloon() for _ in range(score)]
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit

        for index, balloon in enumerate(self.balloon):
            balloon.updata()
            if not balloon.alive:
                del self.balloon[index]


    def draw(self):
        pyxel.cls(12)
        for balloon in self.balloon:
            pyxel.blt(balloon.x, balloon.y, 0, 0, 0, 20, 20, 00000)

        color = 3

        if len(self.balloon) == 0:
            text = "Clear!"
            color = pyxel.frame_count % 15 + 1
        else:
            text = "counter: " + str(len(self.balloon))
        return pyxel.text(0, Hi - 7, text, color)


App()