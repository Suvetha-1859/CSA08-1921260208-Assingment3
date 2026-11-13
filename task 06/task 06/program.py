import time
import sys

# Railway timetable using nested dictionaries
timetable = {
    "12601": {
        "name": "Chennai Express",
        "stops": [
            ("Chennai Central", "06:00", "06:15"),
            ("Katpadi", "08:00", "08:05"),
            ("Jolarpettai", "09:30", "09:35"),
            ("Bangalore", "12:00", "12:10")
        ],
        "days": {"Monday", "Wednesday", "Friday"}
    },

    "12602": {
        "name": "Coimbatore Express",
        "stops": [
            ("Chennai Central", "07:00", "07:20"),
            ("Salem", "10:00", "10:05"),
            ("Erode", "11:00", "11:05"),
            ("Coimbatore", "12:30", "12:40")
        ],
        "days": {"Tuesday", "Thursday", "Saturday"}
    },

    "12603": {
        "name": "Pandian Express",
        "stops": [
            ("Chennai Central", "08:00", "08:15"),
            ("Villupuram", "10:00", "10:05"),
            ("Madurai", "14:00", "14:10")
        ],
        "days": {"Monday", "Tuesday", "Friday"}
    },

    "12604": {
        "name": "Vaigai Express",
        "stops": [
            ("Chennai Central", "09:00", "09:10"),
            ("Trichy", "13:00", "13:05"),
            ("Madurai", "15:00", "15:10")
        ],
        "days": {"Wednesday", "Thursday", "Sunday"}
    },

    "12605": {
        "name": "Nilgiri Express",
        "stops": [
            ("Chennai Central", "10:00", "10:20"),
            ("Salem", "14:00", "14:05"),
            ("Coimbatore", "16:00", "16:10")
        ],
        "days": {"Monday", "Thursday", "Saturday"}
    }
}

# Print timetable neatly
print("RAILWAY TIMETABLE")

for number, details in timetable.items():
    print("\nTrain:", number, "-", details["name"])
    print("Running Days:", sorted(details["days"]))

    for station, arrival, departure in details["stops"]:
        print(station, arrival, departure)


# Find trains stopping at a station on a given day
def find_trains(data, station, day):
    results = []

    for number, details in data.items():
        if day in details["days"]:
            for stop in details["stops"]:
                if stop[0] == station:
                    results.append((number, stop[2]))

    return results


station = "Chennai Central"
day = "Monday"

results = find_trains(timetable, station, day)

# Sort by departure time
results = sorted(results, key=lambda x: x[1])

print("\nTrains at", station, "on", day)

for number, departure in results:
    print(number, "Departure:", departure)


# Access departure time of third station
print("\nThird station departure:",
      timetable["12601"]["stops"][2][2])


# Create station index
station_index = {}

for number, details in timetable.items():
    for stop in details["stops"]:
        station_index.setdefault(stop[0], []).append(number)


print("\nSTATION INDEX")
print(station_index)


# Search using station index
def indexed_search(data, index, station, day):
    results = []

    for number in index.get(station, []):
        details = data[number]

        if day in details["days"]:
            for stop in details["stops"]:
                if stop[0] == station:
                    results.append((number, stop[2]))

    return sorted(results, key=lambda x: x[1])


print("\nIndexed Search:")
print(indexed_search(timetable, station_index, station, day))


# Test unknown station
print("\nUnknown Station:")
print(indexed_search(timetable, station_index,
                     "Mumbai", "Monday"))


# Test train not running on the given day
print("\nNon-running Day:")
print(indexed_search(timetable, station_index,
                     "Chennai Central", "Sunday"))


# Generate larger timetables for experiments
def generate_timetable(count):
    stations = [
        "Chennai Central", "Salem", "Madurai",
        "Trichy", "Coimbatore", "Erode",
        "Katpadi", "Bangalore"
    ]

    days = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]

    data = {}

    for i in range(count):
        stops = []

        for j in range(4):
            station_name = stations[(i + j) % len(stations)]
            stops.append((
                station_name,
                f"{6 + j:02d}:00",
                f"{6 + j:02d}:10"
            ))

        data[str(10000 + i)] = {
            "name": "Train " + str(i + 1),
            "stops": stops,
            "days": set(days[:3])
        }

    return data


# Compare query time with and without index
print("\nPERFORMANCE COMPARISON")

for size in [100, 1000, 10000]:
    data = generate_timetable(size)

    index = {}

    for number, details in data.items():
        for stop in details["stops"]:
            index.setdefault(stop[0], []).append(number)

    start = time.perf_counter()

    for _ in range(100):
        find_trains(data, "Chennai Central", "Monday")

    normal_time = time.perf_counter() - start

    start = time.perf_counter()

    for _ in range(100):
        indexed_search(data, index, "Chennai Central", "Monday")

    indexed_time = time.perf_counter() - start

    print("\nTrains:", size)
    print("Without Index:", normal_time)
    print("With Index:", indexed_time)

    index_memory = sys.getsizeof(index)

    for key, value in index.items():
        index_memory += sys.getsizeof(key)
        index_memory += sys.getsizeof(value)

    print("Index Memory:", index_memory, "bytes")
