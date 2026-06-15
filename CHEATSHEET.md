# JS → Python Loop Cheat Sheet

Side-by-side translations for the most common loop patterns.

---

### Loop over each item

**JavaScript**
```javascript
for (const item of items) {
  console.log(item);
}
```

**Python**
```python
for item in items:
    print(item)
```

---

### Loop a set number of times

**JavaScript**
```javascript
for (let i = 0; i < 5; i++) {
  console.log(i);
}
```

**Python**
```python
for i in range(5):
    print(i)
```

---

### Loop with an index

**JavaScript**
```javascript
for (let i = 0; i < arr.length; i++) {
  console.log(i, arr[i]);
}
```

**Python**
```python
for i in range(len(arr)):
    print(i, arr[i])
```

---

### Loop with index AND value

**JavaScript**
```javascript
arr.forEach((item, i) => {
  console.log(i, item);
});
```

**Python**
```python
for i, item in enumerate(arr):
    print(i, item)
```

---

### While loop

**JavaScript**
```javascript
let count = 0;
while (count < 5) {
  console.log(count);
  count++;
}
```

**Python**
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

---

### Loop over an object / dictionary

**JavaScript**
```javascript
for (const key in obj) {
  console.log(key, obj[key]);
}
```

**Python**
```python
for key, value in d.items():
    print(key, value)
```

---

### Quick reference for syntax differences

| JavaScript | Python |
|------------|--------|
| `arr.length` | `len(arr)` |
| `i++` | `i += 1` |
| `true` / `false` | `True` / `False` |
| `{ }` blocks | indentation |
| `;` line endings | newline |
| `console.log()` | `print()` |
| `for...of` | `for item in ...` |
| `forEach((x, i) => ...)` | `enumerate(...)` |
