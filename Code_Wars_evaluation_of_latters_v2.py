def are_you_playing_banjo(name: str) -> str:
    positive_answer = ' plays banjo'
    negaive_answer = ' does not play banjo'
    if name[0] in 'rR':
        name = name + positive_answer
    else:
        name = name + negaive_answer

    return print(name)


if __name__ == '__main__':
    are_you_playing_banjo(input('Enter your name '))
