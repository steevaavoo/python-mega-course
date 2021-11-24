# Dictionary is key value pairs "items" - like hash table - using {}
# Where a list needs context. For example, like the student grades list
student_grades = [9.1, 8.8, 7.5]
# Who's grade is whose? Rather, use a dictionary:
student_grades = {"Asya": 9.1, "Steve": 8.8, "Luke": 7.5}
# You can then access them individually by the key:
print(student_grades["Asya"])

# A list is more appropriate when we only care about the numbers - such as a list of temperatures on a given day.
# So - how to calculate average of a dictionary - assuming values are numbers?
# First, let's look at the methods available to the dictionary "dict" type:
dir(dict)
# "values" is an option.
help(dict.values)
""" values(...)
    D.values() -> an object providing a view on D's values """
student_grades.values()
# Returns dict_values([9.1, 8.8, 7.5])
# So how do we act upon that to get the mean?
mysum = sum(student_grades.values())
mylen = len(student_grades)
mean = mysum / mylen
print(mean)

# If we want a list of the keys in student_grades:
student_grades.keys()
