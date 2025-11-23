import pandas as pd

# Example DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [30, 25, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Display data types of each column
print("Column Data Types:")
print(df.dtypes)
