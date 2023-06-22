"""
This module implements a game called Brickstroy using the Pygame library.
"""
# pylint: disable=no-member
# pylint: disable=wildcard-import
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-branches, unused-wildcard-import

import pygame
import pygame.locals as pglocals
from pygame.locals import *

# Now you can use specific names from pglocals module
event_type = pglocals.QUIT
mouse_button_down = pglocals.MOUSEBUTTONDOWN

pygame.init()

# ''' Defining gaming window size and font '''

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Brickstroy")

font = pygame.font.SysFont("Arial", 30)

"""
Defining Bricks colour
"""
O_brick = (255, 100, 10)
w_brick = (255, 255, 255)
g_brick = (0, 255, 0)
black = (0, 0, 0)

GAME_ROWS = 6
GAME_COLOUMNS = 6
clock = pygame.time.Clock()
FRAME_RATE = 60
MY_BALL = False
GAME_OVER = 0
SCORE = 0


class Ball:
    """
    Creating ball for the game"""

    def __init__(self, x_value, y_value):
        self.radius = 10
        self.rect = Rect(x_value - self.radius, y_value - 50, self.radius * 2, self.radius * 2)
        self.speed = {'x': 4, 'y': -4}
        self.max_speed = 5
        self.game_over = 0
        self.x_value = x_value - self.radius
        self.y_value = y_value - 50

    @property
    def x_speed(self):
        """
        Get the x speed of the object.

        Returns:
           int: The x speed value.
        """
        return self.speed['x']

    @x_speed.setter
    def x_speed(self, value):
        """
        Set the x speed of the object.

        Args:
            value (int): The new x speed value.
        """
        self.speed['x'] = value

    @property
    def y_speed(self):
        """
        Get the y speed of the object.

        Returns:
               int: The y speed value.
        """
        return self.speed['y']

    @y_speed.setter
    def y_speed(self, value):
        """
        Set the y speed of the object.

        Args:
            value (int): The new y speed value.
        """
        self.speed['y'] = value

    def motion(self):
        """Motion of the bricks"""
        collision_threshold = 5
        block_object = Block.bricks
        brick_destroyed = 1
        count_row = 0

        for row in block_object:
            count_item = 0
            for item in row:
                if block_object[count_row][count_item][0] != (0, 0, 0, 0):
                    brick_destroyed = 0

                if self.rect.colliderect(item[0]):
                    if (
                            abs(self.rect.bottom - item[0].top) < collision_threshold
                            and self.y_speed > 0
                    ):
                        self.y_speed *= -1

                    if (
                            abs(self.rect.top - item[0].bottom) < collision_threshold
                            and self.y_speed < 0
                    ):
                        self.y_speed *= -1

                    if (
                            abs(self.rect.right - item[0].left) < collision_threshold
                            and self.x_speed > 0
                    ):
                        self.x_speed *= -1

                    if (
                            abs(self.rect.left - item[0].right) < collision_threshold
                            and self.x_speed < 0
                    ):
                        self.x_speed *= -1

                    if block_object[count_row][count_item][1] > 1:
                        block_object[count_row][count_item][1] -= 1
                    else:
                        block_object[count_row][count_item][0] = (0, 0, 0, 0)

                count_item += 1
            count_row += 1

        if brick_destroyed == 1:
            self.game_over = 1
            return self.game_over

        if self.rect.left < 0 or self.rect.right > WINDOW_WIDTH:
            self.x_speed *= -1

        if self.rect.top < 0:
            self.y_speed *= -1

        if self.rect.bottom > WINDOW_HEIGHT:
            self.game_over = -1
            return self.game_over

        if self.rect.colliderect(user_basepad):
            if (
                    abs(self.rect.bottom - user_basepad.rect.top) < collision_threshold
                    and self.y_speed > 0
            ):
                self.y_speed *= -1
                self.x_speed += user_basepad.direction
                if self.x_speed > self.max_speed:
                    self.x_speed = self.max_speed
                elif self.x_speed < 0 and self.x_speed < -self.max_speed:
                    self.x_speed = -self.max_speed
                else:
                    self.x_speed *= -1

        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        return self.game_over


    def draw(self):
        """Draw method"""
        pygame.draw.circle(
            window,
            (0, 0, 255),
            (self.rect.x + self.radius, self.rect.y + self.radius),
            self.radius,
        )
        pygame.draw.circle(
            window,
            (255, 255, 255),
            (self.rect.x + self.radius, self.rect.y + self.radius),
            self.radius,
            1,
        )

    def reset(self, x_value, y_value):
        """Reset method"""

        self.radius = 10
        self.x_value = x_value - self.radius
        self.y_value = y_value - 50
        self.rect = Rect(self.x_value, self.y_value, self.radius * 2, self.radius * 2)
        self.x_speed = 4
        self.y_speed = -4
        self.max_speed = 5
        self.game_over = 0


