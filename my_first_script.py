import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen Settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game Menu")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED   = (200, 0, 0)
GRAY  = (100, 100, 100)

# Fonts
font_title = pygame.font.SysFont("Arial", 60, bold=True)
font_button = pygame.font.SysFont("Arial", 30)

def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

def main_menu():
    # Define Button Rects
    play_rect = pygame.Rect(WIDTH // 2 - 100, 150, 200, 50)
    quit_rect = pygame.Rect(WIDTH // 2 - 100, 230, 200, 50)

    while True:
        screen.fill(BLACK)
        
        # Draw Title
        draw_text("SNAKE GAME", font_title, GREEN, WIDTH // 2 - 170, 50)

        # Get Mouse Position
        mouse_pos = pygame.mouse.get_pos()

        # Handle Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint(mouse_pos):
                    game_loop() # Switch to the actual game
                if quit_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        # Button Hover Effects
        play_color = GREEN if play_rect.collidepoint(mouse_pos) else GRAY
        quit_color = RED if quit_rect.collidepoint(mouse_pos) else GRAY

        # Draw Buttons
        pygame.draw.rect(screen, play_color, play_rect)
        pygame.draw.rect(screen, quit_color, quit_rect)

        # Draw Button Text
        draw_text("PLAY", font_button, WHITE, play_rect.x + 65, play_rect.y + 10)
        draw_text("QUIT", font_button, WHITE, quit_rect.x + 65, quit_rect.y + 10)

        pygame.display.update()

def game_loop():
    """ This is where your actual Snake Game logic goes. """
    running = True
    while running:
        screen.fill((20, 20, 20)) # Dark game background
        draw_text("Game is Running...", font_button, WHITE, 200, 180)
        draw_text("Press 'M' for Menu", font_button, GRAY, 200, 220)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    return # Go back to main_menu()

        pygame.display.update()

# Run the program
if __name__ == "__main__":
    main_menu()

