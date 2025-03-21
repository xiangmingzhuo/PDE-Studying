import numpy as np
# 创建一个 3D 张量，形状为 (3, 4, 2)
data = np.array([
    [[1, 2], [3, 4], [5, 6], [7, 8]],  # 样本 0
    [[2, 3], [4, 5], [6, 10], [8, 9]],  # 样本 1
    [[0, 1], [2, 3], [4, 5], [6, 7]]  # 样本 2
])
# 重塑张量
reshaped_data = data.reshape(6, 4)
# 提取前 2 行、第 2 列和第 3 列的数据
extracted_data = reshaped_data[:2, [1, 2]]
# 输出结果
print("原三维数组:")
print(data)
print("\n重塑后数组:")
print(reshaped_data)
print("\n提取数据:")
print(extracted_data)