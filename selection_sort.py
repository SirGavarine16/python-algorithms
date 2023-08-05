def findSmallestElementIn(array):
    smallestIndex = 0
    for i in range(1, len(array)):
        if array[i] < array[smallestIndex]:
            smallestIndex = i
    return smallestIndex

def selectionSort(array):
    '''Given an array, its sorted in an ASC fashion.'''
    sortedArray = []
    for i in range(len(array)):
        smallestElement = findSmallestElementIn(array)
        sortedArray.append(array.pop(smallestElement))
    return sortedArray