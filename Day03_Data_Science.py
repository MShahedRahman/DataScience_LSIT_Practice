import numpy as np

grid = np.array([[1,2,3], [4,5,6]]);

print(np.concatenate(grid))
print(np.concatenate([grid,grid]))

print(np.concatenate([grid,grid], axis=1))