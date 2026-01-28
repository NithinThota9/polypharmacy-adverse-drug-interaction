import pandas as pd

print("CLEANING SCRIPT STARTED")

def normalize(text):
    return text.strip().lower()

# Read processed files
drug_df = pd.read_csv("data/processed/drug_interactions_clean.csv")
patient_df = pd.read_csv("data/processed/patient_medications_clean.csv")

# Normalize text fields
drug_df["drug_a"] = drug_df["drug_a"].apply(normalize)
drug_df["drug_b"] = drug_df["drug_b"].apply(normalize)
patient_df["drug_name"] = patient_df["drug_name"].apply(normalize)

# Save cleaned data back
drug_df.to_csv("data/processed/drug_interactions_clean.csv", index=False)
patient_df.to_csv("data/processed/patient_medications_clean.csv", index=False)

print("CLEANING SCRIPT COMPLETED")
