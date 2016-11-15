import numpy as np
import scipy.signal
import pandas as pd
import matplotlib.pyplot as plt


# Path to data file
datapath = 'PM_ready.csv'

# Load the data
df = pd.read_csv(datapath)

# Convert timestamps to a nicer format
df['Timestamp'] = df['Timestamp'].astype(int)
df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='ms')
df['TimeDeltaMs'] = ((df['Timestamp'] - df['Timestamp'][0]) / np.timedelta64(1,'ms')).astype(int)

# Apply a median filter to the Count data (takes median of kernel_size consecutive samples)
df['CountFiltered'] = scipy.signal.medfilt(df['Count'], kernel_size = 5)

# Plot the results
filteredRange = np.max(df['CountFiltered']) - np.min(df['CountFiltered'])
raw_line = plt.plot(df['TimeDeltaMs'], df['Count'], 'b-', linewidth=2.0)
plt.hold(True)
#filtered_line = plt.plot(df['TimeDeltaMs'], df['CountFiltered'], 'r-', linewidth=2.0)
plt.grid(True)
plt.axis([0, np.max(df['TimeDeltaMs']), np.min(df['CountFiltered'])-filteredRange,
	np.max(df['CountFiltered'])+filteredRange])
plt.xlabel('Time (ms from start of experiment)')
plt.ylabel('RSSi')
plt.legend(['Raw RSSi', 'Filtered RSSi'])
plt.show()
