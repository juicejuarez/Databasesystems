import sqlite3

# Create / connect to DB
conn = sqlite3.connect("barriers.db")
cursor = conn.cursor()

# 1. ZIP CODES TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS ZipCodes (
    zip_code TEXT PRIMARY KEY,
    neighborhood_name TEXT,
    median_income INTEGER,
    population INTEGER,
    income_category TEXT
);
""")

# 2. PROGRAMS TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS Programs (
    program_id INTEGER PRIMARY KEY AUTOINCREMENT,
    program_name TEXT NOT NULL,
    program_type TEXT,
    address TEXT,
    zip_code TEXT,
    monthly_cost INTEGER,
    website TEXT,
    FOREIGN KEY (zip_code) REFERENCES ZipCodes(zip_code)
);
""")

# 3. ENROLLMENT TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS Enrollment (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    program_id INTEGER NOT NULL,
    student_name TEXT,
    date_enrolled TEXT,
    status TEXT,
    FOREIGN KEY (program_id) REFERENCES Programs(program_id)
);
""")

# 4. REVIEWS TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS Reviews (
    review_id INTEGER PRIMARY KEY AUTOINCREMENT,
    program_id INTEGER NOT NULL,
    rating INTEGER,
    comment TEXT,
    date TEXT,
    FOREIGN KEY (program_id) REFERENCES Programs(program_id)
);
""")

conn.commit()
conn.close()

print("Database and all tables created successfully!")
