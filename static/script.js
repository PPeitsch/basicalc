let currentShape = 'cylinder';

document.getElementById('cylinderBtn').addEventListener('click', () => setShape('cylinder'));
document.getElementById('coneBtn').addEventListener('click', () => setShape('cone'));
document.getElementById('calculateBtn').addEventListener('click', calculate);

function setShape(shape) {
    currentShape = shape;
    updateDimensionInput();
    // Update button styles
    document.getElementById('cylinderBtn').classList.remove('active');
    document.getElementById('coneBtn').classList.remove('active');
    document.getElementById(`${shape}Btn`).classList.add('active');
}

function initializeUI() {
    setShape('cylinder');
    document.getElementById('cylinderBtn').classList.add('active');
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
            <input type="number" id="dimensionValue" step="0.01" min="0.01" required>
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

function validateInput(value, fieldName) {
    if (value === "" || isNaN(value)) {
        throw new Error(`Please enter a valid number for ${fieldName}.`);
    }
    if (value <= 0) {
        throw new Error(`${fieldName} must be greater than zero.`);
    }
}

function calculate() {
    try {
        const data = {
            shape: currentShape,
            mass: document.getElementById('mass').value,
            density: document.getElementById('density').value,
            massUnit: document.getElementById('massUnit').value,
            densityUnit: document.getElementById('densityUnit').value,
            lengthUnit: document.getElementById('lengthUnit').value,
            calculationType: document.getElementById('calculationType').value,
        };

        validateInput(data.mass, "Mass");
        validateInput(data.density, "Density");

        if (data.calculationType === 'height') {
            data.radiusOrDiameter = document.getElementById('dimensionValue').value;
            validateInput(data.radiusOrDiameter, currentShape === 'cylinder' ? "Diameter" : "Radius");
        } else {
            data.height = document.getElementById('dimensionValue').value;
            validateInput(data.height, "Height");
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
    } catch (error) {
        document.getElementById('result').textContent = `Error: ${error.message}`;
    }
}

function drawShape(value, dimension) {
    const canvas = document.createElement('canvas');
    canvas.width = 400;
    canvas.height = 420; // Increased height to add space at the bottom
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    const centerX = canvas.width / 2;
    const centerY = canvas.height / 2 - 80; // Move shape up more
    const maxDimension = 200;

    let radius, height;
    if (currentShape === 'cylinder') {
        radius = dimension === 'Diameter' ? value / 2 : maxDimension / 4;
        height = dimension === 'Height' ? value : maxDimension;
    } else { // cone
        radius = dimension === 'Radius' ? value : maxDimension / 4;
        height = dimension === 'Height' ? value : maxDimension;
    }

    // Scale the shape to fit the canvas
    const scale = Math.min(maxDimension / (2 * radius), maxDimension / height);
    radius *= scale;
    height *= scale;

    // Draw the shape
    ctx.beginPath();
    ctx.strokeStyle = 'black';
    if (currentShape === 'cylinder') {
        drawCylinder(ctx, centerX, centerY, radius, height);
    } else {
        drawCone(ctx, centerX, centerY, radius, height);
    }
    ctx.stroke();

    // Draw dimension lines and labels
    const lengthUnit = document.getElementById('lengthUnit').options[document.getElementById('lengthUnit').selectedIndex].text;
    drawDimensionLine(ctx, centerX - radius, centerY + height/2 + 40, centerX + radius, centerY + height/2 + 40,
                      `${(currentShape === 'cylinder' ? radius * 2 : radius).toFixed(2)} ${lengthUnit}`, 'bottom');
    drawDimensionLine(ctx, centerX + radius + 40, centerY - height/2, centerX + radius + 40, centerY + height/2,
                      `${height.toFixed(2)} ${lengthUnit}`, 'right');

    const visualization = document.getElementById('shapeVisualization');
    visualization.innerHTML = '';
    visualization.appendChild(canvas);
}

function drawCylinder(ctx, centerX, centerY, radius, height) {
    ctx.ellipse(centerX, centerY - height/2, radius, radius/4, 0, 0, 2 * Math.PI);
    ctx.moveTo(centerX - radius, centerY - height/2);
    ctx.lineTo(centerX - radius, centerY + height/2);
    ctx.moveTo(centerX + radius, centerY - height/2);
    ctx.lineTo(centerX + radius, centerY + height/2);
    ctx.ellipse(centerX, centerY + height/2, radius, radius/4, 0, 0, 2 * Math.PI);
}

function drawCone(ctx, centerX, centerY, radius, height) {
    ctx.moveTo(centerX - radius, centerY + height/2);
    ctx.lineTo(centerX, centerY - height/2);
    ctx.lineTo(centerX + radius, centerY + height/2);
    ctx.closePath();
    ctx.ellipse(centerX, centerY + height/2, radius, radius/4, 0, 0, 2 * Math.PI);
}

function drawDimensionLine(ctx, x1, y1, x2, y2, label, labelPosition = 'center') {
    const arrowSize = 5;
    ctx.beginPath();
    ctx.moveTo(x1, y1);
    ctx.lineTo(x2, y2);
    ctx.stroke();

    // Draw arrowheads
    drawArrow(ctx, x1, y1, x2, y2, arrowSize);
    drawArrow(ctx, x2, y2, x1, y1, arrowSize);

    // Draw label
    ctx.font = '12px Arial';
    ctx.fillStyle = 'black';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    let textX = (x1 + x2) / 2;
    let textY = (y1 + y2) / 2;

    if (labelPosition === 'bottom') {
        textY += 15; // Move text below the line
    } else if (labelPosition === 'right') {
        textX += 15; // Move text to the right of the line
        ctx.textAlign = 'left';
    }

    ctx.fillText(label, textX, textY);
}

function drawArrow(ctx, fromX, fromY, toX, toY, size) {
    const angle = Math.atan2(toY - fromY, toX - fromX);
    ctx.beginPath();
    ctx.moveTo(fromX, fromY);
    ctx.lineTo(fromX - size * Math.cos(angle - Math.PI / 6), fromY - size * Math.sin(angle - Math.PI / 6));
    ctx.moveTo(fromX, fromY);
    ctx.lineTo(fromX - size * Math.cos(angle + Math.PI / 6), fromY - size * Math.sin(angle + Math.PI / 6));
    ctx.stroke();
}

document.addEventListener('DOMContentLoaded', initializeUI);