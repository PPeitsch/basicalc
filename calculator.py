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


def calcular_altura_cilindro(diametro, masa, densidad, unidad_longitud):
    """
    Calcula la altura de un cilindro en función del diámetro, masa y densidad.

    Args:
        diametro (float): El diámetro del cilindro.
        masa (float): La masa del cilindro.
        densidad (float): La densidad del cilindro.
        unidad_longitud (int): El código de la unidad de longitud (1: mm, 2: cm, 3: m).

    Returns:
        float: La altura del cilindro en la unidad especificada.
    """
    diametro_metros = convertir_a_metros(diametro, unidad_longitud)
    altura_metros = (4 * masa) / (math.pi * (diametro_metros ** 2) * densidad)
    return convertir_desde_metros(altura_metros, unidad_longitud)


def calcular_diametro_cilindro(altura, masa, densidad, unidad_longitud):
    """
    Calcula el diámetro de un cilindro en función de la altura, masa y densidad.

    Args:
        altura (float): La altura del cilindro.
        masa (float): La masa del cilindro.
        densidad (float): La densidad del cilindro.
        unidad_longitud (int): El código de la unidad de longitud (1: mm, 2: cm, 3: m).

    Returns:
        float: El diámetro del cilindro en la unidad especificada.
    """
    altura_metros = convertir_a_metros(altura, unidad_longitud)
    diametro_metros = math.sqrt((4 * masa) / (math.pi * altura_metros * densidad))
    return convertir_desde_metros(diametro_metros, unidad_longitud)


def calcular_altura_cono(radio, masa, densidad, unidad_longitud):
    """
    Calcula la altura de un cono en función del radio, masa y densidad.

    Args:
        radio (float): El radio de la base del cono.
        masa (float): La masa del cono.
        densidad (float): La densidad del cono.
        unidad_longitud (int): El código de la unidad de longitud (1: mm, 2: cm, 3: m).

    Returns:
        float: La altura del cono en la unidad especificada.
    """
    radio_metros = convertir_a_metros(radio, unidad_longitud)
    altura_metros = (3 * masa) / (math.pi * (radio_metros ** 2) * densidad)
    return convertir_desde_metros(altura_metros, unidad_longitud)


def calcular_radio_cono(altura, masa, densidad, unidad_longitud):
    """
    Calcula el radio de la base de un cono en función de la altura, masa y densidad.

    Args:
        altura (float): La altura del cono.
        masa (float): La masa del cono.
        densidad (float): La densidad del cono.
        unidad_longitud (int): El código de la unidad de longitud (1: mm, 2: cm, 3: m).

    Returns:
        float: El radio del cono en la unidad especificada.
    """
    altura_metros = convertir_a_metros(altura, unidad_longitud)
    radio_metros = math.sqrt((3 * masa) / (math.pi * altura_metros * densidad))
    return convertir_desde_metros(radio_metros, unidad_longitud)


def solicitar_datos():
    """
    Solicita al usuario la entrada de los datos necesarios para el cálculo.

    Returns:
        tuple: Una tupla que contiene la densidad, masa, unidad de densidad,
               unidad de masa y unidad de longitud.
    """
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

            print("Seleccione la unidad de longitud (diámetro/altura/radio):")
            for key, value in UNIDADES_LONGITUD.items():
                print(f"{key}: {value}")
            unidad_longitud = int(input("Ingrese el número correspondiente a la unidad de longitud: ").strip())
            if unidad_longitud not in UNIDADES_LONGITUD:
                raise ValueError("Unidad de longitud no válida.")

            densidad = float(input(f"Ingrese la densidad ({UNIDADES_DENSIDAD[unidad_densidad]}): "))
            masa = float(input(f"Ingrese la masa ({UNIDADES_MASA[unidad_masa]}): "))

            return densidad, masa, unidad_densidad, unidad_masa, unidad_longitud
        except ValueError as e:
            print(f"Error: {e}. Por favor intente de nuevo.")


def calcular_figura_geometrica():
    """
    Calcula las dimensiones de una figura geométrica (cilindro o cono) en función de
    su densidad, masa y uno de los parámetros (altura/diámetro/radio).

    Solicita al usuario los datos necesarios y realiza los cálculos según la figura seleccionada.
    """
    densidad, masa, unidad_densidad, unidad_masa, unidad_longitud = solicitar_datos()

    densidad = convertir_densidad(densidad, unidad_densidad)
    masa = convertir_a_kilogramos(masa, unidad_masa)

    figura = input("¿Qué figura desea calcular, cilindro (c) o cono (co)? Ingrese 'c' o 'co': ").lower()
    if figura == 'c':
        parametro = input("¿Qué desea calcular, altura (h) o diámetro (d)? Ingrese 'h' o 'd': ").lower()
        if parametro == 'h':
            try:
                diametro = float(input(f"Ingrese el diámetro del cilindro ({UNIDADES_LONGITUD[unidad_longitud]}): "))
                altura = calcular_altura_cilindro(diametro, masa, densidad, unidad_longitud)
                print(f"La altura del cilindro es: {altura:.2f} {UNIDADES_LONGITUD[unidad_longitud]}")
            except ValueError:
                print("Entrada de diámetro no válida.")
        elif parametro == 'd':
            try:
                altura = float(input(f"Ingrese la altura del cilindro ({UNIDADES_LONGITUD[unidad_longitud]}): "))
                diametro = calcular_diametro_cilindro(altura, masa, densidad, unidad_longitud)
                print(f"El diámetro del cilindro es: {diametro:.2f} {UNIDADES_LONGITUD[unidad_longitud]}")
            except ValueError:
                print("Entrada de altura no válida.")
        else:
            print("Parámetro no válido. Por favor ingrese 'h' para altura o 'd' para diámetro.")
    elif figura == 'co':
        parametro = input("¿Qué desea calcular, altura (h) o radio (r)? Ingrese 'h' o 'r': ").lower()
        if parametro == 'h':
            try:
                radio = float(input(f"Ingrese el radio del cono ({UNIDADES_LONGITUD[unidad_longitud]}): "))
                altura = calcular_altura_cono(radio, masa, densidad, unidad_longitud)
                print(f"La altura del cono es: {altura:.2f} {UNIDADES_LONGITUD[unidad_longitud]}")
            except ValueError:
                print("Entrada de radio no válida.")
        elif parametro == 'r':
            try:
                altura = float(input(f"Ingrese la altura del cono ({UNIDADES_LONGITUD[unidad_longitud]}): "))
                radio = calcular_radio_cono(altura, masa, densidad, unidad_longitud)
                print(f"El radio del cono es: {radio:.2f} {UNIDADES_LONGITUD[unidad_longitud]}")
            except ValueError:
                print("Entrada de altura no válida.")
        else:
            print("Parámetro no válido. Por favor ingrese 'h' para altura o 'r' para radio.")
    else:
        print("Figura no válida. Por favor ingrese 'c' para cilindro o 'co' para cono.")


# Ejecutar la función
if __name__ == "__main__":
    calcular_figura_geometrica()
