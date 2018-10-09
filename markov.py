"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    text_string = open(file_path).read()
    return text_string


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
    word_list = text_string.split()
   # print(word_list)
    # your code goes here
    for word in range(len(word_list) - 2):
        key = (word_list[word], word_list[word + 1])
        value = word_list[word + 2]

        if key not in chains.keys():
            chains[key] = [value]
        else:
            chains[key].append(value)

    return chains


def make_text(chains):
    """Return text from chains."""
    
    # picking a random key (tuple) from the dict
    key = choice(list(chains.keys()))
    sentence = [key[0], key[1]]
    # picking random word from the value (list) associated with the key (tuple)
    next_word = choice(list(chains[key]))
    sentence.append(next_word)

    while next_word is not None:
        # making tuple from first key's second word and first keys random value
        next_key = (key[1], next_word)
        print(next_key)
        # picking random word from next key's list
        next_word = choice(list(chains[next_key]))
        # appending next next word to sentence list
        sentence.append(next_word)
        key = next_key

    

    # return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)


