import re
def max_population(data):
    sData = []
    pData= []
    max = 0
    index = 0
    for d in data:
        reg = re.findall(r"\w+_\w+", d)
        sData += reg
        reg = re.findall(r"\d{5}", d)
        pData += reg
        for i in range(len(pData)):
            pData[i] = int(pData[i])
    for i in range(len(pData)):
        if pData[i] > max:
            max = pData[i]
            index = i
    return sData[index+1], max


data = ["id,name,poppulation,is_capital",
"3024,eu_kyiv,24834,y",
"3025,eu_volynia,20231,n",
"3026,eu_galych,23745,n",
"4892,me_medina,18038,n",
"4401,af_cairo,18946,y",
"4700,me_tabriz,13421,n",
"4899,me_bagdad,22723,y",
"6600,af_zulu,09720,n"]

print(max_population(data))