import sqlite3

def get_connection():
    return sqlite3.connect("barriers.db")


# ============================================
# 1. List all programs in LOW-INCOME ZIP codes
# ============================================
def programs_in_low_income():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT Programs.program_name, Programs.program_type, Programs.monthly_cost,
               ZipCodes.zip_code, ZipCodes.income_category
        FROM Programs
        JOIN ZipCodes ON Programs.zip_code = ZipCodes.zip_code
        WHERE ZipCodes.income_category = 'low'
    """)
    
    rows = cursor.fetchall()
    conn.close()
    return rows


# ============================================
# 2. Average program cost by ZIP code
# ============================================
def average_cost_by_zip():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT zip_code, AVG(monthly_cost)
        FROM Programs
        GROUP BY zip_code
    """)
    
    rows = cursor.fetchall()
    conn.close()
    return rows


# ============================================
# 3. Count how many programs each ZIP code has
# ============================================
def program_count_by_zip():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT zip_code, COUNT(program_id)
        FROM Programs
        GROUP BY zip_code
    """)
    
    rows = cursor.fetchall()
    conn.close()
    return rows


# ============================================
# 4. List all enrollments with program name
# ============================================
def enrollment_with_programs():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT Enrollment.enrollment_id, Enrollment.student_name, Enrollment.status,
               Programs.program_name, Programs.zip_code
        FROM Enrollment
        JOIN Programs ON Enrollment.program_id = Programs.program_id
    """)
    
    rows = cursor.fetchall()
    conn.close()
    return rows


# ============================================
# 5. Highest-rated programs (based on Reviews)
# ============================================
def highest_rated_programs():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT Programs.program_name, AVG(Reviews.rating) AS avg_rating
        FROM Reviews
        JOIN Programs ON Reviews.program_id = Programs.program_id
        GROUP BY Programs.program_id
        ORDER BY avg_rating DESC
    """)
    
    rows = cursor.fetchall()
    conn.close()
    return rows


# ============================================
# TESTING 
# ============================================
if __name__ == "__main__":
    print("\n1. Programs in Low-Income ZIPs:")
    print(programs_in_low_income())

    print("\n2. Average Cost by ZIP:")
    print(average_cost_by_zip())

    print("\n3. Program Count by ZIP:")
    print(program_count_by_zip())

    print("\n4. Enrollment + Program Info:")
    print(enrollment_with_programs())

    print("\n5. Highest Rated Programs:")
    print(highest_rated_programs())
