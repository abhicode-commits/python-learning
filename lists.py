# DAY 4 - PYTHON LISTS COMPLETE PRACTICE



# 1. CREATE A LIST
fruits = ["Apple", "Mango", "Banana", "Orange"]
print("Original List:", fruits)


# 2. LIST INDEXING
print("First Item:", fruits[0])
print("Second Item:", fruits[1])
print("Last Item:", fruits[-1])


# 3. LIST SLICING
numbers = [10, 20, 30, 40, 50]

print("First Three:", numbers[0:3])
print("Middle Items:", numbers[1:4])
print("From Start:", numbers[:3])
print("From Index 2:", numbers[2:])


# 4. CHANGE LIST ITEMS
fruits[1] = "Grapes"
print("Updated List:", fruits)


# 5. APPEND - ADD ONE ITEM
fruits.append("Pineapple")
print("After Append:", fruits)


# 6. INSERT - ADD AT SPECIFIC POSITION
fruits.insert(1, "Kiwi")
print("After Insert:", fruits)


# 7. EXTEND - ADD MULTIPLE ITEMS
fruits.extend(["Papaya", "Guava"])
print("After Extend:", fruits)


# 8. REMOVE - REMOVE SPECIFIC ITEM
fruits.remove("Apple")
print("After Remove:", fruits)


# 9. POP - REMOVE ITEM BY INDEX
fruits.pop(0)
print("After Pop:", fruits)


# 10. SORT - ASCENDING ORDER
marks = [70, 40, 90, 20, 60]
marks.sort()
print("Ascending:", marks)


# 11. REVERSE
marks.reverse()
print("Reversed:", marks)


# 12. LENGTH OF LIST
print("Total Fruits:", len(fruits))


# 13. COUNT
values = [10, 20, 10, 30, 10]
print("Count of 10:", values.count(10))


# 14. INDEX
print("Index of 20:", values.index(20))


# 15. CHECK ITEM EXISTS
if 20 in values:
    print("Number Found")
else:
    print("Number Not Found")


# 16. LOOP THROUGH LIST
students = ["Abhishek", "Rahul", "Aman"]

for student in students:
    print("Student:", student)


# 17. SUM, MAX AND MIN
numbers = [10, 20, 30, 40, 50]

print("Sum:", sum(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))


# 18. CLEAR LIST
sample = [1, 2, 3, 4]
sample.clear()
print("Empty List:", sample)


# 19. DIFFERENT DATA TYPES IN LIST
data = ["Abhishek", 18, 79.4, True]
print("Mixed List:", data)


# 20. NESTED LIST
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("First Row:", matrix[0])
print("Middle Element:", matrix[1][1])


# 21. LIST COMPREHENSION
squares = [x * x for x in range(1, 6)]
print("Squares:", squares)


# 22. EVEN NUMBERS USING LIST COMPREHENSION
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print("Even Numbers:", even_numbers)


# 23. FIND LARGEST NUMBER
numbers = [45, 12, 89, 34, 67]
print("Largest Number:", max(numbers))


# 24. FIND SMALLEST NUMBER
print("Smallest Number:", min(numbers))


# 25. COPY A LIST
original = [10, 20, 30]
copied = original.copy()

print("Original:", original)
print("Copied:", copied)



