import random

actions = ["Click", "Scroll", "Exit"]

sample_space = [(a1, a2) for a1 in actions for a2 in actions]

event = [outcome for outcome in sample_space if "Click" in outcome]

probability_click = len(event) / len(sample_space)

print("Sample Space:", sample_space)
print("Total Outcomes:", len(sample_space))
print("Favorable Outcomes:", len(event))
print("Probability of at least one Click:", probability_click)


rolls = 1000
count_sum_7 = 0

for _ in range(rolls):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    if die1 + die2 == 7:
        count_sum_7 += 1

experimental_probability = count_sum_7 / rolls

print("Experimental Probability of Sum = 7:", experimental_probability)
