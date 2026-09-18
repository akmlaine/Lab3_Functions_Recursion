def validate_reading(reading):
    try:
        if not isinstance(reading, (int, float)):
            raise ValueError("Reading must be numeric")

        if reading < 0 or reading > 100:
            raise ValueError("Reading must be between 0 and 100")

        return True

    except ValueError:
        return False


def process_reading(reading):
    if not validate_reading(reading):
        raise ValueError("Invalid telemetry reading")

    return reading * 2


def logger(func):
    def wrapper(*args, **kwargs):
        print("Executing:", func.__name__)
        result = func(*args, **kwargs)
        print("Completed:", func.__name__)
        return result

    return wrapper


def analyze_abnormality(reading, limit, steps=0):
    print("Recursive analysis:", reading)

    if reading <= limit:
        return steps

    return analyze_abnormality(reading - 10, limit, steps + 1)