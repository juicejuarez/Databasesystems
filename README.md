PROJECT SUMMARY 
-------------------------------------
Breaking Barriers is a Python + SQLite system designed to analyze accessibility gaps in after-school programs across San Antonio. Families face challenges finding programs due to scattered information, inconsistent quality, and limited availability.
This system centralizes all important information—program cost, ratings, availability, ZIP code demographics, and provides insightful queries to highlight where barriers exist.

The application features:
- A structured database with 4 connected tables
- A Tkinter GUI for easy interaction
- Full CRUD operations for all entities
- Five analytical SQL queries
- A clean architecture separating logic, GUI, and data
- Real San Antonio ZIP code and program data

PURPOSE
-------------------------------------
The goal of this project is to identify barriers that prevent families from accessing equitable after-school opportunities.
Barriers include:

- High program costs
- Low-income neighborhoods lack resources
- Capacity issues/waitlists
- Low program quality
- Geographic gaps in access

By analyzing these factors, the system helps reveal underserved neighborhoods and supports informed decision-making by parents, schools, and community leaders.

SYSTEM OVERVIEW
-------------------------------------
This project uses:

- Python 3.x – backend logic and GUI functionality
- Tkinter – graphical user interface
- SQLite (barriers.db) – database engine
- SQL – analytical and CRUD operations

The system includes:

- A simple, functional Tkinter interface
- Four connected database tables
- Full CRUD operations for each table
- Five analytical queries
- Auto-inserted real after-school program data

DATABASE STRUCTURE
-------------------------------------
The system uses four linked tables with foreign keys:

1. ZipCodes Table
  Stores neighborhood-level data.

- zip_code (PRIMARY KEY)
- neighborhood_name
- median_income
- population
- income_category (“high” or “low”)

2. Programs Table
   Stores all after-school program information.
   
- program_id (PRIMARY KEY)
- program_name
- program_type
- address
- zip_code (FOREIGN KEY → ZipCodes)
- monthly_cost
- website

3. Enrollment Table
  Tracks capacity and availability.

- enrollment_id (PRIMARY KEY)
- program_id (FOREIGN KEY → Programs)
- max_capacity
- current_enrollment (“IMMEDIATELY” or “WAITLIST”)

4. Reviews Table
  Stores quality ratings.

- review_id (PRIMARY KEY)
- program_id (FOREIGN KEY → Programs)
- Google_rating
- reviews

CRUD FUNCTIONALITY
-------------------------------------

The application supports full Create, Read, Update, and Delete operations for every table.

Programs CRUD

- Add new program
- View all programs
- Update monthly cost
- Delete program

Zip Code CRUD

- Add new ZIP code
- View all ZIP records
- Update population
- Delete ZIP code
    - Protected by foreign keys (cannot delete if programs exist)

Enrollment CRUD

- Add enrollment details
- Update availability status
- Delete enrollment entry

Reviews CRUD

- Add reviews
- Update star rating or review count
- Delete review

ANALYTICAL QUERIES
-------------------------------------

The system includes five SQL-based analytical queries for meaningful insights.

1. Income Barrier Analysis

- Finds programs in high-income or low-income ZIP codes
- Helps identify affordability gaps

2. Budget-Friendly Program Search

- Filters programs based on a maximum cost entered by the user

3. Quality / Rating Filter

- Displays programs with Google ratings greater than or equal to the user’s input

4. Waitlist Availability Check

- Shows programs that are:

    - WAITLIST ONLY, or
    - IMMEDIATELY AVAILABLE

5. Geographic ZIP Code Search

- Lists all programs in a specific ZIP code
- Highlights underserved areas

HOW RO RUN THE PROJECT
-------------------------------------
**1. Install Python 3.x**

Tkinter and SQLite come pre-installed with Python.

**2. Run the application**
python app_gui.py
The GUI will open with full CRUD and query options.

**3. Database Creation**

If barriers.db does not exist, it will be created automatically the first time the program is run.

Project Files + Folder Structure

Why needed: Shows organization and professionalism.

PROJECT FILES
File	Description
app_gui.py	Main Tkinter application (CRUD + queries)
setup_database.py	Creates SQLite tables
insert_data.py	Inserts real ZIP codes, programs, enrollment & reviews
queries.py	Contains all SQL analytical functions
test_crud.py	Automated CRUD test file
barriers.db	SQLite database file




