import pandas as pd

print("VALIDATION STARTED")

df = pd.read_csv("output/patient_drug_interactions.csv")

assert not df.empty, "No drug interactions found"
assert df["severity"].isin(["High", "Medium", "Low"]).all(), "Invalid severity values"

print("VALIDATION PASSED SUCCESSFULLY")
