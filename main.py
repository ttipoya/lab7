from itertools import product
from random import randint
prove = True
class Password:
    def __init__(self, col_el, zhena_min, zhena_max, kol_odinak_el):
        self.col_el = col_el
        self.firm = []
        self.cena = []
        self.kol = 0
        self.zhena_min = zhena_min
        self.zhena_max = zhena_max
        self.suma = 0
        self.maxi = 0
        self.maxikomb = ''
        self.kol_odinak_el = kol_odinak_el
    def firma(self):
        for i in range(1, self.col_el+1):
            self.firm.append('K'+str(i))
        return
    def rangi(self):
        print("Цена каждой комплектующей:")
        for i in range(1, self.col_el + 1):
            self.cena.append(randint(self.zhena_min, self.zhena_max))
            print('K' + str(i) + '=' + str(self.cena[i - 1]), end=' ')
        print()
        print("---------------------------")
        return
    def usl(self):
        self.firma()
        self.rangi()
        for i in product(self.firm, repeat=self.col_el):
            for m in range(0, self.col_el):
                for j in range(1, self.col_el + 1):
                    if int(i[m][-1]) == j and i.count(i[m]) <= self.kol_odinak_el:
                        self.suma = self.suma + self.cena[j - 1]
                    elif i.count(i[m]) > self.kol_odinak_el:
                        self.suma = 0
            if self.suma > self.maxi and self.suma != 0:
                self.maxi = self.suma
                self.maxikomb = i
            self.suma = 0
        print('Маскимальная цена:',self.maxi)
        print('Комбинация:', self.maxikomb)
        return
while prove == True:
    print('Введите кол-во комплектующих (больше 2): ', end='')
    n = int(input())
    print('Введите минимальную цену: ', end='')
    min = int(input())
    print('Введите максимальную цену: ', end='')
    max = int(input())
    print('Введите число повторяющихся элементов не меньше 1: ', end='')
    kolodinakel = int(input())
    if n > 2 and min > 0 and max > 0 and kolodinakel > 0:
        prove = False
    else:
        print("ДАННЫЕ ВВЕДЕНЫ НЕКОРРЕКТНО. ПОРОБУЙТЕ ЕЩЁ РАЗ")
        print("---------------------------")
print("---------------------------")
pas = Password(n,min,max,kolodinakel)
pas.usl()









