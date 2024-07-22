import matplotlib.pyplot as plt
import math

def simpson_1_3(func, a, b, n):
    if n % 2 != 0:
        raise ValueError("El número de intervalos (n) debe ser par.")

    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    y = [func(xi) for xi in x]

    integral = y[0] + y[-1] + 4 * sum(y[i] for i in range(1, n, 2)) + 2 * sum(y[i] for i in range(2, n, 2))
    integral *= h / 3

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

# Pedir datos al usuario
try:
    # Solicita la función al usuario
    funcion_str = input("Introduce la función f(x) en formato sin math. (por ejemplo, 'x**2'): \n\n")
    
    # Prepara la función lambda reemplazando nombres de funciones
    funcion_str = "lambda x: " + funcion_str  # Prepara el formato lambda
    
# Convierte la cadena en una función lambda
    funcion =  eval(funcion_str, {"math": math})

    # Solicita los límites y el número de intervalos al usuario
    a = float(input("Introduce el límite inferior de integración (a): "))
    b = float(input("Introduce el límite superior de integración (b): "))
    n = int(input("Introduce el número de intervalos (n, debe ser par): "))

    # Calcula la integral usando el Método de Simpson 1/3
    resultado = simpson_1_3(funcion, a, b, n)
    print(f"Resultado de la integral: {resultado}")

    # Graficar la función
    plot_function(funcion, a, b)

except Exception as e:
    print(f"Error: {e}")