from settings import *
from player import Player
from sprites import *
from pytmx.util_pygame import load_pygame


from random import randint

class Game:
    def __init__(self):

        # Setup

        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Survivor")
        self.clock = pygame.time.Clock()
        self.running = True

        # Groups

        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        self.setup()

        # Sprites

        self.player = Player((400, 300), self.all_sprites, self.collision_sprites)
        
    def setup(self):
        map = load_pygame(join("data", "maps", "world.tmx"))
        for obj in map.get_layer_by_name("Objects"):
            CollisionSprite((obj.x, obj.y), obj.image, (self.all_sprites, self.collision_sprites))

            print(obj.x)
            print(obj.y)
            print(obj.image)


    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.all_sprites.update(dt)

            self.display_surface.fill("Black")
            self.all_sprites.draw(self.display_surface)
            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()

