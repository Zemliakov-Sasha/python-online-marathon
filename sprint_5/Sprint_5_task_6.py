class ToSmallNumberGroupError(Exception):
    def __init__(self, text):
        self.txt = text


def check_number_group(num):
    try:
        num = int(num)
        if num > 10:
            return f"Number of your group {num} is valid"
        else:
            raise ToSmallNumberGroupError("We obtain error:Number of your group can't be less than 10")
    except ValueError:
        return "You entered incorrect data. Please try again."
    except ToSmallNumberGroupError as tsndf:
        return tsndf



print(check_number_group("9"))
