# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    for i in range(elements):

        if not len(arrA):
            merged_arr[i] = arrB[0]
            arrB.pop(0)
        elif not len(arrB):
            merged_arr[i] = arrA[0]
            arrA.pop(0)
        elif arrA[0] > arrB[0]:
            merged_arr[i] = arrB[0]
            arrB.pop(0)
        else:
            merged_arr[i] = arrA[0]
            arrA.pop(0)

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) > 1:
        # divide array
        middle = len(arr) // 2
        # use recursion on LHS
        lhs = merge_sort(arr[:middle])
        # use recursion on RHS
        rhs = merge_sort(arr[middle:])
        # merge and sort pieces
        arr = merge(lhs, rhs)

    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here


    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
