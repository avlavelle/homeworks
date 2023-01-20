#Anna Victoria Lavelle 
#AVL578
#1/20/2023
#script02.py

import names

numNames = 0

while numNames < 5:
    currentName = names.get_full_name()
    if (len(currentName) == 9):
        print(currentName)
        numNames += 1

