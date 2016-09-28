# use csv module to read csv data file
import csv
with open('C:\Users\syt.shu\Documents\GitHub\GNUData\arm-test\HS_R_1_0001_0_60.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print row
