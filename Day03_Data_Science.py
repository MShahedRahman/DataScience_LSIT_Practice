import numpy as np

# Grid System Representation.

grid = np.array([[1,2,3], [4,5,6]]);

print(np.concatenate(grid))
print(np.concatenate([grid,grid]))

print(np.concatenate([grid,grid], axis=1))

# Vertical Stack Representation (Row-Size Increment)

x = np.array([3,4,5])
grid = np.array([[1,2,3],[17,18,19]])
print(np.vstack([x,grid]))

# Horizontal Stack Representation (Column-size increment)

z = np.array([[9],[9]])
print(np.hstack([grid,z]))

# Spliting Data

x = np.arange(12)
print(x)
x1, x2, x3, x4, x5 = np.split(x, [1,3,6,8])
print(x1, x2, x3, x4,x5)

# Reshaping the Matrix
grid = np.arange(16).reshape((8,2))
print(grid)

# Vertically Reshaping the Matrix
upper,lower = np.vsplit(grid,[2])
print(upper, lower)