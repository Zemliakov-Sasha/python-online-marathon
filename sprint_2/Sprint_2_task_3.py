import re
import math
def figure_perimetr(test1):
    textlookfor = r"\d:\d"
    pos = re.findall(textlookfor, test1)
    lst = []
    perimetr = 0
    for p in pos:
        lst.append(p.split(':'))
    m = lst[2]
    lst[2] = lst[3]
    lst[3] = m
    for i in range(4):
        if i == 3:
            perimetr += math.sqrt((int(lst[0][0]) - int(lst[i][0])) ** 2 + (int(lst[0][1]) - int(lst[i][1])) ** 2)
        else:
            perimetr += math.sqrt((int(lst[i+1][0])-int(lst[i][0]))**2 + (int(lst[i+1][1])-int(lst[i][1]))**2)
        print(lst)
    return perimetr

test1 = "#LB1:1#RB4:1#LT1:3#RT4:3"
print(figure_perimetr(test1))
