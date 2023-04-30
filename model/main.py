import numpy as np

A = np.array ([
    [1, 2, 5],
    [1, 9, 7],
    [6, 7, 6]
])

B = np.array(
    [1, 2, 9]
)

C = A.dot(B.T)

print(C)