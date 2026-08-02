from utils.loader import load_data
from checks.schema import check_schema
from checks.types import check_types
from checks.duplicates import check_duplicates
# Load data
data = load_data("data/sample.json")

# Define expected structure
expected_keys = {"user_id", "action", "price"}

#Define errors
errors = []

# Run schema|types|duplicates check
errors += check_schema(data, expected_keys)
errors += check_types(data)
errors += check_duplicates(data)

# Output results
print("\n--- SCHEMA CHECK ---\n")

if not errors:
    print("correct ✅")
else:
    for err in errors:
        print("❌", err)