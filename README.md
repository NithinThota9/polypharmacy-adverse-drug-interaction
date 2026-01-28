# Polypharmacy Adverse Drug Interaction System

## Overview
This project implements an end-to-end healthcare analytics pipeline to identify adverse drug interactions for patients prescribed multiple medications (polypharmacy).

## Tech Stack
- Python
- Pandas
- CSV-based data processing

## Project Structure
- data/raw: Raw input datasets
- data/processed: Cleaned datasets
- src: Data pipeline scripts
- output: Final analytics output

## Pipeline Flow
1. Ingest raw medication and interaction data
2. Clean and normalize drug identifiers
3. Generate patient-level drug combinations
4. Detect adverse drug interactions
5. Validate analytical outputs

## Output
The final output is a patient-level table highlighting interacting drug pairs and severity levels.

## Use Case
This system mirrors real-world healthcare analytics used in pharmacy safety, claims analysis, and clinical decision support systems.


## Power BI Dashboard

The project includes a Power BI dashboard built on top of the SQL and Python outputs to visualize polypharmacy risks.

### Key Insights
- Severity distribution of adverse drug interactions
- Patient-level visibility into interacting drug pairs
- KPI highlighting high-risk interactions
- Identification of commonly occurring risky drug combinations

### Dashboard Preview
![Dashboard Overview]("C:\Users\nithi\OneDrive\Pictures\Screenshots\Screenshot 2026-01-28 105937.png")
![Patient Interactions]("C:\Users\nithi\OneDrive\Pictures\Screenshots\Screenshot 2026-01-28 110729.png")

