import matplotlib.pyplot as plt
import math

def Euler(f, xo, yo, h, n):
    las_X = [xo] #Guardamos en lista de x
    las_Y = [yo] #Guardamos en lista de y

    for _ in range(n):
        x = las_X[-1] # ultimo valor de x para luego a evaluar
        y = las_Y[-1] # ultimo valor de y para luego a evaluar
        nueva_y = y + h * f(x, y)
        nueva_x = x + h

        las_X.append(nueva_x) #añadimos a la lista x
        las_Y.append(nueva_y) #añadimos a la lista y

    return las_X, las_Y

# datos del usuario
try:
    funcion = input("Ingrese una función f(x, y): ")
    funcion = "lambda x, y: " + funcion
    f = eval(funcion, {"math": math})
    
    xo = float(input("Ingrese el valor (xo): "))
    yo = float(input("Ingrese el valor (yo): "))
    xn = float(input("Ingrese el valor (xn): "))
    n = int(input("Ingrese el número de iteraciones (n): "))
    h = (xn - xo) / n

    las_X, las_Y = Euler(f, xo, yo, h, n)

    # Imprimir
    for x, y in zip(las_X, las_Y):
        print(f'x = {x:.4f}, y = {y:.4f}')

    # Graficar los resultados
    plt.plot(las_X, las_Y, marker='o')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Euler')
    plt.grid(True)
    plt.show()

except Exception as e:
    print(f"Error: {e}")