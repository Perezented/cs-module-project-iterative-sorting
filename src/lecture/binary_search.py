# returns either the index of the target in hte arr
# or if the target is not in hte arr, return -1

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:

        # 1. compart the target element to the midpoint
        mid = (high + low) // 2
    # how do we find the midpoint, what do we need to know?
    # the length of the array would help us determine the midpoint
    # the 'range': if we have the left most index and the right most index
    # then the midpoint element is the right index - left index // 2
    # 2. determine which half to go in: toss out the other half
        if target == arr[mid]:
            return mid
    # reassign either the left or right index to point to the element past the midpoint
    # 3. if the midpoint element matches our taget, then we have found what we are looking for,
        if target < arr[mid]:
            high = mid - 1
        if target > arr[mid]:
            # cut the left half out, reassign low to mid + 1
            low = mid + 1
    # return the midpoint index
    # 4. Repeat this prcess: we need to loop this
    # What is our looping criteria that tells us it has to stop looping?
    # if we see that low and high are referring to the same index and the element at that index != target, then we can conclude that the element is not in the array, return -1
    return - 1


testArr = [3, 4, 5, 16, 26, 28, 52, 55]
unsorted = [6, 5, 2, 3, 4, 1, 8, 7]
print(binary_search(testArr, 4))
#####################################################

# Find smallest element and move it to the front AKA selection sort
# find smallest item, and swap with index 0.
# find second smallest and swap it with index 1
# Repeat
# if no items left to swap (use slices in indexes)


def selection_sort(arr):
    # iterate thru the array(represents the sorted - unsorted boundary moving across the array)
    for i in range(len(arr)):
        # index of the boundary, as well as the index we are going to swap the smallest element with
        boundary = i
        smallest_value = arr[boundary]
        smallest_index = boundary
        # find the smallest element in the unsorted portion of the array
        for unsorted_index in range(boundary, len(arr)):
            if arr[unsorted_index] < smallest_value:
                smallest_value = arr[unsorted_index]
                smallest_index = unsorted_index
            # smallest is the smallest element in the unsorted portion
        # temp = arr[boundary]
        # arr[boundary] = arr[smallest_index]
        # arr[smallest_index] = temp
        arr[boundary], arr[smallest_index] = arr[smallest_index], arr[boundary]
    return arr

    # once the smallest is found, swap it with the element on the right edge of the sorted-unsorted boundary
print(selection_sort(unsorted))
