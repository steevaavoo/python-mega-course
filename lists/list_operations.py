monday_temperatures = [9.1, 8.8, 7.5]

dir(list)

help(list.append)
# Always ignore "self" - it refers to theobject on which you are performing the action.

monday_temperatures.append(8.1)
print(monday_temperatures)

monday_temperatures.clear()

# Index method returns the index of the value specified - the below will return 1, as it counts 0, 1, 2 in the list
monday_temperatures.index(8.8)
# Start and stop  define where in the list to search (from and to)

monday_temperatures.index(8.8, 2) # this instructs Python to start the search for value 8.8 from position 2 onwards.
# which will return nothing, as it exists before position 2 in our list.
