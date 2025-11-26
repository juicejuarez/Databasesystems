import tkinter as tk
from tkinter import messagebox
import sqlite3

# Connect backend to frontend GUI
DB_NAME = "barriers.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def setup_database_and_seed():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    # Create Tables
    cursor.execute("CREATE TABLE IF NOT EXISTS ZipCodes (zip_code TEXT PRIMARY KEY, neighborhood_name TEXT, median_income INTEGER, population INTEGER, income_category TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS Programs (program_id TEXT PRIMARY KEY, program_name TEXT, program_type TEXT, address TEXT, zip_code TEXT, monthly_cost INTEGER, website TEXT, FOREIGN KEY (zip_code) REFERENCES ZipCodes(zip_code))")
    cursor.execute("CREATE TABLE IF NOT EXISTS Enrollment (enrollment_id TEXT PRIMARY KEY, program_id TEXT, max_capacity TEXT, current_enrollment TEXT, FOREIGN KEY (program_id) REFERENCES Programs(program_id))")
    cursor.execute("CREATE TABLE IF NOT EXISTS Reviews (review_id TEXT PRIMARY KEY, program_id TEXT, Google_rating REAL, reviews INTEGER, FOREIGN KEY (program_id) REFERENCES Programs(program_id))")
    
    # Seed Data if empty
    cursor.execute("SELECT count(*) FROM ZipCodes")
    if cursor.fetchone()[0] == 0:
        print("Seeding Data...")
        conn.executemany("INSERT INTO ZipCodes VALUES (?,?,?,?,?)", [
            ("78258", "Stone Oak", 102000, 40000, "high"), ("78207", "West Side", 28000, 22000, "low"), 
            ("78203", "Denver Heights", 29000, 7000, "low"), ("78260", "North Central", 112000, 25000, "high")
        ])
        conn.executemany("INSERT INTO Programs VALUES (?,?,?,?,?,?,?)", [
            ("PRG001", "Code Ninjas", "Coding", "Huebner Rd", "78258", 300, "codeninjas.com"),
            ("PRG002", "YMCA", "After School", "Iowa St", "78203", 89, "ymca.org"),
            ("PRG003", "Catholic Charities", "Support", "Cesar Chavez", "78207", 0, "ccaosa.org")
        ])
        conn.executemany("INSERT INTO Enrollment VALUES (?,?,?,?)", [
            ("ENR001", "PRG001", "NO", "IMMEDIATELY"), ("ENR002", "PRG002", "NO", "IMMEDIATELY"), 
            ("ENR003", "PRG003", "YES", "WAITLIST")
        ])
        conn.executemany("INSERT INTO Reviews VALUES (?,?,?,?)", [
            ("REV001", "PRG001", 5.0, 63), ("REV002", "PRG002", 4.4, 447), ("REV003", "PRG003", 4.3, 255)
        ])
        conn.commit()
    conn.close()

setup_database_and_seed()

# UI logic

def make_a_popup(popup_title, popup_instruction, field_labels, db_function):
    # Dynamically creates a popup with input fields based on the list of labels provided.
    
    popup = tk.Tk()
    popup.title(popup_title)
    
    # Dynamic height based on number of fields (keeps it looking good)
    window_height = 150 + (len(field_labels) * 50)
    popup.geometry(f"600x{window_height}")
    
    # Title Label
    tk.Label(popup, text=popup_instruction, font=("Arial", 12, "bold")).pack(pady=15)

    # List to store our entry widgets so we can get data from them later
    entry_widgets = []

    # The loop: This replaces the hardcoded A-M variables. 
    for label_text in field_labels:
        tk.Label(popup, text=label_text).pack()
        entry_var = tk.StringVar()
        entry = tk.Entry(popup, width=60, textvariable=entry_var)
        entry.pack(pady=2)
        entry_widgets.append(entry_var)

    def on_save_click():
        # Gather all data from the boxes into a simple list
        user_inputs = [e.get() for e in entry_widgets]
        
        try:
            # Run the specific database function
            result_text = db_function(user_inputs)
            
            # Display output in main window
            output_box.delete(1.0, tk.END)
            output_box.insert(tk.END, str(result_text))
            
            messagebox.showinfo("Success", "Operation Successful")
            popup.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    save_button = tk.Button(popup, text="EXECUTE", bg="#e0e0e0", width=20, command=on_save_click)
    save_button.pack(pady=20)
    
    popup.mainloop()


