import re

patients_dict = {}

regex = re.compile(r"([A-Z]{3}\d{2}(?:\d{2}|[A-Z]{2})) (\d+)")

# with open('medical_charges.txt') as data_file:
with open('exam_papers\\2024_25_winter\\q4_nhi__medical_charges\\medical_charges.txt') as data_file:
    for line in data_file:
        match = re.search(regex, line)

        if match:
            patients_dict[match.group(1)] = float(match.group(2))

    patient_id = max(patients_dict, key=patients_dict.get)

    print(f"Patients with NHI Number {patient_id} had the highest charge {patients_dict[patient_id]:.2f}")