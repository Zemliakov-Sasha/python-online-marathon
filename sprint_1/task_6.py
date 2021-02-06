def order(a):
    asc = 0
    des = 0
    i = 0
    for n in a:
        if n < a[i + 1]:
            asc += 1
        if n > a[i+1]:
            des += 1
        i += 1
        if n == a[-2]:
            break
    if asc + 1 == len(a):
        return "ascending"
    elif des + 1 == len(a):
        return "descending"
    else:
        return "not sorted"
