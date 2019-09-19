"""
@Coding: uft-8
@Time: 2019-09-19 23:39
@Author: Ryne Chen
@File: replace.py 
@Python Version: 3
"""


def replace(string):
    ls = []
    for i in string:
        if i == ' ':
            ls.append('%20')
        else:
            ls.append(i)
    return ''.join(ls)


def main():
    string = 'We Are Happy.'
    print(replace(string))


if __name__ == '__main__':
    main()
