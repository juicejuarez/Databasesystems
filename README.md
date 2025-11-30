**# PROJECT SUMMARY **

Breaking Barriers is a Python + SQLite system designed to analyze accessibility gaps in after-school programs across San Antonio. Families face challenges finding programs due to scattered information, inconsistent quality, and limited availability.
This system centralizes all important information—program cost, ratings, availability, ZIP code demographics, and provides insightful queries to highlight where barriers exist.

**The application features:**
- A structured database with 4 connected tables
- A Tkinter GUI for easy interaction
- Full CRUD operations for all entities
- Five analytical SQL queries
- A clean architecture separating logic, GUI, and data
- Real San Antonio ZIP code and program data

**# PURPOSE**
The goal of this project is to identify barriers that prevent families from accessing equitable after-school opportunities.
Barriers include:

- High program costs
- Low-income neighborhoods lack resources
- Capacity issues/waitlists
- Low program quality
- Geographic gaps in access

By analyzing these factors, the system helps reveal underserved neighborhoods and supports informed decision-making by parents, schools, and community leaders.

┌───────────────────────────┐
│         Tkinter GUI        │
│  - Buttons for CRUD        │
│  - Buttons for Queries     │
│  - Output Display Console  │
└──────────────┬────────────┘
               │
               ▼
┌───────────────────────────┐
│      Application Logic     │
│  - CRUD Functions          │
│  - Query Handlers          │
│  - Input Validation        │
└──────────────┬────────────┘
               │
               ▼
┌───────────────────────────┐
│         SQLite DB          │
│  - ZipCodes Table          │
│  - Programs Table          │
│  - Enrollment Table        │
│  - Reviews Table           │
└───────────────────────────┘
