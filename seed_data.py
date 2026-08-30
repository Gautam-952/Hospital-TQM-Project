import db

additional_patients = [
    ("Aarav Mehta", 37, "Cardiology", "2026-08-10"),
    ("Diya Sengupta", 24, "Dermatology", "2026-08-11"),
    ("Rohan Kulkarni", 58, "Orthopedics", "2026-08-12"),
    ("Meera Joshi", 6, "Pediatrics", "2026-08-13"),
    ("Kavita Reddy", 42, "Neurology", "2026-08-14"),
    ("Farhan Akhtar", 67, "Cardiology", "2026-08-15"),
    ("Pooja Hegde", 29, "General Medicine", "2026-08-16"),
    ("Nikhil Chopra", 52, "Orthopedics", "2026-08-17"),
    ("Tanvi Deshmukh", 11, "Pediatrics", "2026-08-18"),
    ("Manish Pandey", 49, "Gastroenterology", "2026-08-19"),
    ("Ishaan Malhotra", 33, "Dermatology", "2026-08-20"),
    ("Ritu Singhal", 71, "Cardiology", "2026-08-21"),
    ("Aditya Rawat", 15, "Pediatrics", "2026-08-22"),
    ("Simran Kaur", 26, "General Medicine", "2026-08-23"),
    ("Deepak Chawla", 60, "Neurology", "2026-08-24"),
    ("Anjali Saxena", 39, "Gastroenterology", "2026-08-25"),
    ("Harshvardhan Rao", 46, "Orthopedics", "2026-08-26"),
    ("Neha Bhatt", 22, "Dermatology", "2026-08-27"),
    ("Suresh Menon", 64, "Cardiology", "2026-08-28"),
    ("Bhavna Trivedi", 55, "General Medicine", "2026-08-29"),
]

for name, age, disease, date in additional_patients:
    db.add_patient(name, age, disease, date)

print(f"Successfully inserted {len(additional_patients)} records via db.py.")