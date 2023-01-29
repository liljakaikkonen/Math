
import math

def compute_derivate(x):
    return math.cos(float(x))

def ask_number():
    return input("syötä luku (Farid=lopetus): ")


if __name__ == '__main__':
    x=ask_number()
    while x != "Farid":
        print(compute_derivate(x))
        x = ask_number()




