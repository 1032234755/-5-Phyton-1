
import numpy as np
import scipy.interpolate as spi

# ������
xi = np.array([0.0, 1.0, 2.0, 3.0, 4.0])
yi = np.array([0.0, 0.5, 0.86603, 1.0, 0.86603])

# ���������� ������ � ������� ��������� �� ������
spline = spi.CubicSpline(xi, yi, bc_type='clamped')

# �������� ������� � ����� x* = 1.5
x_star = 1.5
y_star = spline(x_star)

print(f"�������� ������� � ����� x* = {x_star}: {y_star}")
