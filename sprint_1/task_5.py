def toPostFixExpression(e):
    postEx = []
    stackList = [""]
    nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "20"]
    k1 = ["+", "-"]
    k2 = ["*", "/"]
    for sym in e:
        for n in nums:
            if sym == n:
                postEx.append(sym)
        for n in k1:
            if sym == n:
                stackList.append(sym)
        for n in k2:
            if sym == n:
                stackList.append(sym)
        if sym == "(":
            stackList.append(sym)
        if sym == ")":
            postEx.append(stackList.pop())
            stackList.pop()
    while stackList[-1] != '':
        postEx.append(stackList.pop())
    return postEx
