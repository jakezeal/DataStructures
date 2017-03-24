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
    # Could also take length of string - decrementer
    # Have reversed_str be a list for str in reversed_str

    # Reverse str_num to make it easier to loop through
    reversed_str = str_num[::-1]
    # Stores the result value
    result = 0
    # Number to add if it is alphaneumeric
    num_to_add = 0
    # Iterate getting index in reversed_str
    for i in range(0, len(reversed_str)):
        # If string at index is not 0
        if reversed_str[i] != '0':

            if reversed_str[i].isalpha():
                # TODO: DOESN'T WORK for caps vs not - only lowercase
                num_to_add = ord(reversed_str[i]) - 87
                print(num_to_add, reversed_str[i])
                result += base**i * num_to_add + num_to_add

            else:
                result += base**i * int(reversed_str[i]) + num_to_add
    return result


def encode(num, base):
    """
    Encode given number from base 10 to given base.
    num -- the number in base 10
    base -- base to convert to
    """
    assert 2 <= base <= 36
    # TODO: Encode number


def convert(str_num, base1, base2):
    """
    Convert given number from base1 to base2.
    """
    assert 2 <= base1 <= 36
    assert 2 <= base2 <= 36
    # TODO: Convert number
    # base_ten = decode(str_num, base1)
    # converted_base = encode(base1, base2)
    # return converted_base

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

    
