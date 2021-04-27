# ex1_4
def total_words(a):
    """ this function counts every word in text and creates a basic histogram """
    letters = 0
    filepath = input('Enter file path: ')
    with open (filepath, 'r') as file:
        for line in file:
            line = line.replace(' ','')
            for word in line:
                word = word.lower()
                if word:
                    letters += 1
    number = line.count(a)
    percent = int(number / letters * 100)
    line1 = '{} ({}%)\t'.format(number, percent)
    line2 = '{} ({}%)\t'.format(letters,100-percent)
    for i in range(percent):
        line1 += '-'
    for i in range(100-percent):
        line2 += '-'
    print(line1)
    print(line2)