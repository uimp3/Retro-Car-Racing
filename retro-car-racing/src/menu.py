import pygame

def show_menu(screen):
    # Cargar la imagen de fondo del menú
    background_img = pygame.image.load('retro-car-racing/images/menubackground.png').convert()
    
    # Configurar el texto del menú
    title_font = pygame.font.Font(None, 60) 
    text_font = pygame.font.Font(None, 36) 
    
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

def show_garage(screen):
    # Cargar la imagen de fondo del garaje
    background_img = pygame.image.load('retro-car-racing/images/garage.png').convert()
    
    # Cargar las imágenes de los autos
    car_images = [
        pygame.image.load('retro-car-racing/images/mycar.png'),
        pygame.image.load('retro-car-racing/images/mycar1.png'),
        pygame.image.load('retro-car-racing/images/mycar2.png')
    ]
    
    selected_car = 0

    while True:
        screen.blit(background_img, (0, 0))
        
        # Dibujar el texto de instrucciones
        font = pygame.font.Font(None, 30) 
        instructions_text1 = font.render("Elija su auto con las flechas", True, (2, 0, 105)) 
        instructions_text2 = font.render("y presione ENTER para iniciar", True, (2, 0, 105)) 
        screen.blit(instructions_text1, (screen.get_width() // 2 - instructions_text1.get_width() // 2, 520)) 
        screen.blit(instructions_text2, (screen.get_width() // 2 - instructions_text2.get_width() // 2, 560)) 
        
        # Dibujar las imágenes de los autos
        for i, car_image in enumerate(car_images):
            x = screen.get_width() // 2 - car_image.get_width() // 2
            y = 15 + i * 170 
            screen.blit(car_image, (x, y))
            if i == selected_car:
                pygame.draw.rect(screen, (255, 0, 0), (x - 5, y - 5, car_image.get_width() + 10, car_image.get_height() + 10), 3)
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_car = (selected_car - 1) % len(car_images)
                if event.key == pygame.K_DOWN:
                    selected_car = (selected_car + 1) % len(car_images)
                if event.key == pygame.K_RETURN:
                    return car_images[selected_car]
                if event.key == pygame.K_ESCAPE:
                    return None