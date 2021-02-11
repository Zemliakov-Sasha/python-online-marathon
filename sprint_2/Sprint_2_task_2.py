def morse_number (number):
    morse = ""
    morNum = ""
    n = "6789"
    for num in number:
        if num not in n:
            for i in range(int(num)):
                morNum += "."
            for i in range(5 - len(morNum)):
                morNum += '-'
        else:
            k = 10 - int(num)
            for i in range(5-k):
                morNum += '-'
            for i in range(5 - len(morNum)):
                morNum += '.'
        morse += morNum + ' '
        morNum = ''
    return morse


print(morse_number("295"))