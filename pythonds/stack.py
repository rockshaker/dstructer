class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


def is_brackets_blanced(brackets):
    """
    Whether the brackets are pairs
    :param brackets: brackets string
    :return: True or False
    """
    blanced = True
    index = 0
    s = Stack()
    b_left = ['(', '[', '{']
    mapping_num_dict = {'(': 1,
                        ')': 1,
                        '[': 2,
                        ']': 2,
                        '{': 3,
                        '}': 3
                        }
    while index < len(brackets) and blanced:
        if brackets[index] in b_left:
            s.push(brackets[index])
        else:
            if s.isEmpty():
                blanced = False
            else:
                if mapping_num_dict[s.peek()] == mapping_num_dict[brackets[index]]:
                    s.pop()
                else:
                    blanced = False
        index += 1

    return blanced and s.isEmpty()


def decimal_to_binary(num):
    """
    Convert decimal number to binary
    :param num: The raw decimal number
    :return: the binary number
    """
    s = Stack()
    binary_str = ''
    while num != 0:
        rem = num % 2
        s.push(rem)
        num //= 2

    while not s.isEmpty():
        binary_str += str(s.pop())

    return binary_str


def convert_base(num, base):
    """
    Convert decimal number to base number, such as 8 or 16
    :param num: The raw decimal number
    :return: the result number
    """
    digit = '0123456789abcdef'
    s = Stack()
    binary_str = ''
    while num != 0:
        rem = num % base
        s.push(rem)
        num //= base

    while not s.isEmpty():
        binary_str += str(digit[s.pop()])

    return binary_str


def infix_to_postfix(expr):
    """
    Convert the infix expression to postfix one
    :param expr: raw infix expression
    :return: result: the converted postfix expression
    """
    prec = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3, ')': 3}
    index = 0
    s = Stack()
    l = []
    while index < len(expr):
        # blank " "
        if expr[index] == ' ':
            index += 1
            continue
        # [*, /, +, -, (, )]
        if expr[index] in prec.keys():
            # stack is empty or "("
            if s.isEmpty() or expr[index] == '(':
                s.push(expr[index])
            else:
                # ")"
                if expr[index] == ')':
                    # Pop all the element up of "(" and append to the list
                    while s.peek() != '(':
                        l.append(s.pop())
                    s.pop()  # Pop "("
                elif not prec[expr[index]] > prec[s.peek()] and s.peek() != '(':
                    l.append(s.pop())
                    s.push(expr[index])
                # Push "(" or the prec of expr[index] lower than s.peek()'s
                else:
                    s.push(expr[index])
        # [abc....012...]
        else:
            l.append(expr[index])
        index += 1

    # Append all remaining operators in stack
    while not s.isEmpty():
        l.append(s.pop())

    result = ''.join(l)
    return result


def do_math(op, opr1, opr2):
    opr1 = int(opr1)
    opr2 = int(opr2)
    if op == '*':
        result = opr1*opr2
    elif op == '/':
        result = opr1/opr2
    elif op == '+':
        result = opr1 + opr2
    else:
        result = opr1 - opr2
    return result


def postfix_result(expr):
    """
    Get the result of postfix expression
    :param expr: postfix expression
    :return: result
    """
    expr_list = expr.split()
    operators = ['*', '/', '+', '-']
    s = Stack()
    index = 0
    while index < len(expr_list):
        if not expr_list[index] in operators:
            s.push(expr_list[index])
        else:
            opr2 = s.pop()
            opr1 = s.pop()
            temp = do_math(expr_list[index], opr1, opr2)
            s.push(temp)
        index += 1

    result = s.pop()
    return result