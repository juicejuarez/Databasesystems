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
    ("78258", "Stone_Oak", 102000, 40000, "high"),
    ("78260", "Stone Oak", 112000, 25000, "high"),
    ("78220", "eastwood Village", 30000, 16000, "low"),
    ("78204", "Southtown", 34000, 37000, "low"),
    ("78203", "Denver Heights", 29000, 7000, "low"),
    ("78207", "southcentral SA", 40000, 22000, "low"),
    ("78226", "southwest side SA", 32000, 8000, "low")
]

cursor.executemany("""
INSERT OR IGNORE INTO ZipCodes (zip_code, neighborhood_name, median_income, population, income_category)
VALUES (?, ?, ?, ?, ?)
""", zip_data)

print("✔ ZIP code data inserted")

# ---------------------------
# INSERT PROGRAM DATA (All 12 programs with PRG001, PRG002, etc.)
# ---------------------------
program_data = [
    ("PRG001", "Code_ninjas", "Coding", "20322 Huebr, San Antonio, TX", "78258", 300, "Coding For Kids in"),
    ("PRG002", "ADC's best afterscho", "After School", "26108 Overlo, San Antonio, TX", "78260", 325, "The Best After Sch"),
    ("PRG003", "edQuisitive_montess", "Montessori", "22215 Wilde, San Antonio, TX", "78258", 155, "After School Prog"),
    ("PRG004", "IVY_kids ELC", "Childcare", "24278 Wilde, San Antonio, TX", "78258", None, "Preschool and Da"),
    ("PRG005", "Kin", "After School", "various, San Antonio, TX", "78258", 270, "Kids Involvement"),
    ("PRG006", "Kumon", "Tutoring", "19239 Stone, San Antonio, TX", "78258", 175, "After School Math"),
    ("PRG007", "Youth_Movement_art", "Arts/Athletics", "510 S. Braun, San Antonio, TX", "78203", None, "HOME | Youth Mo"),
    ("PRG008", "New_Kids_On_The_BI", "After School", "623 S WW W, San Antonio, TX", "78220", 140, "New Kids On The"),
    ("PRG009", "Boys_&_Girls_club", "After School", "123 Ralph Av, San Antonio, TX", "78204", 150, "https://begreatsa"),
    ("PRG010", "YMCA", "After School", "1213 lowa St, San Antonio, TX", "78203", 89, "After School | YM"),
    ("PRG011", "Chatolic Charities aft", "After School", "1801 w. Cesa, San Antonio, TX", "78207", 0, "After School Prog"),
    ("PRG012", "After School Chanller", "After School", "various, San Antonio, TX", "78226", 260, "After School Chal")
]

cursor.executemany("""
INSERT OR IGNORE INTO Programs (program_id, program_name, program_type, address, zip_code, monthly_cost, website)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", program_data)

print("✔ Program data inserted")

# ---------------------------
# INSERT ENROLLMENT DATA (ENR001, ENR002, etc. connected to PRG001, PRG002, etc.)
# ---------------------------
enrollment_data = [
    ("ENR001", "PRG001", "NO", "IMMEDIATELY"),
    ("ENR002", "PRG002", "NO", "IMMEDIATELY"),
    ("ENR003", "PRG003", "NO", "IMMEDIATELY"),
    ("ENR004", "PRG004", "NO", "IMMEDIATELY"),
    ("ENR005", "PRG005", "NO", "IMMEDIATELY"),
    ("ENR006", "PRG006", "NO", "IMMEDIATELY"),
    ("ENR007", "PRG007", "YES", "WAITLIST"),
    ("ENR008", "PRG008", "YES", "WAITLIST"),
    ("ENR009", "PRG009", "NO", "IMMEDIATELY"),
    ("ENR010", "PRG010", "NO", "IMMEDIATELY"),
    ("ENR011", "PRG011", "NO", "IMMEDIATELY"),
    ("ENR012", "PRG012", "NO", "IMMEDIATELY")
]

cursor.executemany("""
INSERT OR IGNORE INTO Enrollment (enrollment_id, program_id, max_capacity, current_enrollment)
VALUES (?, ?, ?, ?)
""", enrollment_data)

print("✔ Enrollment data inserted")

# ---------------------------
# INSERT REVIEW DATA (REV001, REV002, etc. connected to PRG001, PRG002, etc.)
# ---------------------------
review_data = [
    ("REV001", "PRG001", 5.0, 63),
    ("REV002", "PRG002", 4.7, 43),
    ("REV003", "PRG003", 4.1, 13),
    ("REV004", "PRG004", 5.0, 6),
    ("REV005", "PRG005", 4.3, 9),
    ("REV006", "PRG006", 4.6, 16),
    ("REV007", "PRG007", 4.8, 4),
    ("REV008", "PRG008", 4.6, 10),
    ("REV009", "PRG009", 4.6, 94),
    ("REV010", "PRG010", 4.4, 447),
    ("REV011", "PRG011", 4.3, 255),
    ("REV012", "PRG012", None, None)  # N/A values
]

cursor.executemany("""
INSERT OR IGNORE INTO Reviews (review_id, program_id, Google_rating, reviews)
VALUES (?, ?, ?, ?)
""", review_data)

print("✔ Review data inserted")

# ---------------------------
# SAVE AND CLOSE
# ---------------------------
conn.commit()
conn.close()

print("\n🎉 All data inserted successfully!")
