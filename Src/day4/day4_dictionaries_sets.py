print("Task 1: The Personal Contact Book ")
contacts = {
    "Alice": "9876543210",
    "Bob": "9123456780",
    "Charlie": "9988776655"
}

contacts["Diana"] = "9012345678"
contacts["Bob"] = "9000000000"

print("Safe Lookup Results:")
print("Alice:", contacts.get("Alice", "Contact not found"))
print("Eve:", contacts.get("Eve", "Contact not found"))

print("\nContact List:")
for name, phone in contacts.items():
    print("Contact:", name, "| Phone:", phone)

print("\n\nTask 2: The Duplicate Cleaner (Sets)")
raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]

unique_users = set(raw_logs)

print("Unique Users:", unique_users)

print("Is ID05 present?", "ID05" in unique_users)

print("Original log count:", len(raw_logs))
print("Unique user count:", len(unique_users))

print("\n\nTask 3: The Interest Matcher")

friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}

shared_interests = friend_a & friend_b
all_interests = friend_a | friend_b
unique_to_a = friend_a - friend_b

print("Shared interests:", shared_interests)
print("All interests:", all_interests)
print("Unique to Friend A:", unique_to_a)

