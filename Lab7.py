##Create a dictionary whose keys are month names and whose values are the number of days
##in the corresponding months.
# Ask the user to enter a month name and use the dictionary to tell them how many
#days are in the month.
# Print out all keys in the alphabetically order

m = {
    'January': 31,
    'February': 28,
    'March': 31,
    'April': 30,
    'May': 31,
    'June': 30,
    'July': 31,
    'August': 31,
    'September': 30,
    'October': 31,
    'November': 30,
    'December': 31
}

u = input("Enter month name: ")

if u in m:
    print(f"{u} has {m[u]} days")  # Access the value using u as the key, not m[0]
else:
    print("Invalid month name")

print("\nKeys in alphabetical order:")
for month in sorted(m.keys()):
    print(month)

print("\nMonths with 31 days:")
for month, days in m.items():
    if days == 31:
        print(month)

print("\nKey-value pairs sorted by the number of days:")
for month, days in sorted(m.items(), key=lambda x: x[1]):
    print(f"{month}: {days} days")
    