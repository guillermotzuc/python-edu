################################################################################
#               CÓDIGO OPTIMIZACIÓN CON ALGORITMO GENÉTICO                     #
#                                                                              #
# This work by Joaquín Amat Rodrigo is licensed under a Creative Commons       #
# Attribution 4.0 International License.                                       #
################################################################################
# coding=utf-8

################################################################################
#                              CLASE INDIVIDUO                                 #
################################################################################
################################################################################
# LIBRERÍAS NECESARIAS
################################################################################
import numpy as np
import random
import warnings
import random
import copy
import pandas as pd
import time
from datetime import datetime

# Configuración warnings
################################################################################
import warnings
warnings.filterwarnings('ignore')

class Individuo:
    """
    Esta clase representa un individuo con unas características inicial definida
    por una combinación de valores numéricos aleatorios. El rango de posibles
    valores para cada variable puede estar acotado.
    
    Parameters
    ----------
    n_variables : `int`
        número de variables que definen al individuo.
        
    limites_inf : `list` or `numpy.ndarray`, optional
        límite inferior de cada variable. Si solo se quiere predefinir límites
        de alguna variable, emplear ``None``. Los ``None`` serán remplazados
        por el valor (-10**3). (default ``None``)
        
    limites_sup : `list` or `numpy.ndarray`, optional
        límite superior de cada variable. Si solo se quiere predefinir límites
        de alguna variable, emplear ``None``. Los ``None`` serán remplazados
        por el valor (+10**3). (default ``None``)

    verbose : `bool`, optional
        mostrar información del individuo creado. (default ``False``)

    Attributes
    ----------
    n_variables : `int`
        número de variables que definen al individuo.

    limites_inf : `list` or `numpy.ndarray`
        límite inferior de cada variable. Si solo se quiere predefinir límites
        de alguna variable, emplear ``None``. Los ``None`` serán remplazados por
        el valor (-10**3).

    limites_sup : `list` or `numpy.ndarray`
        límite superior de cada variable. Si solo se quiere predefinir límites
        de alguna variable, emplear ``None``. Los``None`` serán remplazados por
        el valor (+10**3).

    valor_variables : `numpy.ndarray`
        array con el valor de cada una de las variables.

    fitness : `float`
        valor de fitness del individuo.

    valor_funcion : `float`
        valor de la función objetivo para el individuo.

    Raises
    ------
    raise Exception
        si `limites_inf` es distinto de None y su longitud no coincide con
        `n_variables`.

    raise Exception
        si `limites_sup` es distinto de None y su longitud no coincide con
        `n_variables`.

    Examples
    --------
    Ejemplo creación individuo.

    >>> individuo = Individuo(
                        n_variables = 3,
                        limites_inf = [-1,2,0],
                        limites_sup = [4,10,20],
                        verbose     = True
                    )

    """
    
    def __init__(self, n_variables, limites_inf=None, limites_sup=None,
                 verbose=False):

        # Número de variables del individuo
        self.n_variables = n_variables
        # Límite inferior de cada variable
        self.limites_inf = limites_inf
        # Límite superior de cada variable
        self.limites_sup = limites_sup
        # Valor de las variables del individuo
        self.valor_variables = np.repeat(None, n_variables)
        # Fitness del individuo
        self.fitness = None
        # Valor de la función objetivo
        self.valor_funcion = None
        
        # CONVERSIONES DE TIPO INICIALES
        # ----------------------------------------------------------------------
        # Si limites_inf o limites_sup no son un array numpy, se convierten en
        # ello.
        if self.limites_inf is not None \
        and not isinstance(self.limites_inf, np.ndarray):
            self.limites_inf = np.array(self.limites_inf)

        if self.limites_sup is not None \
        and not isinstance(self.limites_sup,np.ndarray):
            self.limites_sup = np.array(self.limites_sup)
        
        # COMPROBACIONES INICIALES: EXCEPTIONS Y WARNINGS
        # ----------------------------------------------------------------------
        if self.limites_inf is not None \
        and len(self.limites_inf) != self.n_variables:
            raise Exception(
                "limites_inf debe tener un valor por cada variable. " +
                "Si para alguna variable no se quiere límite, emplear None. " +
                "Ejemplo: limites_inf = [10, None, 5]"
                )
        elif self.limites_sup is not None \
        and len(self.limites_sup) != self.n_variables:
            raise Exception(
                "limites_sup debe tener un valor por cada variable. " +
                "Si para alguna variable no se quiere límite, emplear None. " +
                "Ejemplo: limites_sup = [10, None, 5]"
                )
        elif (self.limites_inf is None) or (self.limites_sup is None):
            warnings.warn(
                "Es altamente recomendable indicar los límites dentro de los " + 
                "cuales debe buscarse la solución de cada variable. " + 
                "Por defecto se emplea [-10^3, 10^3]."
                )
        elif any(np.concatenate((self.limites_inf, self.limites_sup)) == None):
            warnings.warn(
                "Los límites empleados por defecto cuando no se han definido " +
                "son: [-10^3, 10^3]."
            )

        # COMPROBACIONES INICIALES: ACCIONES
        # ----------------------------------------------------------------------

        # Si no se especifica limites_inf, el valor mínimo que pueden tomar las 
        # variables es -10^3.
        if self.limites_inf is None:
            self.limites_inf = np.repeat(-10**3, self.n_variables)

        # Si no se especifica limites_sup, el valor máximo que pueden tomar las 
        # variables es 10^3.
        if self.limites_sup is None:
             self.limites_sup = np.repeat(+10**3, self.n_variables)
            
        # Si los límites no son nulos, se reemplazan aquellas posiciones None por
        # el valor por defecto -10^3 y 10^3.
        if self.limites_inf is not None:
            self.limites_inf[self.limites_inf == None] = -10**3
           
        if self.limites_sup is not None:
            self.limites_sup[self.limites_sup == None] = +10**3
        
        # BUCLE PARA ASIGNAR UN VALOR A CADA UNA DE LAS VARIABLES
        # ----------------------------------------------------------------------
        for i in np.arange(self.n_variables):
        # Para cada variable, se genera un valor aleatorio dentro del rango
        # permitido para esa variable.
            self.valor_variables[i] = random.uniform(
                                        self.limites_inf[i],
                                        self.limites_sup[i]
                                      )

        # INFORMACIÓN DEL PROCESO (VERBOSE)
        # ----------------------------------------------------------------------
        if verbose:
            print("Nuevo individuo creado")
            print("----------------------")
            print("Valor variables: " + str(self.valor_variables))
            print("Valor función objetivo: " + str(self.valor_funcion))
            print("Fitness: " + str(self.fitness))
            print("Límites inferiores de cada variable: " \
                  + str(self.limites_inf))
            print("Límites superiores de cada variable: " \
                  + str(self.limites_sup))
            print("")

    def __repr__(self):
        """
        Información que se muestra cuando se imprime un objeto individuo.

        """

        texto = "Individuo" \
                + "\n" \
                + "---------" \
                + "\n" \
                + "Valor variables: " + str(self.valor_variables) \
                + "\n" \
                + "Valor función objetivo: " + str(self.valor_funcion) \
                + "\n" \
                + "Fitness: " + str(self.fitness) \
                + "\n" \
                + "Límites inferiores de cada variable: " \
                + str(self.limites_inf) \
                + "\n" \
                + "Límites superiores de cada variable: " \
                + str(self.limites_sup) \
                + "\n"

        return(texto)

    def calcular_fitness(self, funcion_objetivo, optimizacion, verbose = False):
        """
        Este método obtiene el fitness del individuo calculando el valor que toma
        la función objetivo con el valor de sus variables.
        
        Parameters
        ----------
        funcion_objetivo : `function`
            función que se quiere optimizar.

        optimizacion : {'maximizar', 'minimizar'}
            ver notas para más información.

        verbose : `bool`, optional
            mostrar información del proceso por pantalla. (default ``False``)
          
        Raises
        ------
        raise Exception
            si el argumento `optimizacion` es distinto de 'maximizar' o
            'minimizar'

        Notes
        -----

        Cada individuo de la población debe ser evaluado para cuantificar su
        bondad como solución al problema, a esta cuantificación se le llama
        fitness.
       
        Dependiendo de si se trata de un problema de maximización o minimización,
        la relación del fitness con la función objetivo :math:`f` puede ser:

        - Maximización: el individuo tiene mayor fitness cuanto mayor es el valor
         de la función objetivo :math:`f(individuo)`.

        - Minimización: el individuo tiene mayor fitness cuanto menor es el valor
         de la función objetivo :math:`f(individuo)`, o lo que es lo mismo,
         cuanto mayor es el valor de la función objetivo, menor el fitness.
         El algoritmo genético selecciona los individuos de mayor fitness, por 
         lo que, para problemas de minimización, el fitness puede calcularse como
         :math:`−f(individuo)` o también :math:`\frac{1}{1+f(individuo)}`.

        Examples
        --------
        Ejemplo evaluar individuo con una función objetivo.

        >>> individuo = Individuo(
                        n_variables = 3,
                        limites_inf = [-1,2,0],
                        limites_sup = [4,10,20],
                        verbose     = True
                    )

        >>> def funcion_objetivo(x_0, x_1, x_2):
                f= x_0**2 + x_1**2 + x_2**2
                return(f)

        >>> individuo.calcular_fitness(
                funcion_objetivo = funcion_objetivo,
                optimizacion     = "minimizar",
                verbose          = True
            )

        """

        # COMPROBACIONES INICIALES: EXCEPTIONS Y WARNINGS
        # ----------------------------------------------------------------------
        if not optimizacion in ["maximizar", "minimizar"]:
            raise Exception(
                "El argumento optimizacion debe ser: 'maximizar' o 'minimizar'"
                )

        # EVALUACIÓN DE LA FUNCIÓN OBJETIVO CON LAS VARIABLES DEL INDIVIDUO Y
        # CÁLCULO DEL FITNESS
        # ----------------------------------------------------------------------
        self.valor_funcion = funcion_objetivo(*self.valor_variables)
        if optimizacion == "maximizar":
            self.fitness = self.valor_funcion
        elif optimizacion == "minimizar":
            self.fitness = -self.valor_funcion

        # INFORMACIÓN DEL PROCESO (VERBOSE)
        # ----------------------------------------------------------------------
        if verbose:
            print("El individuo ha sido evaluado")
            print("-----------------------------")
            print("Valor función objetivo: " + str(self.valor_funcion))
            print("Fitness: " + str(self.fitness))
            print("")

    def mutar(self, prob_mut=0.01, distribucion="uniforme", media_distribucion=1,
              sd_distribucion=1, min_distribucion=-1, max_distribucion=1,
              verbose=False):
        """
        Este método somete al individuo a un proceso de mutación en el que, cada
        una de sus posiciones, puede verse modificada con una probabilidad 
        `prob_mut`. Tras mutar, los atributos `valor_funcion` y `fitness` se
        reinician.
        
        Parameters
        ----------
        prob_mut : `float`, optional
            probabilidad que tiene cada posición del individuo de mutar.
            (default 0.01)

        distribucion : {"normal", "uniforme", "aleatoria"}, optional
            distribución de la que obtener el factor de mutación.
            (default "uniforme")

        media_distribucion : `float`, optional
            media de la distribución si se selecciona `distribucion = "normal"`
            (default 1)

        sd_distribucion : `float`, optional
            desviación estándar de la distribución si se selecciona
            `distribucion = "normal"`. (default 1)

        min_distribucion : `float`, optional
            mínimo de la distribución si se selecciona 
            `distribucion = "uniforme"`. (default -1)

        max_distribucion : `float`, optional
            máximo de la distribución si se selecciona 
            `distribucion = "uniforme"`. (default +1)
        
        verbose : `bool`, optional
            mostrar información del proceso por pantalla. (default ``False``)

        Raises
        ------
        raise Exception
            si el argumento `distribucion` es distinto de 'normal', 'uniforme' o
            'aleatoria'.

        Examples
        --------
        Ejemplo mutar individuo.

        >>> individuo = Individuo(
                        n_variables = 3,
                        limites_inf = [-1,2,0],
                        limites_sup = [4,10,20],
                        verbose     = True
                    )

        >>> individuo.mutar(
                prob_mut         = 0.5,
                distribucion     = "uniforme",
                min_distribucion = -1,
                max_distribucion = 1,
                verbose          = True
            )

        Notes
        -----

        El proceso de mutación añade diversidad al proceso y evitar que el
        algoritmo caiga en mínimos locales por que todos los individuos sean
        demasiado parecidos de una generación a otra. Existen diferentes
        estrategias para controlar la magnitud del cambio que puede provocar una
        mutación.

        - Distribución uniforme: la mutación de la posición i se consigue
        sumándole al valor de i un valor extraído de una distribución uniforme,
        por ejemplo una entre [-1,+1].

        - Distribución normal: la mutación de la posición i se consigue sumándole
         al valor de i un valor extraído de una distribución normal, comúnmente
         centrada en 0 y con una determinada desviación estándar. Cuanto mayor
         la desviación estándar, con mayor probabilidad la mutación introducirá
         cambios grandes.

        - Aleatorio: la mutación de la posición i se consigue reemplazando el
        valor de i por nuevo valor aleatorio dentro del rango permitido para esa
        variable. Esta estrategia suele conllevar mayores variaciones que las dos
        anteriores.

        Hay que tener en cuenta que, debido a las mutaciones, un valor que
        inicialmente estaba dentro del rango permitido puede salirse de él.
        Una forma de evitarlo es: si el valor tras la mutación excede alguno de
        los límites acotados, se sobrescribe con el valor del límite. Es decir,
        se permite que los valores se alejen como máximo hasta el límite impuesto.

        """

        # COMPROBACIONES INICIALES: EXCEPTIONS Y WARNINGS
        # ----------------------------------------------------------------------
        if not distribucion in ["normal", "uniforme", "aleatoria"]:
            raise Exception(
                "El argumento distribucion debe ser: 'normal', 'uniforme' o " \
                + "'aleatoria'"
                )

        # SELECCIÓN PROBABILISTA DE POSICIONES (VARIABLES) QUE MUTAN
        #-----------------------------------------------------------------------
        posiciones_mutadas = np.random.uniform(
                                low=0,
                                high=1,
                                size=self.n_variables
                             )
        posiciones_mutadas = posiciones_mutadas > prob_mut

        # MODIFICACIÓN DE LOS VALORES DE LAS VARIABLES SELECCIONADAS
        #-----------------------------------------------------------------------
        # Si la distribución seleccionada es "uniforme" o "normal", se extrae un
        # valor aleatorio de la distribución elegida que se suma para modificar
        # la/las posiciones mutadas.

        if distribucion in ["normal", "uniforme"]:
            if distribucion == "normal":
                factor_mut = np.random.normal(
                                loc   = media_distribucion,
                                scale = sd_distribucion,
                                size  = np.sum(posiciones_mutadas)
                             )
            if distribucion == "uniforme":
                factor_mut = np.random.uniform(
                                low  = min_distribucion,
                                high = max_distribucion,
                                size = np.sum(posiciones_mutadas)
                             )
            self.valor_variables[posiciones_mutadas] = \
                self.valor_variables[posiciones_mutadas] + factor_mut

            # Se comprueba si algún valor mutado supera los límites impuestos.
            # En tal caso se sobrescribe con el valor del límite correspondiente.
            for i in np.flatnonzero(posiciones_mutadas):
                if self.valor_variables[i] < self.limites_inf[i]:
                    self.valor_variables[i] = self.limites_inf[i]
                if self.valor_variables[i] > self.limites_sup[i]:
                    self.valor_variables[i] = self.limites_sup[i]

        # Si la distribución seleccionada es "aleatoria", se sobreescribe el
        # valor de la variable con un nuevo valor aleatorio dentro de los 
        # límites establecidos.
        if distribucion == "aleatoria":
            for i in np.flatnonzero(posiciones_mutadas):
                self.valor_variables[i] = random.uniform(
                                            self.limites_inf[i],
                                            self.limites_sup[i]
                                          )
        # REINICIO DEL VALOR Y DEL FITNESS
        #-----------------------------------------------------------------------
        # Dado que el individuo ha mutado, el valor de su fitness y de la
        # función objetivo ya no son validos.
        self.fitness = None
        self.valor_funcion = None

        # INFORMACIÓN DEL PROCESO (VERBOSE)
        # ----------------------------------------------------------------------
        if verbose:
            print("El individuo ha sido mutado")
            print("---------------------------")
            print("Total mutaciones: " + str(np.sum(posiciones_mutadas)))
            print("Valor variables: " + str(self.valor_variables))
            print("")
