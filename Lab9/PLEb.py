import pandas as pd

data = {
    'a': 100,
    'b': 200,
    'c': 300,
    'd': 400,
    'e': 500
}

series = pd.Series(data)

print("Dictionary to Series:")
print(series)
