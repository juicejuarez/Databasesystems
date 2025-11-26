import sqlite3

# ---------------------------
# CONNECT TO DATABASE
# ---------------------------
def get_connection():
    return sqlite3.connect("barriers.db")


# ============================================
#           CRUD FOR PROGRAMS TABLE
# ============================================

# CREATE
def create_program(program_name, program_type, address, zip_code, monthly_cost, website):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Programs (program_name, program_type, address, zip_code, monthly_cost, website)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (program_name, program_type, address, zip_code, monthly_cost, website))
    conn.commit()
    conn.close()
    print("✔ Program created successfully")


# READ
def read_program(program_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Programs WHERE program_id = ?", (program_id,))
    result = cursor.fetchone()
    conn.close()
    return result


# UPDATE
def update_program(program_id, program_name=None, program_type=None, address=None, zip_code=None, monthly_cost=None, website=None):
    conn = get_connection()
    cursor = conn.cursor()

    # Build dynamic update
    fields = []
    values = []

    if program_name:
        fields.append("program_name = ?")
        values.append(program_name)
    if program_type:
        fields.append("program_type = ?")
        values.append(program_type)
    if address:
        fields.append("address = ?")
        values.append(address)
    if zip_code:
        fields.append("zip_code = ?")
        values.append(zip_code)
    if monthly_cost:
        fields.append("monthly_cost = ?")
        values.append(monthly_cost)
    if website:
        fields.append("website = ?")
        values.append(website)

    values.append(program_id)

    query = f"UPDATE Programs SET {', '.join(fields)} WHERE program_id = ?"
    cursor.execute(query, values)

    conn.commit()
    conn.close()
    print("✔ Program updated successfully")


# DELETE
def delete_program(program_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Programs WHERE program_id = ?", (program_id,))
    conn.commit()
    conn.close()
    print("✔ Program deleted successfully")


# ============================================
#         CRUD FOR ENROLLMENT TABLE
# ============================================

# CREATE
def create_enrollment(program_id, student_name, date_enrolled, status):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Enrollment (program_id, student_name, date_enrolled, status)
        VALUES (?, ?, ?, ?)
    """, (program_id, student_name, date_enrolled, status))
    conn.commit()
    conn.close()
    print("✔ Enrollment created successfully")


# READ
def read_enrollment(enrollment_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Enrollment WHERE enrollment_id = ?", (enrollment_id,))
    result = cursor.fetchone()
    conn.close()
    return result


# UPDATE
def update_enrollment(enrollment_id, program_id=None, student_name=None, date_enrolled=None, status=None):
    conn = get_connection()
    cursor = conn.cursor()

    fields = []
    values = []

    if program_id:
        fields.append("program_id = ?")
        values.append(program_id)
    if student_name:
        fields.append("student_name = ?")
        values.append(student_name)
    if date_enrolled:
        fields.append("date_enrolled = ?")
        values.append(date_enrolled)
    if status:
        fields.append("status = ?")
        values.append(status)

    values.append(enrollment_id)

    query = f"UPDATE Enrollment SET {', '.join(fields)} WHERE enrollment_id = ?"
    cursor.execute(query, values)

    conn.commit()
    conn.close()
    print("✔ Enrollment updated successfully")


# DELETE
def delete_enrollment(enrollment_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Enrollment WHERE enrollment_id = ?", (enrollment_id,))
    conn.commit()
    conn.close()
    print("✔ Enrollment deleted successfully")


# ============================================
# TESTING FUNCTIONS
# ============================================

if __name__ == "__main__":
    print("CRUD module loaded. You can now call these functions from another Python file.")
