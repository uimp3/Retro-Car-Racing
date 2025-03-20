import pygame
import sys
from game import Game
from menu import show_menu, handle_menu_input

def main():
    pygame.init()
    screen = pygame.display.set_mode((422, 600))
    pygame.display.set_caption("Retro Car Racing")
    
    while True:
        show_menu(screen)
        while True:
            action = handle_menu_input()
            if action == "start":
                break
            if action == "exit":
                pygame.quit()
                sys.exit()

        clock = pygame.time.Clock()
        game = Game(screen)

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