def printTable(tableData):
    colWidths = [0]*len(tableData[0])
    for row in tableData:
        for column in range(len(row)):
            if len(row[column])>colWidths[column]:
                colWidths[column]=len(row[column])
    for row in tableData:
        for column in range(len(row)):
            print(row[column].rjust(colWidths[column]), end = ' ')
        print()
        
def printTable2(tableData):
    colWidths = [0]*len(tableData)
    for column in range(len(tableData)):
        for row in range(len(tableData[column])):
            if len(tableData[column][row])>colWidths[column]:
                colWidths[column]=len(tableData[column][row])
    for row in range(len(tableData[0])):
        for column in range(len(tableData)):
            print(tableData[column][row].rjust(colWidths[column]), end = ' ')
        print()

tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

printTable2(tableData)