from bulletType import BulletType

class BulletManager:
    def __init__(self):
        self.bullets = []
        self.type = 1

    def increase_type(self):
        self.type = ((self.type + 1) % 12) + 1
        #              [0 , 11]          + 1 -> [1, 12]

    def spawn_bullet(self, x, y):
        b = BulletType(x, y, self.type)
        self.bullets.append(b)

    def get_bullets(self):
        return self.bullets

    def update(self):
        for b in self.bullets:
            b.update()

    def draw(self, screen):
        for b in self.bullets:
            b.draw(screen)