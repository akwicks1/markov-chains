"""Generate markov text from text files."""


from random import choice

import sys


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path).read()
    contents = contents.split("\n")
    s = " "
    contents = s.join(contents)

    # print contents

    return contents


def make_chains(text_string, n=2):
    """Takes input text as string; returns dictionary of markov chains.

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
    """

    text = text_string.split(" ")

    chains = {}

    for i in range(len(text) - n):
        key = text[i:i + n]
        key = tuple(key)
        if key not in chains:
            chains[key] = [text[i + n]]
        else:
            chains[key].append(text[i + n])
    # print chains
    return chains


def make_text(chains):
    """Returns text from chains."""
    
    link_key = choice(chains.keys())
    # cap_word = str(link_key[0])
    # # link_key = str(link_key)
    # if cap_word == cap_word.capitalize():
    # # words = [' '.join(link_key)]
    #     print link_key
    if link_key[0][0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        words = list(link_key)
        



    # # print first_link_key
    # # print first_link_value
    # # print second_link_key
    # # your code goes here
    # while True:

    #     try:
    #         # get a random value from the first keys values
    #         # select next word
    #         next_word = choice(chains[link_key])

    #     except KeyError:

    #         # stops at end of file
    #         # there's no key for the last bigram
    #         break
    #     # begin on a capital letter and end on a sentence puntuation
    #     # if
    #     # add next word to list
    #     words.append(next_word)
    #     # words = s.join(words)
    #     # find next key
    #     link_key = (link_key[1:]) + (next_word,)
    #     # print link_key
    # # second_link_key = (first_link_key[1], first_link_value)
    # # second_link_value = choice(chains[second_link_key])
    # #     words.append(first_link_value)
    # #     first_link_key = (first_link_key[1],
    # #     words.append(choice(chains.values()))
    # # print words
    # # print "first link value", first_link_value
    # # print "second_link_key", second_link_key
    # # # return " ".join(words)
    # words = " ".join(words)

    # print words


n = int(raw_input("How many words do you want in your gram?: "))


input_path = sys.argv[1]

# Open the file and turn it into one long string
cheesecake = open_and_read_file(input_path)

# # Get a Markov chain
chains = make_chains(cheesecake, n)

# # Produce random text
random_text = make_text(chains)

# print random_text
