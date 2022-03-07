dict_first_number = {
    1: 'один',
    2: 'два',
    3: 'три',
    4: 'четыре',
    5: 'пять',
    6: 'шесть',
    7: 'семь',
    8: 'восемь',
    9: 'девять',
    10: 'десять',
    11: 'одиннадцать',
    12: 'двенадцать',
    13: 'тринадцать',
    14: 'четырнадцать',
    15: 'пятнадцать',
    16: 'шестнадцать',
    17: 'семнадцать',
    18: 'восемнадцать',
    19: 'девятнадцать',
}

dict_decades = {
    20: 'двадцать',
    30: 'тридцать',
    40: 'сорок',
    50: 'пятдесят',
    60: 'шестьдесят',
    70: 'семьдесят',
    80: 'восемьдесят',
    90: 'девяносто',
}

dict_hundreds = {
    100: 'сто',
    200: 'двести',
    300: 'триста',
    400: 'четыреста',
    500: 'пятьсот',
    600: 'шестьсот',
    700: 'семьсот',
    800: 'восемьсот',
    900: 'девятьсот',
}

dict_other = {
    1: '',
    1000: ('тысяча', 'тысячи', 'тысяч'),
    1000000: ('миллион', 'миллиона', 'миллионов'),
    1000000000: ('миллиард', 'миллиарда', 'миллиардов'),
    1000000000000: ('триллиард', 'триллиарда', 'триллиардов')
}


def number_to_string(number):
    result = ''
    length = len(str(number)) // 3 * 3
    for digit in range(length - 1, 0, -3):
        temp = int(str(number)[length - digit:length - digit + 3]) * 10 ** (digit - 2)
        result += ' ' + translate_part(temp)
    return result


def translate_part(number):
    result = ''
    number = int(number)
    if number // 100 > 0:
        result += dict_hundreds[number - number % 100]
    if number % 100 < 20:
        result += dict_first_number[number % 100]
    else:
        result += ' ' + dict_decades[number // 10 % 10 * 10]
        if number % 10 > 0:
            result += ' ' + dict_first_number[number % 10]
    return result
