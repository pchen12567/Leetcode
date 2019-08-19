"""
@Coding: uft-8
@Time: 2019-08-19 20:42
@Author: Ryne Chen
@File: inver_words.py
@Python Version: 3.6
"""

"""
句子反转，如“I am a boy.”,反转完为“boy. a am I”
"""


def invert_words(s):
    s_new = s.split(' ')
    res = ' '.join(i for i in s_new[::-1])
    print(res)


def main():
    s = "I am a boy."
    invert_words(s)


if __name__ == '__main__':
    main()
