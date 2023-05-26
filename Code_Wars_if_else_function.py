'''Grade book
Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

Numerical Score  Letter Grade
90 <= score <= 100  'A'
80 <= score < 90  'B'
70 <= score < 80  'C'
60 <= score < 70  'D'
0 <= score < 60  'F'
Tested values are all between 0 and 100. Theres is no need to check for negative values or values greater than 100.'''


def get_grade(s1: str, s2: str, s3: str) -> str:
    s_out_1 = int(s1)  # covert from str to int
    s_out_2 = int(s2)
    s_out_3 = int(s3)
    s_total = (s_out_1 + s_out_2 + s_out_3) / 3  # calculate ariphmetic meaning
    if 90 <= s_total <= 100:  # check conditions for the privious calculation
        s_total = 'A'
    elif 80 <= s_total < 90:
        s_total = 'B'
    elif 70 <= s_total < 80:
        s_total = 'C'
    elif 60 <= s_total < 70:
        s_total = 'D'
    elif 0 <= s_total < 60:
        s_total = 'F'

    return print(s_total)  # return the result on the screen


if name == 'main':  # checking work of the function
    get_grade('100', '100', '50')
