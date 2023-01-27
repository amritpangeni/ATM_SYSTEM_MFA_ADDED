from tkinter import *
import random
import mysql.connector
from tkinter import ttk
from playsound import playsound
from twilio.rest import Client


class otp_auth_atm:
    def __init__(self, window, mydb):
        self.data = []
        self.otp_verified = False
        self.otp_generated = False
        self.check_pin = False
        self.cursor = mydb.cursor()
        self.card_in_stat = False
        window.geometry("380x538+812+80")
        window.resizable(0, 0)
        window.configure(background="#0dd754")

        # Frame 2 - Design Purpose (Cash out Frame)
        self.frame2 = Frame(window, relief='groove', borderwidth=2, background="#d9d9d9")
        self.frame2.place(relx=0.282, rely=0.866, relheight=0.065
                          , relwidth=0.405)

        # Frame 3 - Design Purpose (Up Frame after word ATM)
        self.frame3 = Frame(window, relief='groove', background="#43c04d")
        self.frame3.place(relx=0.0, rely=0.102, relheight=0.046
                          , relwidth=1.011)

        # Frame 7 - ATM Screen main frame
        self.frame7 = Frame(window, relief="groove", background="#3cc851")
        self.frame7.place(relx=0.071, rely=0.112, relheight=0.418
                          , relwidth=0.853)

        # Frame 8 - Design Purpose (ATM Screen)
        self.frame8 = Frame(self.frame7, relief="groove", background="#e1e1e1", borderwidth="2")
        self.frame8.place(relx=0.160, rely=0.044, relheight=0.689
                          , relwidth=0.691)

        # Frame 6 - Design Purpose (ATM Keypad main Frame)
        self.frame6 = Frame(window, relief="groove", background="#50b461")
        self.frame6.place(relx=0.079, rely=0.485, relheight=0.299
                          , relwidth=0.853)

        # Frame 9 - Design Purpose (ATM Keypad)
        self.frame9 = Frame(self.frame6, relief="groove", background="#e1e1e1", borderwidth="2")
        self.frame9.place(relx=0.16, rely=0.041, relheight=0.925, relwidth=0.66)

        # Label 1 - Design Purpose
        self.label1 = Label(window, background="#0dd754",
                            font="-family {Segoe UI Variable Display Semib} -size 20 -weight bold",
                            foreground="#ffffff", text='''ATM''')
        self.label1.place(relx=0.263, rely=0.019, height=41, width=173)

        # Frame 4 - Design Purpose (Left Border Frame)
        self.frame4 = Frame(window, relief="groove", background="#43c04d")
        self.frame4.place(relx=0.0, rely=0.112, relheight=0.678
                          , relwidth=0.092)

        # Frame 5 - Design Purpose (Right Border Frame)
        self.frame5 = Frame(window, relief="groove", background="#43c04d")
        self.frame5.place(relx=0.921, rely=0.112, relheight=0.678
                          , relwidth=0.092)

        # Frame 1 - Design Purpose (Down Frame)
        self.frame1 = Frame(window, relief="groove", borderwidth=2, background="#0dd754")
        self.frame1.place(relx=-0.003, rely=0.786, relheight=0.214, relwidth=1.011)

        # Button 1 - Top Screen Left - 1
        self.button1 = Button(self.frame7, background="#d9d9d9", borderwidth=0, command=self.balance_eq)
        self.button1.place(relx=0.049, rely=0.20, height=24, width=27)

        # Button 2 - Top Screen Left - 2
        self.button2 = Button(self.frame7, background="#d9d9d9", borderwidth=0, command=self.cash_checkout)
        self.button2.place(relx=0.049, rely=0.400, height=24, width=27)

        # Button 3 - Top Screen Left - 3
        self.button3 = Button(self.frame7, background="#d9d9d9", borderwidth=0, command=self.pin_change)
        self.button3.place(relx=0.049, rely=0.600, height=24, width=27)

        # Button 01 - Top Screen Right - 1
        self.Button01 = Button(self.frame7, background="#d9d9d9", borderwidth=0, command=self.pin_change)
        self.Button01.place(relx=0.88, rely=0.600, height=24, width=27)

        # Button 02 - Top Screen Right - 2
        self.Button02 = Button(self.frame7, background="#d9d9d9", borderwidth=0, command=self.cash_checkout)
        self.Button02.place(relx=0.88, rely=0.400, height=24, width=27)

        # Button 03 - Top Screen Right - 3
        self.Button03 = Button(self.frame7, background="#d9d9d9", borderwidth=0, command=self.balance_eq)
        self.Button03.place(relx=0.88, rely=0.200, height=24, width=27)

        # Button 001 - Keypad numbers
        self.button001 = ttk.Button(self.frame9, text="1", command=lambda: self.press('1'))
        self.button001.place(relx=0.050, rely=0.030, height=35, width=46)

        # Button 002 - Keypad numbers
        self.button002 = ttk.Button(self.frame9, text="2", command=lambda: self.press('2'))
        self.button002.place(relx=0.270, rely=0.030, height=35, width=46)

        # Button 003 - Keypad numbers
        self.button003 = ttk.Button(self.frame9, text="3", command=lambda: self.press('3'))
        self.button003.place(relx=0.490, rely=0.030, height=35, width=46)

        # Button 004 - Keypad numbers
        self.button004 = ttk.Button(self.frame9, text="4", command=lambda: self.press('4'))
        self.button004.place(relx=0.050, rely=0.260, height=35, width=46)

        # Button 005 - Keypad numbers
        self.button005 = ttk.Button(self.frame9, text="5", command=lambda: self.press('5'))
        self.button005.place(relx=0.270, rely=0.260, height=35, width=46)

        # Button 006 - Keypad numbers
        self.button006 = ttk.Button(self.frame9, text="6", command=lambda: self.press('6'))
        self.button006.place(relx=0.490, rely=0.260, height=35, width=46)

        # Button 007 - Keypad numbers
        self.button007 = ttk.Button(self.frame9, text="7", command=lambda: self.press('7'))
        self.button007.place(relx=0.050, rely=0.500, height=35, width=46)

        # Button 008 - Keypad numbers
        self.button008 = ttk.Button(self.frame9, text="8", command=lambda: self.press('8'))
        self.button008.place(relx=0.270, rely=0.500, height=35, width=46)

        # Button 009 - Keypad numbers
        self.button009 = ttk.Button(self.frame9, text="9", command=lambda: self.press('9'))
        self.button009.place(relx=0.490, rely=0.500, height=35, width=46)

        # Button 010 - Keypad numbers
        self.button010 = ttk.Button(self.frame9, text=" ")
        self.button010.place(relx=0.050, rely=0.740, height=35, width=46)

        # Button 000 - Keypad numbers
        self.button000 = ttk.Button(self.frame9, text="0", command=lambda: self.press('0'))
        self.button000.place(relx=0.270, rely=0.740, height=35, width=46)

        # Button 011 - Keypad numbers
        self.button011 = ttk.Button(self.frame9, text=" ")
        self.button011.place(relx=0.490, rely=0.740, height=35, width=46)

        # Button 012 - Cancel
        self.button012 = Button(self.frame9, background="#feb4b1", borderwidth=0, text="Cancel", command=self.cancel)
        self.button012.place(relx=0.734, rely=0.060, height=34, width=47)

        # Button 013 - Clear
        self.button013 = Button(self.frame9, background='#eaf1be', borderwidth=0, text='Clear', command=self.clear)
        self.button013.place(relx=0.729, rely=0.350, height=34, width=47)

        # Button 014 - Enter
        self.button014 = Button(self.frame9, background="#89da87", borderwidth=0, text='Enter',
                                command=self.pin_auth_check)
        self.button014.place(relx=0.734, rely=0.660, height=34, width=47)

        # Frame 10 - Bill Out - Outside
        self.frame10 = Frame(window, borderwidth="2", background="#d9d9d9", relief='groove')
        self.frame10.place(relx=0.204, rely=0.428, relheight=0.046, relwidth=0.197)

        # Frame 11 - Bill Out - Inside
        self.frame11 = Frame(self.frame10, relief='groove', background='#68979b')
        self.frame11.place(relx=0.211, rely=0.446, relheight=0.007
                           , relwidth=0.550)

        # Frame 12 - Cash in
        self.frame12 = Frame(self.frame7, relief='groove', borderwidth=2, background="#d9d9d9")
        self.frame12.place(relx=0.614, rely=0.756, relheight=0.111, relwidth=0.231)

        # Button 015 - Card In
        self.button015 = ttk.Button(self.frame12, text='CARD', command=self.card_in)
        self.button015.place(relx=0.200, rely=0.010, relheight=0.970
                             , relwidth=0.642)

        # Screen
        self.label = Label(self.frame8, text="* PADAM BANK *", font="times 12", relief='groove', foreground="red")
        self.label.pack()

        self.screen_ent1_var = StringVar()
        self.screen_ent1 = Entry(self.frame8, state='readonly', relief='groove', borderwidth=2, font="times 12",
                                 justify='center',
                                 textvariable=self.screen_ent1_var)
        self.screen_ent1.place(relx=0.050, rely=0.210, relheight=0.200
                               , relwidth=0.900)
        self.screen_ent1_var.set('Welcome')

        self.screen_ent2_var = StringVar()
        self.screen_ent2 = Entry(self.frame8, state='readonly', readonlybackground='white', font="times 10",
                                 justify='center', relief='groove', borderwidth=2, textvariable=self.screen_ent2_var)
        self.screen_ent2.place(relx=0.050, rely=0.480, relheight=0.200
                               , relwidth=0.900)
        self.screen_ent2_var.set('Please insert your card !')

        self.screen_ent3_var = StringVar()
        self.screen_ent3 = Entry(self.frame8, state='readonly', foreground="red", font="times 10", justify='center',
                                 relief='groove', borderwidth=2,
                                 textvariable=self.screen_ent3_var)
        self.screen_ent3_var.set('Inquire | Withdraw | Change')
        self.screen_ent3.place(relx=0.050, rely=0.770, relheight=0.200
                               , relwidth=0.900)

    def card_in(self):
        playsound('atmin.wav')
        self.cursor.execute('select * from card_info')
        data = self.cursor.fetchall()
        for i in data:
            self.data.append(i)
        name = self.data[0][1]
        account_no = self.data[0][2]
        mydb.commit()
        self.card_in_stat = True
        self.button015.config(state='disabled')
        self.screen_ent2.config(show='*')
        self.screen_ent1_var.set("Enter your pin:")
        self.screen_ent2_var.set('')
        self.screen_ent3_var.set(f'Welcome, {account_no}')

    def cancel(self):
        playsound('buttonsound.mp3')
        self.button015.config(state='enabled')
        self.card_in_stat = False
        self.screen_ent2_var.set('Please insert your card !')
        self.screen_ent1_var.set('Welcome')
        self.screen_ent3_var.set('Inquire | Withdraw | Change')
        self.screen_ent2.config(show='')
        self.screen_ent3.config(foreground="red")
        if self.check_pin:
            self.button014.config(command=self.pin_auth_check)

        if self.otp_verified:
            self.otp_verified = False

    def press(self, num):
        playsound('buttonsound.mp3')
        if self.card_in_stat and self.otp_verified == False:
            expression = str(self.screen_ent2_var.get())
            expression = expression + str(num)
            self.screen_ent2_var.set(expression)

    def clear(self):
        playsound('buttonsound.mp3')
        if self.card_in_stat and not self.otp_verified:
            self.screen_ent2_var.set('')

    def pin_auth_check(self):
        playsound('buttonsound.mp3')
        if self.card_in_stat:
            self.data = []
            self.cursor.execute('select * from card_info')
            data = self.cursor.fetchall()
            for i in data:
                self.data.append(i)
            pin_entered = str(self.screen_ent2_var.get())
            pin_stored = str(self.data[0][3])

            # with open('pin_store', 'r') as f:
            #     pin_stored = f.readline()

            if pin_entered == str(pin_stored):
                self.check_pin = True
                otp = random.randint(1000, 9999)
                self.otp_generated = str(otp)
                print(self.otp_generated)
                # client = Client('AC447fc4b360f77d29ecbe49cccc97b775', '802b5879fbfa676fc707082c3b6afd5c')
                # message = client.messages \
                #     .create(
                #     body=f"OTP CODE: {self.otp_generated}",
                #     from_='+13854816093',
                #     to='+9779863856347'
                # )
                self.screen_ent1_var.set('ENTER OTP:')
                self.screen_ent2_var.set('')
                self.screen_ent3_var.set('OTP SENT TO YOUR PHONE')
                self.button014.config(command=self.otp_auth)
            else:
                self.screen_ent2_var.set('')
                self.screen_ent3_var.set('Wrong PIN, Please Try Again')

    def cash_checkout(self):
        if self.card_in_stat and self.otp_verified:
            self.otp_verified = False
            self.screen_ent2_var.set('')
            self.screen_ent1_var.set('Enter Amount:')
            self.screen_ent3_var.set('Amount Withdraw')
            self.button014.config(command=self.amount_withdraw)

    def amount_withdraw(self):
        amount = self.screen_ent2_var.get()
        balance = self.data[0][4]
        # with open('balance', 'r') as f:
        #     balance = f.readline()
        try:
            balance = int(balance)
            amount = int(amount)
            if amount > balance:
                self.screen_ent3_var.set('Insufficient Balance')
            else:
                withdraw = balance - amount
                # with open('balance', 'w') as f:
                #     f.write(str(withdraw))
                self.cursor.execute(f'update card_info set balance={withdraw} where id = 1')
                mydb.commit()
                self.otp_verified = True
                self.screen_ent1_var.set('Thank you')
                self.screen_ent3_var.set('withdraw successful')
                self.screen_ent2_var.set('')
                playsound('cashout.mp3')
                # self.cancel()

        except Exception:
            self.screen_ent3_var.set('Invalid amount')

    def otp_auth(self):
        otp_entered = self.screen_ent2_var.get()
        if otp_entered == self.otp_generated:
            self.otp_verified = True
            self.screen_ent3.config(foreground="black")
            self.screen_ent1_var.set('Balance Enquiry')
            self.screen_ent2_var.set('Withdraw Amount')
            self.screen_ent3_var.set('Change Pin')
            self.screen_ent2.config(show='')
        else:
            self.screen_ent2_var.set('')
            self.screen_ent3_var.set('Wrong PIN, Please Try Again')

    def balance_eq(self):
        if self.card_in_stat and self.otp_verified:
            self.data = []
            self.cursor.execute('select * from card_info')
            data = self.cursor.fetchall()
            for i in data:
                self.data.append(i)

            self.screen_ent1_var.set('Your Current Balance:')
            balance = self.data[0][4]
            # with open('balance', 'r') as f:
            #     balance = str(f.readline())
            self.screen_ent2_var.set(balance)
            self.screen_ent3_var.set('')

    def pin_change(self):
        if self.card_in_stat and self.otp_verified:
            self.screen_ent1_var.set('Enter New Pin:')
            self.otp_verified = False
            self.screen_ent2_var.set('')
            self.screen_ent2.config(show="*")
            self.button014.config(command=self.change_pin)

    def change_pin(self):
        new_pin = self.screen_ent2_var.get()
        if len(new_pin) == 4:

            self.cursor.execute(f'update card_info set pin={new_pin} where id = 1')
            mydb.commit()
            # with open('pin_store', 'w') as f:
            #     f.write(str(new_pin))

            with open('pin_store', 'w') as f:
                pass
            self.screen_ent3_var.set('Change Successful')
            self.screen_ent2_var.set('')
        else:
            self.screen_ent3_var.set('Invalid Pin')


if __name__ == "__main__":
    window = Tk()
    # MySQL connection
    mydb = mysql.connector.connect(user='root',
                                   host='localhost',
                                   password='12345',
                                   database='otp_auth')

    window.title("OTP EMBEDDED ATM")
    otp_auth_atm(window, mydb)
    window.mainloop()
