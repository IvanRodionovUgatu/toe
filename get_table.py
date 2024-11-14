import cmath

import pandas as pd
import math


#35 # 32
def format_complex_number(z):
    modulus = abs(z)
    argument = cmath.phase(z)
    argument_deg = math.degrees(argument)
    return f"{modulus:.2f}e^j{round(argument_deg, 2)}°"


file_path = 'data_table/rgr4.ods'

data = pd.read_excel(file_path, sheet_name='data')

fifth_row = data.iloc[32]
name =  fifth_row['Фамилия Имя Отчество ']
print(name)
E = fifth_row['Фазная ЭДС E, В']
Rl = fifth_row['Сопротивления компонентов фаз, Ом ZЛ RЛ']
XLl = fifth_row['XLЛ']
XCl = fifth_row['XСЛ']
R3 = fifth_row['ZЗ RЗ']
XLz = fifth_row['XLЗ']
XCz = fifth_row['XCЗ']
Rt = fifth_row['ZТ RT']
XLt = fifth_row['XLT']
XCt = fifth_row['XСТ']
Zl = fifth_row['Условия несимметрии трехфазной цепи ZЛ']
Zz = fifth_row['ZЗ']
Zt = fifth_row['ZТ'][-1]

Ea = E
Eb = E
Ec = E
Ua = Ea + 0j
Ub = Ua * cmath.exp(-1j*120*(math.pi / 180))
Uc = Ub

"""Uab, Ubc, Uca - линейные напряжения, Ubc и Uca смещены относительно Uab на -120 и 120"""
Uab = math.sqrt(3) * Ua * cmath.exp(1j*30*(math.pi / 180))
Ubc = Uab * cmath.exp(-1j*120 * (math.pi / 180))
Uca = Uab * cmath.exp(1j*120 * (math.pi / 180))



"""Вывод результатов"""
print('Ua', format_complex_number(Ua))
print('Ub', Ub)
print('Uc', Uc)
print('Uab', format_complex_number(Uab))
print('Ubc', format_complex_number(Ubc))
print('Uca', format_complex_number(Uca))

"""Вторая часть"""
Xl = (1j*XLl * (-1j*XCl)) / (1j*XLl - 1j*XCl)
Zl = Zla = 1/(1/Rl + 1/(1j*XLl) - 1/(1j*XCl))
Zz = Za = R3 + 1j*XLz - 1j*Xl * XCz
Zt = Zab = Xab = Rt + 1j*XLt - 1j*XCt

Zzet = Zta = Xta = Zt*Zt / (Zt + Zt+ Zt)
Zzn = 1 / (1/Za + 1/Zta)
Zf = Zla + Zzn

"""Третья часть"""
IA = Ua / Zf
a = cmath.exp(1j*120*(math.pi / 180))
IB = a ** 2 * IA
IC = a * IA

"""Четвертая часть"""
delta_Ula = IA * Zla
delta_Ulb = a**2 * delta_Ula
delta_Ulc = a * delta_Ula

UA = Ua - delta_Ula
UB = a ** 2 * UA
UC = a * UA

UAB = UA - UB
UBC = UB - UC
UCA = UC - UA

Ia = UA / Za
Ib = a**2 * Ia
Ic = a * Ia

Iat = IA - Ia


print('Ответ', format_complex_number(Ia))
