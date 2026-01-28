-- Table storing which drugs each patient is taking
CREATE TABLE patient_medications (
    patient_id TEXT,
    drug_name TEXT
);

-- Table storing known adverse drug interactions
CREATE TABLE drug_interactions (
    drug_a TEXT,
    drug_b TEXT,
    severity TEXT
);
