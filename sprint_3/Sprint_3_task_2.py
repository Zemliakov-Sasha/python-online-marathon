def create(arg):
    """This function return anonymous function
    that checks if the argument of function is
    equals to the argument of outer function"""
    return lambda val: val == arg

tom = create("pass_for_Tom")("pass_for_Tom")

