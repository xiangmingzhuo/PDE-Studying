import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
# 申明变量
x = sp.symbols('x')
# 申明函数
f = x**3 * sp.sin(x) - sp.exp(-x)
# 求一阶导
f_prime = sp.diff(f, x)
print("一阶导:", f_prime)
# 求二阶导
f_double_prime = sp.diff(f_prime, x)
print("二阶导:", f_double_prime)
# 求不定积分
f_integral = sp.integrate(f, x)
print("不定积分:", f_integral)
# 求在区间 [0, 2*pi] 上的积分
f_definite_integral = sp.integrate(f, (x, 0, 2*sp.pi))
print("定积分:", f_definite_integral)
# matplotlib可视化
x_values = np.linspace(0, 2*np.pi, 100)
f_values = [float(f.subs(x, val)) for val in x_values]
f_prime_values = [float(f_prime.subs(x, val)) for val in x_values]
f_double_prime_values = [float(f_double_prime.subs(x, val)) for val in x_values]
plt.figure(figsize=(12, 8))
plt.subplot(3, 1, 1)
plt.plot(x_values, f_values, label='f(x)')
plt.title('f(x), f\'(x), f\'\'(x) on [0, 2π]')
plt.ylabel('f(x)')
plt.legend()
plt.subplot(3, 1, 2)
plt.plot(x_values, f_prime_values, label="f'(x)", color='r')
plt.ylabel("f'(x)")
plt.legend()
plt.subplot(3, 1, 3)
plt.plot(x_values, f_double_prime_values, label="f''(x)", color='g')
plt.ylabel("f''(x)")
plt.xlabel('x')
plt.legend()
plt.tight_layout()
plt.show()