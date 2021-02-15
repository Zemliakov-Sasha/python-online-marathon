import re


def create_account(user_name, password, secret_words):
    """This function should return inner function check"""

    lst_of_reg = ["[\W_]", "[A-Z]", "[a-z]", "\d"]
    an = 0
    for reg in lst_of_reg:
        regx = r"" + reg
        a = 0 if re.search(regx, password) else 1
        an += a
    if an != 0 or len(password) < 6:
        return ValueError
    else:
        def check(chPassword, chSecret_words):
            """The function compares the values of
            its arguments with password and secret_words"""

            res = []
            if len(secret_words) != len(chSecret_words) or chPassword != password:
                return False
#           res = [True if secret_words.count(se) >= chSecret_words.count(se) else False for se in secret_words]
#           res = ([True if Se == ch else None for ch in chSecret_words for Se in secret_words])
            for se in secret_words:
                print("---", se)
                for ch in chSecret_words:
                    print(ch)
                    if ch == se:
                        res.append(True)
                        chSecret_words.remove(ch)
                        print(res)
                        break
            return True if res.count(True) >= len(secret_words)-1 else False
        return check



tom = create_account("Tom", "Qwerty1_", ['1', '2', '4'])
check1 = tom("Qwerty1_", ['3', '1', '3'])
check2 = tom("Qwerty1_", ['3', '1', '2'])
check3 = tom("Qwerty1_", ['3', '1', '1'])
check4 = tom("Qwerty1_", ['2', '1', '3'])

print(check1)
print(check2)
print(check3)
print(check4)