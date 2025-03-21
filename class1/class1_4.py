import sympy as sp
import numpy as np
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