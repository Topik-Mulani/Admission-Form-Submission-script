

database ={}
while True:
    print("Welcome  to cybersucess ")
    var = int(input("""Enter Input: 
    1. New Admission 
    2. Fee Submission
    3. Owners Access
    4. Exit:_  """))
    if var == 1:
        print("Welcome To New Admission")
        Name = input("Enter Your Name: ")
        F_Name = input("Enter Your Fathers Name: ")
        M_Name = input("Enter Your Mothers Name: ")
        Phone = input("Enter Your Number: ")
        Email = input("Enter Your Email: ")
        Address = input("Enter Your Address: ")
        Id_no = input("Enter Id Number: ")
        if Id_no not in database:
            database[Id_no]=[Name,F_Name,M_Name,Phone,Email,Address,0]     # **** IMP
        else:
            print("Id already exist")
    elif var == 2:
        print("Welcome To Fee Panel")
        Id_no= input("Enter Your Id_no: ")
        if Id_no in database:
            fee = int(input("Enter Fees(>1000 Rs): "))
            if fee >= 1000:
                database[Id_no][-1] = database[Id_no][-1] + fee
                print("Fee Submitted")
            else:
                print("Fees less than 1000 not accepted")
        else:
            print("Wrong Id")
    elif var == 3:
        print("Welcome to owners panel")
        code = input("Enter Code: ")
        if code == "qwert123":
            Id_no = input("Enter student Id_no: ")
            if Id_no in database:
                info =f"""Student Information:
                      Student Name: {database[Id_no][0]}
                      Father Name: {database[Id_no][1]}
                      Mother Name: {database[Id_no][2]}
                      Phone Num. : {database[Id_no][3]}
                      Email      : {database[Id_no][4]}
                      Address    : {database[Id_no][5]}
                      fees       : {database[Id_no][6]}"""
                print(info)
            else:
                print("Wrong ID")
        else:
            print("Incorrect code")
    elif var == 4:
        print("Thank You")
        break
    else:
        print("Invalid Input")
    print()
    print(database)
    print()


