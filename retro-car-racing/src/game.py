import pygame
import sys
import random
from enemy import spawn_enemy, move_enemies, draw_enemies, check_collision, clear_offscreen_enemies, enemies

# Configuración de la pantalla
SCREEN_WIDTH = 422
SCREEN_HEIGHT = 600
FPS = 60

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Carriles
LANE_WIDTH = 95
LANE_LEFT = 85
LANE_RIGHT = 275

# Clase del jugador
class Player:
    def __init__(self, car_image):
        self.image = car_image
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = SCREEN_WIDTH // 2 - self.width // 2
        self.y = SCREEN_HEIGHT - self.height - 10
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, dx):
        new_x = self.x + dx
        if LANE_LEFT <= new_x <= LANE_RIGHT:
            self.x = new_x
            self.rect.x = self.x

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))  # Dibujar la imagen del auto jugador

# Clase del juego
class Game:
    def __init__(self, screen, car_image):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.player = Player(car_image)
        self.enemy_spawn_timer = 0  # Temporizador para generar enemigos
        self.running = True
        self.start_time = pygame.time.get_ticks()  # Tiempo de inicio del juego
        self.score = 0
        enemies.clear()  # Limpiar la lista de enemigos

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.move(-3.3)  # Velocidad a la izquierda
        if keys[pygame.K_RIGHT]:
            self.player.move(3.2)  # Velocidad a la derecha

        move_enemies()
        clear_offscreen_enemies()

        if check_collision(self.player.rect):
            self.running = False

        # Generar enemigos a intervalos regulares
        self.enemy_spawn_timer += 1
        if self.enemy_spawn_timer >= 120:  # Generar enemigos cada dos segundos
            for _ in range(random.randint(1, 2)):  # Generar entre uno y dos enemigos
                spawn_enemy()
            self.enemy_spawn_timer = 0

        # Actualizar la puntuación
        self.score = (pygame.time.get_ticks() - self.start_time) // 1000

    def draw(self):
        self.screen.fill(WHITE)
        background_img = pygame.image.load('retro-car-racing/images/racetrack.png').convert()
        self.screen.blit(background_img, (0, 0))
        self.player.draw(self.screen)
        draw_enemies(self.screen)

        # Mostrar la puntuación
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, BLACK)
        self.screen.blit(score_text, (10, 10))

    def game_over(self):
        # Cargar la imagen de fondo de Game Over
        gameover_img = pygame.image.load('retro-car-racing/images/gameover.png').convert()
        self.screen.blit(gameover_img, (0, 0))

        # Mostrar el texto de Game Over y la puntuación
        font = pygame.font.Font(None, 74)
        game_over_text = font.render("Game Over", True, WHITE)
        self.screen.blit(game_over_text, (self.screen.get_width() // 2 - game_over_text.get_width() // 2, 100))

        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Tu puntuación fue: {self.score}", True, WHITE)
        self.screen.blit(score_text, (self.screen.get_width() // 2 - score_text.get_width() // 2, 200))

        pygame.display.flip()

        # Esperar a que el usuario cierre el juego
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Retro Car Racing")
    
    while True:
        show_menu(screen)
        while True:
            action = handle_menu_input()
            if action == "start":
                car_image = show_garage(screen)
                if car_image:
                    break
            if action == "exit":
                pygame.quit()
                sys.exit()

        clock = pygame.time.Clock()
        game = Game(screen, car_image)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            game.update()
            game.draw()
            pygame.display.flip()
            clock.tick(60)

            if not game.running:
                game.game_over()
                break

if __name__ == "__main__":
    main()