import pygame
import random



WIDTH = 800
HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

score = 0

a = pygame.image.load("D:\image\photo6.png")
b = pygame.image.load("D:\image\photo2.png")
c = pygame.image.load("D:\image\photo3.png")
d = pygame.image.load("D:\image\photo4.png")
e = pygame.image.load("D:\image\photo5.png")

lists = [a, b, c, d, e]

class Bird(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        #self.image.fill(RED)
        self.image = pygame.image.load("D:\image\dinosaur.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y += 1
        if self.rect.y > HEIGHT:
            self.rect.y = 0
            self.rect.x = random.randint(0, WIDTH)
            
    

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([4, 10])
        self.image = pygame.image.load("D:\image\heart.png").convert_alpha()
        self.rect = self.image.get_rect()
        #tọa độ bắn
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y -= 1# chỉnh tốc độ đạn bay
        if self.rect.y < 0:
            self.kill()

pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()

background = pygame.image.load("D:\image\hwq.png").convert() # biến hình nền

birds = pygame.sprite.Group()
bullets = pygame.sprite.Group()

for i in range(10):
    bird = Bird(random.randint(0, WIDTH), random.randint(0, HEIGHT))
    birds.add(bird)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  #MOUSEMOTION: để bắn đạn Theo cách di
            bullet = Bullet(pygame.mouse.get_pos()[0], HEIGHT)
            bullets.add(bullet)

    screen.fill(WHITE)
    screen.blit(background, [0, 0]) # hình nền
    birds.update()
    bullets.update()

    # Tăng giá trị điểm mỗi lần một chim bị trúng đạn
    hits = pygame.sprite.groupcollide(birds, bullets, True, True)
    for hit in hits:
        bird = Bird(random.randint(0, WIDTH), random.randint(0, HEIGHT))
        birds.add(bird)
        score += 1
    

    # Tạo font và vẽ điểm lên màn hình
    font = pygame.font.Font(None, 30)
    text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(text, [10, 10])
    
    birds.draw(screen)
    bullets.draw(screen)

    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
