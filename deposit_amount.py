from tkinter import *
import mysql.connector


def deposit(amount):
    # Change to the amount you want to deposit.
    amount = amount

    mydb = mysql.connector.connect(user='root',
                                   host='localhost',
                                   password='12345',
                                   database='otp_auth')

    cursor = mydb.cursor()


    data = []
    cursor.execute('select * from card_info')
    result = cursor.fetchall()
    for i in result:
        data.append(i)

    balance = int(data[0][4])
    new_balance = balance + amount
    cursor.execute(f'update card_info set balance={new_balance} where id = 1')
    mydb.commit()
    print('Balance Updated')
    mydb.close()

window = Tk()
# Label
label = Label(window, text="Amount :")

# Entry
entry_var = StringVar()
entry = Entry(window, textvariable=entry_var)
entry.pack()

# Button
button = Button(window, text='Deposit', command=lambda: deposit(int(entry_var.get())))
button.pack()

window.mainloop()
