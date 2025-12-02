# py desktop\db.py	# how to run this in windows

import tkinter as tk
import sqlite3



def save(selection, a, b, c, d, e, f, g, h, i, j, k):
	printout = "DATA ENTERED: " + selection + " " + a + " " + b + " " + c + " " + d + " " + e + " " + f + " " + g + " " + h + " " + i + " " + j + " " + k + " " + "\n\n"
	output_box.insert(tk.END, printout)


	connector = sqlite3.connect('database32.db')
	cursor = connector.cursor()


	if selection == "create_parent":
		cursor.execute("INSERT INTO parent (parent_first, parent_last, parent_streetnumber, parent_street, parent_zip, parent_phoneareacode, parent_phoneprefix, parent_phonesuffix, parent_email) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (a, b, c, d, e, f, g, h, i))
		printout = "|Record#|First|Last|Street#|StreetName|Zip|AreaCode|Phone3|Phone4|Email|\n\n"
		output_box.insert(tk.END, printout)
		cursor.execute("SELECT * FROM parent")

	if selection == "create_child":
		cursor.execute("INSERT INTO child (parent_id, program_id, child_first, child_last) VALUES (?, ?, ?, ?)", (a, b, c, d))
		printout = "|Record#|Parent#|Program#|First|Last|\n\n"
		output_box.insert(tk.END, printout)
		cursor.execute("SELECT * FROM child")

	if selection == "read_table":
		cursor.execute("SELECT * FROM " + a)

	if selection == "update_parent":
		cursor.execute("UPDATE parent SET parent_first = ?, parent_last = ?, parent_streetnumber = ?, parent_street = ?, parent_zip = ?, parent_phoneareacode = ?, parent_phoneprefix = ?, parent_phonesuffix = ?, parent_email = ? WHERE parent_id = ?", (a, b, c, d, e, f, g, h, i, j))
		printout = "|Record#|First|Last|Street#|StreetName|Zip|AreaCode|Phone3|Phone4|Email|\n\n"
		output_box.insert(tk.END, printout)
		cursor.execute("SELECT * FROM parent")

	if selection == "update_child":
		cursor.execute("UPDATE child SET parent_id = ?, program_id = ?, child_first = ?, child_last = ? WHERE child_id = ?", (a, b, c, d, e))
		printout = "|Record#|Parent#|Program#|First|Last|\n\n"
		output_box.insert(tk.END, printout)
		cursor.execute("SELECT * FROM child")

	if selection == "delete_parent":
		cursor.execute("DELETE FROM parent WHERE parent_id = " + a)
		printout = "|Record#|First|Last|Street#|StreetName|Zip|AreaCode|Phone3|Phone4|Email|\n\n"
		output_box.insert(tk.END, printout)
		cursor.execute("SELECT * FROM parent")

	if selection == "delete_child":
		cursor.execute("DELETE FROM child WHERE child_id = " + a)
		printout = "|Record#|Parent#|Program#|First|Last|\n\n"
		output_box.insert(tk.END, printout)
		cursor.execute("SELECT * FROM child")

	if selection == "query":
		cursor.execute(a)

	if selection == "hasfinancialassistance":
		printout = "|Record#|Name|Street#|StreetName|Zip|AreaCode|Phone3|Phone4|Email|FinancialAssistance|WaitlistDays|Cost|Rating|\n\n"
		output_box.insert(tk.END, printout)
		cursor.execute("SELECT * FROM program WHERE program_hasfinancialassistance = 'YES'")

	if selection == "waitlistdays":
		printout = "|Record#|Name|Street#|StreetName|Zip|AreaCode|Phone3|Phone4|Email|FinancialAssistance|WaitlistDays|Cost|Rating|\n\n"
		output_box.insert(tk.END, printout)
		cursor.execute("SELECT * FROM program WHERE program_waitlistdays <= " + a)

	if selection == "financialassistancebyzip":
		printout = "|Record#|Name|Street#|StreetName|Zip|AreaCode|Phone3|Phone4|Email|FinancialAssistance|WaitlistDays|Cost|Rating|\n\n"
		output_box.insert(tk.END, printout)
		cursor.execute("SELECT * FROM program WHERE program_hasfinancialassistance = 'YES' AND program_zip = " + a)

	if selection == "waitlistdaysbyzip":
		printout = "|Record#|Name|Street#|StreetName|Zip|AreaCode|Phone3|Phone4|Email|FinancialAssistance|WaitlistDays|Cost|Rating|\n\n"
		output_box.insert(tk.END, printout)
		cursor.execute("SELECT * FROM program WHERE program_waitlistdays <= ? AND program_zip = ?", (a, b))

	if selection == "bycost":
		printout = "|Record#|Name|Street#|StreetName|Zip|AreaCode|Phone3|Phone4|Email|FinancialAssistance|WaitlistDays|Cost|Rating|\n\n"
		output_box.insert(tk.END, printout)
		cursor.execute("SELECT * FROM program WHERE program_cost <= " + a)

	if selection == "zipincome":
		printout = "|ZipCode|MedianIncome|\n\n"
		output_box.insert(tk.END, printout)
		cursor.execute("SELECT * FROM zip WHERE zip_medianincome <= " + a)

	if selection == "byrating":
		printout = "|Record#|Name|Street#|StreetName|Zip|AreaCode|Phone3|Phone4|Email|FinancialAssistance|WaitlistDays|Cost|Rating|\n\n"
		output_box.insert(tk.END, printout)
		cursor.execute("SELECT * FROM program WHERE program_rating >= " + a)


	rows = cursor.fetchall()
	display_str = ""
	for row in rows:
		display_str += str(row) + "\n"
	output_box.insert(tk.END, display_str)

	connector.commit()
	connector.close()

	printout = "\nQUERY PROCESSED\n-----------------------------------------------------------------------------\n"
	output_box.insert(tk.END, printout)





def pressed_create_parent():
	popup_title = "CREATE NEW PARENT RECORD"
	selection = "create_parent"
	label_a = "PARENT'S FIRST NAME:"
	label_b = "PARENT'S LAST NAME:"
	label_c = "PARENT'S STREET NUMBER:"
	label_d = "PARENT'S STREET NAME:"
	label_e = "PARENT'S ZIP CODE:"
	label_f = "PARENT'S PHONE AREA CODE:"
	label_g = "PARENT'S PHONE FIRST 3 NUMBERS AFTER AREA CODE:"
	label_h = "PARENT'S PHONE LAST 4 NUMBERS:"
	label_i = "PARENT'S EMAIL ADDRESS:"
	label_j = ""
	label_k = ""
	make_a_popup(popup_title, selection, label_a, label_b, label_c, label_d, label_e, label_f, label_g, label_h, label_i, label_j, label_k)



def pressed_create_child():
	popup_title = "CREATE NEW STUDENT RECORD"
	selection = "create_child"
	label_a = "PARENT'S DATABASE RECORD NUMBER:"
	label_b = "AFTERSCHOOL PROGRAM DATABASE RECORD NUMBER:"
	label_c = "CHILD'S FIRST NAME:"
	label_d = "CHILD'S LAST NAME:"
	label_e = ""
	label_f = ""
	label_g = ""
	label_h = ""
	label_i = ""
	label_j = ""
	label_k = ""
	make_a_popup(popup_title, selection, label_a, label_b, label_c, label_d, label_e, label_f, label_g, label_h, label_i, label_j, label_k)



def pressed_read_table():
	popup_title = "DISPLAY EXISTING RECORDS"
	selection = "read_table"
	label_a = "NAME OF TABLE (PARENT/CHILD/PROGRAM/ZIP) TO DISPLAY:"
	label_b = ""
	label_c = ""
	label_d = ""
	label_e = ""
	label_f = ""
	label_g = ""
	label_h = ""
	label_i = ""
	label_j = ""
	label_k = ""
	make_a_popup(popup_title, selection, label_a, label_b, label_c, label_d, label_e, label_f, label_g, label_h, label_i, label_j, label_k)



def pressed_query():
	popup_title = "ENTER ANY SQL QUERY"
	selection = "query"
	label_a = "TYPE ANY FULL SQL QUERY IN THIS BOX:"
	label_b = ""
	label_c = ""
	label_d = ""
	label_e = ""
	label_f = ""
	label_g = ""
	label_h = ""
	label_i = ""
	label_j = ""
	label_k = ""
	make_a_popup(popup_title, selection, label_a, label_b, label_c, label_d, label_e, label_f, label_g, label_h, label_i, label_j, label_k)



def pressed_update_parent():
	popup_title = "UPDATE EXISTING PARENT RECORD"
	selection = "update_parent"
	label_a = "PARENT'S FIRST NAME:"
	label_b = "PARENT'S LAST NAME:"
	label_c = "PARENT'S STREET NUMBER:"
	label_d = "PARENT'S STREET NAME:"
	label_e = "PARENT'S ZIP CODE:"
	label_f = "PARENT'S PHONE AREA CODE:"
	label_g = "PARENT'S PHONE FIRST 3 NUMBERS AFTER AREA CODE:"
	label_h = "PARENT'S PHONE LAST 4 NUMBERS:"
	label_i = "PARENT'S EMAIL ADDRESS:"
	label_j = "PARENT'S DATABASE RECORD NUMBER:"
	label_k = ""
	make_a_popup(popup_title, selection, label_a, label_b, label_c, label_d, label_e, label_f, label_g, label_h, label_i, label_j, label_k)



def pressed_update_child():
	popup_title = "UPDATE EXISTING STUDENT RECORD"
	selection = "update_child"
	label_a = "PARENT'S DATABASE RECORD NUMBER:"
	label_b = "AFTERSCHOOL PROGRAM DATABASE RECORD NUMBER:"
	label_c = "CHILD'S FIRST NAME:"
	label_d = "CHILD'S LAST NAME:"
	label_e = "CHILD'S DATABASE RECORD NUMBER:"
	label_f = ""
	label_g = ""
	label_h = ""
	label_i = ""
	label_j = ""
	label_k = ""
	make_a_popup(popup_title, selection, label_a, label_b, label_c, label_d, label_e, label_f, label_g, label_h, label_i, label_j, label_k)



def pressed_delete_parent():
	popup_title = "DELETE AN EXISTING PARENT RECORD"
	selection = "delete_parent"
	label_a = "PARENT'S DATABASE RECORD NUMBER:"
	label_b = ""
	label_c = ""
	label_d = ""
	label_e = ""
	label_f = ""
	label_g = ""
	label_h = ""
	label_i = ""
	label_j = ""
	label_k = ""
	make_a_popup(popup_title, selection, label_a, label_b, label_c, label_d, label_e, label_f, label_g, label_h, label_i, label_j, label_k)



def pressed_delete_child():
	popup_title = "DELETE AN EXISTING STUDENT RECORD"
	selection = "delete_child"
	label_a = "CHILD'S DATABASE RECORD NUMBER:"
	label_b = ""
	label_c = ""
	label_d = ""
	label_e = ""
	label_f = ""
	label_g = ""
	label_h = ""
	label_i = ""
	label_j = ""
	label_k = ""
	make_a_popup(popup_title, selection, label_a, label_b, label_c, label_d, label_e, label_f, label_g, label_h, label_i, label_j, label_k)



def pressed_hasfinancialassistance():
	popup_title = "PROGRAMS WITH FINANCIAL ASSISTANCE"
	selection = "hasfinancialassistance"
	label_a = "PRESS ENTER TO SEE ALL PROGRAMS THAT OFFER FINANCIAL ASSISTANCE"
	label_b = ""
	label_c = ""
	label_d = ""
	label_e = ""
	label_f = ""
	label_g = ""
	label_h = ""
	label_i = ""
	label_j = ""
	label_k = ""
	make_a_popup(popup_title, selection, label_a, label_b, label_c, label_d, label_e, label_f, label_g, label_h, label_i, label_j, label_k)



def pressed_waitlistdays():
	popup_title = "PROGRAMS BY WAITLIST DAYS"
	selection = "waitlistdays"
	label_a = "LIST PROGRAMS WITH WAITLIST DAYS LESS THAN OR EQUAL TO:"
	label_b = ""
	label_c = ""
	label_d = ""
	label_e = ""
	label_f = ""
	label_g = ""
	label_h = ""
	label_i = ""
	label_j = ""
	label_k = ""
	make_a_popup(popup_title, selection, label_a, label_b, label_c, label_d, label_e, label_f, label_g, label_h, label_i, label_j, label_k)



def pressed_financialassistancebyzip():
	popup_title = "PROGRAMS WITH FINANCIAL ASSISTANCE"
	selection = "financialassistancebyzip"
	label_a = "LIST PROGRAMS IN THIS ZIP CODE THAT OFFER FINANCIAL ASSISTANCE:"
	label_b = ""
	label_c = ""
	label_d = ""
	label_e = ""
	label_f = ""
	label_g = ""
	label_h = ""
	label_i = ""
	label_j = ""
	label_k = ""
	make_a_popup(popup_title, selection, label_a, label_b, label_c, label_d, label_e, label_f, label_g, label_h, label_i, label_j, label_k)



def pressed_waitlistdaysbyzip():
	popup_title = "PROGRAMS IN ZIP CODE BY WAITLIST DAYS"
	selection = "waitlistdaysbyzip"
	label_a = "WAITLIST DAYS LESS THAN OR EQUAL TO:"
	label_b = "IN THIS ZIP CODE:"
	label_c = ""
	label_d = ""
	label_e = ""
	label_f = ""
	label_g = ""
	label_h = ""
	label_i = ""
	label_j = ""
	label_k = ""
	make_a_popup(popup_title, selection, label_a, label_b, label_c, label_d, label_e, label_f, label_g, label_h, label_i, label_j, label_k)



def pressed_bycost():
	popup_title = "PROGRAMS BY COST"
	selection = "bycost"
	label_a = "LIST PROGRAMS WITH COST LESS THAN OR EQUAL TO:"
	label_b = ""
	label_c = ""
	label_d = ""
	label_e = ""
	label_f = ""
	label_g = ""
	label_h = ""
	label_i = ""
	label_j = ""
	label_k = ""
	make_a_popup(popup_title, selection, label_a, label_b, label_c, label_d, label_e, label_f, label_g, label_h, label_i, label_j, label_k)



def pressed_zipincome():
	popup_title = "LIST ZIP CODES WITH MEDIAN INCOME LESS THAN OR EQUAL TO"
	selection = "zipincome"
	label_a = "LIST ZIP CODES WITH MEDIAN INCOME LESS THAN OR EQUAL TO:"
	label_b = ""
	label_c = ""
	label_d = ""
	label_e = ""
	label_f = ""
	label_g = ""
	label_h = ""
	label_i = ""
	label_j = ""
	label_k = ""
	make_a_popup(popup_title, selection, label_a, label_b, label_c, label_d, label_e, label_f, label_g, label_h, label_i, label_j, label_k)



def pressed_byrating():
	popup_title = "LIST PROGRAMS WITH RATINGS GREATER THAN OR EQUAL TO"
	selection = "byrating"
	label_a = "LIST PROGRAMS WITH RATINGS (1-5) GREATER THAN OR EQUAL TO:"
	label_b = ""
	label_c = ""
	label_d = ""
	label_e = ""
	label_f = ""
	label_g = ""
	label_h = ""
	label_i = ""
	label_j = ""
	label_k = ""
	make_a_popup(popup_title, selection, label_a, label_b, label_c, label_d, label_e, label_f, label_g, label_h, label_i, label_j, label_k)






def make_a_popup(popup_title, selection, label_a, label_b, label_c, label_d, label_e, label_f, label_g, label_h, label_i, label_j, label_k):
	popup = tk.Tk()
	popup.title(popup_title)
	popup.geometry("1200x600")

	a_label = tk.Label(popup, text=label_a)
	a_label.pack()
	entry_a = tk.StringVar()
	a_entry_box = tk.Entry(popup, width=100, textvariable=entry_a)
	a_entry_box.pack()
	b_label = tk.Label(popup, text=label_b)
	b_label.pack()
	entry_b = tk.StringVar()
	b_entry_box = tk.Entry(popup, width=100, textvariable=entry_b)
	b_entry_box.pack()
	c_label = tk.Label(popup, text=label_c)
	c_label.pack()
	entry_c = tk.StringVar()
	c_entry_box = tk.Entry(popup, width=100, textvariable=entry_c)
	c_entry_box.pack()
	d_label = tk.Label(popup, text=label_d)
	d_label.pack()
	entry_d = tk.StringVar()
	d_entry_box = tk.Entry(popup, width=100, textvariable=entry_d)
	d_entry_box.pack()
	e_label = tk.Label(popup, text=label_e)
	e_label.pack()
	entry_e = tk.StringVar()
	e_entry_box = tk.Entry(popup, width=100, textvariable=entry_e)
	e_entry_box.pack()
	f_label = tk.Label(popup, text=label_f)
	f_label.pack()
	entry_f = tk.StringVar()
	f_entry_box = tk.Entry(popup, width=100, textvariable=entry_f)
	f_entry_box.pack()
	g_label = tk.Label(popup, text=label_g)
	g_label.pack()
	entry_g = tk.StringVar()
	g_entry_box = tk.Entry(popup, width=100, textvariable=entry_g)
	g_entry_box.pack()
	h_label = tk.Label(popup, text=label_h)
	h_label.pack()
	entry_h = tk.StringVar()
	h_entry_box = tk.Entry(popup, width=100, textvariable=entry_h)
	h_entry_box.pack()
	i_label = tk.Label(popup, text=label_i)
	i_label.pack()
	entry_i = tk.StringVar()
	i_entry_box = tk.Entry(popup, width=100, textvariable=entry_i)
	i_entry_box.pack()
	j_label = tk.Label(popup, text=label_j)
	j_label.pack()
	entry_j = tk.StringVar()
	j_entry_box = tk.Entry(popup, width=100, textvariable=entry_j)
	j_entry_box.pack()
	k_label = tk.Label(popup, text=label_k)
	k_label.pack()
	entry_k = tk.StringVar()
	k_entry_box = tk.Entry(popup, width=100, textvariable=entry_k)
	k_entry_box.pack()


	def pressed_save():
		save(selection, a_entry_box.get(), b_entry_box.get(), c_entry_box.get(), d_entry_box.get(), e_entry_box.get(), f_entry_box.get(), g_entry_box.get(), h_entry_box.get(), i_entry_box.get(), j_entry_box.get(), k_entry_box.get())
		popup.destroy()
		return

	save_button = tk.Button(popup, text="ENTER", command=pressed_save)
	save_button.place(x=10, y=10)
	tk.mainloop()





window = tk.Tk()
window.title("DATABASE PROJECT")
window.geometry("1300x700")


query_button = tk.Button(window, text="SQL QUERY", command=pressed_query)
query_button.place(x=10, y=10)

create_parent_button = tk.Button(window, text="ADD PARENT", command=pressed_create_parent)
create_parent_button.place(x=10, y=50)

create_child_button = tk.Button(window, text="ADD CHILD", command=pressed_create_child)
create_child_button.place(x=10, y=90)

read_table_button = tk.Button(window, text="READ TABLE", command=pressed_read_table)
read_table_button.place(x=10, y=130)

update_parent_button = tk.Button(window, text="UPDATE PARENT", command=pressed_update_parent)
update_parent_button.place(x=10, y=170)

update_child_button = tk.Button(window, text="UPDATE CHILD", command=pressed_update_child)
update_child_button.place(x=10, y=210)

delete_parent_button = tk.Button(window, text="DELETE PARENT", command=pressed_delete_parent)
delete_parent_button.place(x=10, y=250)

delete_child_button = tk.Button(window, text="DELETE CHILD", command=pressed_delete_child)
delete_child_button.place(x=10, y=290)

hasfinancialassistance_button = tk.Button(window, text="HAS FINANCIAL ASSISTANCE", command=pressed_hasfinancialassistance)
hasfinancialassistance_button.place(x=10, y=330)

financialassistancebyzip_button = tk.Button(window, text="FINANCIAL ASSISTANCE BY ZIP", command=pressed_financialassistancebyzip)
financialassistancebyzip_button.place(x=10, y=370)

waitlistdays_button = tk.Button(window, text="BY WAITLIST DAYS", command=pressed_waitlistdays)
waitlistdays_button.place(x=10, y=410)

waitlistdaysbyzip_button = tk.Button(window, text="WAITLIST DAYS BY ZIP", command=pressed_waitlistdaysbyzip)
waitlistdaysbyzip_button.place(x=10, y=450)

bycost_button = tk.Button(window, text="BY COST", command=pressed_bycost)
bycost_button.place(x=10, y=490)

zipincome_button = tk.Button(window, text="ZIP CODE INCOMES", command=pressed_zipincome)
zipincome_button.place(x=10, y=530)

byrating_button = tk.Button(window, text="BY RATING", command=pressed_byrating)
byrating_button.place(x=10, y=570)


output_box_label = tk.Label(window, text="SQL OUTPUT:")
output_box_label.place(x=250, y=10)
output_box = tk.Text(window, width=100)
output_box.place(x=250, y=50)

window.mainloop()

