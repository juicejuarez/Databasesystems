import tkinter as tk
from tkinter import messagebox
import sqlite3

# Connect backend to frontend GUI
DB_NAME = "barriers.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

# UI logic
def make_a_popup(popup_title, popup_instruction, field_labels, db_function):
    popup = tk.Tk()
    popup.title(popup_title)
    
    window_height = 150 + (len(field_labels) * 50)
    popup.geometry(f"600x{window_height}")
    
    tk.Label(popup, text=popup_instruction, font=("Arial", 12, "bold")).pack(pady=15)

    entry_widgets = []

    for label_text in field_labels:
        tk.Label(popup, text=label_text).pack()
        # Explicitly link the variable to the popup window
        entry_var = tk.StringVar(master=popup) 
        entry = tk.Entry(popup, width=60, textvariable=entry_var)
        entry.pack(pady=2)
        entry_widgets.append(entry_var)

    def on_save_click():
        # Get data and strip extra spaces immediately
        user_inputs = [e.get().strip() for e in entry_widgets]
        
        try:
            result_text = db_function(user_inputs)
            output_box.delete(1.0, tk.END)
            output_box.insert(tk.END, str(result_text))
            popup.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    save_button = tk.Button(popup, text="EXECUTE", bg="#e0e0e0", width=20, command=on_save_click)
    save_button.pack(pady=20)
    
    popup.mainloop()


# CRUD for Programs

def pressed_create_program():
    fields = ["Program ID", "Name", "Type", "Address", "Zip Code", "Cost", "Website"]
    
    def logic(vals):
        conn = get_connection()
        conn.execute("INSERT INTO Programs VALUES (?,?,?,?,?,?,?)", vals)
        conn.commit()
        conn.close()
        return f"Created Program: {vals[1]}"

    make_a_popup("CREATE PROGRAM", "Enter New Program Details:", fields, logic)

def pressed_read_programs():
    # Reads ALL programs
    conn = get_connection()
    cursor = conn.execute("SELECT program_id, program_name, monthly_cost, zip_code FROM Programs")
    rows = cursor.fetchall()
    conn.close()
    
    if not rows:
        result = "No programs found."
    else:
        result = "ALL PROGRAMS:\n" + "-"*30 + "\n"
        for row in rows:
            result += f"[{row[0]}] {row[1]} - ${row[2]} (Zip: {row[3]})\n"
    
    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, result)

def pressed_update_program():
    fields = ["Program ID to Update", "New Monthly Cost"]
    
    def logic(vals):
        conn = get_connection()
        conn.execute("UPDATE Programs SET monthly_cost = ? WHERE program_id = ?", (vals[1], vals[0]))
        conn.commit()
        conn.close()
        return f"Updated Program {vals[0]} cost to ${vals[1]}"

    make_a_popup("UPDATE PROGRAM", "Update Program Cost:", fields, logic)

def pressed_delete_program():
    fields = ["Program ID to Delete"]
    
    def logic(vals):
        conn = get_connection()
        conn.execute("DELETE FROM Programs WHERE program_id = ?", (vals[0],))
        conn.commit()
        conn.close()
        return f"Deleted Program {vals[0]}"

    make_a_popup("DELETE PROGRAM", "Delete Program Record:", fields, logic)


# CRUD for neighborhoods

def pressed_create_zipcode():
    # Fixed the list format here
    fields = ["Zip Code", "Neighborhood", "Median Income", "Population", "Income Category"]
    
    def logic(vals):
        conn = get_connection()
        conn.execute("INSERT INTO ZipCodes VALUES (?,?,?,?,?)", vals)
        conn.commit()
        conn.close()
        return f"Created Zip Code: {vals[0]}"

    make_a_popup("CREATE ZIP", "Enter New Neighborhood Details:", fields, logic)

