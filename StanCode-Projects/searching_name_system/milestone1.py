"""
File: milestone1.py
Name: Jenny Wei
-----------------------
This file tests the milestone 1 for
our babyname.py project
"""


import sys


def add_data_for_name(name_data, year, rank, name):
    """
    This function will add the data of a given name,
    a specific year and the rank that the name got to the name_data dictionary

    :param name_data: the dic that contains the key represent baby's name and
                    the value that is a sub-dic contains name's rank in a specific year
    :param year: a specific given year
    :param rank: the rank that baby's name holds in a specific year
    :param name: baby's name that will be added to the dic
    :return: this function does not return any value.
    """
    d = name_data
    if name in d:
        name_dic = d[name]
        # if the dic already has the given year and given name's data
        if year in name_dic:
            # to check the already exit rank of the given year
            old = name_dic[year]
            # to keep the higher rank (lower number) of the name
            if int(old) > int(rank):
                # if the new rank's number is lower,
                # assign it to the given year
                name_dic[year] = rank
        else:
            # if the year is not yet be added
            name_dic[year] = rank
    else:
        # if the name is not yet in the name_data dic
        name_new_data = {year: rank}
        d[name] = name_new_data


# ------------- DO NOT EDIT THE CODE BELOW THIS LINE ---------------- #


def test1():
    name_data = {'Kylie': {'2010': '57'}, 'Nick': {'2010': '37'}}
    add_data_for_name(name_data, '2010', '208', 'Kate')
    print('--------------------test1----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def test2():
    name_data = {'Kylie': {'2010': '57'}, 'Nick': {'2010': '37'}}
    add_data_for_name(name_data, '2000', '104', 'Kylie')
    print('--------------------test2----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def test3():
    name_data = {'Kylie': {'2010': '57'}, 'Sammy': {'1980': '451', '1990': '200'}, 'Kate': {'2000': '100'}}
    add_data_for_name(name_data, '1990', '900', 'Sammy')
    add_data_for_name(name_data, '2010', '400', 'Kylie')
    add_data_for_name(name_data, '2000', '20', 'Kate')
    print('-------------------test3-----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def test4():
    name_data = {'Kylie': {'2010': '57'}, 'Nick': {'2010': '37'}}
    add_data_for_name(name_data, '2010', '208', 'Kate')
    add_data_for_name(name_data, '2000', '108', 'Kate')
    add_data_for_name(name_data, '1990', '200', 'Sammy')
    add_data_for_name(name_data, '1990', '90', 'Sammy')
    add_data_for_name(name_data, '2000', '104', 'Kylie')
    print('--------------------test4----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def main():
    args = sys.argv[1:]
    if len(args) == 1 and args[0] == 'test1':
        test1()
    elif len(args) == 1 and args[0] == 'test2':
        test2()
    elif len(args) == 1 and args[0] == 'test3':
        test3()
    elif len(args) == 1 and args[0] == 'test4':
        test4()


if __name__ == "__main__":
    main()
