import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# -----------------------------
# DATABASE CONNECTION
# -----------------------------
def get_connection():
    return sqlite3.connect("barriers.db")

# -----------------------------
# QUERY FUNCTIONS
# -----------------------------
def run_query(query, params=()):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    return rows

# -----------------------------
# GUI APP
# -----------------------------
class App:
    def __init__(self, root):
        self.root = root
        root.title("Afterschool Program Database")
        root.geometry("900x600")

        title = tk.Label(root, text="Afterschool Program Database",
                         font=("Arial", 20, "bold"))
        title.pack(pady=10)

        # Tabs
        tab_control = ttk.Notebook(root)
        self.tab_programs = ttk.Frame(tab_control)
        self.tab_enrollment = ttk.Frame(tab_control)
        self.tab_queries = ttk.Frame(tab_control)

        tab_control.add(self.tab_programs, text="Programs CRUD")
        tab_control.add(self.tab_enrollment, text="Enrollment CRUD")
        tab_control.add(self.tab_queries, text="Queries")
        tab_control.pack(expand=1, fill="both")

        # Load sections
        self.setup_programs_tab()
        self.setup_enrollment_tab()
        self.setup_queries_tab()

    # =============================================
    # PROGRAMS CRUD TAB
    # =============================================
    def setup_programs_tab(self):
        frame = self.tab_programs

        # Input fields
        tk.Label(frame, text="Program Name").grid(row=0, column=0)
        tk.Label(frame, text="Type").grid(row=1, column=0)
        tk.Label(frame, text="Address").grid(row=2, column=0)
        tk.Label(frame, text="Zip Code").grid(row=3, column=0)
        tk.Label(frame, text="Monthly Cost").grid(row=4, column=0)
        tk.Label(frame, text="Website").grid(row=5, column=0)

        self.p_name = tk.Entry(frame)
        self.p_type = tk.Entry(frame)
        self.p_addr = tk.Entry(frame)
        self.p_zip = tk.Entry(frame)
        self.p_cost = tk.Entry(frame)
        self.p_web = tk.Entry(frame)

        self.p_name.grid(row=0, column=1)
        self.p_type.grid(row=1, column=1)
        self.p_addr.grid(row=2, column=1)
        self.p_zip.grid(row=3, column=1)
        self.p_cost.grid(row=4, column=1)
        self.p_web.grid(row=5, column=1)

        # Buttons
        tk.Button(frame, text="Add Program", command=self.add_program).grid(row=6, column=0, pady=10)
        tk.Button(frame, text="Update Program", command=self.update_program).grid(row=6, column=1)
        tk.Button(frame, text="Delete Program", command=self.delete_program).grid(row=6, column=2)
        tk.Button(frame, text="Refresh Table", command=self.load_programs).grid(row=6, column=3)

        # Table
        columns = ("ID", "Name", "Type", "Address", "Zip", "Cost", "Website")
        self.program_table = ttk.Treeview(frame, columns=columns, show="headings")
        for col in columns:
            self.program_table.heading(col, text=col)
        self.program_table.grid(row=7, column=0, columnspan=4, sticky="nsew")

        self.load_programs()

    def add_program(self):
        query = """
        INSERT INTO Programs (program_name, program_type, address, zip_code, monthly_cost, website)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        params = (
            self.p_name.get(), self.p_type.get(), self.p_addr.get(),
            self.p_zip.get(), self.p_cost.get(), self.p_web.get()
        )
        run_query(query, params)
        messagebox.showinfo("Success", "Program added!")
        self.load_programs()

    def update_program(self):
        selected = self.program_table.selection()
        if not selected:
            return messagebox.showerror("Error", "Select a program first")

        program_id = self.program_table.item(selected[0])['values'][0]

        query = """
        UPDATE Programs SET program_name=?, program_type=?, address=?, zip_code=?, monthly_cost=?, website=?
        WHERE program_id=?
        """
        params = (
            self.p_name.get(), self.p_type.get(), self.p_addr.get(),
            self.p_zip.get(), self.p_cost.get(), self.p_web.get(),
            program_id
        )
        run_query(query, params)
        messagebox.showinfo("Updated", "Program updated!")
        self.load_programs()

    def delete_program(self):
        selected = self.program_table.selection()
        if not selected:
            return messagebox.showerror("Error", "Select a program first")

        program_id = self.program_table.item(selected[0])['values'][0]
        run_query("DELETE FROM Programs WHERE program_id=?", (program_id,))
        messagebox.showinfo("Deleted", "Program deleted!")
        self.load_programs()

    def load_programs(self):
        for row in self.program_table.get_children():
            self.program_table.delete(row)

        rows = run_query("SELECT * FROM Programs")
        for r in rows:
            self.program_table.insert("", "end", values=r)

    # =============================================
    # ENROLLMENT CRUD TAB
    # =============================================
    def setup_enrollment_tab(self):
        frame = self.tab_enrollment

        tk.Label(frame, text="Program ID").grid(row=0, column=0)
        tk.Label(frame, text="Student Name").grid(row=1, column=0)
        tk.Label(frame, text="Date Enrolled").grid(row=2, column=0)
        tk.Label(frame, text="Status").grid(row=3, column=0)

        self.e_pid = tk.Entry(frame)
        self.e_name = tk.Entry(frame)
        self.e_date = tk.Entry(frame)
        self.e_status = tk.Entry(frame)

        self.e_pid.grid(row=0, column=1)
        self.e_name.grid(row=1, column=1)
        self.e_date.grid(row=2, column=1)
        self.e_status.grid(row=3, column=1)

        tk.Button(frame, text="Add Enrollment", command=self.add_enrollment).grid(row=4, column=0, pady=10)
        tk.Button(frame, text="Update Enrollment", command=self.update_enroll).grid(row=4, column=1)
        tk.Button(frame, text="Delete Enrollment", command=self.delete_enroll).grid(row=4, column=2)
        tk.Button(frame, text="Refresh Table", command=self.load_enrollments).grid(row=4, column=3)

        columns = ("ID", "Program", "Name", "Date", "Status")
        self.enroll_table = ttk.Treeview(frame, columns=columns, show="headings")
        for col in columns:
            self.enroll_table.heading(col, text=col)
        self.enroll_table.grid(row=5, column=0, columnspan=4, sticky="nsew")

        self.load_enrollments()

    def add_enrollment(self):
        query = """
        INSERT INTO Enrollment (program_id, student_name, date_enrolled, status)
        VALUES (?, ?, ?, ?)
        """
        params = (
            self.e_pid.get(), self.e_name.get(), self.e_date.get(), self.e_status.get()
        )
        run_query(query, params)
        messagebox.showinfo("Success", "Enrollment added!")
        self.load_enrollments()

    def update_enroll(self):
        selected = self.enroll_table.selection()
        if not selected:
            return messagebox.showerror("Error", "Select a row")

        enrollment_id = self.enroll_table.item(selected[0])['values'][0]

        query = """
        UPDATE Enrollment SET program_id=?, student_name=?, date_enrolled=?, status=?
        WHERE enrollment_id=?
        """
        params = (
            self.e_pid.get(), self.e_name.get(), self.e_date.get(),
            self.e_status.get(), enrollment_id
        )
        run_query(query, params)
        messagebox.showinfo("Updated", "Enrollment updated!")
        self.load_enrollments()

    def delete_enroll(self):
        selected = self.enroll_table.selection()
        if not selected:
            return messagebox.showerror("Error", "Select a row")

        enrollment_id = self.enroll_table.item(selected[0])['values'][0]
        run_query("DELETE FROM Enrollment WHERE enrollment_id=?", (enrollment_id,))
        messagebox.showinfo("Deleted", "Enrollment removed!")
        self.load_enrollments()

    def load_enrollments(self):
        for row in self.enroll_table.get_children():
            self.enroll_table.delete(row)

        rows = run_query("SELECT * FROM Enrollment")
        for r in rows:
            self.enroll_table.insert("", "end", values=r)

    # =============================================
    # QUERIES TAB
    # =============================================
    def setup_queries_tab(self):
        frame = self.tab_queries

        tk.Label(frame, text="Analytical Queries", font=("Arial", 16, "bold")).pack(pady=10)

        tk.Button(frame, text="Programs in Low-Income ZIPs", width=40,
                  command=self.show_low_income_programs).pack(pady=5)

        tk.Button(frame, text="Average Cost by ZIP", width=40,
                  command=self.show_avg_cost).pack(pady=5)

        tk.Button(frame, text="Program Count by ZIP", width=40,
                  command=self.show_program_count).pack(pady=5)

        tk.Button(frame, text="Enrollment + Program Info", width=40,
                  command=self.show_enroll_programs).pack

    # =============================================
    # QUERY FUNCTIONS
    # =============================================

    def show_low_income_programs(self):
        result = run_query("""
        SELECT program_name, zip_code 
        FROM Programs 
        WHERE zip_code IN ('78202','78203','78207','78237')
        """)
        messagebox.showinfo("Low Income Programs", str(result))

    def show_avg_cost(self):
        result = run_query("""
        SELECT zip_code, AVG(monthly_cost)
        FROM Programs
        GROUP BY zip_code
        """)
        messagebox.showinfo("Average Cost by ZIP", str(result))

    def show_program_count(self):
        result = run_query("""
        SELECT zip_code, COUNT(*)
        FROM Programs
        GROUP BY zip_code
        """)
        messagebox.showinfo("Program Count by ZIP", str(result))

    def show_enroll_programs(self):
        result = run_query("""
        SELECT Enrollment.student_name, Programs.program_name, Enrollment.status
        FROM Enrollment
        JOIN Programs ON Enrollment.program_id = Programs.program_id
        """)
        messagebox.showinfo("Enrollment + Program Info", str(result))


# =============================================
# START THE APPLICATION
# =============================================

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
