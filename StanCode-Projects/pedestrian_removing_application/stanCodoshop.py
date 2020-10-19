"""
File: stanCodoshop.py
Name: Jenny Wei
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
-----------------------------------------------
This programs will check the images that have taken at the same places,
and return a new picture that has cleared all the passersby.
"""


import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    color_distance = int(((red-pixel.red)**2+(green-pixel.green)**2+(blue-pixel.blue)**2)**0.5)
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    total_pixel_red = 0
    total_pixel_green = 0
    total_pixel_blue = 0
    for i in range(len(pixels)):
        total_pixel_red += pixels[i].red
        total_pixel_green += pixels[i].green
        total_pixel_blue += pixels[i].blue
    return [total_pixel_red//len(pixels), total_pixel_green//len(pixels), total_pixel_blue//len(pixels)]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    average = get_average(pixels)
    average_red = average[0]
    average_green = average[1]
    average_blue = average[2]
    best_closest_dis = get_pixel_dist(pixels[0],average_red,average_green,average_blue)
    best_pixel = pixels[0]
    for i in range(len(pixels)):
        color_dis = get_pixel_dist(pixels[i], average_red, average_green, average_blue)
        # while the color distance is closer to the average
        if color_dis <= best_closest_dis:
            best_closest_dis = color_dis
            best_pixel = pixels[i]
    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed

    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    # to populate image and create the 'ghost' effect
    for x in range(images[0].width):
        for y in range(images[0].height):
            pixel = []
            for i in range(len(images)):
                pixel.append(images[i].get_pixel(x, y))
                best_pixel = get_best_pixel(pixel)
                result_pix = result.get_pixel(x, y)
                # add the best pixel to the blank image canvas
                result_pix.red = best_pixel.red
                result_pix.green = best_pixel.green
                result_pix.blue = best_pixel.blue
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory

    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
