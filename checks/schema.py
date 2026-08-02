def check_schema(data, expected_keys):
    errors = []

    for i, row in enumerate(data):
        if set(row.keys()) != expected_keys:
            errors.append(f"Row {i}: Schema mismatch {row.keys()}")

    return errors