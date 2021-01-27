# COMS 103
# Program 4
# Pig Latin Translator Part 2
# Nuria Perez Casas


VOWELS = "aeiou"


CONSONANTS = "bcdfghjklmnpqrstvwxyz"

SYMBOLS = "()"":,!.?;"

# I know the program crashes very usually because I never got the
# punctuation function to work and that is the one that
# handles all the rest. 

def handle_consonant_word(word):
    """
    Translate one English word that starts with a consonant to Pig Latin.

    The rule is as follows:
        - All initial consonants are moved to the end of the word
        - "ay" is appended to the end

    Parameters:
        word - the word to translate, it must start with a consonant, no punctuation or spaces

    Returns:
        The word after translation.
    """
    if len(word) == 0 or word[0].lower() not in CONSONANTS:
        return word

    consonant_count = 0
    for letter in word:
        if letter.lower() in CONSONANTS:
            consonant_count += 1
        else:
            break
        result = word[consonant_count:] + word[:consonant_count] + "ay"
    return result
    

def handle_one_word(word):
    """
    Translate one single word from English to Pig Latin, regardless of
    capitalization or other factors.

    The rules are as follows:
        - If the word starts with a consonant, move all initial consonants
          to the end of the word, and add "ay" after
        - If the word starts with a vowel, append "way" to the end

    Parameters:
        word - the word to translate, just a word, no punctuation or spaces

    Returns:
        The word after translation, with possibly incorrect capitalization.
    """

    if len(word) == 0:
        return word
    
    if word[0].lower() in CONSONANTS:
        result = handle_consonant_word(word)
    elif word[0].lower() in VOWELS:
        result = word + "way"
    else:
        result = word        
    return result

def handle_capitals(word):
    """
    Take an English word with no puncutation at the start or end and
    translate it into Pig Latin with the correct capitalization.

    The rules are as follows:

        - If the word has no capitals before translation, it will have
          no capitals after translation
        - If every letter in the word is capital before translation,
          every letter will be capital after translation
        - If the first letter of the word is capital before translation,
          the first letter will be capital after translation
        - If there are capital letters other than the first letter before
          translation, then keep the case of the first letter after translation
          and leave the others alone.

    Parameters:
        word - the word to translate, just a word, no punctuation or spaces

    Returns:
        The word after translation, with correct capitalization.
    """

    if len(word) == 0:
        return word

    has_all_capitals = word == word.upper()
    
    has_initial_capital = word[0] == word[0].upper()
    
    has_nonfirst_capital_and_lowercase_first_letter = len(word) > 1 and word[1:] != word[1:].lower() and word[0] == word[0].lower()

    
    result = handle_one_word(word)

    
    if has_all_capitals:
        result = result.upper()
    elif has_initial_capital:
        if len(result) > 1:
            result = result[0].upper() + result[1:]
        else:
            result = result[0].upper()
    elif has_nonfirst_capital_and_lowercase_first_letter:
        result = result[0].lower() + result[1:]

    return result
    

def handle_punctuation(word):
    """ This function is the main function that will be called to translate
    any words. It will handle the hyphen and all the punctuation symbols as well.
    However and very sadly I was not able to get it to work. Which means
    that the program crushes every single time.
    I tried multiple things and I also asked you over email, but I never got it
    to work completely...
    """
    for letter in word:
        if letter == "-":
            chunks = word.split("-")
            pieces = []
            for word in chunks:
                pieces.append(handle_capitals(word))
            result = "-".join(pieces)
            return result
        else:
            break
    # I have tried so many things and I know the error is on this section but
    # for some reason I can't solve it. 
    front_punctuation = 0
    back_punctuation = 0
    for i in range(len(word)):
        if word[0] in SYMBOLS and i>0:
            front_punctuation += word[0]
            word=word[1:]
        elif word[-1] in SYMBOLS and i>0:
            back_puncuation += word[-1]
            word = word[:-1]
        else:
            break

    word = handle_capitals(word)
    result = front_punctuation + word + back_punctuation
    return result


def text_by_hand():
    """This function handles all the text that is written by hand and sends
    it to other functions
    """
    text_by_hand = input("What would you like to translate? ")
    words = text_by_hand.split(' ')
    pieces = []
    for word in words:
        results = handle_punctuation(word)
        pieces.append(results)   
    print("Translated text: ", *pieces, sep=' ')

def load_text_from_file():
    """This function asks the user for the name of the text file they want to
    open and it sends it to the other functions to translate every word on it.
    And then it puts together all the words that have already been translated.
    """
    file = input("What is the exact name of the file you wish to translate? ")
    pieces = []
    with open(file) as f:
        for line in f:
            for word in line.split():
                pieces.append(handle_punctuation(word))
            result = " ".join(pieces)
             
    print("Translated text: ", *result)
            
            

def main():
    """This is the main function and what we call in order to make the program run.
    It asks the user for input and what they want to do and then sends it out.
    """
    while True:
        print("""Welcome to the Pig Latin Translator Program.
            What would you like to do?
            (a)Input text by hand
            (b)Load text from a file
            """)
        choice = input("Choose an option: ")
        if choice.lower() == "a":
            text_by_hand()
            again = input ("Do you want to keep translating? Yes or No:")
            if again.lower() == y or again.lower() == yes:
                continue
            else:
                print("Thank you for using the program!! :)")
                break
        elif choice.lower() == "b":
            load_text_from_file()
            again = input ("Do you want to keep translating? Yes or No:")
            if again.lower() == y or again.lower() == yes:
                continue
            else:
                print("Thank you for using the program!! :)")
                break
        else:
            print("Sorry that is not an option. Try again")
                

if __name__ == "__main__":
    main()
