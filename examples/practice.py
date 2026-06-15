"""
Looping Practice — Office Hours
Fill in each function. Run this file to check your work against the expected output.

    python3 practice.py
"""


# ---------------------------------------------------------------
# Exercise 1: Print each name on its own line.
# Use a direct for-loop (loop over items, no index).
# ---------------------------------------------------------------
def print_names(names):
    # TODO: loop over names and print each one
    pass


# ---------------------------------------------------------------
# Exercise 2: Return a list of numbers from 0 up to n-1.
# Use range().
# ---------------------------------------------------------------
def count_up_to(n):
    result = []
    # TODO: use range(n) to append each number to result
    return result


# ---------------------------------------------------------------
# Exercise 3: Return a list of "index: value" strings.
# Use enumerate().
# Example: ["0: a", "1: b"]
# ---------------------------------------------------------------
def label_items(items):
    result = []
    # TODO: use enumerate to build each "index: value" string
    return result


# ---------------------------------------------------------------
# Exercise 4: Count how many times each character appears.
# Return a dictionary. Loop over the string directly.
# Example: count_chars("aab") -> {"a": 2, "b": 1}
# ---------------------------------------------------------------
def count_chars(s):
    counts = {}
    # TODO: loop over s, build up the counts dictionary
    return counts


# ---------------------------------------------------------------
# Exercise 5: Sum all the values in a dictionary.
# Use .items() or .values().
# Example: sum_values({"a": 2, "b": 3}) -> 5
# ---------------------------------------------------------------
def sum_values(d):
    total = 0
    # TODO: loop over the dictionary values and add them up
    return total


# ---------------------------------------------------------------
# Simple checks — run the file to see if your answers are right
# ---------------------------------------------------------------
if __name__ == "__main__":
    print("Exercise 2:", count_up_to(5), "(expected [0, 1, 2, 3, 4])")
    print("Exercise 3:", label_items(["a", "b"]), '(expected ["0: a", "1: b"])')
    print("Exercise 4:", count_chars("aab"), "(expected {'a': 2, 'b': 1})")
    print("Exercise 5:", sum_values({"a": 2, "b": 3}), "(expected 5)")
    print("\nExercise 1 should print two names below:")
    print_names(["Ada", "Grace"])
