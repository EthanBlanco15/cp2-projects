#Ethan Blanco

alphab = []
morsec_dict = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
morsecode = ""

def morse_translator(morse_alpha_conversion): #Used for translating the morse code into words.
    
    morse_alpha_conversion = input("What morse code word would you like translated? Use capitalizations please")

morse_translator()

def alpha_translator(alpha_conversion): #Used for translating the English words into morse code.

    alpha_conversion = input("What English worde would you like translated?")

alpha_translator()

def main(main_userin): #Main user interface that will mostly be seen when starting.
    
    while True:
        main_userin = input("""Welcome to the morse code translator
                            type yes if you would like to translate words into morse code,
                            or type no to morse code into words?
                            and type exit if you'd like to leave the program\n""")
        if main_userin == "yes" or "Yes" or "YES" or "y" or "Y":
            alpha_translator#(alpha_conversion)
        elif main_userin == "no" or "No" or "NO" or "n" or "N":
            morse_translator#(morse_alpha_conversion)
        elif main_userin == "exit" or "Exit" or "EXIT":
            print("Goodbye!")
            break
        else:
            print("This doesn't work, maybe try again later.")
            continue


main()