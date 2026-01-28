import pandas as pd
from itertools import combinations

print("INTERACTION ANALYSIS STARTED")

# Load cleaned data
patients = pd.read_csv("data/processed/patient_medications_clean.csv")
interactions = pd.read_csv("data/processed/drug_interactions_clean.csv")

results = []

# Group drugs by patient
for patient_id, group in patients.groupby("patient_id"):
    drugs = list(group["drug_name"])

    # Compare drugs in pairs
    for drug1, drug2 in combinations(drugs, 2):

        match = interactions[
            ((interactions["drug_a"] == drug1) & (interactions["drug_b"] == drug2)) |
            ((interactions["drug_a"] == drug2) & (interactions["drug_b"] == drug1))
        ]

        if not match.empty:
            results.append({
                "patient_id": patient_id,
                "drug_a": drug1,
                "drug_b": drug2,
                "severity": match.iloc[0]["severity"]
            })

# Save final results
result_df = pd.DataFrame(results)
result_df.to_csv("output/patient_drug_interactions.csv", index=False)

print("INTERACTION ANALYSIS COMPLETED")
