import numpy as np
from scipy.sparse import coo_matrix, csr_matrix, csc_matrix
# 创建稀疏矩阵A
row = np.array([0, 1, 2, 3, 4])
col = np.array([0, 1, 2, 3, 4])
data = np.array([1, 2, 3, 4, 5])
A = coo_matrix((data, (row, col)), shape=(5, 5))
# 创建稀疏矩阵B
B = csr_matrix((data, (row, col)), shape=(5, 5))
# 创建稀疏矩阵C
C = csc_matrix((data, (row, col)), shape=(5, 5))
# 计算 A + B
A_plus_B = A + B
# 计算 A * A
A_times_A = A.multiply(A)
# 计算 A * B
A_times_B = A.dot(B)
# 计算 B * C
B_times_C = B.dot(C)
# 输出结果
print("A:\n", A)
print("A + B:\n", A_plus_B.toarray())
print("A * A :\n", A_times_A.toarray())
print("A * B :\n", A_times_B.toarray())
print("B * C :\n", B_times_C.toarray())