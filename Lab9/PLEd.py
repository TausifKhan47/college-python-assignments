import pandas as pd

s1 = pd.Series([10, 20, 30, 40])
s2 = pd.Series([50, 60, 70, 80])

print("Series 1:")
print(s1)
print("\nSeries 2:")
print(s2)

vertical_stack = pd.concat([s1, s2], axis=0)
print("\nStacked Vertically:")
print(vertical_stack)

horizontal_stack = pd.concat([s1, s2], axis=1)
print("\nStacked Horizontally:")
print(horizontal_stack)
