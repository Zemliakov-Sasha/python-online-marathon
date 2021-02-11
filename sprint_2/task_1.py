def double_string(data):
    res = []
    for s in set(data):
        for d in data:
            st = d.find(s)
            if st != -1 and len(s) == len(d)/2:
                if d in res:
                    if d[:len(d)//2] != d[len(d)//2:]:
                        res.remove(d)
                res.append(d)

    return len(res)
