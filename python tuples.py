
# DAY 5 - PYTHON TUPLES


# 1. CREATE TUPLE
fruits = ("Apple", "Mango", "Banana")
print(fruits)

# 2. SINGLE ITEM TUPLE
single = ("Apple",)
print(single)

# 3. TUPLE INDEXING
print(fruits[0])
print(fruits[1])
print(fruits[-1])

# 4. TUPLE SLICING
numbers = (10, 20, 30, 40, 50)
print(numbers[0:3])
print(numbers[1:4])
print(numbers[:3])

# 5. TUPLE LENGTH
print(len(fruits))

# 6. COUNT METHOD
values = (10, 20, 10, 30, 10)
print(values.count(10))

# 7. INDEX METHOD
print(values.index(20))

# 8. CHECK ITEM
if "Apple" in fruits:
    print("Apple Found")

# 9. LOOP THROUGH TUPLE
for fruit in fruits:
    print(fruit)

# 10. TUPLE WITH DIFFERENT DATA TYPES
data = ("Abhishek", 18, 79.4, True)
print(data)

# 11. TUPLE UNPACKING
student = ("Abhishek", 18, "Rampur")
name, age, city = student

print(name)
print(age)
print(city)

# 12. TUPLE CONCATENATION
a = (1, 2, 3)
b = (4, 5, 6)

c = a + b
print(c)

# 13. TUPLE REPETITION
print((1, 2) * 3)

# 14. CONVERT LIST INTO TUPLE
my_list = [10, 20, 30]
my_tuple = tuple(my_list)
print(my_tuple)

# 15. CONVERT TUPLE INTO LIST
my_tuple = (10, 20, 30)
my_list = list(my_tuple)
print(my_list)

# 16. MINIMUM AND MAXIMUM
numbers = (10, 50, 20, 40, 30)
print(min(numbers))
print(max(numbers))

# 17. SUM
print(sum(numbers))

# 18. NESTED TUPLE
nested = ((1, 2), (3, 4), (5, 6))
print(nested[0])
print(nested[1][1])

# 19. TUPLE MEMBERSHIP
print(20 in numbers)
print(100 not in numbers)

# =====================================
# END OF TUPLES
# =====================================
