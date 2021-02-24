def check_odd_even(num):
    try:
        num = int(num)
        res = "even" if num % 2 == 0 else "odd"
        return f"Entered number is {res}"
    except:
        return "You entered incorrect data. Please try again."


check_odd_even(24)
