import numpy as np
import matplotlib.pyplot as plt


def gradiente_f(r):
    return -2000 / (r**2) + 4 * np.pi * r


def descenso_gradiente(r0=10, iteraciones=5000, alpha=0.1):
    valores_r = []
    r1 = r0 - alpha * gradiente_f(r0)

    for i in range(iteraciones):
        print(r1)
        valores_r.append(r1)
        r1 = r1 - alpha * gradiente_f(r1)

    h = 1000 / (np.pi * r1**2)
    plt.plot(valores_r)
    plt.title("Valores de r con alpha=" + str(alpha))
    plt.xlabel("Iteraciones")
    plt.ylabel("r")
    plt.show()
    return (r1, h)


optimo = descenso_gradiente(r0=10, iteraciones=5000, alpha=0.0001)
print(optimo)
