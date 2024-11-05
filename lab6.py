import data
from typing import Optional
from data import Book
# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp


# Part 1
# helper function for part 1
# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of books
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def book_index_smallest_from(values:list[Book], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx].title.upper() < values[mindex].title.upper():
            mindex = idx

    return mindex

# A selection sort that works on datatype books and sorts them in alphabetical order
# input a list of book datatypes
# output the input list sorted in alphabetical order

def selection_sort_books(values:list[Book]) -> None:
    for idx in range(len(values) - 1):
        mindex = book_index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp
# Part 2
# function swaps the cases of chars in a string
# input is a string to be swapped cases
# output is a string that has been swapped
def swap_case(str1:str) -> str:
    result = []
    for char in str1:
        if char.isalpha():
            if char.isupper():
                result.append(char.lower())
            else:
                result.append(char.upper())
        else:
            result.append(char)
    return ''.join(result)
# Part 3
#Function that takes a string and replaces every instance of a character x, and replaces it with character y
# input is three strings. The first is the main string, the second is the target character and the third is the replacement
# returns a string with characters specified replaced
def str_translate(input_str:str, old:str, new:str) -> str:
    result = []
    for char in input_str:
        if char == old:
            result.append(new)
        else:
            result.append(char)

    return ''.join(result)
# Part 4
#creates a frequency dictionary that counts the occurances of each word in the given string.
#inputs a string containing words separated by spaces
#outputs a dictionary where keys represent a unique word and the value is the frequency.
def histogram(para: str) -> dict:
    word_count = {}
    words = []

    current_word = ""
    for char in para:
        if char == " ":
            if current_word:
                words.append(current_word)
                current_word = ""
        else:
            current_word += char

    #accounts for end
    if current_word:
        words.append(current_word)

    for word in words:
        if word in word_count:
            word_count[word] +=1
        else:
            word_count[word] = 1

    return word_count
