def quicksort(array):
    '''Given an array, its sorted in an ASC fashion using recursion.'''
    if (len(array) < 2):
        return array
    
    pivot = array[0]
    elementsLowerThanPivot = [i for i in array[1:] if i <= pivot]
    elementsHigherThanPivot = [i for i in array[1:] if i >= pivot]

    return quicksort(elementsLowerThanPivot) + [pivot] + quicksort(elementsHigherThanPivot)