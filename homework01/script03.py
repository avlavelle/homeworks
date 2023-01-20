#Anna Victoria Lavelle
#AVL578
#1/20/2023
#script03.py

import names 

def name_length(name):
    return (len(name) - 1)

for i in range(5):
    currentName = names.get_full_name()
    print(currentName + ' ' + str(name_length(currentName)))
