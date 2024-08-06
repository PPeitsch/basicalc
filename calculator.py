import math
from typing import Dict, Tuple

UNIDADES_DENSIDAD: Dict[int, str] = {1: "g/cm^3", 2: "kg/m^3"}
UNIDADES_MASA: Dict[int, str] = {1: "mg", 2: "g", 3: "kg"}
UNIDADES_LONGITUD: Dict[int, str] = {1: "mm", 2: "cm", 3: "m"}


def convertir_unidad(valor: float, unidad: int, conversion_factor: Dict[int, float]) -> float:
    """
    Convierte un valor a la unidad base según el factor de conversión proporcionado.

    Args:
        valor (float): El valor a convertir.
        unidad (int): El código de la unidad.
        conversion_factor (Dict[int, float]): Diccionario con los factores de conversión.

    Returns:
        float: El valor convertido.
    """
    return valor * conversion_factor.get(unidad, 1)


def convertir_a_metros(valor: float, unidad: int) -> float:
    return convertir_unidad(valor, unidad, {1: 0.001, 2: 0.01, 3: 1})


def convertir_a_kilogramos(valor: float, unidad: int) -> float:
    return convertir_unidad(valor, unidad, {1: 1e-6, 2: 0.001, 3: 1})


def convertir_densidad(densidad: float, unidad: int) -> float:
    return convertir_unidad(densidad, unidad, {1: 1000, 2: 1})


def convertir_desde_metros(valor: float, unidad: int) -> float:
    return convertir_unidad(valor, unidad, {1: 1000, 2: 100, 3: 1})


def calcular_dimension_cilindro(valor: float, masa: float, densidad: float, calcular_altura: bool) -> float:
    """
    Calcula la altura o el diámetro de un cilindro.

    Args:
        valor (float): Diámetro (si calcular_altura es True) o altura (si es False).
        masa (float): La masa del cilindro en kg.
        densidad (float): La densidad del cilindro en kg/m^3.
        calcular_altura (bool): True para calcular altura, False para calcular diámetro.

    Returns:
        float: La altura o el diámetro del cilindro en metros.
    """
    if calcular_altura:
        return (4 * masa) / (math.pi * (valor ** 2) * densidad)
    else:
        return math.sqrt((4 * masa) / (math.pi * valor * densidad))


def calcular_dimension_cono(valor: float, masa: float, densidad: float, calcular_altura: bool) -> float:
    """
    Calcula la altura o el radio de un cono.

    Args:
        valor (float): Radio (si calcular_altura es True) o altura (si es False).
        masa (float): La masa del cono en kg.
        densidad (float): La densidad del cono en kg/m^3.
        calcular_altura (bool): True para calcular altura, False para calcular radio.

    Returns:
        float: La altura o el radio del cono en metros.
    """
    if calcular_altura:
        return (3 * masa) / (math.pi * (valor ** 2) * densidad)
    else:
        return math.sqrt((3 * masa) / (math.pi * valor * densidad))


def solicitar_entrada(prompt: str, opciones: Dict[int, str]) -> int:
    """
    Solicita al usuario que elija una opción de un diccionario.

    Args:
        prompt (str): El mensaje para mostrar al usuario.
        opciones (Dict[int, str]): Un diccionario con las opciones disponibles.

    Returns:
        int: El número de la opción seleccionada.
    """
    while True:
        print(prompt)
        for key, value in opciones.items():
            print(f"{key}: {value}")
        try:
            seleccion = int(input("Ingrese el número correspondiente: ").strip())
            if seleccion in opciones:
                return seleccion
            raise ValueError
        except ValueError:
            print("Entrada no válida. Por favor, intente de nuevo.")


def solicitar_datos() -> Tuple[float, float, int, int, int]:
    """
    Solicita al usuario la entrada de los datos necesarios para el cálculo.

    Returns:
        Tuple[float, float, int, int, int]: densidad, masa, unidad_densidad, unidad_masa, unidad_longitud
    """
    unidad_densidad = solicitar_entrada("Seleccione la unidad de densidad:", UNIDADES_DENSIDAD)
    unidad_masa = solicitar_entrada("Seleccione la unidad de masa:", UNIDADES_MASA)
    unidad_longitud = solicitar_entrada("Seleccione la unidad de longitud (diámetro/altura/radio):", UNIDADES_LONGITUD)

    densidad = float(input(f"Ingrese la densidad ({UNIDADES_DENSIDAD[unidad_densidad]}): "))
    masa = float(input(f"Ingrese la masa ({UNIDADES_MASA[unidad_masa]}): "))

    return densidad, masa, unidad_densidad, unidad_masa, unidad_longitud


