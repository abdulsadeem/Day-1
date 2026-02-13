import matplotlib.pyplot as plt
study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
scores = [50, 55, 65, 70, 75, 85, 90, 95]
plt.figure(figsize=(8, 5))
plt.scatter(study_hours, scores, s=100)
plt.title("Study Hours vs Exam Scores", fontweight='bold')
plt.xlabel("Hours Spent Studying")
plt.ylabel("Exam Score")
plt.grid(True)
plt.show()
