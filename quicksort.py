from random import randrange

def quicksort(array):
    '''Given an array, its sorted in an ASC fashion using recursion.'''
    if (len(array) < 2):
        return array
    
    randomIndex = randrange(len(array))
    pivot = array[randomIndex]

    arrayWithoutPivot = array[:randomIndex] + array[randomIndex+1:]
    elementsLowerThanPivot = [i for i in arrayWithoutPivot if i <= pivot]
    elementsHigherThanPivot = [i for i in arrayWithoutPivot if i >= pivot]

    return quicksort(elementsLowerThanPivot) + [pivot] + quicksort(elementsHigherThanPivot)