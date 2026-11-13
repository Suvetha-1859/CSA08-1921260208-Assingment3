# Elective Registration Clash Detection

# Student registrations
python_students = {101, 102, 103, 104, 105}
java_students = {103, 104, 105, 106, 107}
ai_students = {105, 106, 108, 109}

# Union
all_students = python_students | java_students | ai_students

# Intersection
common_students = python_students & java_students & ai_students

# Difference
python_only = python_students - java_students

# Symmetric Difference
different_students = python_students ^ java_students

# Display results
print("Python Students:", python_students)
print("Java Students:", java_students)
print("AI Students:", ai_students)

print("\nAll Registered Students:", sorted(all_students))
print("Common Students:", sorted(common_students))
print("Python Only Students:", sorted(python_only))
print("Different Registrations:", sorted(different_students))

# Remove duplicate registrations
registrations = [101, 102, 103, 103, 104, 105, 105]
unique_registrations = set(registrations)

print("\nOriginal Registrations:", registrations)
print("Unique Registrations:", sorted(unique_registrations))

# Set methods
new_students = {110, 111}
python_students.update(new_students)

print("\nUpdated Python Students:", sorted(python_students))

# Membership testing
print("Is 103 registered in Python?", 103 in python_students)
print("Is 120 registered in Python?", 120 in python_students)

# Empty set test
empty_set = set()
print("Empty Set:", empty_set)
