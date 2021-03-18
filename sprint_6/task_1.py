import json


def find(file, key):
    res = []
    myfile = open(file, mode="r", encoding="utf_8")
    users = json.load(myfile)
    for user in users:
        keys = list(iter(user))
        if key not in keys:
            for k in keys:
                if user[k] != str(user[k]) and user[k] != list(user[k]) and k != key:
                    val = user[k]
                    if val[key] != str(val[key]):
                        for pas in val[key]:
                            if pas not in res:
                                res.append(pas)
                    else:
                        if val[key] not in res:
                            res.append(val[key])
        else:
            if user[key] != str(user[key]):
                for pas in user[key]:
                    if pas not in res:
                        res.append(pas)
            else:
                if user[key] not in res:
                    res.append(user[key])
    return res



print(find("Sprint_6_task_1.json", "password"))  # returns["pass_1", "qwerty"]
