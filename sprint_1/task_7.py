def Cipher_Zeroes(N):
    point = 0
    lst = ["0", "6", "9"]
    for num in N:
        if num == "8":
            point += 2
        for i in lst:
            if num == i:
                point += 1
    if point % 2 == 0:
        point -= 1
    else:
        point += 1
    if point == -1:
        return 0
    else:
        return int(str(bin(point))[2:])
