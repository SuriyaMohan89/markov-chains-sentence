# import sys
from random import choice


def access_file(file_name):
    """ Open and parse input file"""
    with open(file_name) as text:
        words_in_text = text.read().replace("\n", " ")
    return words_in_text


def construct_dictionary(input_text, n=2):
    """ Creating a dictionary with n-grams """
    word_dictionary = {}
    words = input_text.split()
    for i in range(0, len(words)-n):
        n_grams = tuple(words[i:i+n])
        next_word = words[i+n]

        # if n_grams in word_dictionary:
        #     word_dictionary[n_grams].append(next_word)
        # else:
        #     word_dictionary[n_grams] = [next_word]

        if n_grams not in word_dictionary:
            word_dictionary[n_grams] = []
        word_dictionary[n_grams].append(next_word)

        # try:
        #     word_dictionary[n_grams].append(next_word)
        # except KeyError:
        #     word_dictionary[n_grams] = [next_word]

    return word_dictionary


def markov_generator(word_dictionary, n=2):
    word_list = []
    word_list.extend(choice(word_dictionary.keys()))

    while True:
        n_gram = tuple(word_list[-n:])

        if n_gram not in word_dictionary:
            break

        next_word = choice(word_dictionary[n_gram])
        word_list.append(next_word)

    return " ".join(word_list)


input_text = access_file('gettysburg.txt')
n_grams = construct_dictionary(input_text, 5)
print markov_generator(n_grams, 5)
