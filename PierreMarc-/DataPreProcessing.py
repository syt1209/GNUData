# loop through folder and output processed data file
# average of hydration reading and add hydration status to corresponding column
import pandas as pd
import glob
import numpy as np
import matplotlib.pyplot as plt

#outfilename = 'Averaged' + '.csv'
#add average value to one list
AVG_list = list()
STD_list = list()


folder = glob.glob("Data/*.csv")

#with open(outfilename, 'wb') as outfile:
for fname in folder:
    df = pd.read_csv(fname)
    ls = df['RSSI'].tolist()
    avg = np.mean(ls)
    std = np.std(ls)
    AVG_list.append(avg)
    STD_list.append(std)


print AVG_list
print STD_list

y = AVG_list
y_error = STD_list
#x = ['7.00','7.50','9.33','10.25','11.25','13.25','14.75']
#print y, y_error
print len(y), len(y_error)
#plt.errorbar(y, fmt = 'o')
plt.plot(y, 'o')
plt.axis([0,20,15000,25000])
#plt.xlabel('Time of the Day (hours)')
plt.ylabel('Average RSSi')
plt.show()
