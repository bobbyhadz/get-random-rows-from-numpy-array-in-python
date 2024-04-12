# Get N random Rows from a NumPy Array in Python

import numpy as np

arr = np.array([
    [2, 4, 6],
    [1, 3, 5],
    [3, 5, 7],
    [4, 6, 8],
    [5, 7, 9]
])

index = np.random.randint(arr.shape[0], size=2)

print(index)  # 👉️ [3 2]

print('-' * 50)

random_rows = arr[index, :]

# [[4 6 8]
#  [3 5 7]]
print(random_rows)