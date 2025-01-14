from tkinter import Tk, Label, RIDGE, X,Y, TOP, Frame, LabelFrame, W, ttk, Entry 
from tkinter import Text, Listbox, Scrollbar, END, Button,  HORIZONTAL, VERTICAL, BOTTOM, RIGHT, BOTH
from tkinter import StringVar, messagebox
import mysql.connector
import datetime

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1350x700+0+0")
        
        #================================================Variable=====================
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook=StringVar()
        self.lateratefine_var=StringVar()
        self.dateoverdue=StringVar()
        self.finallprice=StringVar()
        

        lbltitle = Label(self.root, text="Library Management System", bg="powder blue", fg="green", bd=20, relief=RIDGE, font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1530, height=400)

        #=====================================================Data Frame Left======================================================
        DataFrameLeft = LabelFrame(frame, text="Library Membership Information", bg="powder blue", fg="green", bd=20, relief=RIDGE, font=("times new roman", 12, "bold"), padx=2, pady=6)
        DataFrameLeft.place(x=0, y=5, width=900, height=370)
        
        lblMember = Label(DataFrameLeft, bg="powder blue", text="Member Type", font=("times new roman", 15,"bold"),padx=2, pady=6)
        lblMember.grid(row=0, column=0, sticky=W)
        
        comMember = ttk.Combobox(DataFrameLeft, font=("arial", 12, "bold"), width=27, state="readonly", textvariable=self.member_var)
        comMember["value"] = ("Admin Staf", "Student", "Lecture")
        comMember.current(0)
        comMember.grid(row=0, column=1)

        lblPRN_No = Label(DataFrameLeft, bg="powder blue", text="PRN No", font=("arial", 12, "bold"), padx=2, pady=6)
        lblPRN_No.grid(row=1, column=0, sticky=W)
        txtPRN_NO = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=29, textvariable=self.prn_var)
        txtPRN_NO.grid(row=1, column=1)

        lblID_No = Label(DataFrameLeft, bg="powder blue", text="ID No", font=("arial", 12, "bold"), padx=2, pady=6)
        lblID_No.grid(row=2, column=0, sticky=W)
        txtID_NO = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=29, textvariable=self.id_var)
        txtID_NO.grid(row=2, column=1)

        lblFirstName = Label(DataFrameLeft, bg="powder blue", text="First Name", font=("arial", 12, "bold"), padx=2, pady=6)
        lblFirstName.grid(row=3, column=0, sticky=W)
        txtFirstName = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=29, textvariable=self.firstname_var)
        txtFirstName.grid(row=3, column=1)

        lblLastName = Label(DataFrameLeft, bg="powder blue", text="Last Name", font=("arial", 12, "bold"), padx=2, pady=6)
        lblLastName.grid(row=4, column=0, sticky=W)
        txtLastName = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=29, textvariable=self.lastname_var)
        txtLastName.grid(row=4, column=1)

        lblAddress1 = Label(DataFrameLeft, bg="powder blue", text="Address 1", font=("arial", 12, "bold"), padx=2, pady=6)
        lblAddress1.grid(row=5, column=0, sticky=W)
        txtAddress1 = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=29, textvariable=self.address1_var)
        txtAddress1.grid(row=5, column=1)

        lblAddress2 = Label(DataFrameLeft, bg="powder blue", text="Address 2", font=("arial", 12, "bold"), padx=2, pady=6)
        lblAddress2.grid(row=6, column=0, sticky=W)
        txtAddress2 = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=29, textvariable=self.address2_var)
        txtAddress2.grid(row=6, column=1)

        lblPostCode = Label(DataFrameLeft, bg="powder blue", text="Post Code", font=("arial", 12, "bold"), padx=2, pady=6)
        lblPostCode.grid(row=7, column=0, sticky=W)
        txtPostCode = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=29, textvariable=self.postcode_var)
        txtPostCode.grid(row=7, column=1)

        lblMobile = Label(DataFrameLeft, bg="powder blue", text="Mobile", font=("arial", 12, "bold"), padx=2, pady=6)
        lblMobile.grid(row=8, column=0, sticky=W)
        txtMobile = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=29, textvariable=self.mobile_var)
        txtMobile.grid(row=8, column=1)

        lblBookId = Label(DataFrameLeft, bg="powder blue", text="Book Id", font=("arial", 12, "bold"), padx=2, pady=6)
        lblBookId.grid(row=0, column=2, sticky=W)
        txtBookid = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=29, textvariable=self.bookid_var)
        txtBookid.grid(row=0, column=3)

        lblBookTitle = Label(DataFrameLeft, bg="powder blue", text="Book Title", font=("arial", 12, "bold"), padx=2, pady=6)
        lblBookTitle.grid(row=1, column=2, sticky=W)
        txtBookTitle = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=29, textvariable=self.booktitle_var)
        txtBookTitle.grid(row=1, column=3)

        lblauthorName = Label(DataFrameLeft, bg="powder blue", text="author Name", font=("arial", 12, "bold"), padx=2, pady=6)
        lblauthorName.grid(row=2, column=2, sticky=W)
        txtauthorName = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=29, textvariable=self.author_var)
        txtauthorName.grid(row=2, column=3)

        lblDateBorrowed = Label(DataFrameLeft, bg="powder blue", text="Date Borrowed", font=("arial", 12, "bold"), padx=2, pady=6)
        lblDateBorrowed.grid(row=3, column=2, sticky=W)
        txtDateBorrowed = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=29, textvariable=self.dateborrowed_var)
        txtDateBorrowed.grid(row=3, column=3)

        lblDateDue = Label(DataFrameLeft, bg="powder blue", text="Date Due", font=("arial", 12, "bold"), padx=2, pady=6)
        lblDateDue.grid(row=4, column=2, sticky=W)
        txtDateDue = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=29, textvariable=self.datedue_var)
        txtDateDue.grid(row=4, column=3)

        lblDaysOnBook = Label(DataFrameLeft, bg="powder blue", text="Days on Book", font=("arial", 12, "bold"), padx=2, pady=6)
        lblDaysOnBook.grid(row=5, column=2, sticky=W)
        txtDaysOnBook = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=29, textvariable=self.daysonbook)
        txtDaysOnBook.grid(row=5, column=3)

        lblLateReturnFine = Label(DataFrameLeft, bg="powder blue", text="Late Return Fine", font=("arial", 12, "bold"), padx=2, pady=6)
        lblLateReturnFine.grid(row=6, column=2, sticky=W)
        txtLateReturnFine = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=29, textvariable=self.lateratefine_var)
        txtLateReturnFine.grid(row=6, column=3)

        lblDateOverDue = Label(DataFrameLeft, bg="powder blue", text="Date Over Due", font=("arial", 12, "bold"), padx=2, pady=6)
        lblDateOverDue.grid(row=7, column=2, sticky=W)
        txtDateOverDue = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=29, textvariable=self.dateoverdue)
        txtDateOverDue.grid(row=7, column=3)

        lblActualPrice = Label(DataFrameLeft, bg="powder blue", text="Actual Price", font=("arial", 12, "bold"), padx=2, pady=6)
        lblActualPrice.grid(row=8, column=2, sticky=W)
        txtActualPrice = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=29, textvariable=self.finallprice)
        txtActualPrice.grid(row=8, column=3)


        #=====================================================Data Frame Right======================================================
        DataFrameRight = LabelFrame(frame, text="Book Detail", bg="powder blue", fg="green", bd=20, relief=RIDGE, font=("times new roman", 12, "bold"), padx=2, pady=6)
        DataFrameRight.place(x=910, y=5, width=540, height=370)

        self.txtbox=Text(DataFrameRight, font=("times new roman", 12, "bold"), width=32, height=16, padx=2, pady=6)
        self.txtbox.grid(row=0, column=2)
        
        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0, column=1, sticky="ns")
        
        listBooks=['Andrea Hirata-Ayah', 'Andrea Hirata-Sang Pemimpi', 'Andrea Hirata-Edensor', 'Andrea Hirata-Guru Aini', 'Tere Liye-Bumi', 'Tere Liye-Bulan', 'Tere Liye-Matahari', 
        'Tere Liye-Malam', 'Tere Liye-Bintang', 'Tere Liye-Lumpu', 'Tere Liye-Nebula', 'Tere Liye-SagaraS', 'Tere Liye-ILY', 'Tere Liye-Tentang Kamu', 'Tere Liye-Negeri para Bedebah', 
        'Tere Liye-Negeri diujung Tanduk', 'Tere Liye-Bedebah diujung Tanduk', 'Robert Kiyosaki-Rich Dad Poor Dad']

        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if(x=="Andrea Hsirata-Ayah"):
                self.bookid_var.set("BKID4545")
                self.booktitle_var.set("Ayah")
                self.author_var.set("Andrea Hirata")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("Rp 50.000")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rp 100.000")

            elif(x=="Andrea Hirata-Sang Pemimpi"):
                self.bookid_var.set("BKID4546")
                self.booktitle_var.set("Sang Pemimpi")
                self.author_var.set("Andrea Hirata")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("Rp 30.000")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rp 60.000")

            elif(x=="Andrea Hirata-Edensor"):
                self.bookid_var.set("BKID4547")
                self.booktitle_var.set("Edensor")
                self.author_var.set("Andrea Hirata")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("Rp 35.000")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rp 80.000")

            elif(x=="Andrea Hirata-Guru Aini"):
                self.bookid_var.set("BKID4548")
                self.booktitle_var.set("Guru Aini")
                self.author_var.set("Andrea Hirata")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("Rp 35.000")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rp 90.000")

            elif(x=="Tere Liye-Bumi"):
                self.bookid_var.set("BKID4001")
                self.booktitle_var.set("Bumi")
                self.author_var.set("Tere Liye")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("Rp 20.000")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rp 75.000")

            elif(x=="Tere Liye-Bulan"):
                self.bookid_var.set("BKID4002")
                self.booktitle_var.set("Bulan")
                self.author_var.set("Tere Liye")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("Rp 20.000")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rp 70.000")

            elif(x=="Tere Liye-Matahari"):
                self.bookid_var.set("BKID4003")
                self.booktitle_var.set("Matahari")
                self.author_var.set("Tere Liye")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("Rp 25.000")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rp 75.000")

            elif(x=="Tere Liye-Bintang"):
                self.bookid_var.set("BKID4004")
                self.booktitle_var.set("Bintang")
                self.author_var.set("Tere Liye")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("Rp 15.000")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rp 60.000")

            elif(x=="Tere Liye-Lumpu"):
                self.bookid_var.set("BKID4005")
                self.booktitle_var.set("Lumpu")
                self.author_var.set("Tere Liye")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("Rp 20.000")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rp 80.000")

            elif(x=="Tere Liye-Nebula"):
                self.bookid_var.set("BKID4006")
                self.booktitle_var.set("Nebula")
                self.author_var.set("Tere Liye")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("Rp 10.000")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rp 50.000")

            elif(x=="Tere Liye-SagaraS"):
                self.bookid_var.set("BKID4007")
                self.booktitle_var.set("SagaraS")
                self.author_var.set("Tere Liye")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("Rp 10.000")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rp 55.000")

            elif(x=="Tere Liye-ILY"):
                self.bookid_var.set("BKID4008")
                self.booktitle_var.set("ILY")
                self.author_var.set("Tere Liye")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("Rp 10.000")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rp 45.000")

            elif(x=="Tere Liye-Tentang Kamu"):
                self.bookid_var.set("BKID4009")
                self.booktitle_var.set("Tentang Kamu")
                self.author_var.set("Tere Liye")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("Rp 15.000")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rp 60.000")

            elif(x=="Tere Liye-Negeri para Bedebah"):
                self.bookid_var.set("BKID4010")
                self.booktitle_var.set("Negeri para Bedebah")
                self.author_var.set("Tere Liye")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("Rp 15.000")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rp 65.000")

            elif(x=="Tere Liye-Negeri diujung Tanduk"):
                self.bookid_var.set("BKID4011")
                self.booktitle_var.set("Negeri diujung Tanduk")
                self.author_var.set("Tere Liye")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("Rp 15.000")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rp 70.000")

            elif(x=="Tere Liye-Bedebah diujung Tanduk"):
                self.bookid_var.set("BKID4012")
                self.booktitle_var.set("Bedebah diujung Tanduk")
                self.author_var.set("Tere Liye")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("Rp 25.000")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rp 70.000")

            elif(x=="Robert Kiyosaki-Rich Dad Poor Dad"):
                self.bookid_var.set("BKID4013")
                self.booktitle_var.set("Rich Dad Poor Dad")
                self.author_var.set("Robert Kiyosaki")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("Rp 40.000")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rp 100.000")

        listBox=Listbox(DataFrameRight, font=("times new roman", 12, "bold"), width=20, height=16)
        listBox.bind("<<ListboxSelect>>", SelectBook)
        listBox.grid(row=0, column=0, padx=4)
        listScrollbar.config(command=listBox.yview)
        
        for item in listBooks:
            listBox.insert(END, item)

        #=====================================================Button Frame======================================================
        FrameButton = Frame (self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        FrameButton.place(x=0, y=530, width=1530, height=70)
        
        btnAddData=Button(FrameButton,command=self.add_data, text="Add Data", font=("times new roman", 12, "bold"), width=23, bg="tan4", fg="white")
        btnAddData.grid(row=0, column=0)
        btnAddData=Button(FrameButton, command=self.show_data, text="Show Data", font=("times new roman", 12, "bold"), width=23, bg="tan4", fg="white")
        btnAddData.grid(row=0, column=1)
        btnAddData=Button(FrameButton,command=self.update, text="Update", font=("times new roman", 12, "bold"), width=23, bg="tan4", fg="white")
        btnAddData.grid(row=0, column=2)
        btnAddData=Button(FrameButton,command=self.delete, text="Delete", font=("times new roman", 12, "bold"), width=23, bg="tan4", fg="white")
        btnAddData.grid(row=0, column=3)
        btnAddData=Button(FrameButton,command=self.reset, text="Reset", font=("times new roman", 12, "bold"), width=23, bg="tan4", fg="white")
        btnAddData.grid(row=0, column=4)
        btnAddData=Button(FrameButton,command=self.iExit, text="Exit", font=("times new roman", 12, "bold"), width=23, bg="tan4", fg="white")
        btnAddData.grid(row=0, column=5)

        #=====================================================Information Frame======================================================
        FrameDetails = Frame (self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        FrameDetails.place(x=0, y=600, width=1530, height=195)
        
        Table_frame=Frame(FrameDetails, bd=6, relief=RIDGE, bg="antique white")
        Table_frame.place(x=0, y=2, width=1460, height=165)
        
        xscroll=ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame, orient=VERTICAL)        
        
        self.library_table=ttk.Treeview(Table_frame, column=("memberType", "prnNo", "id", "firstName", "lastName", 
                                                            "address1", "address2", "postID", "mobilePhone", "bookID", "bookTitle", 
                                                            "author", "borrowedDate", "days", "dueDate", "lateReturnFund", "overdueDate", 
                                                            "finallprice"), xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
                
        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)
        
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
        
        
        self.library_table.heading("memberType", text= "Member Type")
        self.library_table.heading("prnNo", text= "PRN No")
        self.library_table.heading("id", text= "ID")
        self.library_table.heading("firstName", text= "First Name")
        self.library_table.heading("lastName", text= "Last Name")
        self.library_table.heading("address1", text= "Address 1")
        self.library_table.heading("address2", text= "Address 2")
        self.library_table.heading("postID", text= "Post ID")
        self.library_table.heading("mobilePhone", text= "Mobile Phone")
        self.library_table.heading("bookID", text= "Book ID")
        self.library_table.heading("bookTitle", text= "Book Title")
        self.library_table.heading("author", text= "author")
        self.library_table.heading("borrowedDate", text= "Borrowed Date")
        self.library_table.heading("days", text= "Days Passed")
        self.library_table.heading("dueDate", text= "Due Date")
        self.library_table.heading("lateReturnFund", text= "Lateness Fund")
        self.library_table.heading("overdueDate", text= "Overdue Date")
        self.library_table.heading("finallprice", text= "Final Price")
        
        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH, expand=1)
        
        self.library_table.column("memberType", width=100)
        self.library_table.column("prnNo", width=100)
        self.library_table.column("id", width=100)
        self.library_table.column("firstName", width=100)
        self.library_table.column("lastName", width=100)
        self.library_table.column("address1", width=100)
        self.library_table.column("address2", width=100)
        self.library_table.column("postID", width=100)
        self.library_table.column("mobilePhone", width=100)
        self.library_table.column("bookID", width=100)
        self.library_table.column("bookTitle", width=100)
        self.library_table.column("author", width=100)
        self.library_table.column("borrowedDate", width=100)
        self.library_table.column("days", width=100)
        self.library_table.column("dueDate", width=100)
        self.library_table.column("lateReturnFund", width=100)
        self.library_table.column("overdueDate", width=100)
        self.library_table.column("finallprice", width=100)
    
        self.fatch_data()
        self.library_table.bind('<ButtonRelease-1>', self.get_cursor)
        
    
    def add_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="", database="library_uas_pbo")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library (memberType, prnNo, id ,firstName, lastName, address1, address2, postID, mobilePhone, bookID, bookTitle, author, borrowedDate, days, dueDate, lateReturnFund, overdueDate, finalPrice) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s)",(
            self.member_var.get(),
            self.prn_var.get(),
            self.id_var.get(),
            self.firstname_var.get(),
            self.lastname_var.get(),
            self.address1_var.get(),
            self.address2_var.get(),
            self.postcode_var.get(),
            self.mobile_var.get(),
            self.bookid_var.get(),
            self.booktitle_var.get(),
            self.author_var.get(),
            self.dateborrowed_var.get(),
            self.datedue_var.get(),
            self.daysonbook.get(),
            self.lateratefine_var.get(),
            self.dateoverdue.get(),
            self.finallprice.get()        
        ))
        conn.commit()
        self.fatch_data()
        conn.close()
        messagebox.showinfo("Success", "Member has been inserted successfully")
    
    def update(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="", database="library_uas_pbo")
        my_cursor = conn.cursor()
        my_cursor.execute("update library set memberType=%s, prnNo=%s, id=%s ,firstName=%s, lastName=%s, address1=%s, address2=%s, postID=%s, mobilePhone=%s, bookID=%s, bookTitle=%s, author=%s, borrowedDate=%s, days=%s, dueDate=%s, lateReturnFund=%s, overdueDate=%s, finalPrice=%s", (
                                                                                                                                                                                                              self.member_var.get(),
                                                                                                                                                                                                              self.prn_var.get(),
                                                                                                                                                                                                              self.id_var.get(),
                                                                                                                                                                                                              self.firstname_var.get(),
                                                                                                                                                                                                              self.lastname_var.get(),
                                                                                                                                                                                                              self.address1_var.get(),
                                                                                                                                                                                                              self.address2_var.get(),
                                                                                                                                                                                                              self.postcode_var.get(),
                                                                                                                                                                                                              self.mobile_var.get(),
                                                                                                                                                                                                              self.bookid_var.get(),
                                                                                                                                                                                                              self.booktitle_var.get(),
                                                                                                                                                                                                              self.author_var.get(),
                                                                                                                                                                                                              self.dateborrowed_var.get(),
                                                                                                                                                                                                              self.datedue_var.get(),
                                                                                                                                                                                                              self.daysonbook.get(),
                                                                                                                                                                                                              self.lateratefine_var.get(),
                                                                                                                                                                                                              self.dateoverdue.get(),
                                                                                                                                                                                                              self.finallprice.get()
                                                                                                                                                                                                          ))
        conn.commit()
        self.fatch_data()
        conn.close()
        messagebox.showinfo("Success", "Record has been updated successfully")      

    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="", database="library_uas_pbo")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()
        
        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("", END, values=i)
            conn.commit()
        conn.close()
        
    def get_cursor(self, event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content["values"]
        
        self.member_var.set(row[0]),
        self.prn_var.set(row[1]), 
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.author_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook.set(row[14]),
        self.lateratefine_var.set(row[15]),
        self.dateoverdue.set(row[16]),
        self.finallprice.set(row[17])            
    
    def show_data(self):
        self.txtbox.insert(END, "Member Type:\t" + self.member_var.get() + "\n")
        self.txtbox.insert(END, "PRN No:\t" + self.prn_var.get() + "\n")
        self.txtbox.insert(END, "ID No:\t" + self.id_var.get() + "\n")
        self.txtbox.insert(END, "First Name:\t" + self.firstname_var.get() + "\n")
        self.txtbox.insert(END, "Last Name:\t" + self.lastname_var.get() + "\n")
        self.txtbox.insert(END, "Address 1:\t" + self.address1_var.get() + "\n")
        self.txtbox.insert(END, "Address 2:\t" + self.address2_var.get() + "\n")
        self.txtbox.insert(END, "Post Code:\t" + self.postcode_var.get() + "\n")
        self.txtbox.insert(END, "Mobile No:\t" + self.mobile_var.get() + "\n")
        self.txtbox.insert(END, "Book ID:\t" + self.bookid_var.get() + "\n")
        self.txtbox.insert(END, "Book Title:\t" + self.booktitle_var.get() + "\n")
        self.txtbox.insert(END, "Author:\t" + self.author_var.get() + "\n")
        self.txtbox.insert(END, "Date Borrowed:\t" + self.dateborrowed_var.get() + "\n")
        self.txtbox.insert(END, "Date Due:\t" + self.datedue_var.get() + "\n")
        self.txtbox.insert(END, "Days on Book:\t" + self.daysonbook.get() + "\n")
        self.txtbox.insert(END, "Late Return Fine:\t" + self.lateratefine_var.get() + "\n")
        self.txtbox.insert(END, "Date Over Due:\t" + self.dateoverdue.get() + "\n")
        self.txtbox.insert(END, "Final Price:\t" + self.finallprice.get() + "\n")
        
    def reset(self):
        self.member_var.set("")
        self.prn_var.set("")
        self.id_var.set("")
        self.firstname_var.set("")
        self.lastname_var.set("")
        self.address1_var.set("")
        self.address2_var.set("")
        self.postcode_var.set("")
        self.mobile_var.set("")
        self.bookid_var.set("")
        self.booktitle_var.set("")
        self.author_var.set("")
        self.dateborrowed_var.set("")
        self.datedue_var.set("")
        self.daysonbook.set("")
        self.lateratefine_var.set("")
        self.dateoverdue.set("")
        self.finallprice.set("")
        self.txtbox.delete("1.0", END)
    
    def iExit(self):
        iExit = messagebox.askyesno("Library Management System", "Confirm you want to exit")
        if iExit > 0:
            self.root.destroy()
            return
    
    def delete(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="", database="library_uas_pbo")
        my_cursor = conn.cursor()
        query = "delete from library where prnNo=%s"
        value = (self.prn_var.get(),)
        my_cursor.execute(query, value)
        conn.commit()
        conn.close()
        self.fatch_data()
        self.reset()
        messagebox.showinfo("Success", "Member has been deleted successfully")

    
if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()