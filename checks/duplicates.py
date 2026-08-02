def check_duplicates(data):
    seen = set()
    errors = []

    for i, row in enumerate(data):
        uid = row.get("user_id")

        if uid in seen:
            errors.append(f"Row {i}: Duplicate user_id {uid}")
        else:
            seen.add(uid)

    return errors