def day_of_week(num):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    try:
        num = int(num)
        if num not in range(1, 8):
            raise ValueError
        return days[num - 1]
    except IndexError:
        return "There is no such day of the week! Please try again."
    except ValueError:
        return "You did not enter a number! Please try again."




day_of_week(2)      # output:   "Tuesday"
day_of_week(11)    # output:  "There is no such day of the week! Please try again."
day_of_week("Monday")    # output:   "You did not enter a number! Please try again."