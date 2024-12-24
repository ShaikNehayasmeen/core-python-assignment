class Patient:
  def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease

def search_patients(patients, disease):
   
    matching_patients = [patient['Name'] for patient in patients if patient['Disease'] == disease]
    return matching_patients
patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]
search_disease = "Flu"
matching_patients = search_patients_by_disease(patients, search_disease)
print(f"Patients with {search_disease}: {matching_patients}")
