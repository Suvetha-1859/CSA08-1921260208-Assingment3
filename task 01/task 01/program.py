import random
import time

# Generate 365 rainfall readings
readings = [random.randint(0, 100) for i in range(365)]

# Weekly totals
weekly = [sum(readings[i:i+7])
          for i in range(0, 365, 7)]

print("Weekly Rainfall Totals:", weekly)

# Maximum and minimum rainfall
print("Maximum Rainfall:", max(readings))
print("Minimum Rainfall:", min(readings))

print("Maximum Position:", readings.index(max(readings)))
print("Minimum Position:", readings.index(min(readings)))

# 7-day moving average
averages = []

for i in range(len(readings) - 6):
    avg = sum(readings[i:i+7]) / 7
    averages.append(avg)

print("7-Day Moving Average:", averages)

# Dry days
dry_days = [i+1 for i in range(365) if readings[i] == 0]

print("Dry Days:", dry_days)
