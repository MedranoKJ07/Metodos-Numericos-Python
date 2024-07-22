import matplotlib.pyplot as plt
import math

def Metodo_RungeKutta4(f, xo, yo, h, n):
    x_eje = [xo]
    y_eje = [yo]

    for i in range(n):
        x = x_eje[-1]
        y = y_eje[-1]

        k1 = f(x, y)
        k2 = f(x + h/2, y + h/2 * k1)
        k3 = f(x + h/2, y + h/2 * k2)
        k4 = f(x + h, y + h * k3)

        y_new = y + (h/6) * (k1 + 2*k2 + 2*k3 + k4)
        x_new = x + h

        x_eje.append(x_new)
        y_eje.append(y_new)

        print(f"Iteración {i + 1}:")
        print(f"  k1 = {k1:.6f}")
        print(f"  k2 = {k2:.6f}")
        print(f"  k3 = {k3:.6f}")
        print(f"  k4 = {k4:.6f}")
        print(f"  x = {x_new:.4f}, y = {y_new:.6f}")

    return x_eje, y_eje


try:
    funcion_str = input("Introduce la función f(x, y): \n\n")
    funcion_str = "lambda x, y: " + funcion_str  
    
    f = eval(funcion_str, {"math": math})
    
    xo = float(input("Introduce el valor inicial de x (xo): "))
    yo = float(input("Introduce el valor inicial de y (yo): "))
    xn = float(input("Introduce el valor final de x (xn): "))
    n = int(input("Introduce el número de nodos (n): "))
    h = (xn - xo) / n

    x_eje, y_eje = Metodo_RungeKutta4(f, xo, yo, h, n)
    
    print("\nResultados finales:")
    for x, y in zip(x_eje, y_eje):
            print(f'x = {x:.4f}, y = {y:.6f}')
    
    plt.plot(x_eje, y_eje, marker='o')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Método de Runge-Kutta de Cuarto Orden')
    plt.grid(True)
    plt.show()

except Exception as e:
    print(f"Error: {e}")
