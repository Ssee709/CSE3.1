string_list = ["W", "or", "l", "d!"]
int_list = [5, 15, -67, 191, 88, -23]
float_list = [2.2, -101.9, 60.0]
boolean_list = [False, False, True, False, True]
mixed_list = ["Hello", 2, "the", string_list]
empty = []

# Changed value of first index
boolean_list[0] = True

# Added an item to the list
boolean_list.append(False)

print(string_list)
string_list.remove("l")
print(string_list)

# Remove all true from boolean list
print(boolean_list)
while True in boolean_list:
    boolean_list.remove(True)
print(boolean_list)

