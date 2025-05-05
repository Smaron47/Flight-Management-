import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import PhotoImage,Label
import sqlite3
from datetime import datetime
from tkcalendar import Calendar, DateEntry
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from PIL import Image, ImageTk
# Create a database connection
conn = sqlite3.connect('flights.db')

# Create a flights table if it does not exist
conn.execute('''CREATE TABLE IF NOT EXISTS flights
             (id INTEGER,
             aircraft TEXT,
             flight_type TEXT,
             mission_type TEXT,
             flight_hours TEXT,
             aircraft_regi TEXT,
             date TEXT PRIMARY KEY);''')

class FlightApp:
    def __init__(self, root):
        self.root = root
        self.root.title("École De Spécialisation Transport")
        self.root.geometry("950x600")
        self.root.grid_rowconfigure(1, minsize=10)
        self.root.iconbitmap("images.ico")
    
        img = Image.open("bg.png")
        img = img.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.ANTIALIAS)

        # Create a PhotoImage object from the image
        bg_img = ImageTk.PhotoImage(img)
        bg_label = Label(root, image=bg_img)
        bg_label.image=bg_img
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)



# Set the background color of all widgets to transparent

        # Set the image as the background of the window
        # Labels and Entry Boxes
        self.frm=tk.Frame(root,width=400, highlightthickness=0)
        
        self.frm.grid(row=0,column=0)
        self.id_label = tk.Label(self.frm, text="ID")
        self.id_label.grid(row=0, column=0, padx=10, pady=3)
        self.id_entry = tk.Entry(self.frm)
        self.id_entry.grid(row=0, column=1, padx=10, pady=3)

        self.aircraft_label = tk.Label(self.frm, text="Type of Aircraft")
        self.aircraft_label.grid(row=1, column=0, padx=10, pady=3)
        self.aircraft_options = ["KA 200", "KA 300", "KA 350"]
        self.aircraft_dropdown = ttk.Combobox(self.frm, values=self.aircraft_options)
        self.aircraft_dropdown.grid(row=1, column=1, padx=10, pady=3)

        self.flight_type_label = tk.Label(self.frm, text="Type of Flight")
        self.flight_type_label.grid(row=2, column=0, padx=10, pady=3)
        self.flight_type_options = ["Night Flight", " Day Flight"]
        self.flight_type_dropdown = ttk.Combobox(self.frm, values=self.flight_type_options)
        self.flight_type_dropdown.grid(row=2, column=1, padx=10, pady=3)

        self.mission_type_label = tk.Label(self.frm, text="Type of Mission")
        self.mission_type_label.grid(row=3, column=0, padx=10, pady=3)
        self.mission_type_options = ["Instruction", "Vip", "Entrainement cadre","VDC", "VDF", "Trasport matériels", "Transport personnels", "ALGHAIT", "Det Zone sud", "Autre","Courrier Royale","Courrier Spéciale","Entraînement"]
        self.mission_type_dropdown = ttk.Combobox(self.frm, values=self.mission_type_options)
        self.mission_type_dropdown.grid(row=3, column=1, padx=10, pady=3)

        self.flight_hours_label = tk.Label(self.frm, text="Flight Hours")
        self.flight_hours_label.grid(row=4, column=0, padx=10, pady=3)
        self.flight_hours_entry = tk.Entry(self.frm)
        self.flight_hours_entry.grid(row=4, column=1, padx=10, pady=3)

        self.mission_type_labl = tk.Label(self.frm, text="Aircraft Registration")
        self.mission_type_labl.grid(row=5, column=0, padx=10, pady=3)
        self.mission_type_options = ['CNA-NI','CNA-NG','CNA-NY','CNA-NJ']
        self.aircraft_regi = ttk.Combobox(self.frm, values=self.mission_type_options)
        self.aircraft_regi.grid(row=5, column=1, padx=10, pady=3)





        self.save_button = tk.Button(self.frm, text="Save", command=self.add_flight)
        self.save_button.grid(row=6, column=0, padx=10, pady=3)

        self.delete_button = tk.Button(self.frm, text="Delete", command=self.delete_data)
        self.delete_button.grid(row=6, column=1, padx=10, pady=3)
        
        self.frm1=tk.Frame(self.root,width=400, highlightthickness=0)
        
        self.frm1.grid(row=5,column=0)




        self.date_ = tk.Label(self.frm1, text="Search ID")
        self.date_.grid(row=0, column=0, padx=10, pady=3)
        self.d_e = tk.Entry(self.frm1)
        self.d_e.grid(row=0, column=1, padx=10, pady=3)
        
        self.date_a = tk.Label(self.frm1, text="Aircraft Reg: ")
        self.date_a.grid(row=1, column=0, padx=10, pady=3)
        self.mission_type_options = ['CNA-NI','CNA-NG','CNA-NY','CNA-NJ']
        self.aircraft_regi1 = ttk.Combobox(self.frm1, values=self.mission_type_options)
        self.aircraft_regi1.grid(row=1, column=1, padx=10, pady=3)


        self.date_b = tk.Label(self.frm1, text="Type Of Mission ")
        self.date_b.grid(row=2, column=0, padx=10, pady=3)
        self.mission_type_optio= ["Instruction", "Vip", "Entrainement cadre","VDC", "VDF", "Trasport matériels", "Transport personnels", "ALGHAIT", "Det Zone sud", "Autre","Courrier Royale","Courrier Spéciale","Entraînement"]
        self.aircraft_ = ttk.Combobox(self.frm1, values=self.mission_type_optio)
        self.aircraft_.grid(row=2, column=1, padx=10, pady=3)
        
        
        self.date_c = tk.Label(self.frm1, text="Aircraft Type ")
        self.date_c.grid(row=3, column=0, padx=10, pady=3)
        self.aircraft_options = ["KA 200", "KA 300", "KA 350"]
        self.aircraft = ttk.Combobox(self.frm1, values=self.aircraft_options)
        self.aircraft.grid(row=3, column=1, padx=10, pady=3)





        self.date_label = tk.Button(self.frm1, text="Start Date",command=self.select_date)
        self.date_label.grid(row=4, column=0, padx=10, pady=3)
        
        
        self.end_date_entry = tk.Button(self.frm1, text="End Date",command=self.ends_date)
        self.end_date_entry.grid(row=4, column=1, padx=10, pady=3)
        
        self.search_button = tk.Button(self.frm1, text="Search", command=self.search_data)
        self.search_button.grid(row=6, column=0, padx=10, pady=3)
        self.all = tk.Button(self.frm1, text="All Data", command=self.all_data)
        self.all.grid(row=6, column=1, padx=10, pady=3)
        
        
        
    
        self.pdf_button = tk.Button(self.root, text="PDF Generated", command=self.generate_pdf)
        self.pdf_button.grid(row=2, column=1)
        self.ndwind = tk.Button(self.root, text="Technical Issues", command=self.ndwindow)
        self.ndwind.grid(row=5, column=1)
        # Treeview for displaying the flights table
        self.treeview = ttk.Treeview(self.root, columns=("id", "aircraft", "flight_type", "mission_type", "flight_hours","aircraft_regi", "date"))
        self.treeview.heading("id", text="ID")
        self.treeview.heading("aircraft", text="Type of Aircraft")
        self.treeview.heading("flight_type", text="Type of Flight")
        self.treeview.heading("mission_type", text="Type of Mission")
        self.treeview.heading("flight_hours", text="Flight Hours")
        self.treeview.heading("aircraft_regi", text="Aircraft Registration")
        self.treeview.heading("date", text="Date")
        self.treeview.column('#0',width=0)
        self.treeview.column("id", width=50)
        self.treeview.column("aircraft", width=100)
        self.treeview.column("flight_type", width=110)
        self.treeview.column("mission_type", width=140)
        self.treeview.column("flight_hours", width=50)
        self.treeview.column("aircraft_regi", width=90)
        self.treeview.column("date", width=120)
        
        self.treeview.grid(row=0, column=1, sticky="nsew")
        self.conn=sqlite3.connect('flights.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM flights")
        rows = self.cursor.fetchall()
        for row in rows:
            self.treeview.insert("", "end", values=row)


    def all_data(self):
        self.cursor.execute("SELECT * FROM flights")
        rows = self.cursor.fetchall()
        self.treeview.delete(*self.treeview.get_children())
        for row in rows:
            self.treeview.insert("", "end", values=row)
    def all_data1(self):
        self.cursor.execute("SELECT * FROM issue")
        rows = self.cursor.fetchall()
        self.treeview.delete(*self.treeview.get_children())
        for row in rows:
            self.treeview.insert("", "end", values=row)
    def select_date(self):
        top = tk.Toplevel(self.root)
        cal = Calendar(top, selectmode="day", date_pattern="mm-dd-yyyy")
        cal.pack()
        ok_button = tk.Button(top, text="OK", command=lambda: self.pick_date(cal, top))
        ok_button.pack()
        
    def pick_date(self, cal, top):
        self.start_date=(cal.selection_get().strftime('%m-%d-%Y'))
        self.date_entry = tk.Label(self.frm1, text=f'{self.start_date}')
        self.date_entry.grid(row=5, column=0, padx=10, pady=3)
        top.destroy()

    def ends_date(self):
        top = tk.Toplevel(self.root)
        cal = Calendar(top, selectmode="day", date_pattern="mm-dd-yyyy")
        cal.pack()
        ok_button = tk.Button(top, text="OK", command=lambda: self.ends_dates(cal, top))
        ok_button.pack()
        
    def ends_dates(self, cal, top):
        self.end_date=(cal.selection_get().strftime('%m-%d-%Y'))
        self.date_entry = tk.Label(self.frm1, text=f'{self.end_date}')
        self.date_entry.grid(row=5, column=1, padx=10, pady=3)
        top.destroy()



    def add_flight(self):
        # Get the input values
        flight_id = self.id_entry.get()
        aircraft = self.aircraft_dropdown.get()
        flight_type = self.flight_type_dropdown.get()
        mission_type = self.mission_type_dropdown.get()
        flight_hours = self.flight_hours_entry.get()
        aircraft_regi = self.aircraft_regi.get()
        date = datetime.now().strftime("%m-%d-%Y %H:%M:%S")

        # Insert the data into the database
        self.cursor.execute("INSERT INTO flights VALUES (?, ?, ?, ?, ?, ?, ?)",
                            (flight_id, aircraft, flight_type, mission_type, flight_hours,aircraft_regi, date))
        self.conn.commit()

        # Add the data to the treeview
        self.treeview.insert("", "end", values=(flight_id, aircraft, flight_type, mission_type, flight_hours, aircraft_regi, date))
        self.id_entry.delete(0,tk.END)
        self.aircraft_dropdown.delete(0,tk.END)
        self.flight_type_dropdown.delete(0,tk.END)
        self.mission_type_dropdown.delete(0,tk.END)
        self.flight_hours_entry.delete(0,tk.END)
        self.aircraft_regi.delete(0,tk.END)

    def search_data(self):
        start_date = str(self.start_date)
        end_date = str(self.end_date)
        ids=str(self.d_e.get())
        regi=str(self.aircraft_regi1.get())
        print(start_date,end_date)
        date_obj = datetime.strptime(start_date, '%m-%d-%Y')
        start_date = date_obj.strftime('%m-%d-%Y %H:%M:%S')
        date_obj = datetime.strptime(end_date, '%m-%d-%Y')
        end_date = date_obj.strftime('%m-%d-%Y %H:%M:%S')
        typem= str(self.aircraft_.get())
        aircraft =str(self.aircraft.get())
        # Clear the existing rows in the treeview
        print(start_date,end_date)
        for row in self.treeview.get_children():
            self.treeview.delete(row)
        if ids == "" and regi == "" and typem == "" and aircraft == "":
            messagebox.showwarning("Warning", "Please Enter Search IDs")
            return
        elif ids != "" and regi == "" and typem == "" and aircraft == "":
            # Query the database for rows within the selected date range
            self.cursor.execute("SELECT * FROM flights WHERE id=? AND date BETWEEN ? AND ?", (ids, start_date, end_date))
            rows = self.cursor.fetchall()

            # Add the rows to the treeview
            for row in rows:
                print(row)
                self.treeview.insert("", "end", values=row)
        elif ids == "" and regi != "" and typem == "" and aircraft == "":
            self.cursor.execute("SELECT * FROM flights WHERE aircraft_regi=? AND date BETWEEN? AND?", (regi, start_date, end_date))
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)
                self.treeview.insert("", "end", values=row)
        elif ids == "" and regi == "" and typem != "" and aircraft == "":
            self.cursor.execute("SELECT * FROM flights WHERE mission_type=? AND date BETWEEN? AND?", (typem, start_date, end_date))
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)
                self.treeview.insert("", "end", values=row)
        elif ids != "" and regi != "" and typem == "" and aircraft == "":
            self.cursor.execute("SELECT * FROM flights WHERE id=? AND aircraft_regi=? AND date BETWEEN? AND?", (ids, regi, start_date, end_date))
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)
                self.treeview.insert("", "end", values=row)
        elif ids != "" and regi == "" and typem != "" and aircraft == "":
            self.cursor.execute("SELECT * FROM flights WHERE id=? AND mission_type=? AND date BETWEEN? AND?", (ids, typem, start_date, end_date))
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)
                self.treeview.insert("", "end", values=row)
        elif ids == "" and regi != "" and typem != "" and aircraft == "":
            self.cursor.execute("SELECT * FROM flights WHERE aircraft_regi=? AND mission_type=? AND date BETWEEN? AND?", (regi, typem, start_date, end_date))
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)
                self.treeview.insert("", "end", values=row)
        elif ids == "" and regi == "" and typem == "" and aircraft != "":
            self.cursor.execute("SELECT * FROM flights WHERE aircraft=? AND date BETWEEN? AND?", (aircraft, start_date, end_date))
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)
                self.treeview.insert("", "end", values=row)
        elif ids != "" and regi != "" and typem != "" and aircraft == "":
            self.cursor.execute("SELECT * FROM flights WHERE id=? AND aircraft_regi=? AND mission_type=? AND date BETWEEN? AND?", (ids, regi, typem, start_date, end_date))
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)
                self.treeview.insert("", "end", values=row)

        elif ids != "" and regi == "" and typem != "" and aircraft != "":
            self.cursor.execute("SELECT * FROM flights WHERE id=? AND mission_type=? AND aircraft=? AND date BETWEEN? AND?", (ids, typem, aircraft,start_date,end_date))
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)
                self.treeview.insert("", "end", values=row)
        
        elif ids != "" and regi == "" and typem == "" and aircraft != "":
            self.cursor.execute("SELECT * FROM flights WHERE id=? AND aircraft=? AND date BETWEEN? AND?", (ids,aircraft,start_date,end_date))
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)
                self.treeview.insert("", "end", values=row)
        
        else:
            self.cursor.execute("SELECT * FROM flights WHERE id=? AND aircraft_regi=? AND mission_type=? AND date BETWEEN? AND?", (ids,regi,typem,start_date, end_date))
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)
                self.treeview.insert("", "end", values=row)
        
    def delete_data(self):
        # Get the ID of the selected row
        selection = self.treeview.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a row to delete")
            return
        row_id = self.treeview.item(selection[0])["values"][-1]
        print(row_id)
        # Delete the row from the database
        self.cursor.execute("DELETE FROM flights WHERE date=?", (row_id,))
        self.conn.commit()

        # Delete the row from the treeview
        self.treeview.delete(selection)
    def calculate_total_time(self,times):
        total_minutes = 0
        for t in times:
            print(t)
            h, m = t.split('H')
            total_minutes += int(h) * 60 + int(m)
        total_hours, remaining_minutes = divmod(total_minutes, 60)
        return f"{total_hours:02d} H {remaining_minutes:02d}"

    def generate_pdf(self):
        data = self.export_data()
        print(data)
        i=1
        tm=[]
        while i<len(data):
            tm.append(data[i][4])
            try:
                data[i][5]= str(data[i][5]).split(" ")[0]
            except:
                data[i][-1]=str(data[i][-1]).split(" ")[0]
            i+=1
        # create the header
        try:
            tme=self.calculate_total_time(tm)
            print(tm)
            data[1].append(tme)
        except:
            pass
        data.insert(0,"CRM EST")
        data.insert(1,"\n")
        
        # Define the style of the table
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.white),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 14),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 12),
            ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
            ('GRID', (0, 0), (-1, -1), 0.25, colors.white),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ])

        # Create the table using the data and style
        table = Table(data)
        table.setStyle(style)

        # Create the PDF file
        name=str(data[3][0])
        id=str(data[3][-1])
        filename = f"{name+id}.pdf"
        doc = SimpleDocTemplate(filename, pagesize=landscape(letter))
        doc.build([table])
        messagebox.showinfo('Pdf Generagted', f'PDF generated \n{name}.pdf')
    def export_data(self):
        export_list=[]
        export_list1 = ["ID", "Type of Aircraft", "Type of Flight","Type of Mission","Flight Hours","Aircraft_regi", "Date","Total Hours"]
        export_list.append(export_list1)
        print(self.treeview.get_children())
        for item in self.treeview.get_children():
            export_list.append(self.treeview.item(item)['values'])
            print(export_list)
        return export_list
    
    def onclose(self):
        self.root.destroy()


    def ndwindow(self):
        
        # Hide the main window
        self.root.withdraw()
        
        # Create a new window
        self.second_window = tk.Toplevel()
        self.second_window.title("École De Spécialisation Transport")
        self.second_window.geometry("950x600")
        self.second_window.grid_rowconfigure(1, minsize=10)
        self.second_window.iconbitmap("images.ico")
        self.second_window.protocol("WM_DELETE_WINDOW",self.onclose)
        img = Image.open("bg.png")
        img = img.resize((self.second_window.winfo_screenwidth(), root.winfo_screenheight()), Image.ANTIALIAS)

        # Create a PhotoImage object from the image
        bg_img = ImageTk.PhotoImage(img)
        bg_label = Label(self.second_window, image=bg_img)
        bg_label.image=bg_img
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        conn = sqlite3.connect('flights.db')

