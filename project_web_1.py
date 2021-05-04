# import library
from tkinter import *

# initialize window
blocker = Tk()
blocker.geometry('500x300')
blocker.resizable(0, 0)
blocker.title("TechVidvan - Website Blocker")

# heading
Label(blocker, text='WEBSITE BLOCKER', font='arial 20 bold').pack()
Label(blocker, text='TechVidvan', font='arial 20 bold').pack(side=BOTTOM)

# path of our host file ang ip address
host_path = 'C:\Windows\System32\drivers\etc\hosts'
ip_address = '127.0.0.1'

# ENTER WEBSITE
Label(blocker, text='Enter Website :', font='arial 13 bold').place(x=5, y=60)
Websites = Text(blocker, font='arial 10', height='2', width='40', wrap=WORD, padx=5, pady=5)
Websites.place(x=140, y=60)


# block function
def Blocker():
    website_lists = Websites.get(1.0, END)
    Website = list(website_lists.split(","))
    with open(host_path, 'r+') as host_file:
        file_content = host_file.read()
        for website in Website:
            if website in file_content:
                Label(root, text='Already Blocked', font='arial 12 bold').place(x=200, y=200)
                pass
            else:
                host_file.write(ip_address + " " + website + '\n')
                Label(root, text="Blocked", font='arial 12 bold').place(x=230, y=200)


block_btn = Button(blocker, text='BLOCK', font='arial 12 bold', command=Blocker, width=6, bg='royal blue1',
                   activebackground='sky blue')
block_btn.place(x=230, y=150)

blocker.mainloop()

