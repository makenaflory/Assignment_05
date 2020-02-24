#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# MMezistrano, 2020-Feb-23, Added code
#------------------------------------------#

# Declare variables

strChoice = '' # User input
dicRow = {}  # inner lists of dicts
lstTbl = []  # list of dicts to hold data
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object
dicRow1 = {'ID': 1, 'CD title': 'Happy', 'Artist name': 'Celine Dion'}
dicRow2 = {'ID': 2, 'CD title': 'Yellow', 'Artist name': 'Coldplay'}
lstTbl.append(dicRow1)
lstTbl.append(dicRow2)

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    
    if strChoice == 'l':
        # Adds the functionality of loading existing data
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',') 
            dicRow = {'ID': lstRow[0], 'CD title': lstRow[1], 'Artist name': lstRow[2]} 
            print(dicRow) 
        objFile.close()
        
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow = {'ID': intID, 'CD title': strTitle, 'Artist name': strArtist} 
        lstTbl.append(dicRow) 
        
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist') 
        for row in lstTbl:
            print(*row.values(), sep = ', ') # Changed this to row.values() for readibility 
    
    elif strChoice == 'd':
        # Adds functionality of deleting an entry
        print('This is your current inventory:')
        for row in lstTbl:
            print(*row.values(), sep = ', ')
        deleteID = int(input('Enter the ID of the CD you want to delete: '))
        for row in lstTbl:
            if deleteID in row.values():
                del lstTbl[lstTbl.index(row)]
        print('\n This is your new inventory:')
        for row in lstTbl:
            print(*row.values(), sep = ', ')
            
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'w') # changed from a to w so that it would only add the new line
        for row in lstTbl:
            strRow = ''
            for item in row.values(): # only row.values() needed changing from list code
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')

