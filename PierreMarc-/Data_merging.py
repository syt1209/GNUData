import time, glob
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline ## for printing inside ipython console

# name for merged output file name
outfilename = 'PM_merged' + ".csv"

filenames = glob.glob('/Users/shu/Downloads/PierreMarc/Data/*.csv')

## remove header and merge all csv files in the folder into one csv file with pure numbers
with open(outfilename, 'wb') as outfile:
    for fname in filenames:
    #print type(fname)
    #print fname
        df = pd.read_csv(fname)
        df.to_csv(fname, header=False, index=False)

        with open(fname, 'r') as readfile:
            infile = readfile.read()
            for line in infile:
                outfile.write(line)
