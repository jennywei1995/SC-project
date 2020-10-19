"""
File: best_photoshop_award.py
Name: Jenny Wei
----------------------------------
This file creates a photoshopped image
that is going to compete for the 2020 Best
Photoshop Award for SC101P.
Please put all the images you use in image_contest folder
and make sure to choose which award you are aiming at
"""
from simpleimage import SimpleImage

THRESHOLD=1.2

BLACK_PIXEL=160


def main():
    """
    創作理念/靈感來源：用天線寶寶的太陽，和大家打招呼！
    """
    sun = SimpleImage("image_contest/sun_back.png")
    figure= SimpleImage("image_contest/Jenny.png")
    figure.make_as_big_as(sun)
    new_figure= change_color(figure)
    result = combine(sun, new_figure)
    result.show()


def change_color(fig):
    """
    :param figure: SimpleImage, green screen figure image
    :return: SimpleImage, with picture's tone turned into yellow
    """
    for y in range(fig.height):
        for x in range(fig.width):
            pixel_fig = fig.get_pixel(x, y)
            pixel_fig.red = pixel_fig.red*1.5
            pixel_fig.green =pixel_fig.green*1
            pixel_fig.blue = pixel_fig.blue/3
    return fig


def combine(back, fig):
    """
    : param1 back: SimpleImage, the background image
    : param2 ma: SimpleImage, the figure image with changed color
    : return me: SimpleImage, the green screen pixels are replaced by pixels background image
    """
    for y in range(back.height):
        for x in range(back.width):
            pixel_fig = fig.get_pixel(x, y)
            pixel_bg = back.get_pixel(x, y)
            total = pixel_fig.red + pixel_fig.blue + pixel_fig.green
            avg = total // 3
            if pixel_fig.green > avg * THRESHOLD and total > BLACK_PIXEL:
                # Green pixel
                pixel_fig.red = pixel_bg.red
                pixel_fig.green = pixel_bg.green
                pixel_fig.blue = pixel_bg.blue
            if y>fig.height/3*2:
                pixel_fig.red = pixel_bg.red
                pixel_fig.green = pixel_bg.green
                pixel_fig.blue = pixel_bg.blue
            if x<fig.width/5.5*2:
                pixel_fig.red = pixel_bg.red
                pixel_fig.green = pixel_bg.green
                pixel_fig.blue = pixel_bg.blue
            if x>fig.width/10.5*7:
                pixel_fig.red = pixel_bg.red
                pixel_fig.green = pixel_bg.green
                pixel_fig.blue = pixel_bg.blue
    return fig








if __name__ == '__main__':
    main()
