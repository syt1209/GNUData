import numpy as np
import pandas as pd
df = pd.read_csv("/Users/shu/Documents/GNUData/PierreMarc-/Data/Data_0001.csv", header=None)
ls = df[1].tolist()

print type(ls)
##avg = np.mean(ls)
##std = np.std(ls)
##print avg, std
def mean_ls(list):
    count = 0
    summ = 0
    for number in list:
        count += 1
        summ += number
    mean_ls = float(summ)/float(count)
    return mean_ls
mean_ls(ls)
