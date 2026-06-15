"""
Looping in Python — Runnable Examples
Applied AI Engineering Residency, Office Hours

Run this file with:  python3 looping_examples.py
Each section prints a header so you can follow along with the output.
"""


def section(title):
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)


# ---------------------------------------------------------------
# 1. Loop directly over items (most Pythonic)
# ---------------------------------------------------------------
section("1. Loop directly over items")

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# JS equivalent: for (const fruit of fruits) { ... }


# ---------------------------------------------------------------
# 2. Loop a set number of times with range()
# ---------------------------------------------------------------
section("2. range() - loop a set number of times")

for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

print("range(2, 6):")
for i in range(2, 6):
    print(i)  # 2, 3, 4, 5

print("range(0, 10, 2):")
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8


# ---------------------------------------------------------------
# 3. Loop over an index with range(len(...)) — the JS-style way
# ---------------------------------------------------------------
section("3. range(len()) - the training-wheels JS index loop")

nums = [10, 20, 30]
for i in range(len(nums)):
    print(i, nums[i])

# JS equivalent: for (let i = 0; i < nums.length; i++) { ... }


# ---------------------------------------------------------------
# 4. Get both index and item with enumerate()
# ---------------------------------------------------------------
section("4. enumerate() - index AND value together")

for index, fruit in enumerate(fruits):
    print(index, fruit)


# ---------------------------------------------------------------
# 5. While loops
# ---------------------------------------------------------------
section("5. while loop")

count = 0
while count < 5:
    print(count)
    count += 1  # no ++ in Python!


# ---------------------------------------------------------------
# 6. Looping over a dictionary (hash map)
# ---------------------------------------------------------------
section("6. Looping over a dictionary")

counts = {"a": 2, "b": 1}

print("keys only:")
for key in counts:
    print(key)

print("keys and values:")
for key, value in counts.items():
    print(key, value)


# ---------------------------------------------------------------
# Bonus: strings are iterable too
# ---------------------------------------------------------------
section("Bonus: looping over a string")

for char in "hello":
    print(char)


if __name__ == "__main__":
    print("\nAll looping examples ran. Scroll up to see each one.")
