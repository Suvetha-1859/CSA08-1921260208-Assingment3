import random
import time
import sys

# Sensor readings
readings = [25, 45, -5, 80, 110, 60, 95, 30, -10, 75]

# Method 1: Using loop and append()
cleaned_loop = []

for value in readings:
    if 0 <= value <= 100:
        cleaned_loop.append(value)

print("Using Loop:", cleaned_loop)

# Method 2: Using list comprehension
cleaned_list = [x for x in readings if 0 <= x <= 100]

print("Using List Comprehension:", cleaned_list)

# Method 3: Using map and filter
cleaned_map = list(
    filter(lambda x: 0 <= x <= 100, map(lambda x: x, readings))
)

print("Using Map and Filter:", cleaned_map)

# Alarm detection using enumerate()
print("\nHigh Temperature Alarms:")

for index, value in enumerate(cleaned_list):
    if value >= 80:
        print("Reading", index, ":", value)

# Dictionary comprehension
sensor_dict = {i: value for i, value in enumerate(cleaned_list)}
print("\nDictionary:", sensor_dict)

# Set comprehension
unique_readings = {x for x in cleaned_list}
print("Unique Readings:", unique_readings)

# Generator expression
generator = (x for x in cleaned_list if x >= 60)
print("Generator Result:", list(generator))

# Check identical results
print("\nAll Methods Same:",
      cleaned_loop == cleaned_list == cleaned_map)

# Experimental timing
print("\nExperimental Timing:")

for size in [10000, 100000, 1000000]:

    data = [random.randint(-20, 120) for _ in range(size)]

    start = time.perf_counter()
    loop_result = []
    for x in data:
        if 0 <= x <= 100:
            loop_result.append(x)
    loop_time = time.perf_counter() - start

    start = time.perf_counter()
    list_result = [x for x in data if 0 <= x <= 100]
    list_time = time.perf_counter() - start

    start = time.perf_counter()
    map_result = list(filter(lambda x: 0 <= x <= 100, data))
    map_time = time.perf_counter() - start

    print("\nSize:", size)
    print("Loop Time:", loop_time)
    print("List Comprehension Time:", list_time)
    print("Map and Filter Time:", map_time)

    print("Same Results:", loop_result == list_result == map_result)

    print("Original Memory:", sys.getsizeof(data), "bytes")
    print("Cleaned Memory:", sys.getsizeof(list_result), "bytes")
