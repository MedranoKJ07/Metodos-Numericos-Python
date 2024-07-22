import matplotlib.pyplot as plt
import math

def Metodo_Euler_Mejorado(f, xo, yo, h, n):
    x_eje = [xo]
    y_eje = [yo]

    for _ in range(n):
        x = x_eje[-1]  # Se extrae el último valor de x para luego evaluar
        y = y_eje[-1]  # Se extrae el último valor de y para luego evaluar

        # Paso de Euler
        f_actual = f(x, y)
        y_pred = y + h * f_actual
        
        # Paso de corrección
        f_pred = f(x + h, y_pred)
        y_corr = y + h / 2 * (f_actual + f_pred)

        x_new = x + h
        y_new = y_corr
        
        x_eje.append(x_new)
        y_eje.append(y_new)

    return x_eje, y_eje

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
    funcion = eval(funcion_str, {"math": math})
    # Solicita los valores iniciales y el número de nodos al usuario
    xo = float(input("Introduce el valor inicial de x (xo): "))
    yo = float(input("Introduce el valor inicial de y (yo): "))
    xn = float(input("Introduce el valor final de x (xn): "))
    n = int(input("Introduce el número de nodos (n): "))
    h = (xn - xo) / n

    # Calcula la solución usando el Método de Euler Mejorado
    x_eje, y_eje = Metodo_Euler_Mejorado(funcion, xo, yo, h, n)

    # Imprimir los resultados finales
    print("\nTabla de X, Y:")
    for x, y in zip(x_eje, y_eje):
        print(f'x = {x:.4f}, y = {y:.4f}')

    # Graficar los resultados
    plt.plot(x_eje, y_eje, marker='o')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Método de Euler Mejorado')
    plt.grid(True)
    plt.show()

except Exception as e:
    print(f"Error: {e}")
