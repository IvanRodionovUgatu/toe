import cmath

import matplotlib.pyplot as plt
import numpy as np

# Пример комплексных чисел, представляющих токи
I_a = 10 * cmath.exp(1j * 0)  # Ток в фазе A
I_b = 10 * cmath.exp(1j * -120 * (np.pi / 180))  # Ток в фазе B, с фазовым сдвигом -120°
I_c = 10 * cmath.exp(1j * 120 * (np.pi / 180))  # Ток в фазе C, с фазовым сдвигом 120°

# Создание фигуры и оси
fig, ax = plt.subplots()

# Строим векторы токов
ax.quiver(0, 0, I_a.real, I_a.imag, angles='xy', scale_units='xy', scale=1, color='r', label='I_a')
ax.quiver(0, 0, I_b.real, I_b.imag, angles='xy', scale_units='xy', scale=1, color='g', label='I_b')
ax.quiver(0, 0, I_c.real, I_c.imag, angles='xy', scale_units='xy', scale=1, color='b', label='I_c')

# Настройка осей
ax.set_xlim(-12, 12)
ax.set_ylim(-12, 12)
ax.set_aspect('equal')

# Добавляем подписи
ax.text(I_a.real, I_a.imag, 'I_a', fontsize=12, color='r')
ax.text(I_b.real, I_b.imag, 'I_b', fontsize=12, color='g')
ax.text(I_c.real, I_c.imag, 'I_c', fontsize=12, color='b')

# Подписываем оси
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)

# Добавляем сетку
ax.grid(True)

# Добавляем легенду
ax.legend()

# Показываем диаграмму
plt.title('Векторная диаграмма токов в трехфазной системе')
plt.show()
