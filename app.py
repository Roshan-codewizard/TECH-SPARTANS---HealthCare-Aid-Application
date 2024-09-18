from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import json

app = Flask(__name__)

# Load sample dataset (replace this with your actual dataset)
data = pd.read_csv('sample_symptoms_diseases.csv')  # assume this CSV has 'symptoms' and 'disease' columns

# Preprocess the dataset (tokenizing symptoms into features)
data['symptoms'] = data['symptoms'].apply(lambda x: x.lower().split(', '))

# Create X (symptoms) and y (disease) variables
X = data['symptoms']
y = data['disease']

# Basic tokenization (using unique symptoms as features)
unique_symptoms = sorted(set([item for sublist in X for item in sublist]))

def symptoms_to_vector(symptoms_list):
    """Convert list of symptoms into a binary vector."""
    return [1 if symptom in symptoms_list else 0 for symptom in unique_symptoms]

# Vectorize all symptoms in the dataset
X = np.array([symptoms_to_vector(symptoms) for symptoms in X])

# Train a RandomForestClassifier
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Dummy insurance plans data
insurance_plans = {
    'non-smoker': {
        'USA': 'Plan A - Comprehensive Coverage',
        'India': 'Plan B - Family Health Plan',
        'Canada': 'Plan C - Premium Health Insurance',
    },
    'smoker': {
        'USA': 'Plan D - Smoker Health Coverage',
        'India': 'Plan E - Smoker Health Plan',
        'Canada': 'Plan F - Extended Smoker Coverage',
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from POST request
    data = request.get_json()
    symptoms = data.get('symptoms').lower().split(', ')
    
    # Convert symptoms into a binary vector
    symptoms_vector = np.array([symptoms_to_vector(symptoms)])
    
    # Predict disease
    prediction = clf.predict(symptoms_vector)[0]
    
    # Send the result back as a JSON response
    return jsonify({'disease': prediction})

@app.route('/find-insurance', methods=['POST'])
def find_insurance():
    try:
        # Get the JSON data from the request
        data = request.get_json()
        region = data.get('region').capitalize()  # Ensure region is capitalized for matching
        smoking_status = data.get('smokingStatus').lower()  # Ensure smoking status is in lowercase

        # Validate inputs
        if not region or not smoking_status:
            return jsonify({'success': False, 'message': 'Region or smoking status missing.'})

        # Fetch insurance plan based on smoking status and region
        plan = insurance_plans.get(smoking_status, {}).get(region, None)

        if plan:
            return jsonify({'success': True, 'insurancePlan': plan})
        else:
            return jsonify({'success': False, 'message': 'No insurance plan found for the given inputs.'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
