
import matplotlib.pyplot as plt
import math

def simpson_3_8(func, a, b, n):
    if n % 4 != 0:
        raise ValueError("El número de intervalos (n) debe ser divisible por 4.")
    
    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    y = [func(xi) for xi in x]
    
    integral = y[0] + y[-1] + 3 * sum(y[i] for i in range(1, n, 3)) + 3 * sum(y[i] for i in range(2, n, 3)) + 2 * sum(y[i] for i in range(3, n, 3))
    integral *= (3 * h / 8)
    
    return integral



def plot_function(func, a, b):
    x_vals = [a + i * (b - a) / 1000 for i in range(1001)]
    y_vals = [func(x) for x in x_vals]

    plt.plot(x_vals, y_vals, label="f(x)")
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Función f(x)')
    plt.grid(True)
    plt.legend()
    plt.show()

try:
    funcion_str = input("Introduce la función f(x): \n\n")
    funcion_str = "lambda x: " + funcion_str  
    
    funcion = eval(funcion_str, {"math": math})
    
    a = float(input("Introduce el límite inferior de integración (a): "))
    b = float(input("Introduce el límite superior de integración (b): "))
    n = int(input("Introduce el número de subintervalos (n, debe ser divisible por 4): "))

    resultado = simpson_3_8(funcion, a, b, n)
    print(f"Resultado de la integral: {resultado}")

    plot_function(funcion, a, b)

except Exception as e:
    print(f"Error: {e}")
