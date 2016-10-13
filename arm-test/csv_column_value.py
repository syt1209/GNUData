# changing csv file column value
# read the original csv file
import csv

# file handler
fOpen = raw_input('Enter csv file that needs value change: ')
fOutput = raw_input('Enter the name of new csv file: ')


reader = csv.reader(open(fOpen))
lines = [l for l in reader]

# Give options of changing column options
col_option = int(raw_input('Enter 1, if you wish to change the whole column;\n Enter 2, if you want to modify specific value.\n'))

# modifying column value
if col_option == 1:
    # chaging value of the whole column
    # Ask user to enter the total number of rows
    n_rows = int(raw_input('Enter total number of rows in the csv file you want to modify: '))
    # input updated value
    n_col = int(raw_input('Enter the column number you want to update: '))
    col_update = raw_input('Enter updated value for the column: ')
    for i in range(n_rows):
        lines[i+1][n_col] = col_update
elif col_option == 2:
    # changing a specific value
    # user input row number
    # user input column number
    update = True
    while update:
        n_row = int(raw_input('Enter the row number: ')) # enter the timestamp value
        n_col = int(raw_input('Enter the column number: ')) # enter the column attribute index number
        value_update = int(raw_input('Enter the new value: '))
        lines[n_row+1][n_col] = value_update
        choice = raw_input('Do you want to update another number (y/n): ')
        if choice == 'y':
            update = True
        elif choice == 'n':
            update = False
else:
    print 'input error!!'
# write the new info to a file
writer = csv.writer(open(fOutput, 'w'))
writer.writerows(lines)
