def sum(array):
    '''Sum of all the elements in an array using recursion.'''
    if (len(array) == 0):
        return 0
    return array[0] + sum(array[1:])

def count(array):
    '''Count of all the elements in an array using recursion.'''
    if (len(array) == 0):
        return 0
    return 1 + count(array[1:])

def max(array):
    '''Find the maximum element in an array using recursion.'''
    if (len(array) == 2):
        return array[0] if array[0] > array[1] else array[1]
    maxValue = max(array[1:])
    return array[0] if array[0] > maxValue else maxValue

