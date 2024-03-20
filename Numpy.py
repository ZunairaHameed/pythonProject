import numpy as np
# print the version of numpy library
print(np.__version__)
vehicles = np.array(["car", "bus", "cycle", "bicycle"])
print(vehicles)
print(vehicles.ndim)

# using tuple in 2-d array
fruits = np.array((("apple", "orange"), ("banana", "melon")))
print(fruits)
print(fruits.ndim)

# 3-d array
colors1 = np.array([[["blue", "black"], ["purple", "mustard"]], [["yellow", "red"], ["golden", "white"]]])
print(colors1)
print(colors1.ndim)

# higher dimensional array
bird = np.array(["black" "eagle"], ndmin=4)
print(bird)
print("Number of dimensions: ", bird.ndim)

# indexing
num = np.array([10, 20, 30, 40])
print(num[1] + num[3])

# 2D array in numpy with all operations
import numpy as np

# access 2d array
colors1 = np.array([["black", "blue", "white"], ["red", "yellow", "green"]])
print('3rd element on 2nd row: ', colors1[1, 2], '2nd element on 2nd row:', colors1[1,1])

# access 3d array
colors2 = np.array([[["BLACK", "BLUE"], ["WHITE", "RED"]], [["WHITE", "RED"], ["YELLOW", "GREEN"]]])
print(colors2)

# -ve indexing
num = np.array([[10, 20, 30, 40], [5, 15, 20, 25]])
print("3rd element from 2nd row: ", num[1, -2])

# slicing array
NUM = np.array([1, 2, 3, 4, 5])
print(NUM[1:5])
print(NUM[:4])
print(NUM[2:])

# step slicing 2d array
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])
colors2 = np.array([["red", "blue", "pink", "white"], ["red", "blue", "pink", "white"]])
print(colors2[0:2, 1:4])



