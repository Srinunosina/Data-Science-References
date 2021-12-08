import numpy as np

a1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a1)

for i in range(3):
    for j in range(3):
        if i < j:
            print(a1[i][j], end= " ")
    print("\n")