from _typeshed import Self


x = 10
y = "10"
z = 10.1

sum1 = x + x
sum2 = y + y

print(sum1, sum2)
print(type(x), type(y), type(z))

# Getting Help
# Getting attributes/methods/operators of a data type
dir()

# If you want to know all the stuff you can do with/to/on strings, for example:
dir(str)

# This will list all the operations you can use with a string
# If you want to know what a specific one does, like upper, use:
help(str.upper)

""" upper(self, /)
    Return a copy of the string converted to uppercase.
 """
# To use a method - quite similar to PowerShell
"hello".upper()
# Returns HELLO

# There's also a Title method
"hello".title()
# Returns Hello

# Do the same with variables - try this:
myword = "hello"

myword.title()

# Finding out what code we need...
# We want to get the average of the numbers in this list:
student_grades = [9.1, 8.8, 7.5]
# So we use:
dir(list)
# There is no method for averages here.

# Average is a Function - so it's independent of types, like print().
# So to get a list of all the built-in functions, use:
dir(__builtins__)
# You can add libraries created by other people.

# There is no "average" function, but there is sum. So let's use that.
mysum = sum(student_grades)
print(mysum)
# Alone, this returns the total of the 3 numbers.
# For averaging, we can find the number of items in the list, by using the len function
help(len)

""" len(obj, /)
    Return the number of items in a container. """

mylen = len(student_grades)
print(mylen)

# Then we can divide the sum by the length to get the mean
mean = mysum / mylen
print(mean)
