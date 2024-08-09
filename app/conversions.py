class Converter:
    @staticmethod
    def to_meters(value: float, unit: int) -> float:
        return value * {1: 0.001, 2: 0.01, 3: 1}.get(unit, 1)

    @staticmethod
    def to_kilograms(value: float, unit: int) -> float:
        return value * {1: 1e-6, 2: 0.001, 3: 1}.get(unit, 1)

    @staticmethod
    def density_to_kg_m3(density: float, unit: int) -> float:
        return density * {1: 1000, 2: 1}.get(unit, 1)

    @staticmethod
    def from_meters(value: float, unit: int) -> float:
        return value * {1: 1000, 2: 100, 3: 1}.get(unit, 1)
