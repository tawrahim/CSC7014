#!/usr/bin/env python
# Tawheed Raheem
# Practice of a computer programmer
# This program encrypts messages using the vigenere encryption
# tabdulra@student.fitchburgstate.edu
# Known bugs: there is a problem decrypting text back

letters_of_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                       "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
matrix = [[0]*26 for i in range(26)]


# Builds an N X N matrix that represent the vigenere matrix
def generate_matrix():
    col = 1

    i = 0
    for _ in range(0, len(matrix)):
        j = 0

        col_calc = col % 26
        if col_calc >= 26:
            col = 1

        row = col
        for __ in range(0, len(matrix)):
            calc = row % 26
            if calc >= 26:
                row = 1
            matrix[i][j] = letters_of_alphabet[calc - 1]
            row += 1
            j += 1
        i += 1
        col += 1


def cipher_text(key_letter, plaintext_letter):
    cipher = ""
    top_row = generate_top_row(key_letter, plaintext_letter)
    for x, y in zip(top_row, plaintext_letter):
        if y not in letters_of_alphabet:
            cipher += y
            continue
        row = ord(x) - 97
        col = ord(y) - 97
        cipher += matrix[row][col]
    return cipher


def undo_vig(key_letter, cipher_text):
    plaintext = ""
    top_row = generate_top_row(key_letter, cipher_text)
    for x, y in zip(top_row, cipher_text):
        if y not in letters_of_alphabet:
            plaintext += y
            continue
        row = ord(x) - 97
        col = ord(y) - 97
        plaintext += matrix[col][row]
    return plaintext


def generate_top_row(key, plain_text):
    key_len = len(key)
    result = ""
    count = 0
    for _ in plain_text:
        if count > key_len - 1:
            count = 0
        result += key[count]
        count += 1
    return result


def main():
    print("To run the program type start() at the prompt")

    user_input = input()

    if user_input == "start()":

        print("Welcome to my encryption/decryption program")
        print("This program uses Vignere cipher")
        print("Please enter a text to encrypt: ")

        text_to_be_encrypted = input().lower()

        user_key = input("\n\nPlease enter a key all in lowercase: ").lower()

        output = cipher_text(user_key, text_to_be_encrypted)

        print("Here is the encrypted text")
        print(output)

        print("\n\nThe encrypted text decrypted back is ")
        foo = undo_vig(user_key, output)
        print(foo)


# Entry point of our program
if __name__ == '__main__':
    generate_matrix()
    main()
