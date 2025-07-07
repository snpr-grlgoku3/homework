pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Custom Event - Change Sprite Colors")

clock = pygame.time.Clock()

def random_color():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

class MySprite(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((100, 100))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def change_color(self):
        self.color = random_color()
        self.image.fill(self.color)

sprite1 = MySprite(100, 150, random_color())

sprites = pygame.sprite.Group()
sprites.add(sprite1, sprite2)

CHANGE_COLOR_EVENT = pygame.USEREVENT + 1

running = True
while running:
    screen.fill((255, 255, 255))  # white background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pygame.event.post(pygame.event.Event(CHANGE_COLOR_EVENT))

        elif event.type == CHANGE_COLOR_EVENT:
            for sprite in sprites:
                sprite.change_color()

    sprites.draw(screen)

    pygame.display.flip()

pygame.quit()