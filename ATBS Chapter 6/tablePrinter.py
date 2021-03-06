tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(inputList):
    # The table, 'colWidths' is created, whose amount of
    # zero values corresponds to the number of lists in the table [0,0,0]
    colWidths = [0] * len(inputList)

    # The for loops iterate through each value in the sub-lists, and the
    # if statement iterates through each value that is larger than the current
    # one, and continues until it has found the largest one
    for i in range(len(inputList)):
        for j in range(len(inputList[i])):
            if len(inputList[i][j]) > colWidths[i]:
                colWidths[i] = len(inputList[i][j])
                

    for x in range(len(inputList[0])):
        for y in range(len(inputList)):
            print(inputList[y][x].rjust(colWidths[y]), end = ' ')
        print('')

printTable(tableData)




        
def printTable(inputList):
    # initialize the list "colWidths" with zeroes equal to the length of the input list
    colWidths = [0] * len(inputList)

    # iterate over the input list to find the longest word in each inner list
    # if its larger than the current value, set it as the new value
    for i in range(len(inputList)):
        for j in range(len(inputList[i])):
            if len(inputList[i][j]) > colWidths[i]:
                colWidths[i] = len(inputList[i][j])

    # assuming each inner list is the same length as the first, iterate over the input list
    # printing the x value from each inner list, right justifed to its corresponding value
    # in colWidths
    for x in range(len(inputList[0])):
        for y in range(len(inputList)):
            print(inputList[y][x].rjust(colWidths[y]), end = ' ')
        print('')

             



def printTable(inputList):
    colWidths = [0] * len(inputList)
    
    for i in range(len(inputList)):
        for j in range(len(inputList[i])):
            if len(inputList[i][j]) > colWidths[i]:
                colWidths[i] = len(inputList[i][j])

    for x in range(len(inputList[0])):
        for y in range(len(inputList)):
            print(inputList[y][x].rjust(colWidths[y]), end = ' ')
        print('')

