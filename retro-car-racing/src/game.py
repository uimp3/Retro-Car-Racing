import random
import pygame
import sys
from enemy import spawn_enemy, move_enemies, draw_enemies, check_collision, clear_offscreen_enemies

# Configuración de la pantalla
SCREEN_WIDTH = 422
SCREEN_HEIGHT = 600
FPS = 60

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Clase del jugador
class Player:
    def __init__(self):
        self.image = pygame.image.load("retro-car-racing/images/mycar.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = SCREEN_WIDTH // 2 - self.width // 2
        self.y = SCREEN_HEIGHT - self.height - 10
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, dx):
        if 0 <= self.x + dx <= SCREEN_WIDTH - self.width:
            self.x += dx
            self.rect.x = self.x

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))  # Dibujar la imagen del jugador

# Clase del juego
class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.enemy_spawn_timer = 0  # Temporizador para generar enemigos
        self.running = True

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.move(-5)
        if keys[pygame.K_RIGHT]:
            self.player.move(5)

        move_enemies()
        clear_offscreen_enemies()

        if check_collision(self.player.rect):
            print("Game Over!")
            pygame.quit()
            sys.exit()

        # Generar enemigos a intervalos regulares
        self.enemy_spawn_timer += 1
        if self.enemy_spawn_timer >= 90:  # Generar enemigos cada ... segundos
            for _ in range(random.randint(1, 2)):  # Generar entre uno y dos enemigos
                spawn_enemy()
            self.enemy_spawn_timer = 0

    def draw(self):
        self.screen.fill(WHITE)
        background_img = pygame.image.load('retro-car-racing/images/racetrack.png').convert()
        self.screen.blit(background_img, (0, 0))
        self.player.draw(self.screen)
        draw_enemies(self.screen)

    def game_over(self):
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over", True, BLACK)
        self.screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))

        font = pygame.font.Font(None, 36)
        retry_text = font.render("Press R to Retry", True, BLACK)
        self.screen.blit(retry_text, (SCREEN_WIDTH // 2 - retry_text.get_width() // 2, SCREEN_HEIGHT // 2 + text.get_height()))

        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    return

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Retro Car Racing")
    game = Game(screen)

    while True:
        while game.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            game.update()
            game.draw()
            pygame.display.flip()
            game.clock.tick(FPS)

        game.game_over()
        game.__init__(screen)  # Reiniciar el juego

if __name__ == "__main__":
    main()