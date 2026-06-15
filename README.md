# Looping in Python (for JavaScript Thinkers)

A quick reference and teaching guide for the transition from JavaScript loops to Python loops. Built for Applied AI Engineering Residency office hours.

## The Core Mental Shift

In **JavaScript**, the classic loop is built around an **index counter**:

```javascript
for (let i = 0; i < arr.length; i++) {
  console.log(arr[i]);
}
```

In **Python**, the `for` loop loops over the **items themselves**, not an index. Think of Python's `for` loop as JavaScript's `for...of`: it hands you the value, not the index.

```python
for item in arr:
    print(item)
```

That single difference is what trips most people up. Everything below builds from it.

---

## The Ways to Loop in Python

| # | Technique | Use it when... |
|---|-----------|----------------|
| 1 | `for item in collection` | You just need each value (most Pythonic) |
| 2 | `for i in range(n)` | You need to loop a set number of times |
| 3 | `for i in range(len(collection))` | The "training wheels" JS-style index loop |
| 4 | `for i, item in enumerate(collection)` | You need BOTH the index and the value |
| 5 | `while condition` | You loop until something changes (less common in Python) |
| 6 | `for key, value in dict.items()` | Looping over a dictionary / hash map |

See the `examples/` folder for a runnable file demonstrating each one.

---

## 1. Loop directly over items

The biggest shift. No index, no counter, no `arr[i]`.

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

**JS equivalent:** `for (const fruit of fruits) { ... }`

---

## 2. Loop a set number of times with `range()`

The closest thing to the JS index loop.

```python
for i in range(5):
    print(i)   # 0, 1, 2, 3, 4
```

Three forms:
- `range(stop)` → 0 up to (not including) stop
- `range(start, stop)` → start up to (not including) stop
- `range(start, stop, step)` → with a step size

**Note:** `range(5)` gives 0–4. The stop value is *exclusive*, just like the highest valid index in a JS array of length 5.

---

## 3. Loop over an index: `range(len(...))`

The literal translation of the JS index loop. It works and it's valid — think of it as the training-wheels version while your brain is still thinking in JS indices.

```python
nums = [10, 20, 30]
for i in range(len(nums)):
    print(i, nums[i])
```

**JS equivalent:** `for (let i = 0; i < nums.length; i++) { ... }`

Over time, reach for option 1 or 4 instead.

---

## 4. Get both index and item: `enumerate()`

The elegant Python answer to "but I need the index AND the value."

```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
```

Once you see this, the `range(len())` pattern usually feels clunky.

---

## 5. While loops

Nearly identical to JavaScript.

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

**Note:** Python has no `++` or `--`. Use `count += 1`.

In Python you reach for `while` less often than in JS, because `for` / `range` / `enumerate` cover most cases.

---

## 6. Looping over a dictionary (hash map)

Directly relevant to the counting / anagram problems.

```python
counts = {"a": 2, "b": 1}

for key in counts:                  # keys only
    print(key)

for key, value in counts.items():   # keys and values
    print(key, value)
```

---

## Common Gotchas

- **`range(5)` gives 0–4, not 1–5.** Classic off-by-one.
- **No `++` or `--` in Python.** Use `+= 1` and `-= 1`.
- **Don't change a list's size while looping over it directly** — it causes subtle bugs. Loop over a copy, or build a new list instead.
- **Strings are iterable too.** `for char in "hello":` gives you one character at a time.

---

## The Teaching Arc

1. Write the JS index loop on the board.
2. Ask: "How do we do this in Python?"
3. Let them attempt it — they'll likely write `range(len())`.
4. Validate that it works (it does!).
5. Show the more direct `for item in list` and `enumerate` versions as the natural evolution.

The message: *here's your JS habit translated literally, and here's how Python wants you to think about it.* Honor where they are, then pull them forward.
