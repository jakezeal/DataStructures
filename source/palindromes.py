#!python

# Hint: use string.ascii_letters (all letters in ASCII character set)
import string


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing"""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str)
    return is_palindrome_iterative(text)
    # return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    half = len(text) / 2
    left = 0
    right = -1

    for index in range(0, half):
        left_letter = text[left]
        right_letter = text[right]

        if left_letter is not right_letter:
            return False

        left += 1
        right -= 1
    return True
    # if len(text) <= 1:
    #     return True
    # while len(text) > 1:
    #     if text[-1] == text[0]:
    #         text = text[1:-1]
    #     else:
    #         return False
    # return True


def is_palindrome_recursive(text, left=None, right=None):
    # text = text.lower()
    # text = text.replace(' ', '')
    # text = text.translate(None, string.punctuation)
    #
    # if len(text) <= 1:
    #     return True
    #
    # return text[0] == text[-1] and is_palindrome_recursive(text[1:-1])

    if left is None and right is None:
        text = re.sub('[^A], '', text.lower())
        left = 0
        right = len(text) - 1

    if left >= right:
        return True

    if text[left] == text[right]:
        return is_palindrome_recursive(text, (left + 1), (right - 1))

    return False


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            str_not = 'a' if is_pal else 'not a'
            print('{}: {} is {} palindrome'.format(result, repr(arg), str_not))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
