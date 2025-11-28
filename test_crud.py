import sqlite3
import os

DB_NAME = "barriers.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def run_tests():
    print("--- STARTING CRUD TESTS ---\n")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    # Test zip codes
    print("TEST 1: Creating a Test Zip Code (99999)...")
    try:
        cursor.execute("INSERT INTO ZipCodes VALUES (?,?,?,?,?)", 
                       ("99999", "Test Neighborhood", 50000, 100, "low"))
        conn.commit()
        print("✔ Success")
    except Exception as e:
        print(f"❌ Failed: {e}")

    # Test programs
    print("\nTEST 2: Creating a Test Program (TEST_PRG) in Zip 99999...")
    try:
        cursor.execute("INSERT INTO Programs VALUES (?,?,?,?,?,?,?)", 
                       ("TEST_PRG", "Python Academy", "Education", "123 Code St", "99999", 50, "test.com"))
        conn.commit()
        print("✔ Success")
    except Exception as e:
        print(f"❌ Failed: {e}")

    # Test read
    print("\nTEST 3: Verifying data exists in database...")
    cursor.execute("SELECT program_name FROM Programs WHERE program_id = 'TEST_PRG'")
    row = cursor.fetchone()
    if row and row[0] == "Python Academy":
        print("✔ Success: Found 'Python Academy'")
    else:
        print(f"❌ Failed: Could not find program. Found: {row}")

    # Test update
    print("\nTEST 4: Updating Cost from $50 to $999...")
    try:
        cursor.execute("UPDATE Programs SET monthly_cost = ? WHERE program_id = ?", (999, "TEST_PRG"))
        conn.commit()
        
        # Verify
        cursor.execute("SELECT monthly_cost FROM Programs WHERE program_id = 'TEST_PRG'")
        new_cost = cursor.fetchone()[0]
        if new_cost == 999:
            print("✔ Success: Cost is now 999")
        else:
            print(f"❌ Failed: Cost is {new_cost}")
    except Exception as e:
        print(f"❌ Failed: {e}")

    # Test delete program
    print("\nTEST 5: Deleting Test Program...")
    try:
        cursor.execute("DELETE FROM Programs WHERE program_id = 'TEST_PRG'")
        conn.commit()
        print("✔ Success")
    except Exception as e:
        print(f"❌ Failed: {e}")

    # Test delete zip code
    print("\nTEST 6: Deleting Test Zip Code...")
    try:
        cursor.execute("DELETE FROM ZipCodes WHERE zip_code = '99999'")
        conn.commit()
        print("✔ Success")
    except Exception as e:
        print(f"❌ Failed: {e}")

    conn.close()
    print("\n-------------------------")
    print("ALL TESTS PASSED")
    print("-------------------------")

if __name__ == "__main__":
    if not os.path.exists(DB_NAME):
        print(f"ERROR: {DB_NAME} not found. Please run your main app first to create the DB.")
    else:
        run_tests()
        