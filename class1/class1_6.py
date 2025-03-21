import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as tri
# 申明节点坐标
num_points = 50
points = np.random.rand(num_points, 2)  # 随机生成点
# 使用 Delaunay 三角剖分
triang = tri.Triangulation(points[:, 0], points[:, 1])
# 绘制三角形网格
plt.figure()
plt.triplot(triang, 'bo-')
plt.title('Simple Triangle Mesh')
plt.xlabel('X ')
plt.ylabel('Y')
plt.show()
# 计算长宽比
aspect_ratios = []
for simplex in triang.triangles:
    p0, p1, p2 = points[simplex]
    a = np.linalg.norm(p1 - p2)
    b = np.linalg.norm(p0 - p2)
    c = np.linalg.norm(p0 - p1)
    s = (a + b + c) / 2
    area = np.sqrt(s * (s - a) * (s - b) * (s - c))
    circum_radius = (a * b * c) / (4 * area)
    in_radius = area / s
    aspect_ratio = circum_radius / in_radius
    if aspect_ratio <= 6:  # 保留长宽比<= 6 的值
        aspect_ratios.append(aspect_ratio)
aspect_ratios = np.array(aspect_ratios)
print(f"Aspect Ratios: Min = {np.min(aspect_ratios)}, Max = {np.max(aspect_ratios)}")
# 绘制直方图
plt.figure()
plt.hist(aspect_ratios, bins=10, range=(1, 6), edgecolor='black')  # 限制横坐标范围为 1 到 6
plt.xlabel('Aspect Ratio')
plt.ylabel('Frequency')
plt.title('Distribution of Aspect Ratios')
plt.grid()
plt.show()