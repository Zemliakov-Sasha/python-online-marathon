class MyExcept(Exception):
    def __init__(self, text):
        self.text = text

def check_positive(num):
    try:
        num = float(num)
        if num >= 0 :
            return f"You input positive number: {num}"
        else:
            raise MyExcept(f"You input negative number: {num}. Try again.")
    except ValueError:
        return "Error type: ValueError!"
    except MyExcept as me:
        return me


check_positive (24) #output: "Ви ввели    додатне число: 24"
check_positive (-19) #output:      " Ви введете від'ємне число: -19. Спробуйте ще раз. "
check_positive ( " 38 " ) #output:    "Ви введете додатне число: 38"
check_positive ( "abc" ) #output:      " Тип помилки: ValueError! "