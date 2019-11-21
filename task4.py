# # minimal positive integer:
example1 = [int(i) for i in input("1) Введите цифры через пробел: ").split()]
example2 = [int(i) for i in input("2) Введите цифры через пробел: ").split()]
example3 = [int(i) for i in input("3) Введите цифры через пробел: ").split()]
all_example = [example1, example2, example3]
def mpi(x):
    for i in range(1, max(x)+abs(max(x))+2):    # перебираем цифры от 1 до мах числа в списке правращенного в
        if i > 0:                               # в абсолютное значение( + 2 включая это число и с 1им запасом)
            if i not in x:
                return i
                break                           # остановить сразу после первой печати
        else:
            return 1
mes = list(map(mpi, all_example))
for i in mes:
    print(i)
