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

# 2. PROGRAMS TABLE - program_id as TEXT (PRG001, PRG002, etc.)
cursor.execute("""
CREATE TABLE IF NOT EXISTS Programs (
    program_id TEXT PRIMARY KEY,
    program_name TEXT NOT NULL,
    program_type TEXT,
    address TEXT,
    zip_code TEXT,
    monthly_cost INTEGER,
    website TEXT,
    FOREIGN KEY (zip_code) REFERENCES ZipCodes(zip_code)
);
""")

# 3. ENROLLMENT TABLE - enrollment_id as TEXT (ENR001, ENR002, etc.)
# Connected to program_id via foreign key
cursor.execute("""
CREATE TABLE IF NOT EXISTS Enrollment (
    enrollment_id TEXT PRIMARY KEY,
    program_id TEXT NOT NULL,
    max_capacity TEXT,
    current_enrollment TEXT,
    FOREIGN KEY (program_id) REFERENCES Programs(program_id)
);
""")

# 4. REVIEWS TABLE - review_id as TEXT (REV001, REV002, etc.)
# Connected to program_id via foreign key
cursor.execute("""
CREATE TABLE IF NOT EXISTS Reviews (
    review_id TEXT PRIMARY KEY,
    program_id TEXT NOT NULL,
    Google_rating REAL,
    reviews INTEGER,
    FOREIGN KEY (program_id) REFERENCES Programs(program_id)
);
""")

conn.commit()
conn.close()

print("Database and all tables created successfully!")
