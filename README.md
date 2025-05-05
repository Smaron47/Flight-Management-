# Flight Management System


---

## 1. Project Overview

The **Flight Management System** is a desktop application built with Python and Tkinter to record, search, and export flight operation logs. It provides:

* Data entry forms for flight details (ID, aircraft type, mission type, flight hours, registration).
* Search and filter by date, aircraft, mission, or ID.
* PDF export of flight logs with total flight hours calculation.
* Technical issue tracking window for logging maintenance or operational issues per flight.

Designed for aviation training schools, small operators, or flight departments to maintain clean, searchable records.

---

## 2. Key Features

* **Flight Record Management**: Add, delete, and view flight entries.
* **Search & Filter**: Multi-criteria filtering by date range, flight ID, aircraft registration, mission type.
* **Calendar Integration**: `tkcalendar` for selecting start/end dates.
* **PDF Reporting**: Generate formatted PDF reports with a summary table and total hours using `reportlab`.
* **Issue Logging**: Secondary window for capturing technical issues, searchable by same filters.
* **Background Image**: Custom background using `PIL` for branding.

---

## 3. Technology Stack & Dependencies

* **Python 3.8+**
* **Tkinter**: Standard GUI toolkit
* **tkcalendar**: Date picker widgets
* **SQLite3**: Embedded database for persistence
* **Pillow (PIL)**: Image handling for backgrounds
* **ReportLab**: PDF generation library

Install via pip:

```bash
pip install tkcalendar Pillow reportlab
```

---

## 4. Installation & Setup

1. Clone or download the repository.
2. Ensure Python 3.8+ is installed and added to PATH.
3. Install dependencies: `pip install tkcalendar Pillow reportlab`
4. Place `bg.png` and `images.ico` in the project directory.
5. Run the application: `python flight_management.py`

---

## 5. Database Schema

Two SQLite tables stored in `flights.db`:

```sql
CREATE TABLE flights (
  id INTEGER,
  aircraft TEXT,
  flight_type TEXT,
  mission_type TEXT,
  flight_hours TEXT,
  aircraft_regi TEXT,
  date TEXT PRIMARY KEY
);

CREATE TABLE issue (
  id INTEGER,
  aircraft TEXT,
  idate TEXT,
  problem TEXT,
  date TEXT PRIMARY KEY
);
```

* **flights**: Logs each flight occurrence with timestamp.
* **issue**: Records technical issues linked to flight IDs.

---

## 6. Application Structure

```
flight_management.py     # Main application script
flights.db               # SQLite database file (auto-created)
bg.png                   # Background image for windows
images.ico               # Window icon
```

All logic resides in the `FlightApp` class; no external modules.

---

## 7. GUI Layout & Workflow

1. **Main Window**:

   * **Left Pane**: Entry form for new flight records.
   * **Right Pane**: Treeview listing all flights.
   * **Controls**: Save, Delete, Search filters, PDF Export, Technical Issues button.

2. **Filter Pane**:

   * ID field, Aircraft registration dropdown, Mission type dropdown, Aircraft type dropdown.
   * Start Date / End Date pickers.
   * Search / All Data buttons.

3. **Technical Issues Window**:

   * Similar layout with entry form for issues (ID, registration, date, problem text).
   * Search and list past issues; PDF export if needed.

---

## 8. Module and Function Descriptions

### Main Application Class (`FlightApp`)

Encapsulates UI creation and event handling:

* `__init__`: Builds frames, labels, entries, comboboxes, treeviews, and loads existing data.
* Binds commands to buttons for CRUD and reporting operations.

### Database Operations

* **Initialization**: On startup, connects to `flights.db` and ensures tables exist.
* **Add Record** (`add_flight`): Inserts new flight into DB and Treeview.
* **Delete Record** (`delete_data`): Removes selected flight by date key.
* **Fetch All** (`all_data` / `all_data1`): Refreshes Treeview from DB.

### Date Picking & Searching

* **Calendar Dialogs** (`select_date` / `ends_date`): Opens `tkcalendar.Calendar` in a modal to pick start/end dates.
* **Search Data** (`search_data`): Builds SQL queries based on selected filters and populates Treeview.

### Add/Delete Flight Records

* **Save Button**: Validates form, writes to DB, clears fields.
* **Delete Button**: Requires row selection; prompts warning if none.

### Issue Tracking Window

* **ndwindow**: Launches secondary Tk Toplevel window.
* Mirrors flight entry UI to capture technical problems.
* **saveissue** / **deleteissue** methods manage `issue` table.
* **search\_issues** filters issues similarly to flight search.

### PDF Generation

* **generate\_pdf**: Retrieves Treeview data via `export_data`, calculates total flight hours, builds a stylized `reportlab` table in landscape letter format, and saves to `{PilotName}{Date}.pdf`.
* **export\_data**: Gathers rows from Treeview into a list-of-lists for report.

---

## 9. Styling & Theming

* **Background Image**: Uses `PIL.Image.open` and `ImageTk.PhotoImage` to set `bg.png` as full-window backdrop.
* **Icons**: `images.ico` applied via `root.iconbitmap()`.
* **Treeview**: Column widths and headings styled for readability.

---

## 10. Error Handling & Validation

* **Try/Except** blocks guard against DB and date parsing errors.
* **messagebox** alerts for missing selections or invalid operations.
* **Input Validation**: Minimal; assumes correct user entry formats.

---

## 11. Extensibility & Customization

* **Additional Filters**: Extend `search_data` with more WHERE clauses.
* **Export Formats**: Swap `reportlab` for CSV or Excel export.
* **UI Themes**: Integrate `ttkbootstrap` or custom styles.
* **User Authentication**: Add login screen for multi-user scenarios.

---

## 12. Troubleshooting & FAQs

* **DB Locked**: Close other connections; delete `flights.db` to reset.
* **Calendar Not Showing**: Ensure `tkcalendar` installed: `pip install tkcalendar`.
* **ReportLab Errors**: Verify fonts and permissions for PDF directory.

---

## 13. SEO Keywords

```
Python flight management GUI
Tkinter database application
tkcalendar SQLite filtering
ReportLab PDF report Python
Aviation record-keeping software
Flight log export PDF
Aircraft mission tracking GUI
Technical issue logger Python
Python flight management GUI
Tkinter database application
tkcalendar SQLite filtering
ReportLab PDF report Python
Aviation record-keeping software
Flight log export PDF
Aircraft mission tracking GUI
Technical issue logger Python
```

---

## 14. Author & License

**Author:** Smaron Biswas
**Date:** 2025
**License:** MIT License

*Feel free to fork, extend, or integrate this Flight Management System into your aviation training workflow.*
