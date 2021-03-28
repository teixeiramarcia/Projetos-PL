import re

file = open('train_test.txt', 'r')


num_elems = 0
category = ""
sentence = ""
in_category = 0
line = 1

my_category = {}
my_categories = dict(set(my_category))

dest_file = open('output.html', 'w')

dest_file.write("<!DOCTYPE html>\n")
dest_file.write("<html>\n")
dest_file.write(" <head>\n")
dest_file.write("     <meta charset='UTF-8'/>\n")
dest_file.write("     <title>TP1</title>\n")
dest_file.write(" </head>\n")
dest_file.write("     <body style='background-color: #e6e6ff;'>\n")
dest_file.write("        <h2 style='color: #633b97'>Machine Learning: Datasets de treino</h2>\n")

for linha in file:
    y = re.match(r'(B|I)-([a-zA-Z_]+)\t+([a-zA-Z0-9]+)|(O).+', linha)
    if y:
        if (y.group(1) == 'B'):
            if (in_category == 1):
                dest_file.write("        " + "<p>" + category + sentence + "  (elements: " + str(num_elems) + ")</p>")
                num_elems = 0
                category = ""
                sentence = ""
            in_category = 1
            num_elems += 1
            category = "<strong><a href='https://www.google.com/' style='color: #535353'>" + y.group(2) + "</a>" + ": </strong>"
            sentence = y.group(3) + ' '
            
        elif (y.group(1) == 'I'):
            num_elems += 1
            sentence += y.group(3) + ' '
        elif (y.group(4) == 'O'):
            if (in_category == 1):
                dest_file.write("        " + "<p>" + category + sentence + "  (elements: " + str(num_elems) + ")</p>")
                num_elems = 0
                category = ""
                sentence = ""
                in_category = 0
    else:
        dest_file.write("        " + "<p>" + category + sentence + "  (elements: " + str(num_elems) + ")</p>")
        num_elems = 0
        category = ""
        sentence = ""
        in_category = 0
        dest_file.write("<p>&nbsp;</p>")
dest_file.write("     </body>\n")
dest_file.write(" </html>")
dest_file.close()