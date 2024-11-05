import data
from data import Book
import lab6

import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def test_book_index_smallest_from_valid_start(self):
        # Test `book_index_smallest_from` with a valid start index
        books = [Book(["Author A"], "Zebra"), Book(["Author B"], "Apple"), Book(["Author C"], "Mango")]
        start = 1
        expected_index = 1  # "Apple" is alphabetically the smallest title from index 1
        result = lab6.book_index_smallest_from(books, start)
        assert result == expected_index, f"Expected {expected_index}, but got {result}"

    def test_book_index_smallest_from_invalid_start(self):
        # Test `book_index_smallest_from` with an invalid start index (out of bounds)
        books = [Book(["Author A"], "Zebra"), Book(["Author B"], "Apple"), Book(["Author C"], "Mango")]
        start = 5  # Out of bounds index
        expected_result = None
        result = lab6.book_index_smallest_from(books, start)
        assert result == expected_result, f"Expected {expected_result}, but got {result}"

    def test_selection_sort_books(self):
        # Test `selection_sort_books` with a typical list of books
        books = [
            Book(["Author A"], "Zebra"),
            Book(["Author B"], "Apple"),
            Book(["Author C"], "Mango")
        ]
        lab6.selection_sort_books(books)
        expected_titles = ["Apple", "Mango", "Zebra"]
        # Check if books are sorted by title
        result_titles = [book.title for book in books]
        assert result_titles == expected_titles, f"Expected {expected_titles}, but got {result_titles}"

    def test_selection_sort_books_empty_list(self):
        # Test `selection_sort_books` with an empty list
        books = []
        lab6.selection_sort_books(books)
        expected = []
        assert books == expected, f"Expected {expected}, but got {books}"

    # Part 2


    # Test 1: Standard case with a mix of uppercase and lowercase letters
    def test_swap_case_mixed_letters(self):
        input_str = "HelloWorld"
        expected_output = "hELLOwORLD"
        self.assertEqual(lab6.swap_case(input_str), expected_output)

    # Test 2: String with special characters and numbers
    def test_swap_case_with_special_chars(self):
        input_str = "Python3.8!"
        expected_output = "pYTHON3.8!"
        self.assertEqual(lab6.swap_case(input_str), expected_output)

# Part 3
    # Test 1: Basic replacement of characters
    def test_basic_replacement(self):
        input_str = "abcdcba"
        old = "a"
        new = "x"
        expected_output = "xbcdcbx"
        self.assertEqual(lab6.str_translate(input_str, old, new), expected_output)

    # Test 2: Replacement with no matches (original string should remain the same)
    def test_no_replacement(self):
        input_str = "hello world"
        old = "z"
        new = "x"
        expected_output = "hello world"  # No 'z' in input, so string should remain unchanged
        self.assertEqual(lab6.str_translate(input_str, old, new), expected_output)

# Part 4
    def test_histogram_empty_string(self):
        """
        Test the histogram function with an empty string.
        Expected output: an empty dictionary.
        """
        result = lab6.histogram("")
        expected = {}
        assert result == expected, f"Expected {expected} but got {result}"


    def test_histogram_single_word(self):
        """
        Test the histogram function with a string containing a single word.
        Expected output: a dictionary with that word counted once.
        """
        result = lab6.histogram("apple")
        expected = {"apple": 1}
        assert result == expected, f"Expected {expected} but got {result}"


    def test_histogram_multiple_words(self):
        """
        Test the histogram function with a string containing multiple words.
        Expected output: a dictionary with correct counts for each word.
        """
        result = lab6.histogram("apple banana apple")
        expected = {"apple": 2, "banana": 1}
        assert result == expected, f"Expected {expected} but got {result}"




if __name__ == '__main__':
    unittest.main()
