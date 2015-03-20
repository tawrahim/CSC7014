def get_word_list():
    data_file = open("tester.txt", "r")
    word_list = []

    for word in data_file:
        word_list.append(word.strip().lower())
    return word_list


all_words = get_word_list()

vowel = "aeiou"


def foo(words):
    for x in words:
        count = 0
        for a in x:
            if a in vowel:
                count += 1
        print("Vowel count = " + str(count))


foo(all_words)