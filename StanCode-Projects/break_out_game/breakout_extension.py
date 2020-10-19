"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao
-------------------------
File: Breakout_extension.py
Name: Jenny Wei
-------------------------
This program creates a breakout game.
This file is the user side.
"""
from campy.gui.events.timer import pause
from breakoutgraphics_extension import BreakoutGraphicsExtension


# 120 frames per second.
FRAME_RATE = 1000 / 120
NUM_LIVES = 3


def main():
    graphics = BreakoutGraphicsExtension()
    life = NUM_LIVES
    graphics.life_label.text = 'Life: ' + str(life)
    while True:
        # when the user can still play the game
        if life > 0 and graphics.brick_num > 0:
            dx = graphics.get_dx()
            dy = graphics.get_dy()
            # the ball will be moved with the speed of the velocity given
            graphics.ball.move(dx, dy)
            # to check whether the ball hits the wall
            graphics.bounce_back()
            # to check whether the ball hits the paddle
            graphics.check_paddle()
            # to check whether the ball hits the brick
            graphics.check_brick()
            pause(FRAME_RATE)
            # when the ball is out of the window, user lose one of his/her lives
            if graphics.ball.y > graphics.window.height:
                life -= 1
                graphics.life_label.text= 'Life: '+str(life)
                # the ball will be reset to the start position
                graphics.re_set_ball()
        # if the user clear all the bricks, the game is over
        elif graphics.brick_num == 0:
            break
        # if the user finish all his/her lives, the game is over
        elif life == 0:
            break
    # when the user finish clearing all the bricks
    if graphics.brick_num == 0:
        graphics.window.add(graphics.win_label, x=graphics.window.width/2-graphics.win_label.width/2,
                            y=(graphics.window.height/2-graphics.win_label.height/2) -15)
        graphics.window.remove(graphics.ball)
        graphics.window.remove(graphics.paddle)
    # when the user lose the game by finishing all his/her lives
    if life == 0:
        graphics.window.add(graphics.lose_label, x=graphics.window.width / 2 - graphics.lose_label.width / 2,
                            y=(graphics.window.height / 2 - graphics.lose_label.height / 2) - 20)
        # the ball will be reset at its original position
        graphics.re_set_ball()


if __name__ == '__main__':
    main()
