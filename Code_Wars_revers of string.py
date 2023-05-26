# Convert number to reversed array of digits
# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
#
# Example(Input => Output):
# 35231 => [1,3,2,5,3]
# 0 => [0]


def digitize(n: str) -> list[int]:
    counter = 0
    # обрати внимание, что функция len измеряет длину строки и начинает с 1 а не с 0
    lenth = len(n) - 1

    # создаём список, каждый псико отедльной строчкой чтобы у них была "своя" коробочка
    string = list(n)
    list_numbers = list(n)

    while counter <= lenth:
        # присваиваем первому индексу list_numbers, последний индекс string  и далее по порядку от послденего до 0
        list_numbers[counter] = string[lenth - counter]

        counter += 1
    counter = 0  # после использования в цикле While обнулсяем счётчки, чтобы использовать в цикле for. counter специально смещено так , чтобы выолнялся только после завершения всего цикла while
    # для каждого элемента list_numbers мы конвертируем в целое число и присваиваем в тот же цикл (т.к. по заданию на выхоже должен быть список из int)
    for i in list_numbers:

        list_numbers[counter] = int(i)
        counter += 1

    return print(list_numbers)


if __name__ == '__main__':
    digitize(input('Enter o fnumber: '))
