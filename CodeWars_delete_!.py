# Remove an exclamation mark from the end of a string. For a beginner kata,
# you can assume that the input data is always a string, no need to verify it.


# Examples
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"
# remove("!Hi!") == "!Hi"

def string(x: str) -> str:
    length = len(x)

    if x[length - 1] == '!':
        result = x[:length - 1]
    else:
        result = x

    return print(result)


if '__main__' == __name__:
    string(input('Enter any string: '))
