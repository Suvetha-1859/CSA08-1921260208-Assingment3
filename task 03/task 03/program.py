import re
from collections import Counter

calls = [
    "seeds not received seeds delayed",
    "fertiliser price high",
    "seeds price high subsidy not received"
]

STOP = {"not", "high"}

# TODO 1: Count word frequencies using dictionary get()
def frequencies(texts, stop):
    counts = {}

    for text in texts:
        words = re.findall(r'\b[a-z]+\b', text.lower())

        for word in words:
            if word not in stop:
                counts[word] = counts.get(word, 0) + 1

    return counts


# TODO 2: Find top k frequent words
def top(counts, k):
    return sorted(
        counts.items(),
        key=lambda x: (-x[1], x[0])
    )[:k]


print("Top Words:", top(frequencies(calls, STOP), 3))


# Group complaints by district
complaints = [
    ("Chennai", "Rice", "Seeds not received"),
    ("Madurai", "Wheat", "Fertiliser price high"),
    ("Chennai", "Rice", "Water supply problem"),
    ("Salem", "Cotton", "Seeds delayed")
]

districts = {}
crops = {}

for district, crop, complaint in complaints:
    districts.setdefault(district, []).append(complaint)
    crops.setdefault(crop, []).append(complaint)

print("\nDistrict-wise Complaints:")
print(districts)

print("\nCrop-wise Complaints:")
print(crops)


# Using Counter
words = []

for text in calls:
    words.extend(re.findall(r'\b[a-z]+\b', text.lower()))

counter = Counter(word for word in words if word not in STOP)

print("\nUsing Counter:", counter)


# Testing empty text and punctuation
test = ["", "SEEDS received!", "seeds, price high."]

print("\nTest Result:", frequencies(test, STOP))
