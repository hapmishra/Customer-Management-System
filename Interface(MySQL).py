import tkinter
import json
import tkinter.messagebox
import pymysql
con=pymysql.connect(host="localhost",user="root",passwd="",database="test1")
mycursor=con.cursor()
#make sure to set your MySQL password in this code and also please make sure in this code i have used "tb1" as name of
#the table so please make sure you are using the code with same ame of your table or you can change it.

#----------------------------------------------------------------------------------------------------------------
class Customer:
    listofcustomer=[]
    def __init__(self):
        self.id=""
        self.name=""
        self.age=""
        self.mobile=""
    def add_customer(self):
        globals()
        qu = "insert into tb1 values(%s,%s,%s,%s)"
        mycursor.execute(qu, (self.id,self.name,self.age,self.mobile))
        con.commit()
        tkinter.messagebox.showinfo("Successfull","Customer Added")
    def Search_Customer(self):
        mycursor.execute("select * from tb1 where id=%s",(self.id))
        record=mycursor.fetchall()
        print(record)
        for row in record:
            print("Customer ID:",row[0],end="\t")
            print("Customer Name:", row[1], end="\t")
            print("Customer Age:", row[2], end="\t")
            print("Customer Mobile:", row[3], end="\t")
        root1=tkinter.Tk()
        root1.title("Customer Management System")
        root.minsize(400, 300)
        try:
            lblmobile = tkinter.Label(root1, text="%s" % (row[3])).grid(row=4, column=2)
            title_Label = tkinter.Label(root1, text="Customer Management System")
            title_Label.grid(row=0, column=2)
            lbl_ID_L=tkinter.Label(root1,text="Customer ID:")
            lbl_ID_L.grid(row=1,column=1)
            lbl_ID=tkinter.Label(root1,text="%s"%(row[0]))
            lbl_ID.grid(row=1,column=2)
            lbl_Name_l=tkinter.Label(root1,text="Customer Name:")
            lbl_Name_l.grid(row=2,column=1)
            lbl_Name=tkinter.Label(root1,text="%s"%(row[1]))
            lbl_Name.grid(row=2,column=2)
            lbl_age=tkinter.Label(root1,text="Customer Age:").grid(row=3,column=1)
            lblage=tkinter.Label(root1,text="%s"%(row[2])).grid(row=3,column=2)
            lbl_mobile=tkinter.Label(root1,text="Customer Mobile No.:").grid(row=4,column=1)
        except Exception:
            tkinter.messagebox.showerror("Not Found","Enter ID not Found")
    def remove_customer(self):
        qu = "delete from tb1 where id=%s"
        mycursor.execute(qu, (self.id))
        con.commit()
        tkinter.messagebox.showinfo("Success","Customer Removed Successfull")
    def update_customer(self):
        globals()
        mycursor.execute("update tb1 set age=%s where id=%s",(self.age, self.id))
        mycursor.execute("update tb1 set name=%s where id=%s", (self.name, self.id))
        mycursor.execute("update tb1 set mobile=%s where id=%s", (self.mobile, self.id))
        con.commit()
        print(self.id)

    @staticmethod
    def search_customer_page(a):
        forgo()
        global searchID
        searchID=tkinter.StringVar()
        LBL_Customer_ID = tkinter.Label(root, text="Enter Customer ID")
        LBL_Customer_ID.grid(row=2, column=1)
        En_Customer_ID = tkinter.Entry(root,textvariable=searchID)
        En_Customer_ID.grid(row=2, column=2)
        Search_Customer_button=tkinter.Button(root,text="Search Customer")
        Search_Customer_button.bind("<Button-1>",object_search)
        Search_Customer_button.grid(row=3,column=2)

    @staticmethod
    def remove_customer_page(a):
        forgo()
        global removeID
        removeID = tkinter.StringVar()
        LBL_Customer_ID = tkinter.Label(root, text="Enter Customer ID")
        LBL_Customer_ID.grid(row=2, column=1)
        En_Customer_ID = tkinter.Entry(root, textvariable=removeID)
        En_Customer_ID.grid(row=2, column=2)
        Search_Customer_button = tkinter.Button(root, text="Remove Customer")
        Search_Customer_button.bind("<Button-1>", object_remove)
        Search_Customer_button.grid(row=3, column=2)


    @staticmethod
    def add_customer_page(a):
        forgo()
        cus=Customer()
        global varID,varName,varAge,varMobile
        varID=tkinter.StringVar()
        varName = tkinter.StringVar()
        varAge = tkinter.StringVar()
        varMobile = tkinter.StringVar()
        LBL_Customer_ID = tkinter.Label(root, text="Enter Customer ID")
        LBL_Customer_ID.grid(row=2, column=1)
        En_Customer_ID = tkinter.Entry(root,textvariable=varID)
        En_Customer_ID.grid(row=2, column=2)

        LBL_Customer_Name = tkinter.Label(root, text="Enter Customer Name")
        LBL_Customer_Name.grid(row=3, column=1)
        En_Customer_Name = tkinter.Entry(root, text="", textvariable=varName)
        En_Customer_Name.grid(row=3, column=2)

        LBL_Customer_Age = tkinter.Label(root, text="Enter Customer Age")
        LBL_Customer_Age.grid(row=4, column=1)
        En_Customer_Age = tkinter.Entry(root, text="", textvariable=varAge)
        En_Customer_Age.grid(row=4, column=2)

        LBL_Customer_Mob = tkinter.Label(root, text="Enter Customer Mobile NO.")
        LBL_Customer_Mob.grid(row=5, column=1)
        En_Customer_Mob = tkinter.Entry(root, text="", textvariable=varMobile)
        En_Customer_Mob.grid(row=5, column=2)
        cus.id=varID.get()

        Button_AddCustomer = tkinter.Button(root, text="Add Customer",command=object)
        Button_AddCustomer.grid(row=6, column=2)
    @staticmethod
    def update_page_1(a):
        forgo()
        global updateID
        updateID = tkinter.StringVar()
        LBL_Customer_ID = tkinter.Label(root, text="Enter Customer ID")
        LBL_Customer_ID.grid(row=2, column=1)
        En_Customer_ID = tkinter.Entry(root, textvariable=updateID)
        En_Customer_ID.grid(row=2, column=2)
        Search_Customer_button = tkinter.Button(root, text="Update Customer")
        Search_Customer_button.bind("<Button-1>", object_update)
        Search_Customer_button.grid(row=3, column=2)
    @staticmethod
    def update_page_2():
        forgo()
        global ID,Name,Age,Mobile
        ID=tkinter.StringVar()
        Name = tkinter.StringVar()
        Age = tkinter.StringVar()
        Mobile = tkinter.StringVar()
        root2=tkinter.Tk()
        root2.minsize(400,300)

        LBL_Customer_ID = tkinter.Label(root2, text="Enter Customer ID")
        LBL_Customer_ID.grid(row=2, column=1)
        En_Customer_ID = tkinter.Entry(root2,textvariable=ID)
        En_Customer_ID.grid(row=2, column=2)

        LBL_Customer_Name = tkinter.Label(root2, text="Enter Customer Name")
        LBL_Customer_Name.grid(row=3, column=1)
        En_Customer_Name = tkinter.Entry(root2,textvariable=Name)
        En_Customer_Name.grid(row=3, column=2)

        LBL_Customer_Age = tkinter.Label(root2, text="Enter Customer Age")
        LBL_Customer_Age.grid(row=4, column=1)
        En_Customer_Age = tkinter.Entry(root2,textvariable=Age)
        En_Customer_Age.grid(row=4, column=2)

        LBL_Customer_Mob = tkinter.Label(root2, text="Enter Customer Mobile NO.")
        LBL_Customer_Mob.grid(row=5, column=1)
        En_Customer_Mob = tkinter.Entry(root2,textvariable=Mobile)
        En_Customer_Mob.grid(row=5, column=2)

        Button_updateCustomer = tkinter.Button(root2, text="Update Customer")
        Button_updateCustomer.bind("<Button-1>",object_update_2)
        Button_updateCustomer.grid(row=6, column=2)
