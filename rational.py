class TRational:
    def __init__(self, *args):
        if isinstance(args[0], int) and len(args) == 1:
            self.__num = args[0]
            self.__denom = 1
        elif isinstance(args[0], int):
            self.__num = args[0]
            self.__denom = args[1]
        elif len(args) == 1:
            if '/' in args[0]:
                self.__num = int(args[0].replace(' ', '').split('/')[0])
                self.__denom = int(args[0].replace(' ', '').split('/')[1])
            else:
                self.__num = int(args[0].replace(' ', ''))
                self.__denom = 1
        else:
            self.__num = args[0]
            self.__denom = args[1]


    def __eq__(self, other):
        if self.__num == other.__num and self.__denom == other.__denom:
            return True
        else:
            return False

    def __ne__(self, other):
        return not self == other

    def __abs__(self):
        return TRational(abs(self.__num), self.__denom)
        # return abs(self.__num) / self.__denom

    def __str__(self):
        return f'{self.__num}/{self.__denom}'

    def __mul__(self, other):
        new_num = self.__num * other.__num
        new_denom = self.__denom * self.__denom
        new_number = TRational(new_num, new_denom)
        new_number.__reduce()
        return new_number

    def __add__(self, other):
        new_number = TRational(self.__num * other.__denom + other.__num * self.__denom, self.__denom * other.__denom)
        new_number.__reduce()
        return new_number

    def __sub__(self, other):
        new_number = TRational(self.__num * other.__denom - other.__num * self.__denom, self.__denom * other.__denom)
        new_number.__reduce()
        return new_number
    def __truediv__(self, other):
        new_number = TRational(self.__num * other.__denom, self.__denom * other.__num)
        new_number.__reduce()
        return new_number

    def __neg__(self):
        return TRational(- self.__num, self.__denom)

    ## вспомогательный метод для поиска НОД (используется для сокращения дроби)
    def __nod(self):
        m, n = max(abs(self.__num), abs(self.__denom)), min(abs(self.__num), abs(self.__denom))
        while m != 0 and n != 0:
            if m > n:
                m = m % n
            else:
                n = n % m
        return m + n

    ## вспомогательный метод для сокращения дроби
    def __reduce(self):
        nod = self.__nod()
        self.__num = self.__num // nod
        self.__denom = self.__denom // nod

    def __gt__(self, other):
        if self.__num / self.__denom > other.__num / other.__denom:
            return True
        else:
            return False