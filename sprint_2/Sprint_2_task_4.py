import re
def pretty_message(data):
    nData = re.findall(r"\S+", data)
    res = ''
    res1 = ''
    index = 1
    print(nData)
    for n in nData:
        ml = ''
        if n[-1] =='.':
            n = "." + n[:-1]

        while len(ml) != 4:
            ml += n[len(n)-index]
            k1 = len(n)-2*len(ml)
            k2 = len(n)-len(ml)
            if ml[::-1] == n[k1:k2]:
                reg = r"(?:" + ml[::-1] + ")+"
                res1 = re.sub(reg, ml[::-1], n)
                if res1[0] == ".":
                    res1 = res1[1:] + "."
                res += res1 + " "
                ml = ''
                break
            index += 1
        if len(ml) != 0:
            res += n + " "
        index = 1
    return res[:-1]


data = "Thisssssssss isisisis echooooooo stringggg. Replaceaceaceace repeatedededed groupssss of symbolssss"
print(pretty_message(data))
