# ex1_1

def minmax(numbers = []):
    """ this function returns minimum and maximum value from the list """
    if numbers == []:
        return None
    else:
        min = max = numbers[0]
        for i in numbers[1:]:
            if i < min: 
                min = i 
            elif i > max: 
                max = i
        return min,max