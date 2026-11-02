# 1. FOR LOOP
for i in range(1, 6):
    print(i)


# 2. FOR LOOP - EVEN NUMBERS
for i in range(2, 11, 2):
    print(i)


# 3. WHILE LOOP
i = 1
while i <= 5:
    print(i)
    i += 1


# 4. MULTIPLICATION TABLE
number = 5

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


# 5. BREAK
for i in range(1, 6):
    if i == 4:
        break
    print(i)


# 6. CONTINUE
for i in range(1, 6):
    if i == 3:
        continue
    print(i)