from numpy import *
def my_func(x, a=8, b=8.6):
    return exp(-a * x) + exp(b * x)
import xlrd, xlwt
from xlutils.copy import copy
book = xlrd.open_workbook('test.xls')
sheet = book.sheet_by_index(0)
write_book = copy(book)
sheet1 = write_book.get_sheet(0)
sheet1.write(0,19,'Метод золотого сечения')
sheet1.write(1,19,'Номер итерации')
sheet1.write(1,20,'Точка минимума')
sheet1.write(1,21,'Значение минимума')
sheet1.write(1,22,'Промежуток')
sheet1.write(1,25,'Колличество вызовов функции')

def golden_ratio(func, a_start, b_start, eps):
    a = a_start
    b = b_start
    func_calcs = 0
    x_values = []
    func_values = []
    c, d = (3 - 5 ** 0.5) / 2 * (b - a) + a, (5 ** 0.5 - 1) / 2 * (b - a) + a
    func_calcs += 2
    x_values.append([c, d])
    func_c, func_d = func(c), func(d)
    func_values.append([func_c, func_d])
    iters = 0
    while b - a > eps:
        if func_c > func_d:
            a = c
            c = d
            func_c = func_d
            d = (5 ** 0.5 - 1) / 2 * (b - a) + a
            func_d = func(d)
            func_calcs += 1
        else:
            b = d
            d = c
            func_d = func_c
            c = (3 - 5 ** 0.5) / 2 * (b - a) + a
            func_c = func(c)
            func_calcs += 1
        iters += 1
        sheet1.write(iters + 1, 19, iters)
        sheet1.write(iters + 1, 20, (a + b) / 2.0)
        sheet1.write(iters + 1, 21, func((a+b)/2.0))
        sheet1.write(iters + 1, 22, a)
        sheet1.write(iters + 1, 23, b)
        sheet1.write(iters + 1, 24, func_calcs)

    return {'x_min': (a+b) / 2.0, 'func_min': func_values[-1][0],'func_calcs': func_calcs}
print(golden_ratio(my_func,-1, 1,0.000001))
write_book.save("test.xls")