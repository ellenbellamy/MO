from numpy import *
def my_func(x, a=8, b=8.6):
    return exp(-a * x) + exp(b * x)
def deriv(x):
    return -8*exp(-8*x) + 8.6*exp(8.6*x)
def second_deriv(x1, x2):
    return (deriv(x2) - deriv(x1)) / (x2 - x1)
import xlrd, xlwt
from xlutils.copy import copy
book = xlrd.open_workbook('test.xls')
sheet = book.sheet_by_index(0)
write_book = copy(book)
sheet1 = write_book.get_sheet(0)
sheet1.write(0,39,'Метод секущих')
sheet1.write(1,39,'Номер итерации')
sheet1.write(1,40,'Точка минимума')
sheet1.write(1,41,'Значение минимума')
sheet1.write(1,43,'Колличество вызовов функции')
def hords_method(func, a_start, b_start, eps):
    a = a_start
    b = b_start
    func_calcs = 0
    iters = 0
    x_values = []
    func_values = []
    while abs(deriv(b)) > eps:
       a, b = b,a - deriv(a) / second_deriv(a, b)
       x_min = b
       func_min = func(b)
       func_calcs += 1
       iters += 1
       sheet1.write(iters + 1, 39, iters)
       sheet1.write(iters + 1, 40, b)
       sheet1.write(iters + 1, 41, func_min)
       sheet1.write(iters + 1, 42, func_calcs)
    return {'x_min': x_min, 'func_min': func_min,
            'func_calсs': func_calcs}
print(hords_method(my_func,-1,1,0.000001))
write_book.save("test.xls")