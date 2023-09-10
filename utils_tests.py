import utils

u = utils.utils()

# Test reversed function with strings, floats, and integers
print(u.reversed("hello"))
print(u.reversed(123.5))
print(u.reversed(123))

# Test formatter function with strings, floats, and integers
print(u.formatter("hello"))
print(u.formatter(123.5))
print(u.formatter(123))