# Create a flights table if it does not exist
        conn.execute('''CREATE TABLE IF NOT EXISTS issue
                    (id INTEGER,
                    aircraft TEXT,
                    idate TEXT,
                    problem TEXT,
                    date TEXT PRIMARY KEY);''')
        # Add a label and a button
        self.issue_label = Label(self.second_window, text='Technical Issues', font=("Arial", 20))
        self.issue_label.grid(row=0, column=1, padx=50, pady=3,columnspan=2)
        self.text_area = tk.Text(self.second_window, width=50, height=6)
        self.text_area.grid(row=1,column=1,padx=50, pady=3)

        self.frm=tk.Frame(self.second_window,width=400, highlightthickness=0)
        
        self.frm.grid(row=1,column=0)
        self.id_label = tk.Label(self.frm, text="ID")
        self.id_label.grid(row=0, column=0, padx=10, pady=3)
        self.id_entry = tk.Entry(self.frm)
        self.id_entry.grid(row=0, column=1, padx=10, pady=3)

        self.aircraft_label = tk.Label(self.frm, text="Aircraft Registration")
        self.aircraft_label.grid(row=1, column=0, padx=10, pady=3)
        self.aircraft_options = ['CNA-NI','CNA-NG','CNA-NY','CNA-NJ']
        self.aircraft_dropdown = ttk.Combobox(self.frm, values=self.aircraft_options)
        self.aircraft_dropdown.grid(row=1, column=1, padx=10, pady=3)

        self.flight_type_label = tk.Label(self.frm, text="Date")
        self.flight_type_label.grid(row=2, column=0, padx=10, pady=3)
        self.flight_type_options = ["Night Flight", " Day Flight"]
        self.flight_type_dropdown = DateEntry(self.frm,date_pattern="mm-dd-YYYY")
        self.flight_type_dropdown.grid(row=2, column=1, padx=10, pady=3)
        self.savebtn=tk.Button(self.frm, text='Save', command=self.saveissue)
        self.savebtn.grid(row=3, column=0, padx=10, pady=3)
        self.deletebtn =tk.Button(self.frm, text='Delete', command=self.deleteissue)
        self.deletebtn.grid(row=3, column=1, padx=10, pady=3)



        self.frm1=tk.Frame(self.second_window,width=400, highlightthickness=0)
            
        self.frm1.grid(row=3,column=0)




        self.date_ = tk.Label(self.frm1, text="Search ID")
        self.date_.grid(row=0, column=0, padx=10, pady=3)
        self.d_e1 = tk.Entry(self.frm1)
        self.d_e1.grid(row=0, column=1, padx=10, pady=3)
        
        self.date_a = tk.Label(self.frm1, text="Aircraft Reg: ")
        self.date_a.grid(row=1, column=0, padx=10, pady=3)
        self.mission_type_options1 = ['CNA-NI','CNA-NG','CNA-NY','CNA-NJ']
        self.aircraft_regi11 = ttk.Combobox(self.frm1, values=self.mission_type_options1)
        self.aircraft_regi11.grid(row=1, column=1, padx=10, pady=3)


        

        self.date_label = tk.Button(self.frm1, text="Start Date",command=self.select_date)
        self.date_label.grid(row=4, column=0, padx=10, pady=3)
        
        
        self.end_date_entry = tk.Button(self.frm1, text="End Date",command=self.ends_date)
        self.end_date_entry.grid(row=4, column=1, padx=10, pady=3)
        
        self.search_button = tk.Button(self.frm1, text="Search", command=self.search_issues)
        self.search_button.grid(row=6, column=0, padx=10, pady=3)
        self.all = tk.Button(self.frm1, text="All Data", command=self.all_data1)
        self.all.grid(row=6, column=1, padx=10, pady=3)





        self.treeview = ttk.Treeview(self.second_window, columns=("id", "aircraft", "idate","problem", "date"))
        self.treeview.heading("id", text="ID")
        self.treeview.heading("aircraft", text="Type of Aircraft")
        self.treeview.heading("idate", text="Date")
        self.treeview.heading("problem", text="Issue")
        self.treeview.heading('date',text="Entry Date")
        self.treeview.column('#0',width=0)
        self.treeview.column("id", width=50)
        self.treeview.column("aircraft", width=100)
        self.treeview.column("idate", width=110)
        self.treeview.column("problem", width=110)
        self.treeview.column("date", width=140)



        
        self.treeview.grid(row=3, column=1, sticky="nsew",padx=20, pady=3)
        self.conn=sqlite3.connect('flights.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM issue")
        rows = self.cursor.fetchall()
        for row in rows:
            self.treeview.insert("", "end", values=row)
        
        self.btn_done = tk.Button(self.second_window, text="Back to Main Window", command=self.close_second_window)
        self.btn_done.grid(row=5,column=0,padx=50, pady=20)
        self.btn_done1 = tk.Button(self.second_window, text="PDF Genertor", command=self.generate_pdf1)
        self.btn_done1.grid(row=5,column=1,padx=50, pady=20)

    def saveissue(self):
        date = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
        conn = sqlite3.connect('flights.db')
        conn.execute("INSERT INTO issue VALUES (?,?,?,?,?)",
                (self.id_entry.get(), self.aircraft_dropdown.get(), self.flight_type_dropdown.get(),self.text_area.get("1.0","end-1c"), date ))
        conn.commit()
        idss=str(self.id_entry.get())
        typea=str(self.aircraft_dropdown.get())
        typef=str(self.flight_type_dropdown.get())
        print(idss, typea, typef)
        self.treeview.insert("", "end", values=(idss,typea,typef,self.text_area.get("1.0","end-1c"), date ))
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, "Issue saved successfully")
        self.id_entry.delete(0, tk.END)
        self.aircraft_dropdown.delete(0, tk.END)
        self.flight_type_dropdown.delete(0, tk.END)
        

    
    def deleteissue(self):
        selection = self.treeview.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a row to delete")
            return
        row_id = self.treeview.item(selection[0])["values"][-1]
        print(row_id)
        # Delete the row from the database
        self.cursor.execute("DELETE FROM issue WHERE date=?", (row_id,))
        self.conn.commit()
        self.treeview.delete(selection)
        
    def search_issues(self):
        start_date = str(self.start_date)
        end_date = str(self.end_date)
        ids=str(self.d_e1.get())
        regi=str(self.aircraft_regi11.get())
        print(start_date,end_date,ids)
        date_obj = datetime.strptime(start_date, '%m-%d-%Y')
        start_date = date_obj.strftime('%m-%d-%Y %H:%M:%S')
        date_obj = datetime.strptime(end_date, '%m-%d-%Y')
        end_date = date_obj.strftime('%m-%d-%Y %H:%M:%S')
        
        # Clear the existing rows in the treeview
        print(start_date,end_date)
        for row in self.treeview.get_children():
            self.treeview.delete(row)
        if ids == "" and regi == "":
            messagebox.showwarning("Warning", "Please Enter Search IDs")
            return
        elif ids != "" and regi =="":
            # Query the database for rows within the selected date range
            self.cursor.execute("SELECT * FROM issue WHERE id=? AND date BETWEEN ? AND ?", (ids, start_date, end_date))
            rows = self.cursor.fetchall()

            # Add the rows to the treeview
            for row in rows:
                print(row)
                self.treeview.insert("", "end", values=row)
        elif ids == "" and regi != "" :
            self.cursor.execute("SELECT * FROM issue WHERE aircraft=? AND date BETWEEN? AND?", (regi, start_date, end_date))
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)
                self.treeview.insert("", "end", values=row)
        elif ids !="" and regi != "" :
            self.cursor.execute("SELECT * FROM issue WHERE id=? AND aircraft=? AND date BETWEEN? AND?", (ids,regi, start_date, end_date))
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)
                self.treeview.insert("", "end", values=row)
        else:
            messagebox.showwarning("Warning", "Please Enter Valid ID Or Aircraft")
    def generate_pdf1(self):
        data = self.export_data1()
        print(data)
        i=1
        tm=[]
        while i<len(data):
            tm.append(data[i][4])
            try:
                data[i][5]= str(data[i][5]).split(" ")[0]
            except:
                data[i][-1]=str(data[i][-1]).split(" ")[0]
            i+=1
        # create the header
        try:
            tme=self.calculate_total_time(tm)
            print(tm)
            data[1].append(tme)
        except:
            pass
        data.insert(0,["CRM EST","","","",""])
        data.insert(1,"\n")
        
        # Define the style of the table
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.white),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 14),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 12),
            ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
            ('GRID', (0, 0), (-1, -1), 0.25, colors.white),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ])

        # Create the table using the data and style
        table = Table(data)
        table.setStyle(style)

        # Create the PDF file
        name=str(data[3][0])
        id=str(data[3][-1])
        filename = f"{name+id}.pdf"
        doc = SimpleDocTemplate(filename, pagesize=landscape(letter))
        doc.build([table])
        messagebox.showinfo('Pdf Generagted', f'PDF generated \n{name+id}.pdf')
    def export_data1(self):
        export_list=[]
        export_list1 = ["ID", "Type of Aircraft", "Date","Issue","Entry Date"]
        export_list.append(export_list1)
        print(self.treeview.get_children())
        for item in self.treeview.get_children():
            export_list.append(self.treeview.item(item)['values'])
            print(export_list)
        return export_list







    def close_second_window(self):
        # Destroy the second window
        self.second_window.destroy()
        
        # Show the main window
        self.root.deiconify()

    
        
root = tk.Tk()

app = FlightApp(root)

root.mainloop()
