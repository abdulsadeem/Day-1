
p_heads = 1 / 2
p_six = 1 / 6

p_independent = p_heads * p_six

print("Independent Case:")
print("Probability of Heads AND rolling 6:", p_independent)

red = 5
blue = 5
total = red + blue

p_first_red = red / total
p_second_red = (red - 1) / (total - 1)

p_dependent = p_first_red * p_second_red

print("\nDependent Case:")
print("Probability of two Red marbles:", p_dependent)

print("\nReflection:")
print("The denominator changed because one marble was removed after the first draw.")
print("The total number of marbles decreased from 10 to 9.")
print("So, the second probability depends on the first draw.")