class Block:
    """
    This class will help me create Blocks/bricks of the game"""

    def __init__(self):
        self.width = WINDOW_WIDTH // GAME_COLOUMNS
        self.height = 40
        self.bricks = []

    def make_brick(self):
        """For making the brick"""
        single_brick = []
        for row in range(GAME_ROWS):

            brick_row = []

            for coloumn in range(GAME_COLOUMNS):

                x_brick = coloumn * self.width
                y_brick = row * self.height
                rect = pygame.Rect(x_brick, y_brick, self.width, self.height)
                # assign power to the bricks based on row
                if row < 2:
                    power = 3
                elif row < 4:
                    power = 2
                elif row < 6:
                    power = 1

                single_brick = [rect, power]

                brick_row.append(single_brick)

            self.bricks.append(brick_row)

    def draw_brick(self):
        """Bricks draw after ball hit"""
        for row in self.bricks:
            for brick in row:

                if brick[1] == 3:
                    brick_colour = O_brick
                elif brick[1] == 2:
                    brick_colour = w_brick
                elif brick[1] == 1:
                    brick_colour = g_brick
                pygame.draw.rect(window, brick_colour, brick[0])
                pygame.draw.rect(window, black, (brick[0]), 1)


class Base:
    """
    This class is to create the base pad of the game"""

    def __init__(self):

        self.height = 20
        self.width = int(WINDOW_WIDTH / GAME_COLOUMNS)
        self.x_value = int((WINDOW_WIDTH / 2) - (self.width / 2))
        self.y_value = WINDOW_HEIGHT - (self.height * 2)
        self.speed = 8
        self.rect = Rect(self.x_value, self.y_value, self.width, self.height)
        self.direction = 0

    def slide(self):
        """Slide the bar method"""

        self.direction = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
            self.direction = -1
        if key[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self.rect.x += self.speed
            self.direction = 1

    def draw(self):
        """Draw method"""
        pygame.draw.rect(window, (0, 0, 255), self.rect)
        pygame.draw.rect(window, (255, 255, 255), self.rect, 1)

    def reset(self):
        """Reset method"""

        self.height = 20
        self.width = int(WINDOW_WIDTH / GAME_COLOUMNS)
        self.x_value = int((WINDOW_WIDTH / 2) - (self.width / 2))
        self.y_value = WINDOW_HEIGHT - (self.height * 2)
        self.speed = 8
        self.rect = Rect(self.x_value, self.y_value, self.width, self.height)
        self.direction = 0


def draw_text(text, font_obj, w_brick_color, x_position, y_position):
    """
    Funtion for showing text in gaming window
    """
    image = font_obj.render(text, True, w_brick_color)
    window.blit(image, (x_position, y_position))


Block = Block()
# Creating Brick
Block.make_brick()
# Defining base pad
user_basepad = Base()
ball = Ball(user_basepad.x_value + (user_basepad.width // 2), \
            user_basepad.y_value - user_basepad.height)
# Defining ball

GAME = True
while GAME:

    clock.tick(FRAME_RATE)
    window.fill(black)  # Gaming window Background
    Block.draw_brick()  # Drawing bricks
    user_basepad.draw()  # Drawing user basepad
    ball.draw()  # Drawing gaming ball

    if MY_BALL:
        user_basepad.slide()
        GAME_OVER = ball.motion()
        if GAME_OVER != 0:
            MY_BALL = False

    # Game Info on the gaming window
    if not MY_BALL:
        if GAME_OVER == 0:
            draw_text(
                "CLICK ANYWHERE TO START", font, w_brick, 90, WINDOW_HEIGHT // 2 + 100
            )
        elif GAME_OVER == 1:
            draw_text("YOU WON!", font, w_brick, 180, WINDOW_HEIGHT // 2 + 50)
            draw_text(
                "CLICK ANYWHERE TO RESTART", font, w_brick, 90, WINDOW_HEIGHT // 2 + 100
            )
        elif GAME_OVER == -1:
            draw_text("GAME OVER!", font, w_brick, 180, WINDOW_HEIGHT // 2 + 50)
            draw_text(
                "CLICK ANYWHERE TO RESTART", font, w_brick, 90, WINDOW_HEIGHT // 2 + 100
            )

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME = False
        if event.type == pygame.MOUSEBUTTONDOWN and MY_BALL is False:
            MY_BALL = True
            ball.reset(user_basepad.x_value + (user_basepad.width // 2), \
                       user_basepad.y_value - user_basepad.height)
            user_basepad.reset()
            Block.make_brick()

    pygame.display.update()

pygame.quit()
