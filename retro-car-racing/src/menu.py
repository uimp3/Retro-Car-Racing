import pygame

def show_menu(screen):
    # Cargar la imagen de fondo del menú
    background_img = pygame.image.load('retro-car-racing/images/menubackground.png').convert()
    
    # Configurar el texto del menú
    title_font = pygame.font.Font(None, 60)  # Tamaño de fuente más pequeño para el título
    text_font = pygame.font.Font(None, 36)  # Tamaño de fuente más pequeño para el texto de inicio

    title_text = title_font.render("Retro Car Racing", True, (255, 255, 255))
    start_text = text_font.render("Press ENTER to Start", True, (255, 255, 255))

    # Dibujar la imagen de fondo y el texto en la pantalla
    screen.blit(background_img, (0, 0))
    screen.blit(title_text, (screen.get_width() // 2 - title_text.get_width() // 2, 100))
    screen.blit(start_text, (screen.get_width() // 2 - start_text.get_width() // 2, 300))
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