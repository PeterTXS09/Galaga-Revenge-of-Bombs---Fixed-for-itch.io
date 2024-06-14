class CollisionDetector:
    def __init__(self):
        pass

    def check_collisions(self, bullets, enemies):
        for bullet in bullets:
            for enemy in enemies:
                if bullet.rect.colliderect(enemy.rect):
                    self.handle_collision(bullet, bullets, enemy, enemies)
                    return True
        return False

    def handle_collision(self, bullet, bullets, enemy, enemies):
        if bullet in bullets:
            bullets.remove(bullet)
        if enemy in enemies:
            enemies.remove(enemy)

