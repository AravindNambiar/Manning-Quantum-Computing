import numpy as np

"""
Can you create a row matrix of three elements where each element is sqrt{2}
and a similar column vector. Can you do a a dot product (@) of both vectors? What is the number?

"""
cvector = np.repeat([np.sqrt(2)],3)
print("The column is : ", cvector , " \n of shape : ",cvector.shape)

rvector = cvector.T
print("The row vector is : ", rvector, " \n of shape : ",rvector.shape)
dp = rvector @ cvector

print("Dot product is : ", dp)


"""
    Can you create the following matrices in code and multiply them together?

[1+2i2+3i4+5i]\begin{bmatrix} 1+2i \\ 2+3i \\ 4+5i\\ \end{bmatrix}
⎣⎢⎡​1+2i2+3i4+5i​⎦⎥⎤​

[1+2j2+3j4+5j6+7j4+1j2+0j]\begin{bmatrix} 1 + 2j & 2 + 3j & 4 + 5j \\ 6 + 7j & 4 + 1j & 2 + 0j \\ \end{bmatrix}
[1+2j6+7j​2+3j4+1j​4+5j2+0j​]

"""
matrix1 = np.array([[1 + 2j],
                    [2 + 3j],
                    [4 + 5j]])
matrix2 = np.array([[1+2j, 2+3j, 4+5j],[6+7j, 4+1j, 2+0j] ])
print("Matrix 1 : ", matrix1)
                    
print("Matrix 2 : ", matrix2)

matrix3 = matrix2 @ matrix1
print("Matrix 3 : ", matrix3)
