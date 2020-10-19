"""
File: anagram.py
Name: Jenny Wei
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop

# global variables
python_list = []  # This list will contain the words in the dictionary.txt
words_lst = []  # This list will contain the anagram that has been found


def main():
    """
    This program recursively finds all the anagram(s)
    for the word input by user and terminates when the
    input string matches the EXIT constant defined
    at line 19
    """
    read_dictionary()
    print(fr'Welcome to StanCode "Anagram Generator" (or {EXIT} to quit)')
    s = input('Find anagrams for: ')
    while s != EXIT:
        if not s.isalpha():
            # if the user type wrong format, the program will ask the user to input again
            print('Illegal format, please input again')
            s = input('Find anagrams for: ')
        else:
            find_anagrams(s)
            s = input('Find anagrams for: ')


def read_dictionary():
    """
    This function will read through the dictionary.txt file
    and append all the words in each line into the python list.
    """
    with open('dictionary.txt', 'r') as f:
        for line in f:
            word = line.strip()
            python_list.append(word)


def find_anagrams(s):
    """
    This function combines a helper function to find the anagrams for the searching word
    After all the anagrams be found, it will print out the result that indicates
    the amount and the list of the anagrams on the console.

    :param s: the word given by the user to look for its anagrams.
    :return: This function will not return anything
    """
    s_lst = []
    for ch in s:
        # to make the program case insensitive
        ch = ch.lower()
        s_lst.append(ch)
    print('Searching...')
    find_anagrams_helper(s_lst, [], [], '')
    print(fr'{len(words_lst)} anagrams: {words_lst}')
    while len(words_lst) >= 1:
        words_lst.pop()


def find_anagrams_helper(s_lst, current_lst, str_lst, word_str):
    """
    This function is a helper function of the function-find_anagrams that will find the
    anagrams for the words given by the user.

    :param s_lst: the list that contains the alpha of the word given by the user
    :param current_lst: the list that contains the index of any permutation of the alpha
    :param str_lst: the list that matches the current list with the index's corresponding alphabet
    :param word_str: transfer the str_lst into the word string
    :return: this function won't return anything
    """
    if len(word_str) == len(s_lst):
        if word_str in python_list:
            if word_str not in words_lst:
                print(fr'Found: {word_str}')
                words_lst.append(word_str)
                print('Searching...')
    else:
        for i in range(len(s_lst)):
            if i not in current_lst:
                current_lst.append(i)
                str_lst.append(s_lst[i])
                word_str = ''
                for j in range(len(str_lst)):
                    word_str += str_lst[j]
                if has_prefix(word_str):
                    find_anagrams_helper(s_lst, current_lst, str_lst, word_str)
                current_lst.pop()
                str_lst.pop()


def has_prefix(sub_s):
    """
    :param sub_s: (str) A substring that is constructed by the permutation of the alphabet of the searching word
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    for word in python_list:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
