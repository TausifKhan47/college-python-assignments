import matplotlib.pyplot as plt

x1 = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]

x2 = [1, 2, 3, 4, 5]
y2 = [1, 4, 9, 16, 25]

plt.plot(x1, y1, label="y = 2x")     
plt.plot(x2, y2, label="y = x²")    

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Multiple Line Plot")

plt.legend()

plt.show()
