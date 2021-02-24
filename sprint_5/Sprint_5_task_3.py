import re

def valid_email(val):
    try:
        res = re.fullmatch(r"[a-z]+@[a-z]+\.[a-z]+\.[a-z]+", val)
        if res:
            return "Email is valid"
        else:
            raise ValueError
    except ValueError:
        return "Email is not valid"

print(valid_email("probaggdf@gmail.hhh.com"))