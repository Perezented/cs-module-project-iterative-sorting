testingArray = [3, 2, 1, 6, 4, 5]
print('TestingArray')
print(testingArray)
print('#############')


def linear_search(arr, target):
    # Your code here
    found = False
    while not found:
        found = True
        for i in range(len(arr)-1):
            # print(i)
            if arr[i] != target:
                found = False
            elif arr[i] == target:
                found = True
                return i
        return - 1


print(linear_search(testingArray, 9))
# Write an iterative implementation of Binary Search


def binary_search(arr, target):

    # Your code here
    # setup of left and right most items in the array
    left = 0
    right = len(arr) - 1
    # while the left item is less than or equal to the right item:
    while left <= right:
        # setup a middle item
        mid = (left + right) // 2
        # if our target matches the middle item, return the middle item
        if target == arr[mid]:
            return mid
        # else if the target is less than the mid item, setup right again
        if target < arr[mid]:
            right = mid - 1
        # else if the target is more than the mid item, setup left again
        if target > arr[mid]:
            left = mid + 1

    return -1  # not found
