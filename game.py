import pygame
import random

# Initilizing pygame and defining window
pygame.init()
window_size = width, height = 500, 500,
window = pygame.display.set_mode(window_size)
caption = pygame.display.set_caption("Point Game")
icon_image = pygame.image.load("icon.png")
icon = pygame.display.set_icon(icon_image)


class Player:
    def __init__(self, RGB, x, y, width, height):
        self.RGB = RGB
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 20

    def draw(self):
        """
        Draw the player on the screen
        """
        pygame.draw.rect(window, self.RGB, (self.x, self.y, self.width, self.height))


class Fruit:
    def __init__(self, RGB, width, height):
        self.RGB = RGB
        self.x = 240
        self.y = 60
        self.width = width
        self.height = height
        self.ate_apple = False

    def random(self):       
        """
        Generate random apple x and y values
        """
        if self.ate_apple:
            self.x = 20 * random.randint(0, 23)
            self.y = 20 * random.randint(3, 23)

    def draw(self):
        """
        Draw the apple on the screen if apple was not ate
        """
        if not self.ate_apple:
            pygame.draw.rect(window, self.RGB, (self.x, self.y, self.width, self.height))
        
    def hit(self, player):
        """
        If the player ate the apple, this function increases the score of this player and call the function to generate another apple
        """
        self.ate_apple = True
        self.random()
        self.ate_apple = False
        
        if player == 0:
            score[0] += 1
        elif player == 1:
            score[1] += 1


def draw_all():
    """
    Draw and update all the things on the screen.
    """
    global text, display_message, display_color, display_x, display_y, display_text_size
    window.fill((255, 255, 255))
    player.draw()
    player1.draw()
    apple.draw()
    font = pygame.font.SysFont('comicsansms', display_text_size, True, False)
    text = font.render(display_message, True, display_color)
    window.blit(text, (display_x, display_y, 20, 20))
    pygame.display.update()

# Creating objects and main variables
score = [0, 0]
max_score = 30

display_message = ""
display_color = (0, 0, 0)
display_x = 10
display_y = 10
display_text_size = 20

player = Player((0, 255, 0), 0, 60, 20, 20)
player1 = Player((0, 0, 255), 480, 60, 20, 20)
apple = Fruit((255, 0, 0), 20, 20)
apple.random()

# Main Loop
running = True
while running:
    pygame.time.delay(80)

    # Verifying if some player win
    if score[0] >= max_score:
        display_message = "PLAYER 1 WINS!"
        display_color = (0, 255, 0)
        display_x = (window_size[0] // 2) - (text.get_rect().width // 2)
        display_y = (window_size[1] // 2)
        display_text_size = 30
        draw_all()
        pygame.time.delay(3000)
        running = False

    elif score[1] >= max_score:
        display_message = "PLAYER 2 WINS!"
        display_color = (0, 0, 255)
        display_x = (window_size[0] // 2) - (text.get_rect().width // 2)
        display_y = (window_size[1] // 2) - (text.get_rect().height // 2)
        display_text_size = 30
        draw_all()
        pygame.time.delay(3000)
        running = False

    else:
        display_message = f"SCORE(player1): {score[0]} - SCORE(player2): {score[1]}"

    # Verifying if some player ate the apple
    if player.x == apple.x and player.y == apple.y:
        apple.hit(0)

    elif player1.x == apple.x and player1.y == apple.y:
        apple.hit(1)

    # Listening events and collisions
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and player.y > 60:
        player.y -= player.speed

    elif keys[pygame.K_DOWN] and player.y < window_size[1] - player.height:
        player.y += player.speed

    elif keys[pygame.K_LEFT] and player.x > 0:
        player.x -= player.speed

    elif keys[pygame.K_RIGHT] and player.x < window_size[0] - player.width:
        player.x += player.speed

    if keys[pygame.K_w] and player1.y > 60:
        player1.y -= player1.speed

    elif keys[pygame.K_s] and player1.y < window_size[1] - player1.height:
        player1.y += player1.speed

    elif keys[pygame.K_a] and player1.x > 0:
        player1.x -= player1.speed

    elif keys[pygame.K_d] and player1.x < window_size[0] - player1.width:
        player1.x += player1.speed

    draw_all()


pygame.quit()