# Button functions for CRUD operations

def pressed_create():
    # We only list the 7 fields we actually need. No empty strings!
    fields = ["Program ID", "Name", "Type", "Address", "Zip Code", "Cost", "Website"]
    
    def logic(vals):
        conn = get_connection()
        conn.execute("INSERT INTO Programs VALUES (?,?,?,?,?,?,?)", vals)
        conn.commit()
        conn.close()
        return f"Created Program: {vals[1]}"

    make_a_popup("CREATE", "Enter New Program Details:", fields, logic)

def pressed_read():
    fields = ["Enter Zip Code to Search"]
    
    def logic(vals):
        conn = get_connection()
        cursor = conn.execute("SELECT program_name, monthly_cost FROM Programs WHERE zip_code = ?", (vals[0],))
        rows = cursor.fetchall()
        conn.close()
        return "Programs Found:\n" + "\n".join([str(r) for r in rows])

    make_a_popup("READ", "Search by Zip Code:", fields, logic)

def pressed_update():
    fields = ["Program ID to Update", "New Monthly Cost"]
    
    def logic(vals):
        conn = get_connection()
        conn.execute("UPDATE Programs SET monthly_cost = ? WHERE program_id = ?", (vals[1], vals[0]))
        conn.commit()
        conn.close()
        return f"Updated Program {vals[0]} cost to ${vals[1]}"

    make_a_popup("UPDATE", "Update Program Cost:", fields, logic)

def pressed_delete():
    fields = ["Program ID to Delete"]
    
    def logic(vals):
        conn = get_connection()
        conn.execute("DELETE FROM Programs WHERE program_id = ?", (vals[0],))
        conn.commit()
        conn.close()
        return f"Deleted Program {vals[0]}"

    make_a_popup("DELETE", "Delete Program Record:", fields, logic)

def pressed_custom_query():
    fields = ["Enter SQL Query"]
    
    def logic(vals):
        conn = get_connection()
        cursor = conn.execute(vals[0])
        rows = cursor.fetchall()
        conn.commit()
        conn.close()
        return rows

    make_a_popup("CUSTOM SQL", "Run Manual Database Query:", fields, logic)

# Query functions for analytics

def query_income_barrier():
    fields = ["Enter Income Level ('high' or 'low')"]
    
    def logic(vals):
        conn = get_connection()
        sql = """SELECT p.program_name, p.monthly_cost, z.income_category 
                 FROM Programs p JOIN ZipCodes z ON p.zip_code = z.zip_code 
                 WHERE z.income_category = ?"""
        cursor = conn.execute(sql, (vals[0],))
        rows = cursor.fetchall()
        conn.close()
        return "INCOME ANALYSIS RESULTS:\n" + "\n".join([f"{r[0]} (${r[1]}) - {r[2]}" for r in rows])

    make_a_popup("INCOME BARRIER", "Find Programs by Area Income:", fields, logic)

def query_budget_limit():
    fields = ["Max Monthly Budget ($)"]
    
    def logic(vals):
        conn = get_connection()
        sql = "SELECT program_name, monthly_cost FROM Programs WHERE monthly_cost <= ?"
        cursor = conn.execute(sql, (vals[0],))
        rows = cursor.fetchall()
        conn.close()
        return "BUDGET SEARCH RESULTS:\n" + "\n".join([f"{r[0]} - ${r[1]}" for r in rows])

    make_a_popup("BUDGET SEARCH", "Find Affordable Programs:", fields, logic)

