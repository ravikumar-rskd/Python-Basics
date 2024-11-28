# --- Loops ---

# For Loop - Iterate over a range
for i in ____:
    print(i)  # Should print: 0 1 2 3 4

# For Loop - Iterate over a list
colors = ["red", "green", "blue"]
for color in ____:
    print(color)  # Should print: red, green, blue

# While Loop
x = 0
while x ____ 5:
    print(x)  # Should print: 0 1 2 3 4
    x += 1

# For Loop with break
for i in range(10):
    if i ____ 5:
        break
    print(i)  # Should print: 0 1 2 3 4

# For Loop with continue
for i in range(6):
    if i ____ 3:
        continue
    print(i)  # Should print: 0 1 2 4 5

# While Loop with break
x = 0
while x ____ 10:
    if x ____ 7:
        break
    print(x)  # Should print: 0 1 2 3 4 5 6
    x += 1

# While Loop with continue
x = 0
while x ____ 5:
    x += 1
    if x ____ 3:
        continue
    print(x)  # Should print: 1 2 4 5

# Nested Loops
for i in range(2):
    for j in range(3):
        print(f"i={i}, j={j}")  # Should print: i=0, j=0; i=0, j=1; i=0, j=2; i=1, j=0; i=1, j=1; i=1, j=2

# For Loop with else
for i in range(3):
    print(i)
else:
    print("Done!")  # Should print: 0 1 2 Done!
