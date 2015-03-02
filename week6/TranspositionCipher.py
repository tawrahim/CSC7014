#!/usr/bin/env python
# Tawheed Raheem
# Practice of a computer programmer
# This program encrypts messages using the transposition encryption
# tabdulra@student.fitchburgstate.edu
# Known bugs: none


def scramble_2_encrypt(user_message):
    even_string = ""
    odd_string = ""
    
    counter = 0
    for x in user_message:
        if counter % 2 == 0:
            even_string += x
        else:
            odd_string += x
        counter += 1
    
    return odd_string + even_string


def scramble_2_decrypt(crypted_word):
    
    decrypted_message = ""
    counter = 0
    
    for x in crypted_word:
        if counter % 2 == 0:
            decrypted_message += x
        else:
            decrypted_message += x
        counter += 1
    
    return decrypted_message
    

def main():
    print("To run the program type start() at the prompt")
    user_input = input()

    if user_input == "start()":

        print("Welcome to my encryption/decryption program")
        print("Please enter a text to encrypt: ")

        user_input = input("")

        if user_input:
            print("\nHere is the encrypted text")
            print(scramble_2_encrypt(user_input))

            print("\nThe encrypted text decrypted back is ")
            print(scramble_2_decrypt(user_input))
    

if __name__ == '__main__':
    main()