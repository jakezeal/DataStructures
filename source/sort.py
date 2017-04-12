#!python


def bubble_sort(alist):
    # Time complexity
    # Worst Case: O(n^2) - Quadratic
    # Best Case: Omega(n) - Linear
    # Space complexity
    # Theta(1) - Constant
    is_sorted = False
    while is_sorted is False:
        is_sorted = True
        for i in range(1, len(alist)):
            if alist[i-1] > alist[i]:
                is_sorted = False
                alist[i-1], alist[i] = alist[i], alist[i-1]
    return alist


def selection_sort(alist):
    # Brings smallest element to the left
    # Time complexity
    # Worst Case: O(n^2) -> O(n^2 / 2)
    # Best Case: Omega(n^2) -> O(n^2 / 2)
    # Space complexity
    # Theta(1) - Constant
    # ------------------
    #variable for minimum index element
    # swap


def insertion_sort(alist):
    # Time complexity
    # Worst Case: O(n^2) -> O(n^2 / 2)
    # Best Case: Omega(n)
    # Space complexity
    # Theta(1) - Constant
    # ------------------


def tree_sort(alist):
    # Time complexity
    # Worst Case: O(n^2) if it is an unbalanced tree
    # Best Case: Omega(nlog^n)
    # Space complexity
    # Theta(n) - Constant
    # ------------------
    # Make binary search tree
    # Return items in order
    # b = BinarySearchTree(alist)
    # return b

if __name__ == '__main__':
    alist = [6, 1, 4, 2, 3, 8, 0]
    print(alist)
    new_list = bubble_sort(alist)
    print(new_list)
