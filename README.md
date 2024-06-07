# Geometric Shape Calculator

This Python program calculates dimensions for geometric shapes based on their density, mass, and one of the shape parameters (height, diameter, or radius). It currently supports calculations for cylinders and cones.

## Features

- Convert units of length (mm, cm, m) to meters and vice versa.
- Convert units of mass (mg, g, kg) to kilograms.
- Convert density units (g/cm³, kg/m³) to SI units.
- Calculate height or diameter of a cylinder given its density, mass, and one of the parameters.
- Calculate height or radius of a cone given its density, mass, and one of the parameters.

## Requirements

- Python 3.x

## Usage

1. Clone the repository or download the script.
2. Run the script using Python:

    ```sh
    python geometric_calculator.py
    ```

3. Follow the on-screen instructions to input the required data for calculations.

## Example

### Calculate Cylinder Dimensions

1. Select the density unit:
    - 1: g/cm³
    - 2: kg/m³

2. Select the mass unit:
    - 1: mg
    - 2: g
    - 3: kg

3. Select the length unit (for diameter and height):
    - 1: mm
    - 2: cm
    - 3: m

4. Enter the density value.
5. Enter the mass value.
6. Choose to calculate either height (h) or diameter (d).
7. Enter the known parameter (diameter or height).

### Calculate Cone Dimensions

1. Select the density unit:
    - 1: g/cm³
    - 2: kg/m³

2. Select the mass unit:
    - 1: mg
    - 2: g
    - 3: kg

3. Select the length unit (for radius and height):
    - 1: mm
    - 2: cm
    - 3: m

4. Enter the density value.
5. Enter the mass value.
6. Choose to calculate either height (h) or radius (r).
7. Enter the known parameter (radius or height).

## Code Overview

### Functions

- `convertir_a_metros(valor, unidad)`: Converts a value to meters based on the given unit.
- `convertir_a_kilogramos(valor, unidad)`: Converts a value to kilograms based on the given unit.
- `convertir_densidad(densidad, unidad)`: Converts density to kg/m³ based on the given unit.
- `convertir_desde_metros(valor, unidad)`: Converts a value from meters to the specified unit.
- `calcular_altura_cilindro(diametro, masa, densidad, unidad_longitud)`: Calculates the height of a cylinder.
- `calcular_diametro_cilindro(altura, masa, densidad, unidad_longitud)`: Calculates the diameter of a cylinder.
- `calcular_altura_cono(radio, masa, densidad, unidad_longitud)`: Calculates the height of a cone.
- `calcular_radio_cono(altura, masa, densidad, unidad_longitud)`: Calculates the radius of a cone.
- `solicitar_datos()`: Prompts the user for input data.
- `calcular_figura_geometrica()`: Main function to perform geometric calculations based on user input.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss your changes.

## License

This project is licensed under the MIT License.
