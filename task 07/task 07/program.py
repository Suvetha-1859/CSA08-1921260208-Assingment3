import time
import re

# Normalize phone numbers
def normalize_phone(phone):
    digits = re.sub(r"\D", "", phone)

    if digits.startswith("91") and len(digits) == 12:
        digits = digits[2:]

    return digits


# Normalize names
def normalize_name(name):
    return " ".join(name.lower().split())


# Merge contacts
def merge_contacts(contacts):
    merged = {}
    phone_index = {}

    for contact in contacts:
        name = normalize_name(contact.get("name", ""))
        phones = contact.get("phones", [])
        emails = contact.get("emails", [])

        valid_phones = {
            normalize_phone(p) for p in phones
            if normalize_phone(p)
        }

        valid_emails = {
            e.strip().lower() for e in emails if e.strip()
        }

        # Find existing contact using phone or email
        keys = {
            phone_index[p] for p in valid_phones
            if p in phone_index
        }

        if not keys:
            key = next(iter(valid_phones), None)

            if key is None:
                key = next(iter(valid_emails), None)

            if key is None:
                key = "contact_" + str(len(merged) + 1)

            merged[key] = {
                "names": set(),
                "phones": set(),
                "emails": set()
            }

        else:
            key = next(iter(keys))

            # Combine groups if multiple matches are found
            for old_key in keys:
                if old_key != key and old_key in merged:
                    merged[key]["names"].update(
                        merged[old_key]["names"])
                    merged[key]["phones"].update(
                        merged[old_key]["phones"])
                    merged[key]["emails"].update(
                        merged[old_key]["emails"])

                    del merged[old_key]

                    for p, group in list(phone_index.items()):
                        if group == old_key:
                            phone_index[p] = key

        merged[key]["names"].add(name)
        merged[key]["phones"].update(valid_phones)
        merged[key]["emails"].update(valid_emails)

        for p in valid_phones:
            phone_index[p] = key

    return merged


# Sample contacts from three sources
contacts = [
    {
        "name": "Dr. Ravi",
        "phones": ["+91 98400 12345"],
        "emails": ["ravi@gmail.com"]
    },
    {
        "name": "ravi kumar",
        "phones": ["9840012345", "9876543210"],
        "emails": ["RAVI@gmail.com"]
    },
    {
        "name": "Priya",
        "phones": ["9123456789"],
        "emails": ["priya@gmail.com"]
    },
    {
        "name": "Ravi",
        "phones": [],
        "emails": ["ravi@gmail.com"]
    },
    {
        "name": "Arun",
        "phones": ["9988776655"],
        "emails": []
    }
]


# Display merged contacts
result = merge_contacts(contacts)

print("MERGED CONTACTS")

for key, details in result.items():
    print("\nContact:", key)
    print("Names:", details["names"])
    print("Phone Numbers:", details["phones"])
    print("Emails:", details["emails"])


# Performance measurement
print("\nPERFORMANCE TEST")

for size in [1000, 100000]:
    test_contacts = [
        {
            "name": "Person" + str(i),
            "phones": [str(9000000000 + i)],
            "emails": ["person" + str(i) + "@gmail.com"]
        }
        for i in range(size)
    ]

    start = time.time()
    merged_result = merge_contacts(test_contacts)
    end = time.time()

    print("Contacts:", size)
    print("Time taken:", end - start, "seconds")


print("\nPROGRAM COMPLETED SUCCESSFULLY")
