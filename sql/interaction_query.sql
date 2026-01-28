SELECT
    p1.patient_id,
    p1.drug_name AS drug_a,
    p2.drug_name AS drug_b,
    di.severity
FROM patient_medications p1
JOIN patient_medications p2
    ON p1.patient_id = p2.patient_id
   AND p1.drug_name < p2.drug_name
JOIN drug_interactions di
    ON (
        (p1.drug_name = di.drug_a AND p2.drug_name = di.drug_b)
     OR (p1.drug_name = di.drug_b AND p2.drug_name = di.drug_a)
    );
