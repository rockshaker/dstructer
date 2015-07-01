from example import is_brackets_blanced


def test_is_brackets_blanced():
    print is_brackets_blanced('((()))')
    print is_brackets_blanced('(())))')
    print is_brackets_blanced('((')
    print is_brackets_blanced('))')
    print is_brackets_blanced('{{([][])}()}')
    print is_brackets_blanced('[{()]')


if __name__ == '__main__':
    test_is_brackets_blanced()
