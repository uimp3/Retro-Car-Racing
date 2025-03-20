def load_image(file_path):
    """Load an image from the specified file path."""
    try:
        image = pygame.image.load(file_path)
        return image
    except pygame.error as e:
        print(f"Unable to load image: {file_path}. Error: {e}")
        return None

def draw_text(screen, text, font, color, position):
    """Draw text on the screen at the specified position."""
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)

def reset_game_settings():
    """Reset game settings to default values."""
    return {
        "player_speed": 10,
        "enemy_speed": 15,
        "lane_width": 200,
        "screen_width": 600,
        "screen_height": 800
    }