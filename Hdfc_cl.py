from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox
from tkinter import simpledialog, messagebox


window = Tk()
window.geometry('925x600')
window.configure(bg='white')

class Registration:
    def __init__(self, window):
        self.money = 0
        self.window = window
        self.window.title('HDFC Bank: Secure and Safe')
        self.window.resizable(False, False)
        self.sideimg = Image.open('HDFC_Bank_Logo.jpg').resize((380, 450))
        self.img = ImageTk.PhotoImage(self.sideimg)

        Label(window, image=self.img, bg='white').place(x=50, y=50)
        self.frame = Frame(window, bg='white', width='480', height='980', border=2)
        self.frame.place(x=470, y=40)

        self.mainlabel = ttk.Label(self.frame, text='HDFC Bank: Secure and Safe', font='cambria 23 bold', background='white', foreground='Red')
        self.mainlabel.pack()

        self.name = StringVar()

        self.name_entry = Entry(self.frame, width=25, textvariable=self.name, foreground='blue', border=0, font='cambria 14')
        self.name_entry.insert(0, 'Enter Your Name')
        self.name_entry.pack(pady=(30, 0))
        self.name_entry.bind("<FocusIn>", lambda event: self.on_focus_in(event, 'Enter Your Name'))
        self.name_entry.bind("<FocusOut>", lambda event: self.on_focus_out(event, 'Enter Your Name'))
        Frame(self.frame, width=295, height=2, bg='blue').pack()

        self.pan = StringVar()
        self.pan_entry = Entry(self.frame, width=25, textvariable=self.pan, foreground='blue', font='cambria 14', border=0)
        self.pan_entry.insert(0, 'Enter your Pan card number')
        self.pan_entry.pack(pady=(30, 0))
        self.pan_entry.bind("<FocusIn>", lambda event: self.on_focus_in(event, 'Enter your Pan card number'))
        self.pan_entry.bind("<FocusOut>", lambda event: self.on_focus_out(event, 'Enter your Pan card number'))
        Frame(self.frame, width=295, height=2, bg='blue').pack()

        self.adhar = StringVar()
        self.adhar_entry = Entry(self.frame, width=25, textvariable=self.adhar, foreground='blue', font='cambria 14', border=0)
        self.adhar_entry.insert(0, 'Enter Your Adhar number')
        self.adhar_entry.pack(pady=(30, 0))
        self.adhar_entry.bind("<FocusIn>", lambda event: self.on_focus_in(event, 'Enter Your Adhar number'))
        self.adhar_entry.bind("<FocusOut>", lambda event: self.on_focus_out(event, 'Enter Your Adhar number'))
        Frame(self.frame, width=295, height=2, bg='blue').pack()

        self.email = StringVar()
        self.email_entry = Entry(self.frame, width=25, textvariable=self.email, foreground='blue', font='cambria 14', border=0)
        self.email_entry.insert(0, 'Enter Your Email Identity')
        self.email_entry.pack(pady=(30, 0))
        self.email_entry.bind("<FocusIn>", lambda event: self.on_focus_in(event, 'Enter Your Email Identity'))
        self.email_entry.bind("<FocusOut>", lambda event: self.on_focus_out(event, 'Enter Your Email Identity'))
        Frame(self.frame, width=295, height=2, bg='blue').pack(pady=0)

        self.contact = StringVar()
        self.contact_entry = Entry(self.frame, width=25, textvariable=self.contact, foreground='blue', font='cambria 14', border=0)
        self.contact_entry.insert(0, 'Enter your Contact Number')
        self.contact_entry.pack(pady=(30, 0))
        self.contact_entry.bind("<FocusIn>", lambda event: self.on_focus_in(event, 'Enter your Contact Number'))
        self.contact_entry.bind("<FocusOut>", lambda event: self.on_focus_out(event, 'Enter your Contact Number'))
        self.contact_entry.bind("<KeyRelease>", self.validate_contact)
        Frame(self.frame, width=295, height=2, bg='blue').pack()

        self.button = Button(self.frame, width=36, text='Create Account', border=0, font='Cambria 15 bold', foreground='white', background='red', command=self.create_account)
        self.button.pack(pady=(40, 20))
        Label(self.frame, text='Already Have Account?', font='cambria 10', fg='black', background='white').pack()
        self.sinup = Button(self.frame, text='Log In', width=7, bg='white', border=0, background='white', foreground='Blue', command=self.login)
        self.sinup.pack()

    def on_focus_in(self, event, placeholder):
        if event.widget.get() == placeholder:
            event.widget.delete(0, END)
            event.widget.config(fg='black')

    def on_focus_out(self, event, placeholder):
        if event.widget.get() == '':
            event.widget.insert(0, placeholder)
            event.widget.config(fg='blue')

    def validate_contact(self, event):
        value = self.contact.get()
        if not value.isdigit():
            self.contact.set(value[:-1])  # Remove the last character if it's not a digit
        if len(value) > 10:
            self.contact.set(value[:10])  # Limit to 10 digits

    def create_account(self):
        name = self.name.get()
        pan = self.pan.get()
        adhar = self.adhar.get()
        email = self.email.get()
        contact = self.contact.get()
        password = '123@' + name

        mydb = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password='root@123',
            database='HDFC'
        )
        cursor = mydb.cursor()
        cursor.execute('INSERT INTO Accountholders1 (contact, Name, Pancard, Adharcard, Email, Password) VALUES (%s, %s, %s, %s, %s, %s)',
                       (contact, name, pan, adhar, email, password))
        self.login()
        mydb.commit()
        mydb.close()
    def login(self):
      
     login_window = Toplevel(self.window)
     login_window.title('Login to HDFC Bank')
     login_window.geometry('900x500')
     login_window.title('HDFC Bank: Secure and Safe')
     login_window.resizable(False, False)

     self.sideimg1 = Image.open('HDFC_Bank_Logo.jpg').resize((340, 430))
     self.img = ImageTk.PhotoImage(self.sideimg1)

     Label(login_window, image=self.img, bg='white').place(x=50, y=20)

     self.frame1 = Frame(login_window, bg='white', border=2)
     self.frame1.place(x=450, y=20, width=400, height=480)

     self.mainlabel = ttk.Label(self.frame1, text='HDFC Bank: Secure and Safe', font='cambria 21 bold', background='white', foreground='Red')
     self.mainlabel.pack(pady=(30))

     self.contact1 = StringVar()
     self.contact1_entry = Entry(self.frame1, width=25, textvariable=self.contact1, foreground='blue', font='cambria 14', border=0)
     self.contact1_entry.pack(pady=(50, 10))
     self.contact1_entry.insert(0, 'Enter your PhoneNumber')
     Frame(self.frame1, width=295, height=2, bg='blue').pack()

     self.password1 = StringVar()
     self.passentry = Entry(self.frame1, width=25, textvariable=self.password1, foreground='blue', font='cambria 14', border=0)
     self.passentry.pack(pady=(50, 10))
     self.passentry.insert(0, 'Enter Your password ')
     Frame(self.frame1, width=295, height=2, bg='blue').pack(pady=0)

     login_button = Button(self.frame1, text='Login', width=20, border=0, font='Cambria 15 bold', foreground='white', background='red', command=self.authenticate)
     login_button.pack(pady=(50, 10))

     login_window.mainloop()

    
    def authenticate(self):
     self.gotpass = self.passentry.get()
     self.gotcon = self.contact1_entry.get()

     mydbconfig = {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': 'root@123',
        'database': 'HDFC'
     }

     try:
        connection = mysql.connector.connect(**mydbconfig)

        if connection.is_connected():
            cursor = connection.cursor()

            # Query the database for the user's information based on the contact number
            cursor.execute("SELECT contact, Password FROM Accountholders1 WHERE contact = %s", (self.gotcon,))
            result = cursor.fetchone()

            if result:
                stored_contact, stored_password = result

                # Check if the provided password matches the stored password
                if self.gotpass == stored_password:
                    messagebox.showinfo("Authentication", "Authentication successful")
                    self.thirdmenu()
                    # Add code to open the user's account or perform other actions
                else:
                    messagebox.showerror("Authentication", "Incorrect password")
            else:
                messagebox.showerror("Authentication", "Account Not found")
        else:
            messagebox.showerror("Database Error", "Unable to connect to the database")

     except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
     finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("Database connection closed")
    def thirdmenu(self):
       window3 = Toplevel(self.window)
       window3.title('Login to HDFC Bank')
       window3.geometry('500x500')
       window3.title('HDFC Bank: Secure and Safe')
       window3.resizable(False, False)
       self.labelel=Label(window3,text='HDFC : Credit Info',font='cambria 23 bold',background='white',foreground='red')
       self.labelel.pack()
       self.img3=Image.open('bank2.jpeg')
       self.imgp=ImageTk.PhotoImage(self.img3)
       Label(window3, image=self.imgp, bg='white').place(x=150, y=50)
       self.wl=Label(window3,text='Welcome to HDFC internet Banking',foreground='blue',background='white',font='cambria 18',).pack(pady=(200,10))
       self.button1=Button(window3,text='Deposit Money',width=15,font='Cambria 17 bold',background='Red',foreground='white',command=self.deposit).pack(pady=10)
       self.button2=Button(window3,text='WithDraw Money',width=15,font='Cambria 17 bold',background='Red',foreground='white',command=self.withdraw).pack(pady=10)
       self.button3=Button(window3,text='Show Balance',width=15,font='Cambria 17 bold',background='Red',foreground='white',command=self.show_balance).pack(pady=10)
    
    def deposit(self):
        amount = simpledialog.askfloat("Deposit Money", "Enter the amount to deposit:")
        if amount > 0 and amount < 100000:
            self.money += amount
            self.update_balance_in_database()  # Update the balance in the database
            messagebox.showinfo("Deposit Successful", f"Deposited {amount} successfully.")
        else:
            messagebox.showerror("Invalid Amount", "Amount should be between 0 and 100000.")

    def withdraw(self):
        amount2 = simpledialog.askfloat("Withdraw Money", "Enter the amount to withdraw:")
        if amount2 <= self.money:
            self.money -= amount2
            self.update_balance_in_database()  # Update the balance in the database
            messagebox.showinfo("Withdrawal Successful", f"Withdrew {amount2} successfully.")
        else:
            messagebox.showerror("Insufficient Balance", "Not enough balance for this withdrawal.")

    def show_balance(self):
        messagebox.showinfo("Account Information", f"Balance: {self.money}")

    def update_balance_in_database(self):
        mydbconfig = {
            'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'password': 'root@123',
            'database': 'HDFC'
        }

        try:
            connection = mysql.connector.connect(**mydbconfig)

            if connection.is_connected():
                cursor = connection.cursor()

                # Update the balance in the database
                cursor.execute("UPDATE Accountholders1 SET Balance = %s WHERE contact = %s", (self.money, self.gotcon))
                connection.commit()

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

        finally:
            if 'connection' in locals() and connection.is_connected():
                connection.close()
                print("Database connection closed")

if __name__ == "__main__":
    registration = Registration(window)
    window.mainloop()
