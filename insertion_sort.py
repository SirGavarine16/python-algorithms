def insertionSort(array):
    for i in range(1, len(array)):
        element = array[i]
        comparisonIndex = i - 1
        while comparisonIndex >= 0 and element < array[comparisonIndex]:
            array[comparisonIndex + 1] = array[comparisonIndex]
            comparisonIndex -= 1
        array[comparisonIndex + 1] = element