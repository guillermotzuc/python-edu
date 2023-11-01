import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 7.5, 100)
y = []

for i in x:
    y.append(1000 / (np.pi * (i**2)))

c = []
for i in x:
    h = 1000 / (np.pi * (i**2))
    c.append(2 * np.pi * i * h + 2 * np.pi * (i**2))

minimo = np.min(c)
for i in range(len(x)):
    if c[i] == minimo:
        punto = [x[i], y[i]]

plt.figure()
plt.plot(x, y, color="k")
plt.scatter(punto[0], punto[1], color="k", linewidths=5)
plt.xlabel("r (radio)")
plt.ylabel("h (altura)")
plt.title(
    "Combinaciones (radio, altura) de las latas de conserva de un Litro de volumen"
)
plt.figure()
plt.plot(x, c, color="k")
plt.scatter(punto[0], minimo, color="k", linewidths=5)
plt.xlabel("radio")
plt.ylabel("coste de las latas de conserva")
plt.title("Coste de las latas de conserva de un litro en funcion del radio de su base")
plt.show()
