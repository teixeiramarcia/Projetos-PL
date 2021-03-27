import re

file = open('train_test.txt', 'r')

num_elems = 0
sentence = ""
in_category = 0
line = 1

for linha in file:
    y = re.match(r'(B|I)-([a-zA-Z_]+)\t+([a-zA-Z0-9]+)|(O).+', linha)
    if y:
        if (y.group(1) == 'B'):
            if (in_category == 1):
                print(sentence)
                print("Elements: " + str(num_elems))
                num_elems = 0
                sentence = ""
            in_category = 1
            num_elems += 1
            sentence = y.group(2) + ': ' + y.group(3) + ' '
        elif (y.group(1) == 'I'):
            num_elems += 1
            sentence += y.group(3)
            sentence += ' '
        elif (y.group(4) == 'O'):
            if (in_category == 1):
                print(sentence)
                print("Elements: " + str(num_elems))
                num_elems = 0
                sentence = ""
                in_category = 0
    else:
        print(sentence)
        print("Elements: " + str(num_elems))
        num_elems = 0
        sentence = ""
        in_category = 0
        print('')