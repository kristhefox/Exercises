#ex2_1.py

def bubble_sort(x):
    """ this function implements Bubble Sort Algorithm """
    arraylenght = len(x)
    for i in range(arraylenght-1):
        for j in range(0,arraylenght-i-1):
            if x[j] > x[j+1]:
            # swap these elements
                x[j], x[j+1] = x[j+1], x[j]
    return x

def merge_sort(x):
    """ this function implements Merge Sort Algorithm """
    arraylenght = len(x)
    if arraylenght > 1:
        middle = arraylenght//2
        left = x[:middle]
        right = x[middle:]
        # implementation of algorithm
        merge(left)
        merge(right)
        i = j = k = 0
        #copy elements to arrays left and right
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                x[k] = left[i]
                i += 1
            else:
                x[k] = right[j]
                j += 1
            k += 1
        #check for any left elemets
        while i < len(left):
            x[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            x[k] = right[j]
            j += 1
            k += 1
    return x

def quick_sort(x):
    """ this function implemetns Quick Sort Algorithm """
    arraylenght = len(x)
    less = []
    equal = []
    greater = []
    if arraylenght < 2:
        return x
    else:
        # first element
        pivot = x[0]
        less = [i for i in x[1:] if i <= pivot] 
        more = [i for i in x[1:] if i > pivot]
        return qsort(less) + [pivot] +qsort(more)