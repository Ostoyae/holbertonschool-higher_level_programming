#!/use/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str:
        return None
    rome = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100, 'D': 500,
            'M': 1000}
    ls = list(roman_string)
    num = 0

    for n in ls:
        num += rome.get(n)

    return num
