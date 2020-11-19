from numpy import *
def my_func(x, a=8, b=8.6):
    return exp(-a * x) + exp(b * x)
import xlrd, xlwt
from xlutils.copy import copy
book = xlrd.open_workbook('test.xls')
sheet = book.sheet_by_index(0)
write_book = copy(book)
sheet1 = write_book.get_sheet(0)
sheet1.write(0,29,'Метод касательных')
sheet1.write(1,29,'Номер итерации')
sheet1.write(1,30,'Точка минимума')
sheet1.write(1,31,'Значение минимума')
sheet1.write(1,32,'Промежуток')
sheet1.write(1,34,'Колличество вызовов функции')
def deriv(x):
    return -8*exp(-8*x) + 8.6*exp(8.6*x)
def tangential(func, a_start, b_start, eps):
    func_calcs = 0
    iters = 0
    x_values = []
    func_values = []
    a, b = a_start, b_start
    while b - a > eps:
        deriv_a = deriv(a)
        deriv_b = deriv(b)
        func_a = func(a)
        func_b = func(b)
        x_values.append([a, b])
        func_values.append([func_a, func_b])
        c = (func_b - func_a + deriv_a * a - deriv_b * b) / (deriv_a - deriv_b)
        deriv_c = deriv(c)
        func_calcs += 8
        if deriv_c > 0:
            b = c
        elif deriv_c < 0:
            a = c
        elif deriv_c == 0:
            a = c
            b = c
            break

        x_values.append([a, b])
        func_values.append([func_a, func_b])
        iters += 1
        sheet1.write(iters + 1, 29, iters)
        sheet1.write(iters + 1, 30, (a + b) / 2.0)
        sheet1.write(iters + 1, 31, func((a + b) / 2.0))
        sheet1.write(iters + 1, 32, a)
        sheet1.write(iters + 1, 33, b)
        sheet1.write(iters + 1, 34, func_calcs)
    return {'x_min': (a + b) / 2.0, 'func_min': func((a + b) / 2.0),
            'func_calсs': func_calcs}
print(tangential(my_func,-1,1,0.000001))
write_book.save("test.xls")