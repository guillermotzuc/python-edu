from Individuo import Individuo
from Poblacion import Poblacion

# Ejemplo de función objetivo con la que evaluar a los individuos.
def funcion_objetivo(x_0, x_1, x_2):
    f= x_0**2 + x_1**2 + x_2**2
    return(f)


if __name__ == "__main__":
    individuo = Individuo(
                    n_variables = 3,
                    limites_inf = [-1,2,0],
                    limites_sup = [4,10,20],
                    verbose     = True
                )
    # Ejemplo de función objetivo con la que evaluar a los individuos.
def funcion_objetivo(x_0, x_1, x_2):
    f= x_0**2 + x_1**2 + x_2**2
    return(f)

individuo.calcular_fitness(
    funcion_objetivo = funcion_objetivo,
    optimizacion     = "minimizar",
    verbose          = True
)

individuo.mutar(
    prob_mut         = 0.5,
    distribucion     = "uniforme",
    min_distribucion = -1,
    max_distribucion = 1,
    verbose          = True
)

poblacion = Poblacion(
                n_individuos = 3,
                n_variables  = 3,
                limites_inf  = [-5,-5,-5],
                limites_sup  = [5,5,5],
                verbose = True
            )

poblacion.mostrar_individuos(n=2)

def funcion_objetivo(x_0, x_1, x_2):
    f= x_0**2 + x_1**2 + x_2**2
    return(f)

poblacion.evaluar_poblacion(
    funcion_objetivo = funcion_objetivo,
    optimizacion     = "minimizar",
    verbose          = True
)

poblacion.seleccionar_individuo(
    n                = 2,
    return_indices   = True,
    metodo_seleccion = "tournament",
    verbose          = True
)