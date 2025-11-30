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
