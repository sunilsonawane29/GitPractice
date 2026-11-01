from collections import Counter

# Count items in a list
fruits = ["apple", "banana", "apple", "cherry", "banana", "apple"]
fruit_counts = Counter(fruits)
print(fruit_counts)
# Output: Counter({'apple': 3, 'banana': 2, 'cherry': 1})

# Count letters in a string
text_counts = Counter("mississippi")
print(text_counts)
# Output: Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
