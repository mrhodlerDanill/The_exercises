# # Usually when you buy something, you're asked whether your credit
# card number, phone number or answer to your most secret question
# is still correct. However, since someone could look over your shoulder,
# you don't want that shown on your screen. Instead, we mask it.
# #
# # Your task is to write a function maskify, which changes all but
# the last four characters into '#'.
# maskify("4556364607935616") == "############5616"
# maskify(     "64607935616") ==      "#######5616"
# maskify(               "1") ==                "1"
# maskify(                "") ==                 ""


def maskify(cc: str) -> str:
    list_str = list(cc)  # convert string into list to we can iterate elements
    if len(list_str) <= 4:  # the first condition

        # use method .join to convert the list into a string
        string_var = ''.join(list_str)

    else:  # the second condition
        i = 0  # counter
        # deduct 5 from the length of the list to the last four numbers will be without changes
        while i <= len(list_str) - 5:
            list_str[i] = '#'  # replace i-element on #
            i += 1  # increase counter on 1

    # use method .join to convert the list into a string
    string_var = ''.join(list_str)

    return print(string_var)  # return string and print result


if __name__ == '__main__':  # checking of work of the function
    maskify('1234657567')
