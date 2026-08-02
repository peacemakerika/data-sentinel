def check_types(data):
    errors = []

    for i, row in enumerate(data):
        price = row.get("price")

        if not isinstance(price, int):
            errors.append(f"Row {i}: price is not int (value={price})")

    return errors