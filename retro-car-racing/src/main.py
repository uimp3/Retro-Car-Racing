import pygame
import sys
from game import Game
from menu import show_menu, handle_menu_input, show_garage

def main():
    pygame.init()
    screen = pygame.display.set_mode((422, 600))
    pygame.display.set_caption("Retro Car Racing")
    
    while True:
        # Mostrar el menú principal
        show_menu(screen)
        
        # Manejar la entrada del menú
        while True:
            action = handle_menu_input()
            if action == "start":
                car_image = show_garage(screen)
                if car_image:
                    break
            if action == "exit":
                pygame.quit()
                sys.exit()

        # Iniciar el juego con el auto seleccionado
        clock = pygame.time.Clock()
        game = Game(screen, car_image)

        # Bucle principal del juego
        while game.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            game.update()
            game.draw()
            pygame.display.flip()
            clock.tick(60)

        # Mostrar la pantalla de Game Over
        game.game_over()

if __name__ == "__main__":
    main()