#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    with open(sys.argv[1]) as file_1:
        line_no = 0
        characters = 0
        for line in file_1:
            line_no += 1
            wordslist=line.split()
            words = len(line)
            characters += sum(len(word) for word in wordslist)
        print(f'Line:{line_no}, words:{words} character:{characters}')