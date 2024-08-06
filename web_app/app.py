from flask import Flask, render_template, request, jsonify
from geometric_calculator import GeometricCalculator, Units

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',
                           density_units=Units.DENSITY,
                           mass_units=Units.MASS,
                           length_units=Units.LENGTH)


@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    try:
        calculator = GeometricCalculator(
            shape=data['shape'],
            mass=float(data['mass']),
            density=float(data['density']),
            mass_unit=int(data['massUnit']),
            density_unit=int(data['densityUnit']),
            length_unit=int(data['lengthUnit'])
        )

        if data['calculationType'] == 'height':
            result = calculator.calculate_height(float(data['radiusOrDiameter']))
            dimension = 'Height'
        else:
            result = calculator.calculate_radius_or_diameter(float(data['height']))
            dimension = 'Radius' if data['shape'].lower() == 'cone' else 'Diameter'

        return jsonify({
            'success': True,
            'result': round(result, 2),
            'dimension': dimension,
            'unit': Units.LENGTH[int(data['lengthUnit'])]
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
