import matplotlib.pyplot as plt

# Data
months = ["Jan", "Feb", "Mar", "Apr", "May"]
revenue = [2000, 4500, 4000, 7500, 9000]

# Calculate growth %
growth = [0]
for i in range(1, len(revenue)):
    percent = ((revenue[i] - revenue[i-1]) / revenue[i-1]) * 100
    growth.append(round(percent, 1))

# Create Dashboard
plt.figure(figsize=(14, 8))
plt.style.use("ggplot")

#  Line Plot 
plt.subplot(2, 2, 1)
plt.plot(months, revenue, marker='o', linewidth=3)
plt.title(" Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue (USD)")

#  Bar Chart 
plt.subplot(2, 2, 2)
plt.bar(months, revenue)
plt.title(" Monthly Revenue Comparison")

#  Scatter Plot
plt.subplot(2, 2, 3)
plt.scatter(months, revenue, s=200)
plt.title("Revenue Distribution")

#  Growth % Plot 
plt.subplot(2, 2, 4)
plt.plot(months, growth, marker='o', linestyle='--')
plt.title("Monthly Growth %")
plt.ylabel("Growth Percentage")

plt.suptitle("Startup Growth Intelligence Dashboard", fontsize=18, fontweight='bold')
plt.tight_layout()
plt.savefig("dashboard_output.png")
plt.show()
