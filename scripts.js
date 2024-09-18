// Disease Prediction Functionality
document.getElementById('disease-form').addEventListener('submit', function(event) {
    event.preventDefault();

    // Collect user input
    const symptoms = document.getElementById('symptoms').value;

    // Send a POST request to the Flask backend
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ symptoms: symptoms })
    })
    .then(response => response.json())
    .then(data => {
        // Display the result in the disease-result div
        document.getElementById('disease-result').innerHTML = `Predicted Disease: ${data.disease}`;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

// BMI Calculation Functionality
document.getElementById('bmi-form').addEventListener('submit', function(event) {
    event.preventDefault();

    // Collect user input
    const height = parseFloat(document.getElementById('height').value);
    const weight = parseFloat(document.getElementById('weight').value);

    // Calculate BMI
    if (height > 0 && weight > 0) {
        const bmi = (weight / ((height / 100) ** 2)).toFixed(2);
        let category;

        // Determine BMI category
        if (bmi < 18.5) {
            category = "Underweight";
        } else if (bmi >= 18.5 && bmi < 24.9) {
            category = "Normal weight";
        } else if (bmi >= 25 && bmi < 29.9) {
            category = "Overweight";
        } else {
            category = "Obesity";
        }

        // Display the result in the bmi-result div
        document.getElementById('bmi-result').innerHTML = `Your BMI is ${bmi} (${category}).`;
    } else {
        document.getElementById('bmi-result').innerHTML = "Please enter valid height and weight values.";
    }
});

// Insurance Plan Functionality
document.getElementById('insurance-form').addEventListener('submit', function(event) {
    event.preventDefault();

    // Collect user input
    const region = document.getElementById('region-insurance').value;
    const smokingStatus = document.getElementById('smoking-insurance').value;

    // Validate inputs
    if (region && smokingStatus) {
        // Send a POST request to the Flask backend for insurance plans
        fetch('/find-insurance', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                region: region,
                smokingStatus: smokingStatus
            })
        })
        .then(response => response.json())
        .then(data => {
            // Display the result in the insurance-result div
            if (data.success) {
                document.getElementById('insurance-result').innerHTML = `Recommended Insurance Plan: ${data.insurancePlan}`;
            } else {
                document.getElementById('insurance-result').innerHTML = `No insurance plans found for your inputs.`;
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    } else {
        document.getElementById('insurance-result').innerHTML = "Please provide valid inputs for region and smoking status.";
    }
});
