def generate_telemetry(last_name, seed_digit, favorite_artist):
    readings = [
        seed_digit * 10,
        len(last_name) * 5,
        len(favorite_artist) * 4,
        "OFFLINE"
    ]

    for reading in readings:
        yield reading