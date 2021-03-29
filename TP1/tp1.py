import re

file = open('train.txt', 'r')

num_elems = 0
cat = ""
category = ""
sentence = ""
in_category = 0
line = 1

my_categories = dict(set())

#### Helper functions ####
def update_categories(category):
    if(category not in my_categories.keys()):
        vals = set()
        my_categories[category] = vals

def update_in_category(category, value):
    if (category in my_categories.keys()):
        my_categories.get(category).add(value)

def showCategory(category):
    cat = my_categories.get(category)
    return cat

def createOutput():
    file = open('output.html', 'w')

    file.write("<!DOCTYPE html>\n")
    file.write("<html>\n")
    file.write("    <head>\n")
    file.write("        <meta charset='UTF-8'/>\n")
    file.write("        <title>Categorias</title>\n")
    file.write("    </head>\n")
    file.write("    <body style='background-color: #e6e6ff;'>\n")
    file.write("        <h2 style='color: #633b97'>Machine Learning: Datasets de treino</h2>\n")
    file.write("        <h3 style='color: #633b97'>Categorias:</h3>\n")
    file.write("        <ul>")
    for (cat,val) in my_categories.items():
        file.write(f"           <li><strong><a href='{cat}.html' style='color: #535353'>" + cat + "</a>" + ": </strong>" + str(len(val)) + " elementos" +"<p></li>\n")
    file.write("        </ul>")
    file.write("        <button><a href='extra.html'>Extras</a></button>")
    file.write("    </body>\n")
    file.write("</html>")
    file.close()

def createFiles():
    for (cat,val) in my_categories.items():
        file = open(cat + '.html', 'w')

        file.write("<!DOCTYPE html>\n")
        file.write("<html>\n")
        file.write("    <head>\n")
        file.write("        <meta charset='UTF-8'/>\n")
        file.write("        <title>" + cat + "</title>\n")
        file.write("    </head>\n")
        file.write("    <body style='background-color: #e6e6ff;'>\n")
        file.write("        <h2 style='color: #633b97'>Categoria: " + cat + "</h2>\n")
        file.write("        <button><a href='output.html'>Home</a></button>")
        file.write("        <p>&nbsp;</p>\n")
        
        for v in val:
            file.write("        <p>" + v + "<p>\n")
            file.write("        <p>&nbsp;</p>\n")
        file.write("    </body>\n")
        file.write("</html>")
        file.close()


dest_file = open('extra.html', 'w')

dest_file.write("<!DOCTYPE html>\n")
dest_file.write("<html>\n")
dest_file.write("   <head>\n")
dest_file.write("       <meta charset='UTF-8'/>\n")
dest_file.write("       <title>TP1</title>\n")
dest_file.write("   </head>\n")
dest_file.write("   <body style='background-color: #e6e6ff;'>\n")
dest_file.write("       <h2 style='color: #633b97'>Extras</h2>\n")

for linha in file:
    y = re.match(r'(B|I)-([a-zA-Z_]+)(\t| )+([a-zA-Z0-9]+)|(O).+', linha)
    if y:
        if (y.group(1) == 'B'):
            if (in_category == 1):
                if (num_elems != 0):
                    dest_file.write("       " + "<p>" + cat + sentence + "  (elements: " + str(num_elems) + ")</p>\n")
                    update_in_category(category, sentence)
                    num_elems = 0
                    category = ""
                    cat = ""
                    sentence = ""
            in_category = 1
            num_elems += 1
            category = y.group(2)
            cat = f"<strong><a href='{category}.html' style='color: #535353'>" + category + "</a>" + ": </strong>"
            update_categories(category)
            sentence = y.group(4) + ' '
            
        elif (y.group(1) == 'I'):
            num_elems += 1
            sentence += y.group(4) + ' '
        elif (y.group(5) == 'O'):
            if (in_category == 1):
                if(num_elems != 0):
                    dest_file.write("       " + "<p>" + cat + sentence + "  (elements: " + str(num_elems) + ")</p>\n")
                    update_in_category(category, sentence)
                    num_elems = 0
                    category = ""
                    cat = ""
                    sentence = ""
                    in_category = 0
    else:
        if (num_elems != 0):
            dest_file.write("       " + "<p>" + cat + sentence + "  (elements: " + str(num_elems) + ")</p>\n")
            update_in_category(category, sentence)
            num_elems = 0
            category = ""
            cat = ""
            sentence = ""
            in_category = 0
            dest_file.write("       <p>&nbsp;</p>\n")
dest_file.write("   </body>\n")
dest_file.write("</html>")
dest_file.close()

createOutput()
createFiles()