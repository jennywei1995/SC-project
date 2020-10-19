"""
File: boggle.py
Name: Jenny Wei
----------------------------------------
This program will ask the user to give 4 rows of 4 letters.
And the program will check the board (4*4), starting form one of the letter
and link to its neighbor letter(in 8 directions) and print all the possible
words (length should be at least 4 letters) on the console.
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
from typing import Dict, Any

FILE = 'dictionary.txt'

# Global variables
dic_lst = []  # the list to contain all the words in the dictionary
row_lst = []  # to contain the letter (in the order of row) given by the user
count = 0


def main():
    """
    This program will ask the user to give 4 rows of 4 letters.
    And the program will check the board (4*4), starting form one of the letter
    and link to its neighbor letter(in 8 directions) and print all the possible
    words (length should be at least 4 letters) on the console.
    """
    read_dictionary()
    if row_input():
        find_boggle(row_lst)
        print(fr'There are {count} words in total.')


def row_input():
    """
    This function enables the user to input the letter they want
    to create the board of the boggle game
    :return: (bool) True or False
    """
    for i in range(4):
        row = input(fr'{i+1} row of letters: ')
        single_row = row.split()
        if len(single_row) == 4:
            for j in range(len(single_row)):
                if len(single_row[j]) != 1 or not single_row[j].isalpha():
                    print('Illegal format')
                    return False
                else:
                    single_row[j] = single_row[j].lower()
            row_lst.append(single_row)
        else:
            print('Illegal format')
            return False
    return True


def find_boggle(rows):
    """
    This function will check the board, by firstly giving all the letters their x,y coordinate
    and by  using the helper function to make sure all the words could be found
    :param rows: the row list that are given by the user
    :return: This function won't return anything
    """
    # to contain the (x,y) of each letter
    xy_lst = []
    words_lst = []
    for x in range(len(rows)):
        for y in range(len(rows)):
            xy_lst.append((x, y))
    for x, y in xy_lst:
        find_boggle_helper([], words_lst, '', x, y)


def find_boggle_helper(coordinate_lst, boggle_words, current_str, x, y):
    """
    This is a helper function that will use recursion to find all the possible words
    from the board that is created by users' input in the dictionary
    :param coordinate_lst: the list to contain the coordinate of the letter that already exist in the word
    :param boggle_words: the words_lst to contain the word that is printed on the console
    :param current_str: the string of the word
    :param x: the x coordinate of a specific letter(the started one is 0)
    :param y: the y coordinate of a specific letter(the started one is 0)
    :return: this function won't return anything
    """
    global count
    if len(current_str) >= 4:
        if current_str in dic_lst:
            if current_str not in boggle_words:
                boggle_words.append(current_str)
                count += 1
                print(fr'Found: {current_str}')
    if (x, y) not in coordinate_lst:
        coordinate_lst.append((x, y))
        current_str = ''
        for x1, y1 in coordinate_lst:
            current_str += row_lst[x1][y1]
        if has_prefix(current_str):
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    new_x = x + i
                    new_y = y + j
                    if 0 <= new_x < len(row_lst):
                        if 0 <= new_y < len(row_lst):
                            find_boggle_helper(coordinate_lst, boggle_words, current_str, new_x, new_y)
        coordinate_lst.pop()


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    with open('dictionary.txt', 'r') as f:
        for line in f:
            word = line.strip()
            dic_lst.append(word)


def has_prefix(sub_s):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    for word in dic_lst:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()