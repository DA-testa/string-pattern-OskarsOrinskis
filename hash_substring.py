import os

def read_input():
    input_type = input().strip().upper()
    if input_type == "I":
        search_pattern = input().strip()
        search_text = input().strip()
    elif input_type == "F":
        file_path = 'tests/06'
        with open(file_path) as file:
            search_pattern = file.readline().strip()
            search_text = file.readline().strip()
    else:
        exit()
    return input_type, search_pattern, search_text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def aaa(pattern, text):
    m = len(pattern)
    n = len(text)
    if m == 0: return []
    skip = []
    for k in range(256): skip.append(m)
    for k in range(m - 1): skip[ord(pattern[k])] = m - k - 1
    skip = tuple(skip)
    occurrences = []
    k = m - 1
    while k < n:
        j = m - 1
        i = k
        while j >= 0 and text[i] == pattern[j]:
            j -= 1
            i -= 1
        if j == -1: occurrences.append(i + 1)
        k += skip[ord(text[k])]
    return occurrences

def get_occurrences(input_type, search_pattern, search_text):
    # this function should find the occurances using Rabin Karp alghoritm 

    # and return an iterable variable
    return aaa(search_pattern, search_text)

# this part launches the functions

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
