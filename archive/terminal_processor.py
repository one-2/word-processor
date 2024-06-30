# Word processor
# This program was begun by Stephen Elliott on 4/2/23.

# libraries
import os

# constants
USER_ACTION_DICT = [
    "read_to_terminal"  : read_to_terminal(path),
    "write_new_file"    : write_new_file(path),
    "write_to_end"      : write_to_end(path),
    "count_words"       : count_words(path)
    ]


def read_to_terminal(path):
    # Takes a file path and prints the plaintext file at that path to terminal.
    # Otherwise throws an exception.
    print("Please input the filepath of your text file:")
    filepath = input()
    if filepath == ERROR_VALUE: # WHAT IS ERROR VALUE?
        print("Invalid file path.")
        Exception
    else:
        return filepath

def write_new_file(path):
    # Takes input in terminal and writes it to a new plaintext file.
    # Otherwise throws an exception.
    pass

def write_to_end(path):
    # Takes a file path and writes to the end of the plaintext file.
    # Otherwise throws an exception.
    pass

def count_words(path):
    # Prints the number of words in each line of a plaintext file to terminal.
    # Otherwise throws an exception.
    pass

def main():
    print("Hello. This is a word processor begun by Stephen Elliott on 4/2/23.")
    print("Please enter the path of a plaintext (.txt) file you would like to access, or hit enter to exit the program.")
    path = input()
    while path != "":
        print(f"What would you like to do with the file at {path}? You can:")
        print(USER_ACTION_DICT)

        # Run user action on path
        print("Please enter your preferred action.")
        action = input()
        user_function = USER_ACTION_DICT[action]
        user_function(path)

        # Report exceptions

        # Perform more actions or terminate
        print("If you would like to perform another action, please input another path. To act on the same file, press space and then enter.")
        u_input = input()
        if u_input == "":
            path = ""
        elif u_input == " " | u_input == path:
            pass
        elif u_input != path:
            path = u_input
    print("Program terminating. Goodbye.")

# main blocker
if __name__ == "main":
    main()
