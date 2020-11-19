from numpy import *
def func(x, a=8, b=8.6):
    return exp(-a * x) + exp(b * x)
import xlwt
book = xlwt.Workbook()
sheet1 = book.add_sheet("Sheet1")
sheet1.write(0,0,'Метод дихотомии')
sheet1.write(1,0,'Номер итерации')
sheet1.write(1,1,'Точка минимума')
sheet1.write(1,2,'Значение минимума')
sheet1.write(1,3,'Промежуток')
sheet1.write(1,5,'Колличество вызовов функции')
def dichotomy(func, a_start, b_start, eps):
    a = a_start
    b = b_start
    x_min_values = []
    func_min_values = []
    delta = eps / 2.0
    interval_length = b - a
    iters = 0
    func_calcs = 0
    while interval_length > eps:
        c = (a + b - delta) / 2.0
        d = (a + b + delta) / 2.0
        if func(c) > func(d):
            a = c
        else:
            b = d
        interval_length = b - a
        x_min_values.append((a + b)/2.0)
        func_min_values.append(func((a + b)/2.0))
        func_calcs += 2
        iters += 1
        sheet1.write(iters + 1, 0, iters)
        sheet1.write(iters + 1, 1, (a + b)/2.0)
        sheet1.write(iters + 1, 2, func((a + b) / 2.0))
        sheet1.write(iters + 1, 3, c)
        sheet1.write(iters + 1, 4, d)
        sheet1.write(iters + 1, 5, func_calcs )
    return {'x_min' : (a + b) / 2.0, 'func_min' : func((a + b)/2.0), 'func_calcs' : func_calcs}
print(dichotomy(func,-1,1,0.000001))
book.save("test.xls")