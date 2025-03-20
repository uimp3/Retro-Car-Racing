import random
import pygame

# Configuración de los autos enemigos
enemy_width = 50
enemy_height = 80
enemy_speed = 5
enemies = []

# Cargar las imágenes de los autos enemigos
enemy_images = [
    pygame.image.load("retro-car-racing/images/car1.png"),
    pygame.image.load("retro-car-racing/images/car2.png"),
    pygame.image.load("retro-car-racing/images/car3.png")
]

# Generar autos enemigos
def spawn_enemy():
    x = random.choice([90, 183, 274])  # Tres carriles
    y = -2 * enemy_height
    enemy_image = random.choice(enemy_images)
    enemy_rect = enemy_image.get_rect(topleft=(x, y))
    enemies.append((enemy_rect, enemy_image))

# Mover enemigos
def move_enemies():
    for enemy in enemies[:]:
        enemy[0].y += enemy_speed
        if enemy[0].y > pygame.display.get_surface().get_height():
            enemies.remove(enemy)

# Dibujar enemigos en la pantalla
def draw_enemies(screen):
    for enemy in enemies:
        screen.blit(enemy[1], enemy[0].topleft)

# Colisión con el jugador
def check_collision(player_rect):
    for enemy in enemies:
        if player_rect.colliderect(enemy[0]):
            return True
    return False

# Limpiar enemigos fuera de la pantalla
def clear_offscreen_enemies():
    global enemies
    enemies = [enemy for enemy in enemies if enemy[0].y <= pygame.display.get_surface().get_height()]