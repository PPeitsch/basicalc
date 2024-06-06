import math

UNIDADES_DENSIDAD = {1: "g/cm^3", 2: "kg/m^3"}
UNIDADES_MASA = {1: "mg", 2: "g", 3: "kg"}
UNIDADES_LONGITUD = {1: "mm", 2: "cm", 3: "m"}


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


def calcular_altura(diametro, masa, densidad, unidad_longitud):
    diametro_metros = convertir_a_metros(diametro, unidad_longitud)
    altura_metros = (4 * masa) / (math.pi * (diametro_metros ** 2) * densidad)
    return convertir_desde_metros(altura_metros, unidad_longitud)


def calcular_diametro(altura, masa, densidad, unidad_longitud):
    altura_metros = convertir_a_metros(altura, unidad_longitud)
    diametro_metros = math.sqrt((4 * masa) / (math.pi * altura_metros * densidad))
    return convertir_desde_metros(diametro_metros, unidad_longitud)


def solicitar_datos():
    while True:
        try:
            print("Seleccione la unidad de densidad:")
            for key, value in UNIDADES_DENSIDAD.items():
                print(f"{key}: {value}")
            unidad_densidad = int(input("Ingrese el número correspondiente a la unidad de densidad: ").strip())
            if unidad_densidad not in UNIDADES_DENSIDAD:
                raise ValueError("Unidad de densidad no válida.")

            print("Seleccione la unidad de masa:")
            for key, value in UNIDADES_MASA.items():
                print(f"{key}: {value}")
            unidad_masa = int(input("Ingrese el número correspondiente a la unidad de masa: ").strip())
            if unidad_masa not in UNIDADES_MASA:
                raise ValueError("Unidad de masa no válida.")

            print("Seleccione la unidad de longitud (diámetro y altura):")
            for key, value in UNIDADES_LONGITUD.items():
                print(f"{key}: {value}")
            unidad_longitud = int(input("Ingrese el número correspondiente a la unidad de longitud: ").strip())
            if unidad_longitud not in UNIDADES_LONGITUD:
                raise ValueError("Unidad de longitud no válida.")

            densidad = float(input(f"Ingrese la densidad del cilindro ({UNIDADES_DENSIDAD[unidad_densidad]}): "))
            masa = float(input(f"Ingrese la masa del cilindro ({UNIDADES_MASA[unidad_masa]}): "))

            return densidad, masa, unidad_densidad, unidad_masa, unidad_longitud
        except ValueError as e:
            print(f"Error: {e}. Por favor intente de nuevo.")


def calcular_cilindro():
    """
    Calcula la altura o el diámetro de un cilindro basado en su densidad, masa, y
    uno de los dos parámetros (diámetro o altura).
    """
    densidad, masa, unidad_densidad, unidad_masa, unidad_longitud = solicitar_datos()

    # Convertir unidades a SI
    densidad = convertir_densidad(densidad, unidad_densidad)
    masa = convertir_a_kilogramos(masa, unidad_masa)

    parametro = input("¿Qué desea calcular, altura (h) o diámetro (d)? Ingrese 'h' o 'd': ").lower()

    if parametro == 'h':
        try:
            diametro = float(input(f"Ingrese el diámetro del cilindro ({UNIDADES_LONGITUD[unidad_longitud]}): "))
            altura = calcular_altura(diametro, masa, densidad, unidad_longitud)
            print(f"La altura del cilindro es: {altura:.2f} {UNIDADES_LONGITUD[unidad_longitud]}")
        except ValueError:
            print("Entrada de diámetro no válida.")
    elif parametro == 'd':
        try:
            altura = float(input(f"Ingrese la altura del cilindro ({UNIDADES_LONGITUD[unidad_longitud]}): "))
            diametro = calcular_diametro(altura, masa, densidad, unidad_longitud)
            print(f"El diámetro del cilindro es: {diametro:.2f} {UNIDADES_LONGITUD[unidad_longitud]}")
        except ValueError:
            print("Entrada de altura no válida.")
    else:
        print("Parámetro no válido. Por favor ingrese 'h' para altura o 'd' para diámetro.")


# Ejecutar la función
if __name__ == "__main__":
    calcular_cilindro()
