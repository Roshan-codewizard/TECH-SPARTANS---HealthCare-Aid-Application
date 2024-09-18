import pandas as pd

# Create sample data
data = {
    "symptoms": [
        "headache, fever",
        "cough, sore throat",
        "fatigue, fever",
        "nausea, vomiting",
        "headache, nausea",
        "muscle pain, fatigue",
        "diarrhea, stomach pain",
        "cough, fatigue",
        "chest pain, shortness of breath",
        "fever, rash",
        "fever, headache",
        "swelling, joint pain",
        "high blood sugar, frequent urination"
    ],
    "disease": [
        "cold",
        "cold",
        "flu",
        "food poisoning",
        "migraine",
        "flu",
        "food poisoning",
        "asthma",
        "heart attack",
        "measles",
        "malaria",
        "arthritis",
        "diabetes"
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('sample_symptoms_diseases.csv', index=False)

print("CSV file created: 'sample_symptoms_diseases.csv'")
