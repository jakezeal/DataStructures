#!python


def bubble_sort(alist):
    # Time complexity
    # Worst Case: O(n^2) - Quadratic | Best Case: Omega(n) - Linear
    # Space complexity
    # Beta(1) - Constant
    is_sorted = False
    while is_sorted is False:
        is_sorted = True
        for i in range(1, len(alist)):
            if alist[i-1] > alist[i]:
                is_sorted = False
                alist[i-1], alist[i] = alist[i], alist[i-1]
    return alist




if __name__ == '__main__':
    alist = [6, 1, 4, 2, 3, 8, 0]
    print(alist)
    new_list = bubble_sort(alist)
    print(new_list)
