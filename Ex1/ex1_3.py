# ex1_3

def exchange(a,b):
    """ this function swaps word 'a' to word 'b' in text file """
    filepath = input('Enter file path: ')
    with open(filepath, 'r') as file:
        content = file.read().replace(a, b)
    
    with open(filepath, 'w')as file:
        file.write(content)
