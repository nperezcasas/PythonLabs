# COMS 103
# Nuria Perez Casas
# Lab 07

# Download accompanying file `book.txt`, place in same directory as this file.

# Three separate tasks:
# - count_letters()
#		Count the letters in the book
#		Print out the top 10 most used letters
# - count_words()
#		Count the words in the book
#		Print out the top 10 most used words
# - count_capitalized_words()
#		Count the capitalized words in the book
#		Print out the top 10 most used capitalized words

# We will work on the count_letters() function together in class
# and you will be responsible for the others.

# Each function should be called from main() and should print out
# its results, no returns necessary


# We import string because we will need it.

import string

def count_letters():
    """Count the total number of letters in the book file, it also
    selects the ten most used ones.

    No parameter, the book file name is hardcoded in this case.
    """
    with open("book.txt") as f:
        # f.read() - will just pull in the entire file to a single string...
        # then you are no longer doing file input, but just string work
        
        file_contents = f.read()
    # now the file is closed automatically,
    # and we just have to process a string

    # We will use an Accumulator:
    total_letters = 0

    # And we will open a dictionary:
    letter_counts = {} 

    # ANd now we create the loop itself that will check every single letter
    # in lower case and it will add the letter to the dictionary if it
    # doesn't exist and it will add to every existing one and in the total 
    for character in file_contents:
        if character.isalpha():
            if character.lower() not in letter_counts:
                letter_counts[character.lower()] = 1
            else:
                letter_counts[character.lower()] += 1
            total_letters += 1
        
    print("Total letters:", total_letters)

    # We want to only print out the top 10 most used,
    # not the whole collection:
    print(sorted(letter_counts, key=letter_counts.get, reverse=True)[:10])
    # slice of the list: [] with a number inside
    # after this point, we do not need to open or look at the file anymore
    
def count_words():
    """Count the total number of words in the book file. And it sorts and
    prints which are the 10 most used. 

    No parameter, the book file name is hardcoded in this case.
    """
    # We basically do the same thing we did in the top but instead of with
    # letters we do it with words.
    with open("book.txt") as f:
        my_string = f.read()
        
    total_words = 0
    word_counts = {}
    
    words = my_string.split()
    
    for word in words:
        if word.isalpha():
            if word.lower() not in word_counts:
                word_counts[word.lower()] = 1
            else:
                word_counts[word.lower()] += 1
            total_words += 1
        
    print("Total words: ", total_words)
    
    print(sorted(word_counts, key=word_counts.get, reverse=True)[:10])

def count_capitalized_words():
    """Count the total number of capitalized words in the book file.
    And it sorts and prints the 10 most used. 

    No parameter, the book file name is hardcoded in this case.
    """
    with open("book.txt") as f:
        my_string_capitalized = f.read()

    total_capitalized = 0
    capitalize_counts = {}
    
    capitalized = my_string_capitalized.split()
    
    # Now we do the same thing we did with the word function but this time
    # we have to sort through the capitalized words and that's why we add
    # an extra if statement.
    for word_capitalized in capitalized:
        if word_capitalized[0] in string.ascii_uppercase:
            if word_capitalized not in capitalize_counts:
                capitalize_counts[word_capitalized] = 1
            else:
                capitalize_counts[word_capitalized] += 1
            total_capitalized += 1
        
    print("Total capitalized words: ", total_capitalized)
    
    print(sorted(capitalize_counts, key=capitalize_counts.get, reverse=True)[:10])
    

def main():
    count_letters()
    count_words()
    count_capitalized_words()

if __name__ == "__main__":
    main()
