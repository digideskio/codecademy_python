pyg = 'ay'

original = raw_input('Enter a word:')

# Verify that the word provided is valid.
if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]

    # If the word starts with a vowel we only add "ay" to the end of it.
    if first == "a" or first == "e" or first == "i" or first == "o" or first == "u":
        new_word = word + pyg
        print new_word

    # If the word starts with a consonant we need to move the first letter to the end, then add "ay"
    else:
        new_word = word[1:len(word)] + word[0] + pyg
        print new_word

# This means we didn't get a valid word :(
else:
    print 'empty'
