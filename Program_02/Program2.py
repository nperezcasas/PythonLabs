# Program 2
# Nuria Perez Casas
# COMS 103

def main():
    
# First of all we create a dictionary and we add all the words from our imported
# file to the dictionaty.
    texting_dictionary = {}
    with open("texting_to_english.txt") as f:
        for line in f:
            line = line.strip()
            result = line.split("|")
            if len(result) == 2:
                key = result[0]
                value = result[1]
                texting_dictionary[key] = value
                
# We also create a list that will include all the phrases we translate to make
# it easy to keep track of them for the 'p' option. 
    phrases_list = []
        
    print("Welcome to the texting to English translator.")
    print("You can enter a line of texting and it will be translated to English.")
    
# Now we create a loop for all the different options we are giving to the user.
    while True:
        print()
        print("""Available options:
            (a) add a new texting to English translation
            (n) translate a new line
            (p) print all previous lines
            (q) to quit""")
        choice = input("Choose an option:")
        print()
        if choice.lower() == "a":
        # For option 'a' we create a function that will add the words the user wishes to our
        # existing dictionary. 
            def adding_words():
                """This function asks the user for the texting word/phrase and the translation
                they wish to create and adds it to the dictionary. No parameters.

                It prints at the end a short phrase to let the user know what has been added.
                """
                texting_word = input("What is the new texting word you wish to translate? ")
                english_word = input("What is it's english equivalent? ")
                key = texting_word.lower()
                value = english_word.lower()
                texting_dictionary[key] = value
                print()
                print("Added '", texting_word, "' to translator as '", english_word, "'")
            adding_words()

        elif choice.lower() == "n":
        # For option 'n' we create a function that will translate what the user has said to from
        # texting to english and it will add all the translations to the list we created in
        # the begining. 
            def translate_line():
                """This function translates the texting using a list, it splits the words from the
                phrase and checks if they are part of the dictionary. After checking each word it
                adds it to a list and then it prints the list without [],and creating spaces.
                No parameters.
                It also adds every phrase translated to the first list (phrases_list)
                """
                line_to_translate = input("Enter a line containing texting abbreviations to be translated:  ")
                phrase = []
                for word in line_to_translate.lower().split():
                    if word in texting_dictionary:
                        word = texting_dictionary[word]
                        phrase.append(word)
                    else:
                        phrase.append(word)
                print()
                print("Translated line: ",*phrase, sep=' ')
                print()
                phrases_list.append(phrase)
            translate_line()
            
        elif choice.lower() == "p":
        # If the user wants to see all the phrases translated we will print the list that we have been
        # creating in separate lines and without[], and adding spaces.
            print("Printing translation record: ")
            print()
            for elem in phrases_list:
                print(*elem, sep = " ")
            print()
            print("End of translation history.")
                
        elif choice.lower() == "q":
        # Finally, if the user wishes to exit the function we will stop the loop and finish the program. 
            break
        
        else:
        # We add this function so that we have input validation in case the user misspells something
        # or he asks for something that doesn't exist.
            print("Option not recognized. Try again.")
            
    print("Thank you for using this program")


if __name__ == "__main__":
    main()
