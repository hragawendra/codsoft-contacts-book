from tkinter import *
from tkinter import messagebox, simpledialog

root = Tk()
root.geometry('800x700')
root.config(bg='#F5DEB3')
root.title('Contact Book')
root.resizable(0, 0)

contactlist = [
    ['Raghava', '8790029381', 'hrr5656@gmail.com', 'Mantralayam'],
    ['Inddiira', '9741365872', 'hindu@gmail.com', 'Yemmiganur'],
    ['Gangadhar', '7894561450', 'gangadhar@gmail.com', 'Madanapalli'],
    ['Rajasekhar', '8745246120', 'rajasekhar@gmail.com', 'Tadipatri'],
    ['Sai kumar', '8469755478', 'saikumar@gmail.com', 'Ananthapur'],
    ['Bharath', '6478926321', 'bharath@gmail.com', 'chittor'],
    ['Leela vardhan', '8968532054', 'leela@gmail.com', 'Kadiri'],
    ['Anand', '9856478506', 'anand@gmail.com', 'Nandyal']
]

Name = StringVar()
Number = StringVar()
Email = StringVar()
Address = StringVar()

frame = Frame(root)
frame.pack(side=RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, font=('Times new roman', 16), bg="#FFFFFF", width=20, height=27,
                 borderwidth=3, relief="groove")
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)


def Selected(index=None):
    if index is not None:
        return int(index)
    elif len(select.curselection()) == 0:
        messagebox.showerror("Error", "Please Select the Name")
    else:
        
        selected_index_in_listbox = int(select.curselection()[0])

       
        selected_name = select.get(selected_index_in_listbox)

        try:
            
            selected_contact_index = next(
                (i for i, contact in enumerate(contactlist) if contact[0] == selected_name),
                None
            )
            if selected_contact_index is not None:
                return selected_contact_index
            else:
                raise ValueError("Selected contact not found in the contactlist")
        except ValueError as e:
            messagebox.showerror("Error", str(e))



def AddContact():
    if Name.get() != "" and Number.get() != "" and Email.get() != "" and Address.get() != "":
        contactlist.append([Name.get(), Number.get(), Email.get(), Address.get()])
        Select_set()
        EntryReset()
        messagebox.showinfo("Confirmation", "Successfully Add New Contact")
    else:
        messagebox.showerror("Error", "Please fill in the information")


def UpdateDetail():
    if Name.get() and Number.get():
        contactlist[Selected()] = [Name.get(), Number.get(), Email.get(), Address.get()]
        messagebox.showinfo("Confirmation", "Successfully Update Contact")
        EntryReset()
        Select_set()
    elif not (Name.get()) and not (Number.get()) and not (Email.get()) and not (Address.get()) and not (
            len(select.curselection()) == 0):
        messagebox.showerror("Error", "Please fill in the information")
    else:
        if len(select.curselection()) == 0:
            messagebox.showerror("Error", "Please Select the Name and \n press Load button")
        else:
            message1 = """To Load all information of \n
                          selected row press Load button\n.
                          """
            messagebox.showerror("Error", message1)


def EntryReset():
    Name.set('')
    Number.set('')
    Email.set('')
    Address.set('')


def Delete_Entry():
    if len(select.curselection()) != 0:
        result = messagebox.askyesno('Confirmation', 'You Want to Delete Contact\n Which you selected')
        if result == True:
            del contactlist[Selected()]
            Select_set()
    else:
        messagebox.showerror("Error", 'Please select the Contact')


def VIEW():
    selected_index = Selected()
    if selected_index is not None:
        
        NAME, PHONE, EMAIL, ADDRESS = contactlist[selected_index]
        Name.set(NAME)
        Number.set(PHONE)
        Email.set(EMAIL)
        Address.set(ADDRESS)


def EXIT():
    root.destroy()


def Select_set():
    contactlist.sort()
    select.delete(0, END)
    for name, phone, email, address in contactlist:
        select.insert(END, name)
Select_set()


def SearchContact():
    search_query = simpledialog.askstring("Search", "Enter name or number to search:")
    if search_query:
        search_results = [
            contact for contact in contactlist
            if (search_query.lower() in contact[0].lower()) or (search_query in contact[1])
        ]
        if search_results:
            select.delete(0, END)
            for name, _, _, _ in search_results:
                select.insert(END, name)
        else:
            messagebox.showinfo("Search Results", f"No contacts found for '{search_query}'")
    else:
        Select_set()


Label(root, text='Name :', font=("Times new roman", 25, "bold"), bg='#F5DEB3').place(x=30, y=20)
Entry(root, textvariable=Name, width=30, font=('Arial', 12), bg='#FFFFFF').place(x=200, y=30)
Label(root, text='Contact No :', font=("Times new roman", 22, "bold"), bg='#F5DEB3').place(x=30, y=70)
Entry(root, textvariable=Number, width=30, font=('Arial', 12), bg='#FFFFFF').place(x=200, y=80)
Label(root, text='Email :', font=("Times new roman", 25, "bold"), bg='#F5DEB3').place(x=30, y=110)
Entry(root, textvariable=Email, width=30, font=('Arial', 12), bg='#FFFFFF').place(x=200, y=130)
Label(root, text='Address :', font=("Times new roman", 25, "bold"), bg='#F5DEB3').place(x=30, y=160)
Entry(root, textvariable=Address, width=30, font=('Arial', 12), bg='#FFFFFF').place(x=200, y=180)

Button(root, text="VIEW", font=("Times new roman", 18, "bold"), bg='#87CEFA', command=VIEW).place(x=100, y=250)
Button(root, text="EDIT", font=("Times new roman", 18, "bold"), bg='#87CEFA', command=UpdateDetail, padx=20).place(x=250, y=250)
Button(root, text="ADD", font=("Times new roman", 18, "bold"), bg='#87CEFA', command=AddContact, padx=20).place(x=100, y=320)
Button(root, text="DELETE", font=("Times new roman", 18, "bold"), bg='#87CEFA', command=Delete_Entry, padx=20).place(x=250, y=320)
Button(root, text="RESET", font=("Times new roman", 18, "bold"), bg='#87CEFA', command=EntryReset).place(x=100, y=390)
Button(root, text="SEARCH", font=("Times new roman", 18, "bold"), bg='#87CEFA', command=SearchContact, padx=20).place(x=250, y=390)
Button(root, text="Back to Contacts", font=("Times new roman", 18, "bold"), bg='#87CEFA', command=Select_set).place(x=130, y=470)
Button(root, text="EXIT", font=("Times new roman", 25, "bold"), bg='#FF0000', command=EXIT).place(x=180, y=550)

root.mainloop()
