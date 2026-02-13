import matplotlib.pyplot as plt

scores = [50, 55, 65, 70, 75, 85, 90, 95]

low = len([s for s in scores if s < 60])
medium = len([s for s in scores if 60 <= s <= 80])
high = len([s for s in scores if s > 80])

labels = ["Needs Improvement", "Average", "Excellent"]
values = [low, medium, high]

plt.figure(figsize=(6, 6))
plt.pie(values, labels=labels, autopct="%1.1f%%")

plt.title("Student Performance Distribution", fontweight='bold')

plt.show()
