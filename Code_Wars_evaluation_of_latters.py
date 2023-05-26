

def are_you_playing_banjo(name: str) -> str:
    positive_answer = ' plays banjo'
    negative_answer = ' does not play banjo'
#     if 'r' or 'R' in name[0]:  # Этот вариант не рабочий, см объяснение снизу. !
#         name = name + positive_answer
#     else:
#         name = name + negaive_answer
    name = name + \
        positive_answer if name[0].lower(
        ) == 'r' else name + negative_answer  # в одну строку, тернарный оператор

    return print(name)


if __name__ == '__main__':
    are_you_playing_banjo(input('Enter your name '))

# # if 'r' or 'R' in name[0]: - тут косяк в том что, Питон считает if 'r' or, что 'r' всегда
# True т.к. это не пустая строка.
# При таком написании нужно сделать так
# для python if ('r' это True) or ('R' in name[0]) этот кусок
# или
# if 'r' in name[0] or 'R' in name[0]:
# или
# def are_you_playing_banjo(name: str) -> str:
#     positive_answer = ' plays banjo'
#     negative_answer = ' does not play banjo'
#     if name[0] in 'rR':
#         name = name + positive_answer
#     else:
#         name = name + negative_answer
#
#     return print(name)

# самый простой вариант тут имхо if name[0].lower() == 'r':



