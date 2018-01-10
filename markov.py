"""Generate Markov text from text files."""

from random import choice
import sys


def open_and_read_file(file_path1, file_path2):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    file_object1 = open(file_path1)
    file_object2 = open(file_path2)
    contents = file_object1.read() + " " + file_object2.read()
    file_object1.close()
    file_object2.close()

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
    words.append(None)
    
    for i in range(0, len(words)-n):
        t = tuple(words[i:n+i])
        chains[t] = chains.get(t, []) + [words[i+n]]
       
    return chains




def make_text(chains, uppercase=True, break_on_first_punctuation=False, character_limit=True):
    """Return text from chains."""

    random_key = choice(chains.keys())
    if uppercase:
        while True:
            if random_key[0][0].isalpha() and random_key[0][0].isupper():
                break
            else:
                random_key = choice(chains.keys())


    words = list(random_key)
    #words.extend(list(random_key))

    while True:
        random_value = choice(chains[random_key])
        if random_value is None:
            break       
        words.append(random_value)
        if break_on_first_punctuation:
            if words[-1][-1] in ["?", ".", ":"]:
                break         
        next_key = random_key[1:] + (random_value,)
        random_key = next_key

    return_value =  " ".join(words)
    
    if character_limit:
        return return_value[:280]
    
    return return_value







# Open the file and turn it into one long string
input_text = open_and_read_file(sys.argv[1], sys.argv[2])


# Get a Markov chain
chains = make_chains(input_text, 4)


# Produce random text
random_text = make_text(chains)


# print random_text
print random_text
