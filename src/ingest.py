print("INGEST SCRIPT STARTED")

import pandas as pd

print("Reading raw CSV files...")

drug_df = pd.read_csv("data/raw/drug_interactions.csv")
patient_df = pd.read_csv("data/raw/patient_medications.csv")

print("Writing to processed folder...")

drug_df.to_csv("data/processed/drug_interactions_clean.csv", index=False)
patient_df.to_csv("data/processed/patient_medications_clean.csv", index=False)

print("INGEST SCRIPT COMPLETED SUCCESSFULLY")
