from numpy import *
def my_func(x, a=8, b=8.6):
    return exp(-a * x) + exp(b * x)
import xlrd, xlwt
from xlutils.copy import copy
book = xlrd.open_workbook('test.xls')
sheet = book.sheet_by_index(0)
write_book = copy(book)
sheet1 = write_book.get_sheet(0)
sheet1.write(0,10,'Метод Фибоначчи')
sheet1.write(1,10,'Номер итерации')
sheet1.write(1,11,'Точка минимума')
sheet1.write(1,12,'Значение минимума')
sheet1.write(1,13,'Промежуток')
sheet1.write(1,14,'Колличество вызовов функции')
def fibonacci(func, a_start, b_start, eps):
    def fib_iter(a, b, eps):
        fib_next = 1
        fib_current = 1
        n = 0
        while (fib_next < (b - a) / (0.00005 * eps)):
            fib_next = fib_next + fib_current
            fib_current = fib_next - fib_current
            n += 1
        return fib_next, fib_current, n
    a = a_start
    b = b_start
    iters = 0
    fib_next, fib_current, n = fib_iter(a, b, eps)
    fib_previous = fib_next - fib_current
    c = a + (b - a) * (fib_previous/fib_next)
    d = a + (b - a) * (fib_current/fib_next)
    func_c = func(c)
    func_d = func(d)
    func_calcs = 2
    for i in range(n):
        fib_next, fib_current = fib_current, fib_previous
        fib_previous = fib_next - fib_current
        if (func_c > func_d):
            a = c
            c = d
            d = a + (fib_current/fib_next) * (b - a)
            func_c = func_d
            func_d = func(d)
            func_calcs += 1
        else:
            b = d
            d = c
            c = a + (fib_previous/fib_next) * (b - a)
            func_d = func_c
            func_c = func(c)
            func_calcs += 1
        iters += 1
        sheet1.write(iters + 1, 10, iters)
        sheet1.write(iters + 1, 11, (a + b) / 2.0)
        sheet1.write(iters + 1, 12, func((a + b) / 2.0))
        sheet1.write(iters + 1, 13, c)
        sheet1.write(iters + 1, 14, d)
        sheet1.write(iters + 1, 16, func_calcs)

    return {'x_min' : (a+b) / 2.0,
            'func_min' : func((a+b)/2.0),
            'func_calcs' : func_calcs }
print(fibonacci(my_func,-1,1,0.000001))
write_book.save("test.xls")