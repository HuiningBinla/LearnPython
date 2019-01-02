def print_line(char, times):
    """打印分隔线

    :param char:分隔线使用的分隔符
    :param times: 分隔符重读的次数
    """
    print(char * times)


def print_lines(char, times):
    """打印多行分隔线

    :param char:分隔线使用的分隔符
    :param times:分隔线重复的次数
    """
    row = 0

    while row < 5:
        print_line(char, times)

        row += 1

name = "菜鸟也疯狂"
# print("小鸟要疯狂")