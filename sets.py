
# DAY 5 - PYTHON SETS

# 1. CREATE A SET
fruits = {"Apple", "Mango", "Banana"}
print(fruits)

# 2. DUPLICATE VALUES
numbers = {10, 20, 10, 30, 20}
print(numbers)  # Duplicates automatically removed

# 3. ADD ITEM
fruits.add("Orange")
print(fruits)

# 4. ADD MULTIPLE ITEMS
fruits.update(["Grapes", "Kiwi"])
print(fruits)

# 5. REMOVE ITEM
fruits.remove("Apple")
print(fruits)

# 6. DISCARD ITEM
fruits.discard("Mango")
print(fruits)

# 7. POP ITEM
fruits.pop()
print(fruits)

# 8. SET LENGTH
print(len(fruits))

# 9. CHECK ITEM
if "Banana" in fruits:
    print("Found")
else:
    print("Not Found")

# 10. LOOP THROUGH SET
for fruit in fruits:
    print(fruit)

# 11. UNION
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))

# 12. INTERSECTION
print(a.intersection(b))

# 13. DIFFERENCE
print(a.difference(b))

# 14. SYMMETRIC DIFFERENCE
print(a.symmetric_difference(b))

# 15. SUBSET
x = {1, 2}
y = {1, 2, 3, 4}

print(x.issubset(y))

# 16. SUPERSET
print(y.issuperset(x))

# 17. DISJOINT
print({1, 2}.isdisjoint({3, 4}))

# 18. COPY SET
original = {10, 20, 30}
copied = original.copy()
print(copied)

# 19. CLEAR SET
sample = {1, 2, 3}
sample.clear()
print(sample)

# 20. CONVERT LIST INTO SET
my_list = [10, 20, 10, 30, 20]
my_set = set(my_list)
print(my_set)

# 21. FROZENSET
fixed = frozenset([1, 2, 3])
print(fixed)


# END OF SETS