#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str:
        return 0
    rome = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100, 'D': 500,
            'M': 1000, 'IV': 4, 'IX': 10,
            'XL': 40, 'XC': 90, 'CD': 400,
            'CM': 900}
    ls = list(reversed(roman_string.upper()))
    pair = ""
    num = 0
    for i, n in enumerate(ls):
        if n in list(rome):
            if i - 1 >= 0 :
                if ls[i - 1] == 'V' and num <= 4:
                    num -= 1
                elif ls[i - 1] == 'X' and num <= 10:
                    num -= 1 
                elif (ls[i - 1] == 'L' or ls[i - 1] == 'C') and num <= 40:
                    num +=  10
                elif (ls[i - 1] == 'D' or ls[i - 1] == 'M') and num <= 400:
                    num += 100
                else:
                    num += rome.get(n)
            else:
                num += rome.get(n)
        else:
            continue

    return num
