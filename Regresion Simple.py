import matplotlib.pyplot as plt
import statistics

def plot_regresion(x, y, y_pred):
    plt.scatter(x, y, color='blue', label='Datos registrados')
    plt.plot(x, y_pred, color='red', label='Grafica de regresion')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Regresion Simple')
    plt.legend()
    plt.grid(True)
    plt.show()
    
def calcular_regresion_simple(x, y):
    n = len(x)
    mean_x = statistics.mean(x)
    mean_y = statistics.mean(y)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))
    sum_x2 = sum(xi**2 for xi in x)
    a = (sum_xy - n * mean_x * mean_y) / (sum_x2 - n * mean_x**2)
    b = mean_y - a * mean_x 
    y_pred = [a * xi + b for xi in x]
    ss_total = sum((yi - mean_y)**2 for yi in y)
    ss_residual = sum((yi - y_predi)**2 for yi, y_predi in zip(y, y_pred))
    r2 = 1 - (ss_residual / ss_total)
    
    return a, b, r2, y_pred

try:
    print("Al ingresar datos Separar por un aguion bajo _ ")
    print("Por ejemplo:  1_2_3")
    lista_x = list(map(float, input("Ingrese los valores independientes (x):  ").split('_')))
    lista_y = list(map(float, input("Ingrese los valores dependientes (y):  ").split('_')))

    if len(lista_x) != len(lista_y):
        raise ValueError("Cantidad de Valores de 'X' y 'Y' deben iguales")

    a, b, r2, regresion = calcular_regresion_simple(lista_x, lista_y)
    plot_regresion(lista_x, lista_y, regresion)
    print("\n\n\n")
    print(f"Coeficiente de determinación: {r2:.4f}\n")
    
    if r2 > 0.7:
        print("El modelo tiene un buen ajuste.")
    elif r2 > 0.5:
        print("El modelo tiene un ajuste moderado.")
    else:
        print("El modelo tiene un ajuste bajo.")
        
        
    print(f"\n\nModelo de regresión lineal simple:\n")
    print(f"y = {a:.4f} * x + {b:.4f}\n\n")        

    

except Exception as e:
    print(f"Error: {e}")