def pressed_read_zipcodes():
    conn = get_connection()
    cursor = conn.execute("SELECT * FROM ZipCodes")
    rows = cursor.fetchall()
    conn.close()
    
    if not rows:
        result = "No zip codes found."
    else:
        result = "ALL NEIGHBORHOODS:\n" + "-"*30 + "\n"
        for row in rows:
            result += f"Zip: {row[0]} | {row[1]} | Pop: {row[3]} | {row[4]} Income\n"
    
    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, result)

def pressed_update_zipcode():
    fields = ["Zip Code to Update", "New Population Count"]
    
    def logic(vals):
        conn = get_connection()
        conn.execute("UPDATE ZipCodes SET population = ? WHERE zip_code = ?", (vals[1], vals[0]))
        conn.commit()
        conn.close()
        return f"Updated Population for Zip {vals[0]} to {vals[1]}"

    make_a_popup("UPDATE ZIP", "Update Neighborhood Population:", fields, logic)

def pressed_delete_zipcode():
    fields = ["Zip Code to Delete"]
    
    def logic(vals):
        conn = get_connection()
        # Note: This will fail if Programs still exist in this Zip Code due to Foreign Keys
        try:
            conn.execute("DELETE FROM ZipCodes WHERE zip_code = ?", (vals[0],))
            conn.commit()
            conn.close()
            return f"Deleted Zip Code {vals[0]}"
        except sqlite3.IntegrityError:
            return "Error: Cannot delete this Zip Code because Programs are still linked to it.\nDelete the Programs first."

    make_a_popup("DELETE ZIP", "Delete Neighborhood Record:", fields, logic)


# Queries

def query_income_barrier():
    fields = ["Enter Income Level ('high' or 'low')"]
    def logic(vals):
        search_term = vals[0].strip().lower()
        conn = get_connection()
        sql = """SELECT p.program_name, p.monthly_cost, z.income_category 
                 FROM Programs p JOIN ZipCodes z ON TRIM(p.zip_code) = TRIM(z.zip_code) 
                 WHERE LOWER(TRIM(z.income_category)) = ?"""
        cursor = conn.execute(sql, (search_term,))
        rows = cursor.fetchall()
        conn.close()
        if not rows: return f"No results for '{search_term}'."
        return "INCOME ANALYSIS RESULTS:\n" + "\n".join([f"{r[0]} (${r[1]}) - {r[2]}" for r in rows])
    make_a_popup("INCOME BARRIER", "Find Programs by Area Income:", fields, logic)
    
def query_budget_limit():
    fields = ["Max Monthly Budget ($)"]
    def logic(vals):
        conn = get_connection()
        budget = vals[0].strip()
        sql = "SELECT program_name, monthly_cost FROM Programs WHERE monthly_cost <= ?"
        cursor = conn.execute(sql, (budget,))
        rows = cursor.fetchall()
        conn.close()
        if not rows: return "No programs found within this budget."
        return "BUDGET SEARCH RESULTS:\n" + "\n".join([f"{r[0]} - ${r[1]}" for r in rows])
    make_a_popup("BUDGET SEARCH", "Find Affordable Programs:", fields, logic)

def query_quality_ratings():
    fields = ["Minimum Star Rating (1-5)"]
    def logic(vals):
        conn = get_connection()
        sql = """SELECT p.program_name, r.Google_rating FROM Programs p 
                 JOIN Reviews r ON p.program_id = r.program_id 
                 WHERE r.Google_rating >= CAST(? AS REAL)"""
        cursor = conn.execute(sql, (vals[0],))
        rows = cursor.fetchall()
        conn.close()
        if not rows: return "No programs found with this rating."
        return "HIGH QUALITY RESULTS:\n" + "\n".join([f"{r[0]} - {r[1]} Stars" for r in rows])
    make_a_popup("QUALITY FILTER", "Search by Rating:", fields, logic)

