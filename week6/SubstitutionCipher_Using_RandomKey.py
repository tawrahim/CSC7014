#!/usr/bin/env python
# Tawheed Raheem
# Practice of a computer programmer
# This program encrypts messages using the substituition encryption
# tabdulra@student.fitchburgstate.edu
# Known bugs: none


from random import randint

letters_of_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                       "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def hey_generate():
    key = ""
    
    while len(key) != 26:
        random_number = randint(0,25)
        if letters_of_alphabet[random_number] not in key:
            key += letters_of_alphabet[random_number]
    
    return key


def scramble_2_encrypt(text, key):
    encrypted_message = ""
    for x in text.lower():
        position = ord(x) - 97
        if 0 <= position <= 25:
            encrypted_message += key[position]
        else:
            encrypted_message += x
    
    return encrypted_message


def scramble_2_decrypt(text, key):
    decrypted_message = ""
    for x in text.lower():    
        position = ord(x) - 97
        if 0 <= position <= 25:
            decrypted_message += letters_of_alphabet[key.index(x)]
        else:
            decrypted_message += x
    
    return decrypted_message


def main():
    print("To run the program type start() at the prompt")
    user_input = input()
    
    if user_input == "start()":
        
        random_key = hey_generate()
        
        print("Welcome to my encryption/decryption program")
        print("This program uses substitution cipher using a randomly generated key")
        print("Here is the generated key")
        print(random_key)
        
        print("Please enter a text to encrypt: ")
        text_to_encrypt = input()

        print("\nHere is the encrypted text")
        scrambled = scramble_2_encrypt(text_to_encrypt, random_key)
        print(scrambled)
        
        print("\nThe encrypted text decrypted back is ")
        print(scramble_2_decrypt(scrambled, random_key))

if __name__ == '__main__':
    main()