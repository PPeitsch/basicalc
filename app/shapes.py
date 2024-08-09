from abc import ABC, abstractmethod
import math


class GeometricShape(ABC):
    def __init__(self, mass: float, density: float):
        self.mass = mass
        self.density = density

    @abstractmethod
    def calculate_height(self, value: float) -> float:
        pass

    @abstractmethod
    def calculate_radius_or_diameter(self, value: float) -> float:
        pass


class Cylinder(GeometricShape):
    def calculate_height(self, diameter: float) -> float:
        return (4 * self.mass) / (math.pi * (diameter ** 2) * self.density)

    def calculate_radius_or_diameter(self, height: float) -> float:
        return math.sqrt((4 * self.mass) / (math.pi * height * self.density))


class Cone(GeometricShape):
    def calculate_height(self, radius: float) -> float:
        return (3 * self.mass) / (math.pi * (radius ** 2) * self.density)

    def calculate_radius_or_diameter(self, height: float) -> float:
        return math.sqrt((3 * self.mass) / (math.pi * height * self.density))