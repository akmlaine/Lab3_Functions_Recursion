# EXERCISE 2: RECURSIVE FAULT TRACE

LAST_NAME = "MALITAO"
STUDENT_ID = "TUPM-26-1135"
FAVORITE_ARTIST = "ADIE"

SEED_DIGIT = int(STUDENT_ID[-1])
NAME_LENGTH = len(LAST_NAME)


def generate_fault_code():
    fault_code = SEED_DIGIT * NAME_LENGTH + len(FAVORITE_ARTIST)
    return fault_code


def trace_fault(fault_level, trace=None):
    if trace is None:
        trace = []

    trace.append(f"Fault level: {fault_level}")

    if fault_level <= 0:
        return trace

    return trace_fault(fault_level - 1, trace)


def count_recursive_calls(trace):
    return len(trace)


fault_code = generate_fault_code()

# Keep the recursion trace short and readable.
starting_level = fault_code % 5 + 3

print("Generated Fault Data:")
print("Fault Code:", fault_code)
print("Starting Fault Level:", starting_level)

print("Recursive Trace:")
fault_trace = trace_fault(starting_level)

for step in fault_trace:
    print(step)

recursive_calls = count_recursive_calls(fault_trace)

print("Number of Recursive Calls:", recursive_calls)
