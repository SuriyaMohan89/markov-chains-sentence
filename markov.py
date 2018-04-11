"""Generate Markov text from text files."""

import sys
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    with open(file_path) as text:
        return text.read()


def make_chains(text_string, n=2):
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

    for i in range(len(word_sequence) - n):
        n_gram = tuple(word_sequence[i:i+n])
        next_word = word_sequence[i+n]

        if n_gram not in chains.keys():
            chains[n_gram] = []

        chains[n_gram].append(next_word)

    return chains


def make_text(chains, n=2, sentence=False):
    """Return text from chains."""

    words = []
    punctuation = ['.', '?', '!']

    while True:
        initial_key = choice(chains.keys())

        if not sentence or initial_key[0][0] == initial_key[0][0].upper():
            break

    words.extend(initial_key)

    while True:
        n_gram = tuple(words[-n:])

        if n_gram not in chains.keys():
            break

        words.append(choice(chains[n_gram]))

        if sentence and words[-1][-1] in punctuation:
            break

    return " ".join(words)


# Open the file and turn it into one long string
input_text = open_and_read_file(sys.argv[1])

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains, 2, True)

print random_text
