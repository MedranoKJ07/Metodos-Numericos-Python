import matplotlib.pyplot as plt 
import math

def RungeKutta3(f, xo, yo, h, n):
    x_lista = [xo]
    y_lista = [yo]

    for i in range(n):
        x = x_lista[-1]  # Se extrae el último valor de x para luego evaluar
        y = y_lista[-1]  # Se extrae el último valor de y para luego evaluar

        k = f(x, y)

        # Calculamos los valores intermediarios
        x_intermedio = x + (3/4) * h
        y_intermedio = y + (3/4) * k

        k2 = f(x_intermedio, y_intermedio)

        # Calculamos el nuevo valor de y usando la fórmula proporcionada
        y_new = y + (h/3) * (k + 2 * k2)
        x_new = x + h

        x_lista.append(x_new)
        y_lista.append(y_new)

    return x_lista, y_lista

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
    funcion_str = input("Introduce la función f(x, y) en formato sin math. (por ejemplo, 'x + y'): \n\n")
    
    # Prepara la función lambda reemplazando nombres de funciones
    funcion_str = "lambda x, y: " + funcion_str  # Prepara el formato lambda


    # Convierte la cadena en una función lambda
    funcion =  eval(funcion_str, {"math": math})
    # Solicita los valores iniciales y el número de nodos al usuario
    xo = float(input("Introduce el valor inicial de x (xo): "))
    yo = float(input("Introduce el valor inicial de y (yo): "))
    xn = float(input("Introduce el valor final de x (xn): "))
    n = int(input("Introduce el número de nodos (n): "))
    h = (xn - xo) / n

    # Calcula la solución usando el Método de Runge-Kutta de Tercer Orden Mejorado
    x_lista, y_lista = RungeKutta3(funcion, xo, yo, h, n)

    # Imprimir los resultados finales
    print("\nResultados finales:")
    for x, y in zip(x_lista, y_lista):
        print(f'x = {x:.4f}, y = {y:.6f}')

    # Graficar los resultados
    plt.plot(x_lista, y_lista, marker='o')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Método de Runge-Kutta de Tercer Orden')
    plt.grid(True)
    plt.show()

except Exception as e:
    print(f"Error: {e}")