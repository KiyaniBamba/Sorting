# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    # OPTION 1
    # smallest = arr[0]
    # smallest_index = 0
    # for i in range(1, len(arr) - 1):
    #     # TO-DO: find next smallest element
    #     # (hint, can do in 3 loc)
    #     if arr[i] < smallest:
    #         smallest = arr[i]
    #         smallest_index = i
    #     smallest_item = arr.pop(smallest_index)
    #     highest_item = arr.pop(i)
    #     # inserting in each others positions
    #     arr.insert(smallest_index, smallest_item)
    #     arr.insert(i, highest_item)
    #     return smallest_index
    # return arr
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr) - 1):
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    # TO-DO: swap
    smallest, arr[smallest_index ] = arr[smallest_index ], smallest
    return arr

arr_test = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print("selection sort function:", selection_sort(arr_test))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(lst):
    for i in range(len(lst)-1, 0, -1):
        for k in range(i):
            if lst[k] > lst[k + 1]:
                lst[k], lst[k + 1] = lst[k + 1], lst[k]
    return lst

print("bubble sort function:", bubble_sort(arr_test))

# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
