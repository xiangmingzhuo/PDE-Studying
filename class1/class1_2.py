import numpy as np
# 生成 (1, 2, 3) 的三维数组
array_3d = np.random.rand(1, 2, 3)
# 生成 (3, 4) 的二维数组
array_2d = np.random.rand(3, 4)
# tensordot 实现三维数组中矩阵与二维数组矩阵的乘法
result = np.tensordot(array_3d, array_2d, axes=([2], [0]))
print("结果形状:")
print(result.shape)