# A tuple is declared like a list but in brackets.
monday_temperatures = (1, 4, 5)

print(monday_temperatures)

# The difference between a list and a tuple is that a tuple is immutable. Where you can append to/change values
# in a list, you cannot do this with a tuple.

# Here's a list type for comparison:
monday_temperatures2 = [1, 4, 5]
print(monday_temperatures2)

# We can append to this as follows:
monday_temperatures2.append(6)
print(monday_temperatures2)

# Now if we try the same with the tuple:
monday_temperatures.append(6)
""" Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'append' """

# It also doesn't have a remove method like the list type does. However tuples can be faster than lists, so
# if immutable is fine, the speed benefit may be worth using a tuple instead.

# A tuple of tuples:
color_codes = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(color_codes[0][1])

# A dictionary of tuples
day_temperatures={"morning": (2.2, 4.4, 6.6),  "noon": (2.2, 4.4, 6.6), "evening": (2.2, 4.4, 6.6) }
print(day_temperatures["noon"][1])
