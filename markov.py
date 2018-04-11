"""Generate Markov text from text files."""

import sys
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    with open(file_path) as text:
        text_one_line = text.read().replace('\n', ' ')

    return text_one_line


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    word_sequence = text_string.split()

    for i in range(0, len(word_sequence) - 2):
        bigram = (word_sequence[i], word_sequence[i+1])
        next_word = word_sequence[i+2]

        try:
            chains[bigram].append(next_word)
        except KeyError:
            chains[bigram] = [next_word]

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    words.extend(choice(chains.keys()))

    while True:
        bigram = (words[-2:])

        try:
            next_word = choice(chains[bigram])
        except KeyError:
            break

        words.append(next_word)

    return " ".join(words)


# input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(sys.argv[1])

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
