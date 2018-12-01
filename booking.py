from tkinter import *
import psycopg2 as p

connect = p.connect(database='Booking', user='postgres', password='root')
connect1 = p.connect(database='Cinema', user='postgres', password='root')

cursor = connect.cursor()
cursor1 = connect1.cursor()

def booking():
	Label(screen7, text = "Booking sucess", fg = "green", font = ("Calibri", 11)).pack()

def free_seats():
	global screen7
	screen7 = Toplevel(screen)
	screen7.title("Free Seats")
	screen7.geometry("500x500")

	cursor1.execute('SELECT * from Free;')
	f = cursor1.fetchall()

	Label(screen7, text = "Free places: ", bg = "grey", fg = "black", width = "500", height = "3").pack()
	Label(text = "").pack()

	for i in f:
		Label(screen7, text = i[1], height = "2", width = "30").pack()
		Button(screen7, text = "Select", height = "2", width = "30", command = booking).pack()

def booking_seats():
	global screen6
	screen6 = Toplevel(screen)
	screen6.title("Seats")
	screen6.geometry("500x500")

	cursor1.execute('SELECT * from Hall;')
	h = cursor1.fetchall()

	Label(screen6, text = "All places: ", bg = "grey", fg = "black", width = "500", height = "3").pack()
	Label(text = "").pack()

	for i in h:
		Label(screen6, text = i[1], height = "2", width = "30").pack()
	Button(screen6, text = "Free places", height = "2", width = "30", command = free_seats).pack()

def movie():
	global screen5
	screen5 = Toplevel(screen)
	screen5.title("Movies")
	screen5.geometry("500x500")

	cursor1.execute('SELECT * from Movies;')
	m = cursor1.fetchall()

	Label(screen5, text = "Please, select the movie", bg = "grey", fg = "black", width = "500", height = "3").pack()
	Label(text = "").pack()

	for i in m:
		movie = "Movie: " + i[1]
		date = "Date: " + str(i[2])
		time = "Time: " + str(i[3])
		price = "Price: " + i[4]
		hall = "Hall: " + str(i[5])

		Label(screen5, text = movie, height = "2", width = "30").pack()
		Label(screen5, text = date, height = "2", width = "30").pack()
		Label(screen5, text = time, height = "2", width = "30").pack()
		Label(screen5, text = price, height = "2", width = "30").pack()
		Label(screen5, text = hall, height = "2", width = "30").pack()

		Button(screen5, text = "Select", height = "2", width = "30", command = booking_seats).pack()

def delete():
	screen4.destroy()

def incorrect():
	
	global screen4
	screen4 = Toplevel(screen)
	screen4.title("incorrect")
	screen4.geometry("200x150")
	Label(screen4, text = "Login or password is incorrect").pack()
	Button(screen4, text = "OK", command = delete).pack()

def cinema():

	global screen3
	screen3 = Toplevel(screen)
	screen3.title("Cinema")
	screen3.geometry("500x500")

	cursor1.execute('SELECT * from Cinemas;')
	c = cursor1.fetchall()

	Label(screen3, text = "Welcome, select the cinema, in which you wanna buy a ticket:", bg = "grey", fg = "black", width = "500", height = "3").pack()
	Label(text = "").pack()

	for i in c:
		Label(screen3, text = i[1]).pack()

		Button(screen3, text = "Select", height = "2", width = "30", command = movie).pack()


def login_user():

	login1 = login_verify.get()
	password1 = password_verify.get()

	login_entry.delete(0, END)
	password_entry.delete(0, END)

	cursor.execute('SELECT * from Users;')
	data = cursor.fetchall()
	
	correct = False
	for i in data:
		if i[0] == login1:
			if i[1] == password1:
				correct = True
				#cinema()
				break	
	if correct == True:
		cinema()
	else:
		incorrect()


def register_user():
	log = username.get()
	pas = password.get()

	cursor.execute("INSERT INTO Users(login, password) VALUES('%s', '%s')"%(log,pas))
	connect.commit()

	username_entry.delete(0, END)
	pass_entry.delete(0, END)

	Label(screen1, text = "Registration sucess", fg = "green", font = ("Calibri", 11)).pack()

def register():
	global screen1
	screen1 = Toplevel(screen)

	screen1.title("Register")
	screen1.geometry("400x350")

	global username
	global password
	global username_entry
	global pass_entry

	username = StringVar()
	password = StringVar()

	Label(screen1, text = "Please, sign up:").pack()
	Label(screen1, text = "").pack()

	Label(screen1, text = "Username:").pack()
	username_entry = Entry(screen1, textvariable = username)
	username_entry.pack()

	Label(screen1, text = "Password:").pack()
	pass_entry = Entry(screen1, textvariable = password)
	pass_entry.pack()

	Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()

def login():
	global screen2
	global login_verify
	global password_verify
	global login_entry
	global password_entry
	screen2 = Toplevel(screen)

	login_verify = StringVar()
	password_verify = StringVar()

	screen2.title("Log in")
	screen2.geometry("400x350")

	Label(screen2, text = "Please, sign in:").pack()
	Label(screen2, text = "").pack()

	Label(screen2, text = "Login:").pack()
	login_entry = Entry(screen2, textvariable = login_verify)
	login_entry.pack()

	Label(screen2, text = "Password:").pack()
	password_entry = Entry(screen2, textvariable = password_verify)
	password_entry.pack()
	Label(screen2, text = "").pack()

	Button(screen2, text = "Sign in", width = 10, height = 1, command = login_user).pack()

def console():
	global screen
	screen = Tk()
	screen.geometry("500x500")
	screen.title("Ticket booking")

	head = Label(text = "Ticket booking", bg = "grey", fg = "black", width = "500", height = "3")
	head.pack()
	Label(text = "").pack()
	Button(text = "Sign in", height = "2", width = "30", command = login).pack()
	Label(text = "").pack()
	Button(text = "Sign up", height = "2", width = "30", command = register).pack()

	screen.mainloop()

console()
