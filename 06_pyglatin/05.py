print "Welcome to the English to Pig Latin translator!"

original = raw_input("What word would you like to be translated?")

if len(original) > 0 and original.isalpha():
    print original
else:
    print "empty"
