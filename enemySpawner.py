import random
from enemyBomb import EnemyBomb


class EnemySpawner:
    x_vals = [i for i in range(60, 740, 60)]
    dy_vals = [i for i in range(1, 10)]
    difficulties = {
        'easy': 50,
        'medium': 13,
        'hard': 10,
        'very hard': 3
    }

    def __init__(self):
        self.difficulty = 'easy'
        self.enemies = []

    def change_difficulty(self):
        if self.difficulty == 'easy':
            self.difficulty = 'medium'
        elif self.difficulty == 'medium':
            self.difficulty = 'hard'
        elif self.difficulty == 'hard':
            self.difficulty = 'very hard'
        elif self.difficulty == 'very hard':
            self.difficulty = 'easy'

    def get_enemies(self):
        return self.enemies

    def spawn(self):
        enemy_bomb = EnemyBomb(random.choice(self.x_vals), random.choice(self.dy_vals))
        self.enemies.append(enemy_bomb)

    def update(self):
        num = random.randint(1, 100)
        if num % self.difficulties[self.difficulty] == 0:
            self.spawn()
        for enemy in self.enemies:
            enemy.update()

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

