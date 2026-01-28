import sqlite3

print("RUNNING SQL PIPELINE")

# Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect("polypharmacy.db")
cursor = conn.cursor()

# Run schema
with open("sql/schema.sql", "r") as f:
    cursor.executescript(f.read())

# Load data manually (SQLite CLI .import doesn't work in Python)
cursor.execute("DELETE FROM patient_medications")
cursor.execute("DELETE FROM drug_interactions")

cursor.executemany(
    "INSERT INTO patient_medications VALUES (?, ?)",
    [
        ("P001", "warfarin"),
        ("P001", "aspirin"),
        ("P002", "metformin"),
        ("P002", "contrast dye"),
        ("P003", "ibuprofen"),
        ("P003", "lisinopril"),
    ],
)

cursor.executemany(
    "INSERT INTO drug_interactions VALUES (?, ?, ?)",
    [
        ("warfarin", "aspirin", "High"),
        ("metformin", "contrast dye", "Medium"),
        ("ibuprofen", "lisinopril", "Medium"),
    ],
)

conn.commit()

# Run interaction query
with open("sql/interaction_query.sql", "r") as f:
    query = f.read()

print("\nSQL OUTPUT:")
for row in cursor.execute(query):
    print(row)

conn.close()
print("\nSQL PIPELINE COMPLETED")
