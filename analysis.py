import pandas as pd

# Load some sample data
data = pd.DataFrame({
    'Name': ['John', 'Jane', 'Bob', 'Alice'],
    'Age': [25, 32, 45, 28],
    'City': ['New York', 'London', 'Paris', 'Tokyo']
})

# Perform some basic data processing
print(data.head())
print(data.describe())
