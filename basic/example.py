from stack import Stack


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
        binary_str += s.pop()

    return binary_str
