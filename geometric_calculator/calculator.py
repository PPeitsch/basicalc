from .shapes import GeometricShape, Cylinder, Cone
from .conversions import Converter
from .units import Units


class GeometricCalculator:
    def __init__(self, shape: str, mass: float, density: float,
                 mass_unit: int, density_unit: int, length_unit: int):
        self.mass = Converter.to_kilograms(mass, mass_unit)
        self.density = Converter.density_to_kg_m3(density, density_unit)
        self.length_unit = length_unit

        if shape.lower() == 'cylinder':
            self.shape = Cylinder(self.mass, self.density)
        elif shape.lower() == 'cone':
            self.shape = Cone(self.mass, self.density)
        else:
            raise ValueError("Invalid shape. Please choose 'cylinder' or 'cone'.")

    def calculate_height(self, radius_or_diameter: float) -> float:
        value_meters = Converter.to_meters(radius_or_diameter, self.length_unit)
        height_meters = self.shape.calculate_height(value_meters)
        return Converter.from_meters(height_meters, self.length_unit)

    def calculate_radius_or_diameter(self, height: float) -> float:
        height_meters = Converter.to_meters(height, self.length_unit)
        value_meters = self.shape.calculate_radius_or_diameter(height_meters)
        return Converter.from_meters(value_meters, self.length_unit)
