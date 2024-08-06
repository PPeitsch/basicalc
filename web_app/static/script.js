let currentShape = '';

document.getElementById('cylinderBtn').addEventListener('click', () => setShape('cylinder'));
document.getElementById('coneBtn').addEventListener('click', () => setShape('cone'));
document.getElementById('calculateBtn').addEventListener('click', calculate);

function setShape(shape) {
    currentShape = shape;
    updateDimensionInput();
}

function updateDimensionInput() {
    const dimensionInput = document.getElementById('dimensionInput');
    let html = `
        <div>
            <label for="calculationType">Calculate:</label>
            <select id="calculationType" onchange="updateDimensionLabel()">
                <option value="height">Height</option>
                <option value="${currentShape === 'cylinder' ? 'diameter' : 'radius'}">
                    ${currentShape === 'cylinder' ? 'Diameter' : 'Radius'}
                </option>
            </select>
        </div>
        <div>
            <label id="dimensionLabel" for="dimensionValue">
                ${currentShape === 'cylinder' ? 'Diameter' : 'Radius'}:
            </label>
            <input type="number" id="dimensionValue" step="0.01" required>
        </div>
    `;
    dimensionInput.innerHTML = html;
}

function updateDimensionLabel() {
    const calculationType = document.getElementById('calculationType').value;
    const dimensionLabel = document.getElementById('dimensionLabel');
    if (calculationType === 'height') {
        dimensionLabel.textContent = currentShape === 'cylinder' ? 'Diameter:' : 'Radius:';
    } else {
        dimensionLabel.textContent = 'Height:';
    }
}

function calculate() {
    const data = {
        shape: currentShape,
        mass: document.getElementById('mass').value,
        density: document.getElementById('density').value,
        massUnit: document.getElementById('massUnit').value,
        densityUnit: document.getElementById('densityUnit').value,
        lengthUnit: document.getElementById('lengthUnit').value,
        calculationType: document.getElementById('calculationType').value,
    };

    if (data.calculationType === 'height') {
        data.radiusOrDiameter = document.getElementById('dimensionValue').value;
    } else {
        data.height = document.getElementById('dimensionValue').value;
    }

    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            document.getElementById('result').textContent =
                `${data.dimension}: ${data.result} ${data.unit}`;
            drawShape(data.result, data.dimension);
        } else {
            document.getElementById('result').textContent = `Error: ${data.error}`;
        }
    })
    .catch((error) => {
        console.error('Error:', error);
        document.getElementById('result').textContent = 'An error occurred.';
    });
}

function drawShape(value, dimension) {
    const canvas = document.createElement('canvas');
    canvas.width = 300;
    canvas.height = 300;
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    const centerX = canvas.width / 2;
    const centerY = canvas.height / 2;

    ctx.beginPath();
    if (currentShape === 'cylinder') {
        const radius = dimension === 'Diameter' ? value / 2 : 50;
        const height = dimension === 'Height' ? value : 100;
        ctx.ellipse(centerX, centerY - height / 2, radius, radius / 4, 0, 0, 2 * Math.PI);
        ctx.moveTo(centerX - radius, centerY - height / 2);
        ctx.lineTo(centerX - radius, centerY + height / 2);
        ctx.moveTo(centerX + radius, centerY - height / 2);
        ctx.lineTo(centerX + radius, centerY + height / 2);
        ctx.ellipse(centerX, centerY + height / 2, radius, radius / 4, 0, 0, 2 * Math.PI);
    } else if (currentShape === 'cone') {
        const radius = dimension === 'Radius' ? value : 50;
        const height = dimension === 'Height' ? value : 100;
        ctx.moveTo(centerX - radius, centerY + height / 2);
        ctx.lineTo(centerX, centerY - height / 2);
        ctx.lineTo(centerX + radius, centerY + height / 2);
        ctx.closePath();
        ctx.ellipse(centerX, centerY + height / 2, radius, radius / 4, 0, 0, 2 * Math.PI);
    }
    ctx.stroke();

    const visualization = document.getElementById('shapeVisualization');
    visualization.innerHTML = '';
    visualization.appendChild(canvas);
}