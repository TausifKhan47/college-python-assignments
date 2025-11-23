import pandas as pd
import numpy as np

# Sample DataFrame
data = {
    'Scores': [85, 90, np.nan, 75, np.nan, 95]
}

df = pd.DataFrame(data)

# Fill missing values with the mean of the column
df['Scores'] = df['Scores'].fillna(df['Scores'].mean())

print(df)
