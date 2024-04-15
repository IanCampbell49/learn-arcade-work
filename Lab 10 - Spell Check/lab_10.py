import re


def split_line(line):
    # Regular expression to extract words
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


dictionary_list = []
dictionary = open('dictionary.txt')
for word in dictionary:
    dictionary_list.append(word.strip())
dictionary.close()

print("--- Linear Search ---")

alice_text = open('AliceInWonderLand200.txt')
line_number = 0
for line in alice_text:
    line_number += 1
    words = split_line(line)
    for word in words:
        if word.upper() not in dictionary_list:
            print("Line", line_number, "The word:", word, '. Might be misspelled.')
alice_text.close()

print("--- Binary Search ---")

alice_text = open('AliceInWonderLand200.txt')
line_number = 0
for line in alice_text:
    line_number += 1
    words = split_line(line)
    for word in words:
        key = word.upper()
        lower_bound = 0
        upper_bound = len(dictionary_list) - 1
        found = False
        while lower_bound <= upper_bound and not found:
            middle_pos = (lower_bound + upper_bound) // 2
            if dictionary_list[middle_pos] > key:
                upper_bound = middle_pos - 1
            elif dictionary_list[middle_pos] < key:
                lower_bound = middle_pos + 1
            else:
                found = True

        if not found:
            print("Line", line_number, "The word:", word, '. Might be misspelled.')
alice_text.close()
