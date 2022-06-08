# Калькулятор.
# Создайте класс, где реализованы функции(методы) математических операций.
# А также функция, для ввод данных.
import cmath
class Calсulator:
    def __init__(self, a, b, s):
        self.a = a
        self.b = b
        self.s = s
    def summa(self):  # сумма
        return self.a + self.b
    def diff(self):  # разница
        return self.a - self.b
    def mult(self):  # произведение
        return self.a * self.b
    def div(self):  # деление
        try:
            self.c = self.a / self.b
        except ZeroDivisionError:
            print('Ошибка деления на ноль, попробуйте снова')
        else:
            print('Деление а на b равно: ', self.a / self.b)
            return self.a / self.b
    def exp(self):  # возв в степень
        # print('а в степени b равно: ',a**b)
        return self.a ** self.b
    def dwr(self):  # деление без остатка
        try:
            self.c = self.a // self.b
        except ZeroDivisionError:
            print('Ошибка деления на ноль, попробуйте снова')
        else:
            print('Деление без остатка равно: ', self.a // self.b)
            return self.a // self.b
    def drem(self):  # остаток при делении
        try:
            self.c = self.a % self.b
        except ZeroDivisionError:
            print('Ошибка деления на ноль, попробуйте снова')
        else:
            print('Остаток при делении равен: ', self.a % self.b)
            return self.a % self.b
    def sqrt(self):  # квадратный корень
        # print('Квадратный корень числа а равен: ',cmath.sqrt(a))
        return cmath.sqrt(self.a)
while True:
    try:
        a = float(input("Ведите число a:  "))
    except ValueError:
        print('Введен неверный символ, введите еще раз')
        continue
    else:
        try:
            b = float(input("Ведите число b:  "))
        except ValueError:
            print('Введен неверный символ, введите еще раз')
            continue
    s = input("Введите действие (+,-,*,/,//,%,**,sqrt; 0 - завершение программы) :  ")
    calc = Calсulator(a,b,s)
    if s == '-':
        print('Разница а и b равна: ',calc.diff())
#сложение
    elif s == '+':
        print('Сумма а  и b равна: ',calc.summa())
#умножение
    elif s == '*':
        print('Произведение а на b равно: ',calc.mult())
# #деление
    elif s == '/':
        calc.div()
# #возведение в степень
    elif s == '**':
        print('а в степени b равно: ',calc.exp())
# #деление без остатка
    elif s == '//':
        calc.dwr()
# #остаток при делении
    elif s == '%':
        calc.drem()
# квадратный корень
    elif s == 'sqrt':
        print('Квадратный корень числа а равен: ',calc.sqrt())
# выход
    elif s == '0':
        print('Завершение работы')
        break
# #ответ при введении непредусмотренной команды
    else:
        print('Неверная команда, введите заново')

