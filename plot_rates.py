import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Read the treasury rates data
data = pd.read_csv(r'data/daily-treasury-rates.csv')

# Convert the 'Date' column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Set 'Date' as the index
data.set_index('Date', inplace=True)

# Plot the daily treasury rates
data.plot(figsize=(12, 8))
plt.title('Daily Treasury Rates')
plt.xlabel('Date')
plt.ylabel('Rate (%)')
plt.show()# Purpose:
