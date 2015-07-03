from example import *


def test_is_brackets_blanced():
    print is_brackets_blanced('((()))')
    print is_brackets_blanced('(())))')
    print is_brackets_blanced('((')
    print is_brackets_blanced('))')
    print is_brackets_blanced('{{([][])}()}')
    print is_brackets_blanced('[{()]')

def test_decimal_to_binary():
    print decimal_to_binary(42)
    print decimal_to_binary(8)

def test_convert_base():
    print convert_base(10, 8)
    print convert_base(1211, 16)


def test_infix_to_postfix():
    print infix_to_postfix("a * b + c * ( e - f )")
    print infix_to_postfix("a + b + c")
    print infix_to_postfix("a * b + c * d")
    print infix_to_postfix("( a + b ) * c - ( d - e ) * ( f + g )")
    print infix_to_postfix("( A + B ) * ( C + D )")

def test_postfix_result():
    print postfix_result('7 8 + 3 2 + /')
    print postfix_result('17 10 + 3 * 9 /')

if __name__ == '__main__':
    test_postfix_result()
