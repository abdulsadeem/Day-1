import numpy as np

# 0D
a0 = np.array(10)
print(a0, a0.ndim, a0.shape)

# 1D
a1 = np.array([1, 2, 3])
print(a1, a1.ndim, a1.shape)

# 2D
a2 = np.array([[1, 2], [3, 4]])
print(a2, a2.ndim, a2.shape)

# 3D
a3 = np.array([[[1, 2], [3, 4]]])
print(a3, a3.ndim, a3.shape)

print("#################################")

###################################
import numpy as np
a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([10, 20, 30])
result = a + b
print(result)
# Vectorized vs Loop example
arr = np.random.rand(10)
# Vectorized
squared = arr ** 2
print(squared)

print("#################################")#

arr = np.arange(9)
reshaped = arr.reshape(3, 3)
print(reshaped)

a = np.array([[1, 2]])
b = np.array([[3, 4]])

vstacked = np.vstack((a, b))
print(vstacked)

hstacked = np.hstack((a, b))
print(hstacked)


print("#########################")

data = np.array([[10, 20, 30],
                 [40, 50, 60]])

print(np.mean(data))
print(np.mean(data, axis=0))
print(np.mean(data, axis=1))

print("#########################")

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print(np.dot(A, B))















