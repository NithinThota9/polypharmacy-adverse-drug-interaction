-- Set CSV mode
.mode csv

-- Load patient medication data
.import data/raw/patient_medications.csv patient_medications

-- Load drug interaction reference data
.import data/raw/drug_interactions.csv drug_interactions
