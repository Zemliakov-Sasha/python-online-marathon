import cmath
def solve_quadric_equation(a, b, c):
    try:
        D = b**2 - 4*a*c
        x1 = (-b - cmath.sqrt(D))/(2*a)
        x2 = (-b + cmath.sqrt(D)) / (2 * a)
        return f"The solution are x1={x1} and x2={x2}"
    except TypeError:
        return "Could not convert string to float"
    except ZeroDivisionError:
        return "Zero Division Error"


print(solve_quadric_equation(1, 3, -4))
print(solve_quadric_equation(1, 4, 5))
