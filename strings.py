

# PYTHON STRINGS - COMPLETE PRACTICE


# 1. STRING BASICS
name = "Abhishek"
city = 'Rampur'

print(name)
print(city)


# 2. STRING LENGTH
print("Length:", len(name))


# 3. POSITIVE INDEXING
language = "Python"

print(language[0])
print(language[1])
print(language[2])
print(language[3])
print(language[4])
print(language[5])


# 4. NEGATIVE INDEXING
print(language[-1])
print(language[-2])
print(language[-3])


# 5. STRING SLICING
word = "Programming"

print(word[0:4])
print(word[0:7])
print(word[3:8])
print(word[:5])
print(word[5:])


# 6. UPPER AND LOWER
text = "Python Programming"

print(text.upper())
print(text.lower())


# 7. TITLE AND CAPITALIZE
print(text.title())
print(text.capitalize())


# 8. STRIP
message = "  Hello Python  "

print(message.strip())
print(message.lstrip())
print(message.rstrip())


# 9. REPLACE
text = "I love Java"

print(text.replace("Java", "Python"))


# 10. FIND
text = "Python is easy"

print(text.find("is"))
print(text.find("Java"))


# 11. COUNT
text = "banana"

print(text.count("a"))
print(text.count("n"))


# 12. STARTSWITH AND ENDSWITH
language = "Python"

print(language.startswith("Py"))
print(language.endswith("on"))


# 13. STRING CHECKING
text = "Python123"

print(text.isalpha())
print(text.isdigit())
print(text.isalnum())


# 14. STRING CONCATENATION
first_name = "Abhishek"
last_name = "Arora"

full_name = first_name + " " + last_name

print(full_name)


# 15. STRING REPETITION
print("Python " * 3)


# 16. F-STRING
name = "Abhishek"
age = 18

print(f"My name is {name} and my age is {age}")


# 17. STRING INPUT
# Uncomment these lines to practise input

# user_name = input("Enter your name: ")
# print("Welcome", user_name)


# 18. PALINDROME CHECK
word = "madam"

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
