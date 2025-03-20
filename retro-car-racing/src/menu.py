import pygame

def show_menu(screen):
    font = pygame.font.Font(None, 74)
    title_text = font.render("Retro Car Racing", True, (255, 255, 255))
    start_text = font.render("Press ENTER to Start", True, (255, 255, 255))
    exit_text = font.render("Press ESC to Exit", True, (255, 255, 255))

    screen.fill((0, 0, 0))  # Background color
    screen.blit(title_text, (screen.get_width() // 2 - title_text.get_width() // 2, 100))
    screen.blit(start_text, (screen.get_width() // 2 - start_text.get_width() // 2, 300))
    screen.blit(exit_text, (screen.get_width() // 2 - exit_text.get_width() // 2, 400))
    pygame.display.flip()

def handle_menu_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return "exit"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return "start"
            if event.key == pygame.K_ESCAPE:
                return "exit"
    return "continue"