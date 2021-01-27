# COMS 103
# Nuria Perez Casas
# Program 3

VOWELS = "aeiouAEIOU"
CONSONANTS = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
# To make it a lot easier to identify we create a list of the capital letters and a
# list of the lower letters.
capitals = "AEIOUBCDFGHJKLMNPQRSTVWXYZ"
lower = "aeioubcdfghjklmnpqrstvwxyz"

print ("Welcome to the Pig Latin Translator.")

def capitalization():
    """ This function will take care of the uppercase letters and the
    capitalization of the words. No parameters.

    """
    # We have created a loop that will count how many uppercase letters we have
    # and how many letters the word has in total.
    while True:
        word = input("Enter word: ")
        capital_counts = 0
        word_counts = 0
        result = translation(word)
        for letter in word:
            letter = letter.strip()
            word_counts += 1
            if letter in capitals:
                capital_counts += 1
        # Now we make different if statements for all the options we have with the
        # information we have at the top. 
        if word_counts == capital_counts: # This in case all the words are capital:
            print(result.upper())        
        elif capital_counts > 1: # This one if we have some extra capitals
            print(result[0].upper() + result[1:])
        elif word[0] in capitals: # This one if the first is capital
            print(result.capitalize())
        else: # The rest would be if the word has no capitals
            print(result)



def translation(word):
    """ This function only does the translation part, it picks if the word has a vowel
    in front and if not how many consonants it has to make the appropriate translations.
    It has a parameter, the input word from the capitalization function. And it
    returns the 'result' that is the translation made.
    """
    # We have created this loop that loops over one letter at a time to see how
    # mant consonants we have in the front of the word
    # If we have more than one they will add up and then they will make the translation
    # until it finds a vowel that will break the loop. 
    if word[0] in CONSONANTS:
        consonant_count = 0
        for letter in word:
            letter = letter.strip()
            if letter in CONSONANTS:
                consonant_count += 1
            elif letter in VOWELS:
                break
        result = word[consonant_count:] + word[:consonant_count] + "ay"
            
    elif word[0] in VOWELS:
        result = word + "way"  
    return result

def main():
    capitalization()
    
if __name__ == "__main__":
    main()
    