#==================================================================================================================
def forgo():
    addcustomer_button.grid_forget()
    search_customer_button.grid_forget()
    remove_customer_button.grid_forget()
    update_customer_button.grid_forget()
def object():#creating object for adding customer
    globals()
    cus=Customer()
    cus.id=varID.get()
    cus.name=varName.get()
    cus.age=varAge.get()
    cus.mobile=varMobile.get()
    mycursor.execute("select count(*) from tb1 where id=%s",(cus.id))
    rc=mycursor.fetchall()
    for i in rc:
        print(i[0])
    a=i[0]
    if(a==0):
        cus.add_customer()
    elif(a>0):
        tkinter.messagebox.showerror("Abort","ID already exist")
def object_search(a):#creating object for searching customer
    globals()
    cus=Customer()
    cus.id=searchID.get()
    cus.Search_Customer()
def object_remove(a):#creating object for removing customer
    globals()
    cus=Customer()
    cus.id=removeID.get()
    mycursor.execute("select count(*) from tb1 where id=%s", (cus.id))
    rc = mycursor.fetchall()
    for i in rc:
        print(i[0])
    a = i[0]
    if (a == 0):
        tkinter.messagebox.showerror("Abort","ID Does not exist")
    elif (a > 0):
        cus.remove_customer()
def object_update(a):#creating object for update customer
    globals()
    cus=Customer()
    cus.id=updateID.get()
    mycursor.execute("select count(*) from tb1 where id=%s", (cus.id))
    rc = mycursor.fetchall()
    for i in rc:
        print(i[0])
    a = i[0]
    if (a == 0):
        tkinter.messagebox.showerror("Abort", "ID Does not exist")
    elif (a > 0):
       Customer.update_page_2()
def object_update_2(a):
    globals()
    cus=Customer()
    cus.id=ID.get()
    cus.name=Name.get()
    cus.age=Age.get()
    cus.mobile=Mobile.get()
    cus.update_customer()

#-------------------------------------------------------------------------------------------------------------------
root=tkinter.Tk()
root.title("Customer Management System")

root.minsize(400,300)
title_Label=tkinter.Label(root,text="Customer Management System")
title_Label.grid(row=0,column=2)
addcustomer_button=tkinter.Button(root,text="Add Customer",width=15)
addcustomer_button.bind("<Button-1>",Customer.add_customer_page)
addcustomer_button.grid(row=1,column=2)

search_customer_button=tkinter.Button(root,text="Search Customer",width=15)
search_customer_button.bind("<Button-1>",Customer.search_customer_page)
search_customer_button.grid(row=2,column=2)

remove_customer_button=tkinter.Button(root,text="Remove Customer",width=15)
remove_customer_button.bind("<Button-1>",Customer.remove_customer_page)
remove_customer_button.grid(row=3,column=2)

update_customer_button=tkinter.Button(root,text="Update Customer",width=15)
update_customer_button.bind("<Button-1>",Customer.update_page_1)
update_customer_button.grid(row=4,column=2)




root.mainloop()
