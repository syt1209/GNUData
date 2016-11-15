## add header to the pure data file
import pandas as pd
import matplotlib.pyplot as plt

df_al = pd.read_csv('PM_merged.csv')
df_al.columns = ['Timestamp','Count','Configuration Version','Status Version','Calibration Action']
df_al.to_csv('PM_ready.csv', index = False)

df_ready = pd.read_csv('PM_ready.csv')
plt.scatter(df_ready['Timestamp'], df_ready['Count'])
