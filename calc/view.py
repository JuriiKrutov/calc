def get_type():
    type = int(input('С какими числами хотите рабртать? 0 - комплексные, 1 - целые\n'))
    return type

def get_value_int():
    a = int(input('Введите число: '))
    b = int(input('Введите число: '))
    return a, b

def get_value_complex():
    a = complex(input('Введите число: '))
    b = complex(input('Введите число: '))
    return a, b

def get_sign(type):
    if type:
        sign = input("Введите знак: ")
        if sign in ['+', '-', '*', '/', '%', '//']:
            return sign
        else:
            print('Неверная операция')
    else:
        sign = input()
        if sign in ['+', '-', '*', '/']:
            return sign
        else:
            print('Неверная операция')

def out_res(res):
    print(res)