def query_waitlist_status():
    fields = ["Check Status (e.g. WAITLIST)"]
    def logic(vals):
        search_term = vals[0].strip().upper()
        conn = get_connection()
        sql = """SELECT p.program_name, e.current_enrollment FROM Enrollment e 
                 JOIN Programs p ON e.program_id = p.program_id 
                 WHERE UPPER(e.current_enrollment) = ?"""
        cursor = conn.execute(sql, (search_term,))
        rows = cursor.fetchall()
        conn.close()
        if not rows: return f"No programs found with status '{search_term}'"
        return "AVAILABILITY RESULTS:\n" + "\n".join([f"{r[0]} is {r[1]}" for r in rows])
    make_a_popup("WAITLIST CHECK", "Check Program Availability:", fields, logic)

def query_zip_search():
    fields = ["Enter Zip Code"]
    def logic(vals):
        zip_search = vals[0].strip()
        conn = get_connection()
        sql = "SELECT program_name, address FROM Programs WHERE TRIM(zip_code) = ?"
        cursor = conn.execute(sql, (zip_search,))
        rows = cursor.fetchall()
        conn.close()
        if not rows: return f"No programs found in Zip Code {zip_search}"
        return "GEOGRAPHIC RESULTS:\n" + "\n".join([f"{r[0]} at {r[1]}" for r in rows])
    make_a_popup("GEO SEARCH", "Search Programs by Location:", fields, logic)


# Window Layout

window = tk.Tk()
window.title("BREAKING BARRIERS: DATABASE PROJECT")
window.geometry("1000x700")

tk.Label(window, text="BREAKING BARRIERS DATABASE SYSTEM", font=("Arial", 18, "bold")).place(x=20, y=10)

# Manage Programs
tk.Label(window, text="MANAGE PROGRAMS", font=("Arial", 10, "bold"), fg="blue").place(x=20, y=50)
tk.Button(window, text="CREATE (Add Program)", width=30, command=pressed_create_program).place(x=20, y=80)
tk.Button(window, text="READ (View All Programs)", width=30, command=pressed_read_programs).place(x=20, y=110)
tk.Button(window, text="UPDATE (Modify Cost)", width=30, command=pressed_update_program).place(x=20, y=140)
tk.Button(window, text="DELETE (Remove Program)", width=30, command=pressed_delete_program).place(x=20, y=170)

# Manage Zipcodes
tk.Label(window, text="MANAGE ZIPCODES", font=("Arial", 10, "bold"), fg="green").place(x=20, y=210)
tk.Button(window, text="CREATE (Add Zip Code)", width=30, command=pressed_create_zipcode).place(x=20, y=240)
tk.Button(window, text="READ (View All Zips)", width=30, command=pressed_read_zipcodes).place(x=20, y=270)
tk.Button(window, text="UPDATE (Modify Population)", width=30, command=pressed_update_zipcode).place(x=20, y=300)
tk.Button(window, text="DELETE (Remove Zip)", width=30, command=pressed_delete_zipcode).place(x=20, y=330)

# Manage Queries
tk.Label(window, text="ANALYTICAL QUERIES", font=("Arial", 10, "bold"), fg="red").place(x=20, y=370)
tk.Button(window, text="1. Income Barrier Analysis", width=30, command=query_income_barrier).place(x=20, y=400)
tk.Button(window, text="2. Budget Search", width=30, command=query_budget_limit).place(x=20, y=430)
tk.Button(window, text="3. Quality/Ratings Filter", width=30, command=query_quality_ratings).place(x=20, y=460)
tk.Button(window, text="4. Waitlist Availability Check", width=30, command=query_waitlist_status).place(x=20, y=490)
tk.Button(window, text="5. Geographic Search", width=30, command=query_zip_search).place(x=20, y=520)

# Output box
tk.Label(window, text="DATABASE RESULTS:", font=("Arial", 10, "bold")).place(x=300, y=50)
output_box = tk.Text(window, width=80, height=35, bg="#f0f0f0", borderwidth=2, relief="sunken")
output_box.place(x=300, y=80)

window.mainloop()