def query_quality_ratings():
    fields = ["Minimum Star Rating (1-5)"]
    
    def logic(vals):
        conn = get_connection()
        sql = """SELECT p.program_name, r.Google_rating FROM Programs p 
                 JOIN Reviews r ON p.program_id = r.program_id 
                 WHERE r.Google_rating >= ?"""
        cursor = conn.execute(sql, (vals[0],))
        rows = cursor.fetchall()
        conn.close()
        return "HIGH QUALITY RESULTS:\n" + "\n".join([f"{r[0]} - {r[1]} Stars" for r in rows])

    make_a_popup("QUALITY FILTER", "Search by Rating:", fields, logic)

def query_waitlist_status():
    fields = ["Check Status (e.g. WAITLIST)"]
    
    def logic(vals):
        conn = get_connection()
        sql = """SELECT p.program_name, e.current_enrollment FROM Enrollment e 
                 JOIN Programs p ON e.program_id = p.program_id 
                 WHERE e.current_enrollment = ?"""
        cursor = conn.execute(sql, (vals[0],))
        rows = cursor.fetchall()
        conn.close()
        return "AVAILABILITY RESULTS:\n" + "\n".join([f"{r[0]} is {r[1]}" for r in rows])

    make_a_popup("WAITLIST CHECK", "Check Program Availability:", fields, logic)

def query_zip_search():
    fields = ["Enter Zip Code"]
    
    def logic(vals):
        conn = get_connection()
        sql = "SELECT program_name, address FROM Programs WHERE zip_code = ?"
        cursor = conn.execute(sql, (vals[0],))
        rows = cursor.fetchall()
        conn.close()
        return "GEOGRAPHIC RESULTS:\n" + "\n".join([f"{r[0]} at {r[1]}" for r in rows])

    make_a_popup("GEO SEARCH", "Search Programs by Location:", fields, logic)


# Button functions for main window layout
window = tk.Tk()
window.title("BREAKING BARRIERS: DATABASE PROJECT")
window.geometry("1000x650")

tk.Label(window, text="BREAKING BARRIERS DATABASE SYSTEM", font=("Arial", 18, "bold")).place(x=20, y=10)

# CRUD section
tk.Label(window, text="MANAGE RECORDS", font=("Arial", 10, "bold"), fg="#555").place(x=20, y=50)
tk.Button(window, text="CREATE (Add Program)", width=30, command=pressed_create).place(x=20, y=80)
tk.Button(window, text="READ (Search by Zip)", width=30, command=pressed_read).place(x=20, y=120)
tk.Button(window, text="UPDATE (Modify Cost)", width=30, command=pressed_update).place(x=20, y=160)
tk.Button(window, text="DELETE (Remove Program)", width=30, command=pressed_delete).place(x=20, y=200)
tk.Button(window, text="CUSTOM SQL QUERY", width=30, command=pressed_custom_query).place(x=20, y=240)

# Analytics section
tk.Label(window, text="ANALYTICAL QUERIES", font=("Arial", 10, "bold"), fg="#555").place(x=20, y=290)
tk.Button(window, text="1. Income Barrier Analysis", width=30, command=query_income_barrier).place(x=20, y=320)
tk.Button(window, text="2. Budget Search", width=30, command=query_budget_limit).place(x=20, y=360)
tk.Button(window, text="3. Quality/Ratings Filter", width=30, command=query_quality_ratings).place(x=20, y=400)
tk.Button(window, text="4. Waitlist Availability Check", width=30, command=query_waitlist_status).place(x=20, y=440)
tk.Button(window, text="5. Geographic Search", width=30, command=query_zip_search).place(x=20, y=480)

# Output box
tk.Label(window, text="DATABASE RESULTS:", font=("Arial", 10, "bold")).place(x=300, y=50)
output_box = tk.Text(window, width=80, height=32, bg="#f0f0f0", borderwidth=2, relief="sunken")
output_box.place(x=300, y=80)

window.mainloop()
