from abc import ABC, abstractmethod
import math
from typing import Dict, Tuple


class UnidadesMedida:
    DENSIDAD: Dict[int, str] = {1: "g/cm^3", 2: "kg/m^3"}
    MASA: Dict[int, str] = {1: "mg", 2: "g", 3: "kg"}
    LONGITUD: Dict[int, str] = {1: "mm", 2: "cm", 3: "m"}


class Conversor:
    @staticmethod
    def a_metros(valor: float, unidad: int) -> float:
        return valor * {1: 0.001, 2: 0.01, 3: 1}.get(unidad, 1)

    @staticmethod
    def a_kilogramos(valor: float, unidad: int) -> float:
        return valor * {1: 1e-6, 2: 0.001, 3: 1}.get(unidad, 1)

    @staticmethod
    def densidad_a_kg_m3(densidad: float, unidad: int) -> float:
        return densidad * {1: 1000, 2: 1}.get(unidad, 1)

    @staticmethod
    def desde_metros(valor: float, unidad: int) -> float:
        return valor * {1: 1000, 2: 100, 3: 1}.get(unidad, 1)


class FiguraGeometrica(ABC):
    def __init__(self, masa: float, densidad: float):
        self.masa = masa
        self.densidad = densidad

    @abstractmethod
    def calcular_altura(self, valor: float) -> float:
        pass

    @abstractmethod
    def calcular_radio_o_diametro(self, valor: float) -> float:
        pass


class Cilindro(FiguraGeometrica):
    def calcular_altura(self, diametro: float) -> float:
        return (4 * self.masa) / (math.pi * (diametro ** 2) * self.densidad)

    def calcular_radio_o_diametro(self, altura: float) -> float:
        return math.sqrt((4 * self.masa) / (math.pi * altura * self.densidad))


class Cono(FiguraGeometrica):
    def calcular_altura(self, radio: float) -> float:
        return (3 * self.masa) / (math.pi * (radio ** 2) * self.densidad)

    def calcular_radio_o_diametro(self, altura: float) -> float:
        return math.sqrt((3 * self.masa) / (math.pi * altura * self.densidad))


class InterfazUsuario:
    @staticmethod
    def solicitar_entrada(prompt: str, opciones: Dict[int, str]) -> int:
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

    @staticmethod
    def solicitar_datos() -> Tuple[float, float, int, int, int]:
        unidad_densidad = InterfazUsuario.solicitar_entrada("Seleccione la unidad de densidad:",
                                                            UnidadesMedida.DENSIDAD)
        unidad_masa = InterfazUsuario.solicitar_entrada("Seleccione la unidad de masa:", UnidadesMedida.MASA)
        unidad_longitud = InterfazUsuario.solicitar_entrada("Seleccione la unidad de longitud (diámetro/altura/radio):",
                                                            UnidadesMedida.LONGITUD)

        densidad = float(input(f"Ingrese la densidad ({UnidadesMedida.DENSIDAD[unidad_densidad]}): "))
        masa = float(input(f"Ingrese la masa ({UnidadesMedida.MASA[unidad_masa]}): "))

        return densidad, masa, unidad_densidad, unidad_masa, unidad_longitud


class CalculadoraGeometrica:
    def __init__(self):
        self.figura: FiguraGeometrica = None
        self.unidad_longitud: int = 0

    def configurar(self):
        densidad, masa, unidad_densidad, unidad_masa, self.unidad_longitud = InterfazUsuario.solicitar_datos()

        densidad = Conversor.densidad_a_kg_m3(densidad, unidad_densidad)
        masa = Conversor.a_kilogramos(masa, unidad_masa)

        figura = input("¿Qué figura desea calcular, cilindro (c) o cono (co)? Ingrese 'c' o 'co': ").lower()
        if figura == 'c':
            self.figura = Cilindro(masa, densidad)
        elif figura == 'co':
            self.figura = Cono(masa, densidad)
        else:
            raise ValueError("Figura no válida. Por favor ingrese 'c' para cilindro o 'co' para cono.")

    def calcular(self):
        if isinstance(self.figura, Cilindro):
            self._calcular_cilindro()
        elif isinstance(self.figura, Cono):
            self._calcular_cono()

    def _calcular_cilindro(self):
        parametro = input("¿Qué desea calcular, altura (h) o diámetro (d)? Ingrese 'h' o 'd': ").lower()
        if parametro == 'h':
            diametro = float(
                input(f"Ingrese el diámetro del cilindro ({UnidadesMedida.LONGITUD[self.unidad_longitud]}): "))
            diametro_metros = Conversor.a_metros(diametro, self.unidad_longitud)
            altura_metros = self.figura.calcular_altura(diametro_metros)
            altura = Conversor.desde_metros(altura_metros, self.unidad_longitud)
            print(f"La altura del cilindro es: {altura:.2f} {UnidadesMedida.LONGITUD[self.unidad_longitud]}")
        elif parametro == 'd':
            altura = float(input(f"Ingrese la altura del cilindro ({UnidadesMedida.LONGITUD[self.unidad_longitud]}): "))
            altura_metros = Conversor.a_metros(altura, self.unidad_longitud)
            diametro_metros = self.figura.calcular_radio_o_diametro(altura_metros)
            diametro = Conversor.desde_metros(diametro_metros, self.unidad_longitud)
            print(f"El diámetro del cilindro es: {diametro:.2f} {UnidadesMedida.LONGITUD[self.unidad_longitud]}")
        else:
            print("Parámetro no válido. Por favor ingrese 'h' para altura o 'd' para diámetro.")

    def _calcular_cono(self):
        parametro = input("¿Qué desea calcular, altura (h) o radio (r)? Ingrese 'h' o 'r': ").lower()
        if parametro == 'h':
            radio = float(input(f"Ingrese el radio del cono ({UnidadesMedida.LONGITUD[self.unidad_longitud]}): "))
            radio_metros = Conversor.a_metros(radio, self.unidad_longitud)
            altura_metros = self.figura.calcular_altura(radio_metros)
            altura = Conversor.desde_metros(altura_metros, self.unidad_longitud)
            print(f"La altura del cono es: {altura:.2f} {UnidadesMedida.LONGITUD[self.unidad_longitud]}")
        elif parametro == 'r':
            altura = float(input(f"Ingrese la altura del cono ({UnidadesMedida.LONGITUD[self.unidad_longitud]}): "))
            altura_metros = Conversor.a_metros(altura, self.unidad_longitud)
            radio_metros = self.figura.calcular_radio_o_diametro(altura_metros)
            radio = Conversor.desde_metros(radio_metros, self.unidad_longitud)
            print(f"El radio del cono es: {radio:.2f} {UnidadesMedida.LONGITUD[self.unidad_longitud]}")
        else:
            print("Parámetro no válido. Por favor ingrese 'h' para altura o 'r' para radio.")


def main():
    calculadora = CalculadoraGeometrica()
    try:
        calculadora.configurar()
        calculadora.calcular()
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
