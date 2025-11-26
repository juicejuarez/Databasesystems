import sqlite3

# ---------------------------
# CONNECT TO DATABASE
# ---------------------------
conn = sqlite3.connect("barriers.db")
cursor = conn.cursor()

# ---------------------------
# INSERT ZIP CODE DATA
# ---------------------------
zip_data = [
    ("78258", "Stone Oak", 102000, 40000, "high"),
    ("78260", "Stone Oak", 112000, 25000, "high"),
    ("78220", "Eastwood Village", 30000, 16000, "low"),
    ("78203", "Denver Heights", 27000, 13000, "low"),
    ("78202", "Dignowity Hill", 32000, 15000, "low")
]

cursor.executemany("""
INSERT OR IGNORE INTO ZipCodes (zip_code, neighborhood_name, median_income, population, income_category)
VALUES (?, ?, ?, ?, ?)
""", zip_data)

print("✔ ZIP code data inserted")

# ---------------------------
# INSERT PROGRAM DATA
# ---------------------------
program_data = [
    ("Code Ninjas", "Coding", "19179 Blanco Rd, San Antonio, TX", "78258", 180, "https://www.codeninjas.com"),
    ("Kumon Math & Reading", "Tutoring", "26108 Overlook Pkwy, San Antonio, TX", "78260", 175, "https://www.kumon.com"),
    ("Ivy Kids", "Childcare", "24278 Wilderness Oak, San Antonio, TX", "78258", 260, "https://www.ivykids.com"),
    ("YMCA Youth Program", "Sports/After School", "21654 Blanco Rd, San Antonio, TX", "78260", 95, "https://www.ymcasatx.org")
]

cursor.executemany("""
INSERT INTO Programs (program_name, program_type, address, zip_code, monthly_cost, website)
VALUES (?, ?, ?, ?, ?, ?)
""", program_data)

print("✔ Program data inserted")

# ---------------------------
# INSERT ENROLLMENT DATA
# ---------------------------
enrollment_data = [
    (1, "John Doe", "2024-11-01", "active"),
    (2, "Maria Lopez", "2024-10-20", "active"),
    (3, "Kevin Smith", "2024-09-15", "inactive")
]

cursor.executemany("""
INSERT INTO Enrollment (program_id, student_name, date_enrolled, status)
VALUES (?, ?, ?, ?)
""", enrollment_data)

print("✔ Enrollment data inserted")

# ---------------------------
# INSERT REVIEW DATA
# ---------------------------
review_data = [
    (1, 5, "Great program! My son learned to code.", "2024-11-20"),
    (2, 4, "Helpful tutoring but expensive.", "2024-10-22"),
    (3, 5, "Amazing childcare and activities!", "2024-11-10")
]

cursor.executemany("""
INSERT INTO Reviews (program_id, rating, comment, date)
VALUES (?, ?, ?, ?)
""", review_data)

print("✔ Review data inserted")

# ---------------------------
# SAVE AND CLOSE
# ---------------------------
conn.commit()
conn.close()

print("\n🎉 All data inserted successfully!")
