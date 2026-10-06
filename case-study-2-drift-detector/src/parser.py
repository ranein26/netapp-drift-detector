def normalize(data: dict) -> dict:
    """
    Normalize resource keys, booleans, list ordering, and null values.
    Handles lists of scalars and lists of dicts safely.
    """
    normalized = {}
    for k, v in data.items():
        key = k.lower()  # lowercase keys

        if isinstance(v, list):
            # If list contains dicts, sort by string representation
            if all(isinstance(item, dict) for item in v):
                v = sorted(v, key=lambda x: str(x))
            else:
                v = sorted(v)

        if isinstance(v, bool):
            v = str(v).lower()  # normalize booleans

        if v is None:
            v = "null"  # replace nulls

        normalized[key] = v
    return normalized
