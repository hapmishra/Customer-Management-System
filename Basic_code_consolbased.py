namelist=[]
agelist=[]
idlist=[]
moblist=[]
index=0
while(1):
    try:
        print("Welcome to the Customer Management System")
        print("Please select your choice from given below : ")
        print("1.Add Customer","2.Update Customer","3.Remove Customer","4.Search Customer","5.Display All","6.Exit",sep="\n")
        x=int(input("Please Enter your Choice here : "))
    # ----------------------------(Add Customer)-----------------------------------------------------------------------
        if(x==1):
            index+=1
            print("Enter the Details of the Customer")
            a=input("Enter the Name of the Customer : ")
            namelist.append(a)
            while(1):
                b=input("Enter the Age of the Customer : ")
                if(b.isnumeric()):
                    agelist.append(b)
                    break
                else:
                    print("Please Enter Age only in Numeric Form")
            while(1):
                c=input("Please Enter your 10 Digit Mobile Number : ")
                if(c.isnumeric()):
                    moblist.append(c)
                    break
                else:
                    print("Please enter a valid mobile number")
            idlist.append(index)
        print(namelist,agelist,idlist,moblist,sep='\n')
    # ----------------------(update Customer)------------------------------------------------------------------------------
        if(x==2):
            while(1):
                id=input("Enter Customer ID :")
                if(id.isnumeric()):
                    id=int(id)
                    namelist.pop(id)
                    agelist.pop(id)
                    moblist.pop(id)
                    a = input("Enter the Name : ")
                    namelist.insert(id,a)
                    while(1):
                        b = input("Enter the Age of Customer")
                        if(b.isnumeric()):
                            b=int(b)
                            agelist.insert(id,b)
                            break
                        else:
                            print("Please enter valid age")
                    while(1):
                        c = input("Enter Mobile Number : ")
                        if(c.isnumeric()):
                            moblist.insert(id,c)
                            break
                        else:
                            print("Please enter valid mobile number")
                    break
    # ---------------------------------------------------------------------------------------------------------------------
    # -------------------------------------(Remove Customer)---------------------------------------------------------------
        elif(x==3):
            while (1):
                id = input("Enter Customer ID :")
                if (id.isnumeric()):
                    id = int(id)
                    id-=1
                    namelist.pop(id)
                    agelist.pop(id)
                    moblist.pop(id)
                    idlist.pop(id)
                    print("Customer Removed Sucessfully")
                    break
                else:
                    print("Please Enter Valid Customer ID")
    # ---------------------------------------------------------------------------------------------------------------------
    # -----------------------------------(Search Customer)-----------------------------------------------------------------
        elif (x==4):
            while (1):
                id = input("Enter Customer ID :")
                if (id.isnumeric()):
                    id=int(id)
                    index=idlist.index(id)
                    name=namelist[index]
                    age=agelist[index]
                    mob=moblist[index]
                    print("Name :",name,"Age : ",age,"Mobile No. : ",mob,sep="\n")
                    break
                else:
                    print("The Please enter a valid ID")
    # ---------------------------------------------------------------------------------------------------------------------
    # -----------------------------(Display All)---------------------------------------------------------------------------
        elif(x==5):
            for i in range(len(idlist)):
                print("Cus. Name :",namelist[i],"Cus. Age :",agelist(i),"Cus. ID :",idlist(i),"Cus. Mobile :",moblist(i))
        elif(x==6):
            print("Thankyou")
    except Exception as e:
        print("Error",e)
# ---------------------------------------------------------------------------------------------------------------------