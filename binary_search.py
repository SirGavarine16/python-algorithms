from math import floor

def binarySearch(array, item):
    '''Binary Search takes a sorted array and returns the index of the item if found.'''
    lowestIndex = 0
    highestIndex = len(array) - 1 
    while lowestIndex <= highestIndex:
        middleIndex = floor((lowestIndex + highestIndex) / 2)
        guess = array[middleIndex]
        if guess == item:
            return middleIndex
        if guess > item:
            highestIndex = middleIndex - 1
        if guess < item:
            lowestIndex = middleIndex + 1 
    return None