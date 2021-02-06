def studying_hours(a):
    mlist = list(a)
    maxCom = []
    mc = 1
    for i in range(0, len(mlist)-1):
        if mlist[i] <= mlist[i+1]:
            mc += 1
        elif mlist[i] > mlist[i+1]:
            maxCom.append(mc)
            mc = 1
        if mc == len(mlist):
            maxCom.append(mc)

    return max((maxCom))
