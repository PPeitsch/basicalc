# Geometric Calculator App

## Overview

The Geometric Calculator App is a Flask-based web application that allows users to perform calculations related to cylindrical and conical shapes. Users can calculate the height or radius/diameter of these shapes based on their mass, density, and other dimensions.

## Features

- Calculate height or radius/diameter for cylinders and cones
- Support for multiple units of measurement
- Interactive shape visualization
- Responsive web interface

## Technologies Used

- Backend: Python, Flask
- Frontend: HTML, CSS, JavaScript
- Visualization: HTML5 Canvas

## Project Structure

```
geometric-calculator/
├── app/
│   ├── __init__.py
│   ├── calculator.py
│   ├── conversions.py
│   ├── shapes.py
│   └── units.py
├── static/
│   ├── script.js
│   └── styles.css
├── templates/
│   └── index.html
├── app.py
├── requirements.txt
├── LICENSE
└── README.md
```

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/geometric-calculator.git
   cd geometric-calculator
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   python app.py
   ```

5. Open a web browser and navigate to `http://localhost:5000` to use the application.

## Usage

1. Select the shape (cylinder or cone) you want to calculate.
2. Enter the mass and density of the object.
3. Choose the appropriate units for mass, density, and length.
4. Select whether you want to calculate the height or the radius/diameter.
5. Enter the known dimension (height or radius/diameter).
6. Click the "Calculate" button to see the result.
7. The calculated dimension will be displayed along with a visualization of the shape.

## Contributing

Contributions to improve the Geometric Calculator App are welcome. Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive commit messages.
4. Push your changes to your fork.
5. Submit a pull request to the main repository.

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0). For the full license text, see the [LICENSE](LICENSE) file in the project root.