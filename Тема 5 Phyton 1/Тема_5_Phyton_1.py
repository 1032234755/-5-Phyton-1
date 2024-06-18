
import numpy as np
import scipy.interpolate as spi

# Данные
xi = np.array([0.0, 1.0, 2.0, 3.0, 4.0])
yi = np.array([0.0, 0.5, 0.86603, 1.0, 0.86603])

# Кубический сплайн с нулевой кривизной на концах
spline = spi.CubicSpline(xi, yi, bc_type='clamped')

# Значение функции в точке x* = 1.5
x_star = 1.5
y_star = spline(x_star)

print(f"Значение функции в точке x* = {x_star}: {y_star}")
