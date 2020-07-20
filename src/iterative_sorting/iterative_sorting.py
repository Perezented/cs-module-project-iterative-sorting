testingArray = [3, 2, 1, 4, 9, 7, 6, 5]
print('TestingArray')
print(testingArray)
print('#############')

# TO-DO: Complete the selection_sort() function below


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(len(arr)):
        cur_index = i
        smaller_value = arr[cur_index]
        smallest_index = cur_index

        for rightSideIndex in range(cur_index, len(arr)):
            # to begin, find the smallest value.
            if arr[rightSideIndex] < smaller_value:
                smaller_value = arr[rightSideIndex]
                smallest_index = rightSideIndex
        # swap it with the left most value of the array, index 0.
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
        # so on until the end
    return arr


# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    # Your code here
    # bubble sort compares the values and switches values depending on how they stack up on a comparision test.
    # for i in range(len(arr)):
    #     index = i
    #     while i != len(arr) - 1:
    #         leftValue = arr[index]
    #         rightvalue = arr[index+1]
    #         if leftValue > rightvalue:
    #             arr[index], arr[index + 1] = arr[index + 1], arr[index]
    #         else:
    #             break
    checkingSort = False
    # for i in range(len(arr) - 1):
    #     index = i
    # print(f'arr item: {arr[i]}')
    # print(arr[len(arr) - 1])
    # if arr[len(arr) - 1] == arr[i]:
    #     print('This is the last line')
    # print(f'arr[i:][0]{arr[i:][0]}')

    while not checkingSort:
        checkingSort = True
        for i in range(len(arr) - 1):
            # want to start with the left item and compare with the item right to it.
            if arr[i] > arr[i+1]:
                # if the left item is greater than the right, then swap them
                checkingSort = False
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    # if the right is greater, then continue on with the next item
    return arr


# print(bubble_sort(testingArray))
'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''


def counting_sort(arr, maximum=None):
    # Your code here
    while maximum is not 0:
        print(f'max: {maximum}')
        for i in range(len(arr)):
            print(arr)
            if arr[i] == maximum:
                arr.pop(i)
                arr.insert(0, maximum)
        maximum -= 1
    return arr


print(counting_sort(testingArray, 9))
