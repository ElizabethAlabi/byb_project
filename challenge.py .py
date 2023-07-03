"""
1. Add a prefix to a word
One of the most common prefixes in English is un, meaning "not". In this activity, your sister needs to make negative, or "not" words by adding un to them.

Implement the add_prefix_un() function that takes word as a parameter and returns a new un prefixed word:
"""


def add_prefix_un(word):
    return "un" + word


"""
2. Add prefixes to word groups
There are four more common prefixes that your sister's class is studying: en (meaning to 'put into' or 'cover with'), pre (meaning 'before' or 'forward'), auto (meaning 'self' or 'same'), and inter (meaning 'between' or 'among').

In this exercise, the class is creating groups of vocabulary words using these prefixes, so they can be studied together. Each prefix comes in a list with common words it's used with. The students need to apply the prefix and produce a string that shows the prefix applied to all of the words.

Implement the make_word_groups(<vocab_words>) function that takes a vocab_words as a parameter in the following form: [<prefix>, <word_1>, <word_2> .... <word_n>], and returns a string with the prefix applied to each word that looks like: '<prefix> :: <prefix><word_1> :: <prefix><word_2> :: <prefix><word_n>'
"""


def make_word_groups(vocab_words):
    # loop to add the first element to every other elements in the list
    for i in range(1, len(vocab_words)):
        vocab_words[i] = vocab_words[0] + vocab_words[i]
    return ' :: '.join(vocab_words)


"""
3. Remove a suffix from a word
ness is a common suffix that means 'state of being'. In this activity, your sister needs to find the original root word by removing the ness suffix. But of course there are pesky spelling rules: If the root word originally ended in a consonant followed by a 'y', then the 'y' was changed to 'i'. Removing 'ness' needs to restore the 'y' in those root words. e.g. happiness --> happi --> happy.

Implement the remove_suffix_ness(<word>) function that takes in a word str, and returns the root word without the ness suffix.
"""


def remove_suffix_ness(word):
    # removes 'ness' from the word
    w = word.split("ness")[0]
    # gets the length of the word
    num = len(w)-1
    # checks if the last letter is "i"
    if w[-1] == "i":
        new_word = w[:num] + "y"
        return new_word
    # returns the word if the last letter is not 'i'
    else:
        return w


"""
4. Extract and transform a word
Suffixes are often used to change the part of speech a word has. A common practice in English is "verbing" or "verbifying" -- where an adjective becomes a verb by adding an en suffix.

In this task, your sister is going to practice "verbing" words by extracting an adjective from a sentence and turning it into a verb. Fortunately, all the words that need to be transformed here are "regular" - they don't need spelling changes to add the suffix.

Implement the adjective_to_verb(<sentence>, <index>) function that takes two parameters. A sentence using the vocabulary word, and the index of the word, once that sentence is split apart. The function should return the extracted adjective as a verb.
"""


def adjective_to_verb(sentence, index):
    temp = sentence.split()
    # removing the fullstop after the sentence
    word = temp[index].rstrip(".")
    return word + "en"


# print(add_prefix_un("happy"))
# print(remove_suffix_ness("heaviness"))

# print(make_word_groups(['en', 'close', 'joy', 'lighten']))
# print(make_word_groups(['pre', 'serve', 'dispose', 'position']))
# print(adjective_to_verb('I need to make that bright.', -1))
# print(adjective_to_verb('It got dark as the sun set.', 2))
