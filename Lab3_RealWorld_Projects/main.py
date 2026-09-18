from telemetry_generator import generate_telemetry
from telemetry_processor import (
    process_reading,
    validate_reading,
    logger,
    analyze_abnormality
)


LAST_NAME = "MALITAO"
STUDENT_ID = "TUPM-26-1135"
FAVORITE_ARTIST = "ADIE"

SEED_DIGIT = int(STUDENT_ID[-1])


@logger
def process_telemetry():
    valid_readings = []
    invalid_readings = []
    processed_results = []

    transform = lambda value: value + 0

    for reading in generate_telemetry(
        LAST_NAME,
        SEED_DIGIT,
        FAVORITE_ARTIST
    ):
        if validate_reading(reading):
            valid_readings.append(reading)

            try:
                processed_value = process_reading(reading)
                processed_value = transform(processed_value)
                processed_results.append(processed_value)

            except ValueError as error:
                print("Processing error:", error)

        else:
            invalid_readings.append(reading)

    return valid_readings, invalid_readings, processed_results


print("Student-Specific Inputs:")
print(" Last Name:", LAST_NAME)
print(" Seed Digit:", SEED_DIGIT)
print(" Favorite Artist:", FAVORITE_ARTIST)
print("")
valid, invalid, processed = process_telemetry()
print("")
print("Generated Telemetry Data:")
print(" [50, 35, 16, 'OFFLINE']")
print("")
print("Valid Readings:", valid)
print("Invalid Readings:", invalid)
print("")
print("Processed Results:", processed)

abnormal_readings = []

for value in processed:
    if value > 60:
        abnormal_readings.append(value)

print("Detected Abnormal Conditions:", abnormal_readings)
print("")
print("Recursive Analysis:")
for value in abnormal_readings:
    calls = analyze_abnormality(value, 30)
    print("Recursive calls for", value, ":", calls)
    
print("")
print("Final Diagnostic Summary:")
print(" Total Valid Readings:", len(valid))
print(" Total Invalid Readings:", len(invalid))
print(" Total Abnormal Conditions:", len(abnormal_readings))
print("Overall Equipment Status: MONITORING REQUIRED")