def calcular_figura_geometrica():
    """
    Calcula las dimensiones de una figura geométrica (cilindro o cono) en función de
    su densidad, masa y uno de los parámetros (altura/diámetro/radio).
    """
    densidad, masa, unidad_densidad, unidad_masa, unidad_longitud = solicitar_datos()

    densidad = convertir_densidad(densidad, unidad_densidad)
    masa = convertir_a_kilogramos(masa, unidad_masa)

    figura = input("¿Qué figura desea calcular, cilindro (c) o cono (co)? Ingrese 'c' o 'co': ").lower()
    if figura == 'c':
        calcular_cilindro(masa, densidad, unidad_longitud)
    elif figura == 'co':
        calcular_cono(masa, densidad, unidad_longitud)
    else:
        print("Figura no válida. Por favor ingrese 'c' para cilindro o 'co' para cono.")


def calcular_cilindro(masa: float, densidad: float, unidad_longitud: int):
    """
    Calcula las dimensiones de un cilindro.

    Args:
        masa (float): La masa del cilindro en kg.
        densidad (float): La densidad del cilindro en kg/m^3.
        unidad_longitud (int): El código de la unidad de longitud.
    """
    parametro = input("¿Qué desea calcular, altura (h) o diámetro (d)? Ingrese 'h' o 'd': ").lower()
    if parametro == 'h':
        diametro = float(input(f"Ingrese el diámetro del cilindro ({UNIDADES_LONGITUD[unidad_longitud]}): "))
        diametro_metros = convertir_a_metros(diametro, unidad_longitud)
        altura_metros = calcular_dimension_cilindro(diametro_metros, masa, densidad, True)
        altura = convertir_desde_metros(altura_metros, unidad_longitud)
        print(f"La altura del cilindro es: {altura:.2f} {UNIDADES_LONGITUD[unidad_longitud]}")
    elif parametro == 'd':
        altura = float(input(f"Ingrese la altura del cilindro ({UNIDADES_LONGITUD[unidad_longitud]}): "))
        altura_metros = convertir_a_metros(altura, unidad_longitud)
        diametro_metros = calcular_dimension_cilindro(altura_metros, masa, densidad, False)
        diametro = convertir_desde_metros(diametro_metros, unidad_longitud)
        print(f"El diámetro del cilindro es: {diametro:.2f} {UNIDADES_LONGITUD[unidad_longitud]}")
    else:
        print("Parámetro no válido. Por favor ingrese 'h' para altura o 'd' para diámetro.")


def calcular_cono(masa: float, densidad: float, unidad_longitud: int):
    """
    Calcula las dimensiones de un cono.

    Args:
        masa (float): La masa del cono en kg.
        densidad (float): La densidad del cono en kg/m^3.
        unidad_longitud (int): El código de la unidad de longitud.
    """
    parametro = input("¿Qué desea calcular, altura (h) o radio (r)? Ingrese 'h' o 'r': ").lower()
    if parametro == 'h':
        radio = float(input(f"Ingrese el radio del cono ({UNIDADES_LONGITUD[unidad_longitud]}): "))
        radio_metros = convertir_a_metros(radio, unidad_longitud)
        altura_metros = calcular_dimension_cono(radio_metros, masa, densidad, True)
        altura = convertir_desde_metros(altura_metros, unidad_longitud)
        print(f"La altura del cono es: {altura:.2f} {UNIDADES_LONGITUD[unidad_longitud]}")
    elif parametro == 'r':
        altura = float(input(f"Ingrese la altura del cono ({UNIDADES_LONGITUD[unidad_longitud]}): "))
        altura_metros = convertir_a_metros(altura, unidad_longitud)
        radio_metros = calcular_dimension_cono(altura_metros, masa, densidad, False)
        radio = convertir_desde_metros(radio_metros, unidad_longitud)
        print(f"El radio del cono es: {radio:.2f} {UNIDADES_LONGITUD[unidad_longitud]}")
    else:
        print("Parámetro no válido. Por favor ingrese 'h' para altura o 'r' para radio.")


if __name__ == "__main__":
    calcular_figura_geometrica()
