import numpy as np

""" -------------------- THE BASICS OF ARRAY IN NUMPY  ------------------  """
foo = np.ndarray(shape=(2, 2), dtype=float, order='F')
print(foo, "\n", "*" * 50)

bar = np.ndarray((2,), buffer=np.array([1, 2, 3]), offset=np.int_().itemsize, dtype=int)
print(bar, "\n", "*" * 50)

a = np.arange(12).reshape(2, 6)
print(f"a.shape: {a.shape}")
print(f"a.ndim: {a.ndim}")
print(f"a.dtype: {a.dtype}")
print(f"a.itemsize: {a.itemsize}")
print(f"a.size: {a.size}")
print(f"type of a: {type(a)}", "\n", "*" * 50)

""" ------------------- ARRAY CREATE  ----------------------------------"""
# reference: https://numpy.org/doc/stable/user/quickstart.html#array-creation
b = np.array([2, 3, 4])
print(f"b: {b}", "\n", "*" * 50)

###########     IN BUILT FUNCTIONS/METHODS   #######################
# Reference: https://numpy.org/doc/stable/reference/generated/numpy.empty.html

c = np.arange(5)  # this is similar to [i for i in range(5)] in python
print(f"arange: {c}", "\n", "*" * 50)
d = np.empty((2, 3), dtype=int)
print(f"empty: {d}", "\n", "*" * 50)
e = np.linspace(0, 10)
print(f"linspace: {e}", "\n", "*" * 50)

# Reference: https://numpy.org/doc/stable/user/quickstart.html#shape-manipulation
# It is advisable to use ravel() then flattened(), since it's consumed less memory and fast in speed

############# Indexing and Slicing ##########################
# Rerefence: https://numpy.org/doc/stable/user/absolute_beginners.html#indexing-and-slicing
arr = np.arange(10) ** 3
print(f"Indexing in Array: {arr}", "\n", "*" * 50)
print(f"element at index 2, similar to Python indexing: {arr[2]}", "\n", "*" * 50)
print(f"element between 2 to 5, similar to Python indexing: {arr[2:5]}", "\n", "*" * 50)
# # from start to position 6, exclusive, set every 2nd element to 1000
arr[:6:2] = 1000
print(f"start to position 6, element is 1000:   {arr}", "\n", "*" * 50)
print(f"array: {arr}", "\n", f"Reversed array:   {arr[::-1]}", "\n", "*" * 50)