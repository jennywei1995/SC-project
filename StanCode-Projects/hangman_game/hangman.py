"""
File: hangman.py
Name: Jenny Wei
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
to try in order to win this game.
"""


import random


# This constant controls the number of guess the player has
N_TURNS = 7


def main():
    """
    This program can play a hangman game.
    At the beginning, a random word will be given by the program.
    And then the user will have N_TURNS guessing opportunities to find out the word.
    If the user made a wrong guess, the user will lose 1 opportunity.
    Once user used all turns and still doesn't find the answer, he/she lose the game.
    If the user find out the answer before using all guessing turns, the user wins.
    """
    word = random_word()
    old_ans = dashed(word)
    print('You have ' + str(N_TURNS) + ' guesses left.')
    guess(word, old_ans)


def random_word():
    """
    This function will pick a random word in below choices
    :return: str, a random word be chose
    """
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


def dashed(word):
    """
    This function will turn the character of random word into dash
    :param word: str, random word given by the program that have to be guessed by the user
    :return: ans(called as old_ans in the program), str, dashed word
    """
    ans = ''
    for ch in word:
        if ch.isalpha():
            ans += '-'
    print('THe word looks like ' + ans)
    return ans


def guess(word, old_ans):
    """
    This function will let the user to guess the character of the word,
    the function will either stop while user find the answer,
    or stop while the user finish all his/her guessing turns.
    :param word: str, random word given by the program that have to be guessed by the user
    :param old_ans: str, dashed word, will be compared with the answer that includes user's guess.
    """
    life = N_TURNS
    while life > 0:
        guess_ch = input('Your guess: ')
        guess_ch = guess_ch.upper()
        if guess_ch.isalpha() != True or len(guess_ch) != 1:
            print('Illegal format.')
        else:
            ans = ''
            if word.find(guess_ch) == -1:
                # when user doesn't find the right character
                print('There is no ' + guess_ch + "'s in the word.")
                life -= 1
                life = life
                for ch in word:
                    if ch == guess_ch:
                        ans += ch
                    else:
                        ans += '-'
            else:
                # when user make a correct guess that find out the right character of the word
                print('You are correct!')
                for ch in word:
                    if ch != guess_ch:
                        ans += '-'
                    else:
                        ans += guess_ch
            new_ans = ''
            for i in range(len(old_ans)):
                # to keep the previous right guess' result
                ch = old_ans[i]
                if ch.isalpha():
                    new_ans += ch
                elif ch != ans[i]:
                    new_ans += guess_ch
                else:
                    new_ans += ch
            old_ans = new_ans
            if old_ans.isalpha():
                # when the user find all characters of the random word ans still alive
                print('You win!!')
                print('The word was: '+word)
                break
            else:
                if life > 0:
                    print('The word looks like '+old_ans)
                    print('You have '+str(life)+' guesses left.')
    # when the user make wrong guesses and finish all his/her guess opportunities
    if life == 0:
        print('You are completely hung : (')
        print('The word was: '+word)





#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
