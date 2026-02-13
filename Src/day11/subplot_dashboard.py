import matplotlib.pyplot as plt

months = [1, 2, 3, 4, 5]
revenue = [2000, 4500, 4000, 7500, 9000]

plt.figure(figsize=(10,5))

# Line Plot
plt.subplot(1, 3, 1)
plt.plot(months, revenue, marker='o')
plt.title("Line Plot")

# Bar Plot
plt.subplot(1, 3, 2)
plt.bar(months, revenue)
plt.title("Bar Plot")

# Scatter Plot
plt.subplot(1, 3, 3)
plt.scatter(months, revenue)
plt.title("Scatter Plot")

plt.tight_layout()
plt.show()
