import view
import math_operathion
def start():
    type = view.get_type()
    if type:
        a, b = view.get_value_int()
    else:
        a, b = view.get_value_complex()
    sign = view.get_sign(type)
    math_operathion.init(a, b)

    res = 'Ошибка знака'

    if sign == '+':
       res = math_operathion.summ()
    elif sign == '-':
        res = math_operathion.sub()
    elif sign == '*':
       res = math_operathion.mult()
    elif sign == '/':
        res = math_operathion.div()
    elif sign == '//':
        res = math_operathion.cel_div()
    elif sign == '%':
        res = math_operathion.ost_div()

    view.out_res(res)



