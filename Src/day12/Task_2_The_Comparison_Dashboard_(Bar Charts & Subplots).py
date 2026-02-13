import matplotlib.pyplot as plt

# Data for Bar Chart
categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]

# Data for Line Plot (Monthly Trend Example)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
monthly_sales = [500, 650, 700, 850, 900]

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.bar(categories, sales)
plt.title("Sales by Product Category", fontweight='bold')
plt.xlabel("Category")
plt.ylabel("Sales Units")

plt.subplot(1, 2, 2)
plt.plot(months, monthly_sales, marker='o')
plt.title("Monthly Sales Trend", fontweight='bold')
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.show()
