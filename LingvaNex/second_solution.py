#!/usr/bin/python
import sys
from itertools import product

ENGLISH_OUTPUT = 'English.txt'
RUSSIAN_OUTPUT = 'Russian.txt'


def parse(
    dictionary_path,
    english_output=ENGLISH_OUTPUT,
    russian_output=RUSSIAN_OUTPUT,
):
    with open(dictionary_path, 'r') as dictionary:
        english_translates = []
        russian_translates = []
        for line in dictionary.readlines():
            english_words, russian_words = [
                translates_string.split(' ; ')
                for translates_string in line.strip().split('\t')
            ]
            translates = product(english_words, russian_words)
            for english_word, russian_word in translates:
                english_translates.append(f'{english_word}\n')
                russian_translates.append(f'{russian_word}\n')

    with open(english_output, 'w') as english_file, \
            open(russian_output, 'w') as russian_file:
        english_file.writelines(english_translates)
        russian_file.writelines(russian_translates)


if __name__ == '__main__':
    parse(sys.argv[1])
