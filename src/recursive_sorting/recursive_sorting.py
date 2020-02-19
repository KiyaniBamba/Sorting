# TO-DO: complete the helpe function below to merge 2 sorted arrays

def merge( arrA, arrB ):
    # elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    # TO-DO
    if max(arrA) < max(arrB):
      return  arrA + arrB
    else:
      return  arrB + arrA  

print("Merge function:",merge([1, 2, 3], [5, 6, 7, 8]))

import numpy as np

x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
print(np.concatenate([x, y, z]))

def merge_sort( arr ):
    # retList = []
    # TO-DO
    # Base case: arr is empty
    if arr == []:
      return 0
    # first = arr[0]
    # second = merge_sort(arr[1:])
    return arr[0] + merge_sort(arr[1:])
    # return arr[0].extend(second) 


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
