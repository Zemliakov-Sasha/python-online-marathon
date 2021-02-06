def findPermutation(n, p, q):
    r = []
    p1 = []

    for i in range(1, len(p) + 1):
        for j in range(0, len(p)):
            if i == p[j]:
                p1.append(j + 1)
    for i in range(0, n):
        r.append(p1[q[i]-1])
    return r
