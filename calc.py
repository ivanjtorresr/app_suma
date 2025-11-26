def sum_two(a, b):
    try:
        return float(a) + float(b)
    except Exception as e:
        raise ValueError("Entradas no numéricas") from e
