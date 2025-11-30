**Breaking Barriers: After-School Program Database System **
This project is a Python + SQLite database application designed to help identify barriers to accessing after-school programs across different neighborhoods. The system analyzes factors such as monthly cost, income level, waitlist status, and program quality to highlight where access is limited and where resources are needed.

The project includes a full Tkinter-based GUI, CRUD functionality across all tables, and five analytical queries.

**Project Purpose**

Families often struggle to find after-school programs because information is scattered, hard to compare, and varies a lot between neighborhoods.
Our system solves this by:

- Collecting all after-school program data in one place
- Making it easier to compare cost, availability, quality, and location
- Using data to show where access gaps exist
- Helping highlight low-income areas with fewer program opportunities

**Project Components | Graphical User Interface (Tkinter) |**

A clean, simple UI that allows users to:

- Manage Programs
- Manage Zip Codes
- Run 5 analytical queries
- View results instantly in the output panel

🔹 SQLite Database

Database name: barriers.db
Created automatically using Python code

**Database Tables**
1. ZipCodes

Stores neighborhood-level info.

Column	Description
zip_code (PK)	ZIP code
neighborhood_name	Name of neighborhood
median_income	Average household income
population	Population size
income_category	"high" or "low" income area
