#create a Maze
from pygame import*
class GSprite(sprite.Sprite):
    def __init__ (self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.x = player_x
        self.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x> 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x< win_width - 80:
            self.rect.x += self.speed    
        if keys[K_UP] and self.rect.y> 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Enemy(GSprite):
    direction = "left"
    def update(self):
        self.rect.y = 300
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= win_width - 85:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, wall_x, wall_y, width, height):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.width = width
        self.height = height
        self.image = Surface((self.width, self.height))
        self.image.fill((color1, color2, color3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


w1 = Wall(154,205,50,100,20,450,10)
w2 = Wall(154,205,50,100,480,350,10)
w3 = Wall (154,205,50,100,20,10,380)

w4 = Wall(154,205,50,220,130,10,400)
w6 = Wall(154,205,50,450,130,10,400)
w5 = Wall (154,205,50,350,20,10,380)




win_width = 700
win_height = 500
window = display.set_caption("mAzE")
window = display.set_mode((win_width,win_height))

background = transform.scale(image.load("background.jpg"),(win_width,win_height))
pacman = Player("hero.png", 5, win_height - 80, 4)
enemy = Enemy("cyborg.png", win_width - 80, 280, 7)
kho_bau = GSprite("treasure.png", win_width - 120, win_height - 80, 8)

finish = False
game = True
clock = time.Clock()
FPS = 60

font.init()
font = font.SysFont('Arial', 70)
win = font.render('You lose xD', True, (255,215,0))
lose = font.render('You win xD', True, (210,215,0))
# mixer.init()
# mixer.music.load("jungles.ogg")
# mixer.music.play()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0,0))
        
        pacman.update()
        enemy.update()
        
        kho_bau.update()
        pacman.reset()
        enemy.reset()
        kho_bau.reset()


        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        # if sprite.collide_rect(pacman, enemy) or sprite.collide_rect(pacman, w1) or sprite.collide_rect(pacman, w2) or sprite.collide_rect(pacman, w3) or sprite.collide_rect(pacman, w4) or sprite.collide_rect(pacman, w5) or sprite.collide_rect(pacman, w6):
        #     finish = True
        #     window.blit(lose, (200,200))
        # if sprite.collide_rect(pacman, kho_bau):
        #     finish =True
        #     window.blit(win, (200,200))

    display.update()
    clock.tick(FPS)