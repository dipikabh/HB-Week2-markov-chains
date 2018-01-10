"""Generate Markov text from text files."""

from random import choice
import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    file_object = open(file_path)
    contents = file_object.read()
    file_object.close()

    return contents


def make_chains(text_string, n):
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

    # your code goes here
    words = text_string.split()
    
    for i in range(0, len(words)-n):
        t = tuple(words[i:n+i])
        chains[t] = chains.get(t, []) + [words[i+n]]
       # bigram = (words[i], words[i+1])
       # chains[bigram] = chains.get(bigram, []) + [words[i+2]]

    # print chains

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    random_key = choice(chains.keys())
    #random_key=('I', 'am?')
    # print "\n\nfirst random key is: ", (random_key)

    #words.append(random_key[0])
    #words.append(random_key[1])

    words.extend(list(random_key))

    while True:
        if random_key in chains:
            random_value = choice(chains[random_key])
            words.append(random_value)
            next_key = random_key[1:] + (random_value,)
            random_key = next_key
        else:
            break

    return " ".join(words)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# print input_text

# Get a Markov chain
chains = make_chains(input_text, 4)

# Produce random text
random_text = make_text(chains)

print random_text

