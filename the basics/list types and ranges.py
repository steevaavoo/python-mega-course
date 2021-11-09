# Lists

# Lists are similar to arrays
student_grades = [9.1, 8.8, 7.5]

print(student_grades)

# To pick out a specific element of an array (print in this case)
print(student_grades[1])

# Lists can also contain other lists:
rainfall = [28.2, 15, "monument", [100, "banana", 28.7]]

print(rainfall)

# Access specific elements of list as before:
print(rainfall[2])

# Access sub-list elements similarly - remember the count starts at 0:
print(rainfall[3][1])

# Ranges

# You can create a list of numbers automatically using a range. For example:
range_example = list(range(1, 10))

print(range_example)

# As you can see we just needed to specify the list boundaries inside range(). So, we specified 1and 10. Note
# that 10 is not included in the list. The generated list always runs up to one number before the upper number.
# In our example, it goes up to 9 since the upper number is 10.

# You can also specify a step (how many to increment by each count) as a third argument:

range_example = list(range(1, 10, 2))

print(range_example)

# So, the count happens every two items starting from 1 and ending at 9.
