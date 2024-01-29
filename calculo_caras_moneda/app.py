import math

def binomial_probability(n, k, p):
    """
    Calcula la probabilidad de obtener exactamente k caras en una serie de lanzamientos de monedas.

    Args:
    - n (int): Número total de lanzamientos de monedas.
    - k (int): Número de caras deseadas.
    - p (float): Probabilidad de obtener cara en un solo lanzamiento.

    Returns:
    - float: Probabilidad de obtener exactamente k caras.
    """
    coefficient = math.comb(n, k)
    prob_success = p ** k
    prob_failure = (1 - p) ** (n - k)
    return coefficient * prob_success * prob_failure

# Solicitar al usuario que ingrese los parámetros
num_lanzamientos = int(input("Ingrese el número de lanzamientos de monedas: "))
probabilidad_cara = float(input("Ingrese la probabilidad de obtener cara en un solo lanzamiento (entre 0 y 1): "))
num_caras_deseadas = round(num_lanzamientos * probabilidad_cara)

# Calcular probabilidad de obtener exactamente num_caras_deseadas caras
probabilidad_caras_deseadas = binomial_probability(num_lanzamientos, num_caras_deseadas, probabilidad_cara)
print("Probabilidad de obtener exactamente", num_caras_deseadas, "caras en", num_lanzamientos, "lanzamientos de monedas:", probabilidad_caras_deseadas)
print("Probabilidad en porcentaje: {:.2%}".format(probabilidad_caras_deseadas))
