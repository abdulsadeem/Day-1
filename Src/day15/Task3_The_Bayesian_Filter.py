p_spam = 0.1
p_ham = 0.9

p_free_given_spam = 0.9
p_free_given_ham = 0.05

p_free = (p_free_given_spam * p_spam) + (p_free_given_ham * p_ham)

p_spam_given_free = (p_free_given_spam * p_spam) / p_free

print("P(Free):", p_free)
print("P(Spam | Free):", p_spam_given_free)
