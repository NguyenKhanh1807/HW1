import matplotlib.pyplot as plt
import pandas as pd

# Sample data
data = {
    'Month': pd.date_range(start='1/1/2022', periods=24, freq='M'),
    'Sales': [5000, 5200, 5100, 5300, 5400, 5600, 5500, 5700, 5900, 6100, 6000, 6200, 
              6300, 6500, 6400, 6600, 6700, 6900, 6800, 7000, 7200, 7400, 7300, 7500]
}

df = pd.DataFrame(data)

# Adding forecasted data
forecast_data = {
    'Month': pd.date_range(start='1/1/2024', periods=1, freq='M'),
    'Sales': [None],
    'MA Forecast': [7400],
    'ES Forecast': [7350],
    'LR Forecast': [7700]
}
forecast_df = pd.DataFrame(forecast_data)
df = pd.concat([df, forecast_df], ignore_index=True)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(df['Month'], df['Sales'], label='Actual Sales')
plt.plot(df['Month'][23:], df['MA Forecast'][23:], label='MA Forecast (3-Month)')
plt.plot(df['Month'][23:], df['ES Forecast'][23:], label='Exponential Smoothing')
plt.plot(df['Month'][23:], df['LR Forecast'][23:], label='Linear Regression')
plt.xlabel('Month')
plt.ylabel('Sales Volume')
plt.title('Phone Case Sales Forecast')
plt.legend()
plt.grid(True)
plt.show()
