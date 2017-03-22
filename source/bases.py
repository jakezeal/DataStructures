#!python

import string


def decode(str_num, base):
    """
    Decode given number from given base to base 10.
    str_num -- string representation of number in given base
    base -- base of given number
    """
    assert 2 <= base <= 36
    # TODO: Decode number
    reversed_str = str_num[::-1]
    total = 0
    for i in range(0, len(reversed_str)):
        if reversed_str[i] != '0':
            num_to_add = 0
            if reversed_str[i].isalpha():
                # TODO: DOESN'T WORK for caps vs not - only lowercase
                # num_to_add = ord(reversed_str[i]) - 86
            total += base**i * int(reversed_str[i])
    return total


def encode(num, base):
    """
    Encode given number from base 10 to given base.
    num -- the number in base 10
    base -- base to convert to
    """
    assert 2 <= base <= 36
    # TODO: Encode number
    # if num % 2 ==

    # digs = string.digits + string.letters
    # if num < 0:
    #     sign = -1
    # elif num == 0:
    #     return digs[0]
    # else:
    #     sign = 1
    #
    # x *= sign
    # digits = []
    #
    # while x:
    #     digits.append(digs[x % base])
    #     x /= base
    #
    # if sign < 0:
    #     digits.append('-')
    #
    # digits.reverse()
    #
    # return ''.join(digits)


def convert(str_num, base1, base2):
    """
    Convert given number from base1 to base2.
    """
    assert 2 <= base1 <= 36
    assert 2 <= base2 <= 36
    # TODO: Convert number


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        str_num = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        result = convert(str_num, base1, base2)
        print('{} in base {} is {} in base {}'.format(str_num, base1, result, base2))
    else:
        print('Usage: {} number base1 base2'.format(sys.argv[0]))


if __name__ == '__main__':
    main()
