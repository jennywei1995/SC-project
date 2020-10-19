"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao
-------------------------
File: Breakoutgraphics＿extension.py
Name: Jenny Wei
-------------------------
This program creates a breakout game.
This file is the coder side, which build the important components of the game.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random


# constants
BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10  # Radius of the ball (in pixels).
PADDLE_WIDTH = 75  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).
INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball.


class BreakoutGraphicsExtension:
    """
    This class will build the components of the game.
    """
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title="Jenny Wei's Breakout"):
        # Create a graphical window, with some extra space.
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)
        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height, x=(self.window.width - paddle_width) / 2,
                            y=self.window.height - paddle_offset)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window.
        self.ball_radius = ball_radius
        self.original_x = self.window.width / 2 - self.ball_radius
        self.original_y = self.window.height / 2 - self.ball_radius
        self.ball = GOval(2 * self.ball_radius, 2 * self.ball_radius,
                          x=self.original_x, y=self.original_y)
        self.ball.filled = True
        self.window.add(self.ball)
        # Default initial velocity for the ball.
        self.__dx = 0
        self.__dy = 0
        self.original_dx = self.__dx
        self.original_dy = self.__dy
        # to make sure the ball will go up when it hits the paddle
        self.up_initial_y_speed = -INITIAL_Y_SPEED # to make sure the ball will go up when it hits the paddle
        # Draw bricks.
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick_offset = brick_offset
                self.brick_spacing = brick_spacing
                self.brick = GRect(brick_width, brick_height, x=0 + i * (brick_width + brick_spacing),
                                   y=self.brick_offset + j * (brick_height + brick_spacing))
                self.brick.filled = True
                if j // 2 == 0:
                    self.brick.fill_color = 'tan'
                    self.brick.color = 'tan'
                elif j // 2 == 1:
                    self.brick.fill_color = 'dark_salmon'
                    self.brick.color = 'dark_salmon'
                elif j // 2 == 2:
                    self.brick.fill_color = 'indian_red'
                    self.brick.color = 'indian_red'
                elif j // 2 == 3:
                    self.brick.fill_color = 'slate_gray'
                    self.brick.color = 'slate_gray'
                elif j // 2 == 4:
                    self.brick.fill_color = 'cadet_blue'
                    self.brick.color = 'cadet_blue'
                self.window.add(self.brick)
        self.brick_num = brick_cols * brick_rows
        # Initialize our mouse listeners.
        onmouseclicked(self.check_game_start)
        # to draw the score label
        self.score = 0
        self.score_label=GLabel(f'Score:{self.score}')
        self.score_label.font = '-20'
        self.score_label.color = 'black'
        self.window.add(self.score_label,x=10, y=self.window.height-10)
        # to draw the life label
        self.life_label = GLabel(f'Life: ')
        self.life_label.font = '-20'
        self.life_label.color = 'black'
        self.window.add(self.life_label, x=self.window.width-self.life_label.width-20, y=self.window.height - 10)
        # to draw the start label
        self.start_label = GLabel('Please click the mouse to start!')
        self.start_label.font = '-20'
        self.start_label.color = 'black'
        self.window.add(self.start_label,x=self.window.width / 2 - self.start_label.width / 2,
                        y=self.window.height / 2 - self.start_label.height / 2 -20)
        # to draw the win label
        self.win_label=GLabel(f'You win! You got: {self.score}')
        self.win_label.font = '-20'
        self.win_label.color = 'black'
        # to draw the lose label
        self.lose_label = GLabel(f'Game over! You got: {self.score}')
        self.lose_label.font = '-20'
        self.lose_label.color = 'black'

    def paddle_move(self, mouse):
        """
        The paddle will move while the user move the mouse.
        The user's mouse will be at the middle of the paddle
        """
        self.paddle.x = mouse.x - self.paddle.width / 2
        if self.paddle.x+self.paddle.width>self.window.width:
            self.paddle.x = self.window.width - self.paddle.width
        if self.paddle.x <= 0:
            self.paddle.x = 0

    def check_game_start(self, mouse):
        """
        once the user click the mouse, the game will start that the function
        will give the ball velocity to move.
        once the ball is out of the window, the user have to click the mouse again
        to drop the ball.
        """
        if self.ball.x == self.original_x and self.ball.y == self.original_y:
            onmousemoved(self.paddle_move)
            self.window.remove(self.start_label)
            # give the ball velocity
            if self.__dx == 0:
                self.__dy = INITIAL_Y_SPEED
                self.__dx = random.randint(1, MAX_X_SPEED)
                if random.random() > 0.5:
                    self.__dx = -self.__dx
                    print(f'{self.__dy}')

    def bounce_back(self):
        """
        once the ball bump into the wall,
        it will bounce back.
        """
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:
            self.__dx = -self.__dx
        if self.ball.y <= 0:
            self.__dy = -self.__dy

    def check_paddle(self):
        """
        To check whether the ball bump into any object, including the brick and the paddle.
        If the ball hit the brick, the brick will be cleared,
        and it will bounce back if it doesn't hit anything anymore.
        once the ball hit the paddle, the ball will bounce back.
        """
        left_up = self.window.get_object_at(self.ball.x, self.ball.y)
        right_up = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        left_down = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        right_down = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)
        # when ball hits the paddle
        if left_up is self.paddle or right_up is self.paddle:
            pass
        elif left_down is self.paddle and right_down is None:
            self.__dy = self.up_initial_y_speed
        elif right_down is self.paddle and left_down is self.paddle:
            self.__dy = self.up_initial_y_speed
        elif right_down is self.paddle and left_down is None:
            self.__dy = self.up_initial_y_speed
        if self.ball.y + self.__dy >= self.paddle.y:
            if self.ball.y + self.__dy <= self.paddle.y+self.paddle.height:
                if left_down is self.paddle:
                    self.__dy = self.up_initial_y_speed
                elif right_down is self.paddle:
                    self.__dy = self.up_initial_y_speed
        # to make the ball faster while the user reach certain scores
        if self.score >= 150:
            if self.__dy < 0:
                self.__dy = -9
            elif self.__dy > 0:
                self.__dy = 9
        if self.score >= 600:
            if self.__dy < 0:
                self.__dy = -10.5
            elif self.__dy > 0:
                self.__dy = 10.5

    def check_brick(self):
        """
        To check whether the ball hits the brick.
        If the ball hit the brick, the brick will be cleared,
        and it will bounce back if it doesn't hit things anymore.
        """
        left_up = self.window.get_object_at(self.ball.x, self.ball.y)
        right_up = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        left_down = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        right_down = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)
        # if the ball's left_up corner hit the brick
        if left_up is not None:
            if left_up is not self.score_label:
                if left_up is not self.life_label and left_up is not self.paddle:
                    if left_up is not self.paddle:
                        self.window.remove(left_up)
                        self.__dy = -self.__dy
                        self.brick_num -= 1
                        # when the ball hits different color's brick, it will get different scores
                        if left_up.y >= self.brick_offset + 8 * (self.brick.height + self.brick_spacing):
                            self.score += 5
                        elif left_up.y >= self.brick_offset + 6 * (self.brick.height + self.brick_spacing):
                            if left_up.y <= self.brick_offset + 7 * (self.brick.height + self.brick_spacing):
                                self.score += 10
                        elif left_up.y >= self.brick_offset + 4 * (self.brick.height + self.brick_spacing):
                            if left_up.y <= self.brick_offset + 5 * (self.brick.height + self.brick_spacing):
                                self.score += 15
                        elif left_up.y >= self.brick_offset + 2 * (self.brick.height + self.brick_spacing):
                            if left_up.y <= self.brick_offset + 3 * (self.brick.height + self.brick_spacing):
                                self.score += 20
                        else:
                            self.score += 25
                        self.score_label.text = 'Score: ' + str(self.score)
                        self.win_label.text = 'You win! You got: ' + str(self.score)
                        self.lose_label.text = 'Game over! You got: ' + str(self.score)
        # if the ball's right_up corner hit the brick
        elif right_up is not None:
            if right_up is not self.score_label:
                if right_up is not self.life_label:
                    if right_up is not self.paddle:
                        self.window.remove(right_up)
                        self.__dy = -self.__dy
                        self.brick_num -= 1
                        # when the ball hits different color's brick, it will get different scores
                        if right_up.y >= self.brick_offset + 8 * (self.brick.height + self.brick_spacing):
                            self.score += 5
                        elif right_up.y >= self.brick_offset + 6 * (self.brick.height + self.brick_spacing):
                            if right_up.y <= self.brick_offset + 7 * (self.brick.height + self.brick_spacing):
                                self.score += 10
                        elif right_up.y >= self.brick_offset + 4 * (self.brick.height + self.brick_spacing):
                            if right_up.y <= self.brick_offset + 5 * (self.brick.height + self.brick_spacing):
                                self.score += 15
                        elif right_up.y >= self.brick_offset + 2 * (self.brick.height + self.brick_spacing):
                            if right_up.y <= self.brick_offset + 3 * (self.brick.height + self.brick_spacing):
                                self.score += 20
                        else:
                            self.score += 25
                        self.score_label.text = 'Score: ' + str(self.score)
                        self.win_label.text = 'You win! You got: ' + str(self.score)
                        self.lose_label.text = 'Game over! You got: ' + str(self.score)
        # if the ball's left_down corner hit the brick
        elif left_down is not None:
            if left_down is not self.score_label:
                if left_down is not self.life_label:
                    if left_down is not self.paddle:
                        self.window.remove(left_down)
                        self.__dy = -self.__dy
                        self.brick_num -= 1
                        # when the ball hits different color's brick, it will get different scores
                        if left_down.y >= self.brick_offset + 8 * (self.brick.height + self.brick_spacing):
                            self.score += 5
                        elif left_down.y >= self.brick_offset + 6 * (self.brick.height + self.brick_spacing):
                            if left_down.y <= self.brick_offset + 7 * (self.brick.height + self.brick_spacing):
                                self.score += 10
                        elif left_down.y >= self.brick_offset + 4 * (self.brick.height + self.brick_spacing):
                            if left_down.y <= self.brick_offset + 5 * (self.brick.height + self.brick_spacing):
                                self.score += 15
                        elif left_down.y >= self.brick_offset + 2 * (self.brick.height + self.brick_spacing):
                            if left_down.y <= self.brick_offset + 3 * (self.brick.height + self.brick_spacing):
                                self.score += 20
                        else:
                            self.score += 25
                        self.score_label.text = 'Score: ' + str(self.score)
                        self.win_label.text = 'You win! You got: ' + str(self.score)
                        self.lose_label.text = 'Game over! You got: ' + str(self.score)
        # if the ball's right_down corner hit the brick
        elif right_down is not None:
            if right_down is not self.score_label:
                if right_down is not self.life_label:
                    if right_down is not self.paddle:
                        self.window.remove(right_down)
                        self.__dy = -self.__dy
                        self.brick_num -= 1
                        # when the ball hits different color's brick, it will get different scores
                        if right_down.y >= self.brick_offset + 8 * (self.brick.height + self.brick_spacing):
                            self.score += 5
                        elif right_down.y >= self.brick_offset + 6 * (self.brick.height + self.brick_spacing):
                            if right_down.y <= self.brick_offset + 7 * (self.brick.height + self.brick_spacing):
                                self.score += 10
                        elif right_down.y >= self.brick_offset + 4 * (self.brick.height + self.brick_spacing):
                            if right_down.y <= self.brick_offset + 5 * (self.brick.height + self.brick_spacing):
                                self.score += 15
                        elif right_down.y >= self.brick_offset + 2 * (self.brick.height + self.brick_spacing):
                            if right_down.y <= self.brick_offset + 3 * (self.brick.height + self.brick_spacing):
                                self.score += 20
                        else:
                            self.score += 25
                        self.score_label.text = 'Score: ' + str(self.score)
                        self.win_label.text = 'You win! You got: ' + str(self.score)
                        self.lose_label.text = 'Game over! You got: ' + str(self.score)

    def get_dx(self):
        """
        to return the value of the dx to the user side
        """
        return self.__dx

    def get_dy(self):
        """
        to return the value of the dy to the user side
        """
        return self.__dy

    def re_set_ball(self):
        """
        once the ball is out of the window, its position will be reset.
        It's velocity will be set to 0 again. And the user will have to
        click the mouse to continue the game.
        """
        self.__dy = 0
        self.__dx = 0
        self.ball.x = self.original_x
        self.ball.y = self.original_y
        onmouseclicked(self.check_game_start)

