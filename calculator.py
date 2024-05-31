import math


def convertir_a_metros(valor, unidad):
    """
    Convierte un valor a metros basado en la unidad dada.

    Args:
        valor (float): El valor a convertir.
        unidad (int): El código de la unidad (1: mm, 2: cm, 3: m).

    Returns:
        float: El valor convertido a metros.
    """
    conversiones = {
        1: valor / 1000,  # mm a m
        2: valor / 100,  # cm a m
        3: valor  # m
    }
    return conversiones.get(unidad, valor)


def convertir_a_kilogramos(valor, unidad):
    """
    Convierte un valor a kilogramos basado en la unidad dada.

    Args:
        valor (float): El valor a convertir.
        unidad (int): El código de la unidad (1: mg, 2: g, 3: kg).

    Returns:
        float: El valor convertido a kilogramos.
    """
    conversiones = {
        1: valor / 1_000_000,  # mg a kg
        2: valor / 1000,  # g a kg
        3: valor  # kg
    }
    return conversiones.get(unidad, valor)


def convertir_densidad(densidad, unidad):
    """
    Convierte la densidad a kg/m^3 basado en la unidad dada.

    Args:
        densidad (float): La densidad a convertir.
        unidad (int): El código de la unidad (1: g/cm^3, 2: kg/m^3).

    Returns:
        float: La densidad convertida a kg/m^3.
    """
    conversiones = {
        1: densidad * 1000,  # g/cm^3 a kg/m^3
        2: densidad  # kg/m^3
    }
    return conversiones.get(unidad, densidad)


def convertir_desde_metros(valor, unidad):
    """
    Convierte un valor desde metros a la unidad especificada.

    Args:
        valor (float): El valor en metros.
        unidad (int): El código de la unidad a convertir (1: mm, 2: cm, 3: m).

    Returns:
        float: El valor convertido a la unidad especificada.
    """
    conversiones = {
        1: valor * 1000,  # m a mm
        2: valor * 100,  # m a cm
        3: valor  # m
    }
    return conversiones.get(unidad, valor)


def calcular_cilindro():
    """
    Calcula la altura o el diámetro de un cilindro basado en su densidad, masa, y
    uno de los dos parámetros (diámetro o altura).

    La densidad y la masa son datos que siempre se deben ingresar.
    """

    # Selección de unidades
    print("Seleccione la unidad de densidad:")
    print("1: g/cm^3")
    print("2: kg/m^3")
    unidad_densidad = int(input("Ingrese el número correspondiente a la unidad de densidad: ").strip())

    print("Seleccione la unidad de masa:")
    print("1: mg")
    print("2: g")
    print("3: kg")
    unidad_masa = int(input("Ingrese el número correspondiente a la unidad de masa: ").strip())

    print("Seleccione la unidad de longitud (diámetro y altura):")
    print("1: mm")
    print("2: cm")
    print("3: m")
    unidad_longitud = int(input("Ingrese el número correspondiente a la unidad de longitud: ").strip())

    # Solicitar datos
    densidad = float(input(f"Ingrese la densidad del cilindro ({'g/cm^3' if unidad_densidad == 1 else 'kg/m^3'}): "))
    masa = float(
        input(f"Ingrese la masa del cilindro ({'mg' if unidad_masa == 1 else 'g' if unidad_masa == 2 else 'kg'}): "))

    # Convertir unidades a SI
    densidad = convertir_densidad(densidad, unidad_densidad)
    masa = convertir_a_kilogramos(masa, unidad_masa)

    parametro = input("¿Qué desea calcular, altura (h) o diámetro (d)? Ingrese 'h' o 'd': ").lower()

    if parametro == 'h':
        diametro = float(input(
            f"Ingrese el diámetro del cilindro ({'mm' if unidad_longitud == 1 else 'cm' if unidad_longitud == 2 else 'm'}): "))
        diametro_metros = convertir_a_metros(diametro, unidad_longitud)
        altura_metros = (4 * masa) / (math.pi * (diametro_metros ** 2) * densidad)
        altura = convertir_desde_metros(altura_metros, unidad_longitud)
        print(
            f"La altura del cilindro es: {altura:.2f} {'mm' if unidad_longitud == 1 else 'cm' if unidad_longitud == 2 else 'm'}")

    elif parametro == 'd':
        altura = float(input(
            f"Ingrese la altura del cilindro ({'mm' if unidad_longitud == 1 else 'cm' if unidad_longitud == 2 else 'm'}): "))
        altura_metros = convertir_a_metros(altura, unidad_longitud)
        diametro_metros = math.sqrt((4 * masa) / (math.pi * altura_metros * densidad))
        diametro = convertir_desde_metros(diametro_metros, unidad_longitud)
        print(
            f"El diámetro del cilindro es: {diametro:.2f} {'mm' if unidad_longitud == 1 else 'cm' if unidad_longitud == 2 else 'm'}")

    else:
        print("Parámetro no válido. Por favor ingrese 'h' para altura o 'd' para diámetro.")


# Ejecutar la función
if __name__ == "__main__":
    calcular_cilindro()
