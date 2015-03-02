#!/usr/bin/env python
# Tawheed Raheem
# Practice of a computer programmer
# This program encrypts messages using the substituition encryption
# tabdulra@student.fitchburgstate.edu
# Known bugs: There appears to be problem with password being generated


letters_of_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                       "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def generated_password(clean_password):
    generated_key = clean_password

    print(clean_password)

    index = ord(generated_key[len(generated_key) - 1]) - 97 + 1

    while len(generated_key) <= 26:
        for x in letters_of_alphabet:
            if x not in generated_key:
                if x == "t":
                    print("Seen a tT")
                if index >= 25:
                    index = 0
                generated_key += letters_of_alphabet[index]
                index += 1

    return generated_key


def key_generate(user_password):
    # remove duplicates from the password
    clean_password = ""
    for x in user_password:
        if x not in clean_password:
            clean_password += x

    # Now we take the alphabet and remove the letters in our password
    new_alphabets = ""
    for a in letters_of_alphabet:
        if a not in clean_password:
            new_alphabets += a

    # We then use the alphabet, in order,
    # starting with the letter after the last letter in the password. When we get to 'z', we go to the
    # beginning of the alphabet and use the rest of the characters.
    return generated_password(clean_password)


def scramble_2_encrypt(text, key):
    encrypted_message = ""
    for x in text.lower():
        position = ord(x) - 97
        if 0 <= position < 25:
            encrypted_message += key[position]
        else:
            encrypted_message += x

    return encrypted_message


def scramble_2_decrypt(text, key):
    decrypted_message = ""
    for x in text.lower():    
        position = ord(x) - 97
        if 0 <= position < 25:
            decrypted_message += letters_of_alphabet[key.index(x)]
        else:
            decrypted_message += x
    
    return decrypted_message


def main():
    print("To run the program type start() at the prompt")
    user_input = input()
    
    if user_input == "start()":
        
        print("Welcome to my encryption/decryption program")
        print("This program uses substitution cipher using a randomly generated key")
        
        user_password = input("Please enter a password consisting only of lowercase letters: ").lower()
        
        print("Here is the generated key")
        random_key = key_generate(user_password)
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
