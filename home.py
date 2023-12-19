from crudOperations import MyHospitalDB


class Home:

    def administration(self):
        crudObj = MyHospitalDB()
        while (True):
            print("""
                        1. Display the details
                        2. Add a new member
                        3. Delete a member
                        4. Update member details
                        5. Make an exit
                                                 """)

            a = int(input("Enter your choice please!! : "))
            # Display details
            if a == 1:
                print("""
                                1. Doctors Details
                                2. Nurse Details
                                3. Others
                                                 """)
                b = int(input("Enter your choice please!! : "))

                # doctor details
                if b == 1:
                    crudObj.showDetails(
                        doc="doctorDet")  # doc= workas key bcz in function one arg will go at a time for all cases either in nurseor doc. So based on the key will bound value with the function paramter.
                    print("Showed DOC DETAILS now exist \U0001f60A")
                    # exit(1) # later we remove  this and make continue


                # Nurse details
                elif b == 2:
                    crudObj.showDetails(nurse="nurseDet")
                    print("Showed Nurse DETAILS \U0001f60A")

                elif b == 4:
                    exit(1)

            #  Add a new member
            if a == 2:
                print("""
                                 1. Add Doctors
                                 2. Add Nurse
                                 3. Add Others
                                                  """)

                b = int(input("Enter your choice please!! : "))

                if b == 1:
                    # enter doctor details
                    # will ASK THE DETAILS new addDetails() function otherwise i would ask here then i have to send all th cred from here.
                    crudObj.addDetails(doc="doctor")  # by this string in this function will identify to ask for doc or nurse

                elif b == 2:
                    # enter nurse details
                    # will ASK THE DETAILS
                    crudObj.addDetails(nurse="nurse")


            # Delete a member
            elif a == 3:
                print("""
                                 1. Delete Doctors 
                                 2. Delete Nurse 
                                 3. Delete Others
                                                  """)
                b = int(input("Enter your choice please!! : "))
                if b == 1:
                    crudObj.deleteDetails(doc="doctors")

                elif b == 2:
                    crudObj.deleteDetails(nurse="nurse")

            # update member details
            elif a == 4:
                print("""
                                1. Update Doctors 
                                2. Update Nurse 
                                3. Update Others
                                                 """)
                b = int(input("Enter your choice please!! : "))
                if b == 1:  # for doctors
                    crudObj.updateDetails(doc="doctors")

                elif b == 2:  # for nurses
                    crudObj.updateDetails(nurse="nurse")
            # Make an exit
            if a == 5:
                break

    def patient(self):
        crudObj = MyHospitalDB()
        print("""
                    1. Show Patients Info
                    2. Add New Patient
                    3. Discharge Summary
                    4. Exit
                                           """)
        b = int (input ("Please enter your choice: "))
    #     show patient info
        if b == 1 :
            crudObj.showDetails(patient="patient")
        #     add patient
        elif b == 2 :
            crudObj.addDetails(patient="patient")
        # discharge/ delete patient info
        elif b == 3 :
            crudObj.deleteDetails(patient="patient")


    def userMenu(self):
        crudObj = MyHospitalDB()  # so that we don't have to make this object in each condition for calling its functions.
        print('''
                 ================================
                    Welcome To NHKHAN Hospital
                 ================================
         ''')

        print(''' Start :

                        1- Sign In
                        2- Registration     
             ''')
        choice = int(input("Enter your choice please!! : "))

        if (choice == 1):  # for Sign In
            print("Wao, you selected Sign In !")
            print("""
                         ==================================
                         !!!!!!!!  {{Sign In}}  !!!!!!!!!!
                         ==================================
                """)
            username = input("Plase enter your username : ")
            password = input("Plase enter your password : ")
            verified = crudObj.userLogin(username, password)
            if verified :
                print("You are successfully Logged in!!!")
                while (True):
                    print("""
                                                   1.Administration
                                                   2.Patient
                                                   3.Sign Out

                                                                               """)

                    a = int(input("ENTER YOUR CHOICE: "))

                    if a == 1: # for Doctors and Nurses
                        self.administration()

                    elif a == 2: # for patient
                        self.patient()

                    elif a == 3:
                        print("Thank you for your time!! :\U0001f643")
                        break
                    else:
                        print("Please enter the provided options!! ")

            else:  # if username or password is wrong
                print(" Please try again !!")
                # exit(0)

        elif (choice == 2):  # for Registration
            print("Wao, you selected Registration !")
            print('''
                ================================
           !!!!!!!!!!!! Register Yourself Please !!!!!!!!!!!!
                ================================
             ''')
            username = input("Input your username please !!: ")
            password = input("Input the password (Password must be strong!!! : ")
            crudObj.showEnteredData(username, password)
            crudObj.userData(username, password)


        else:
            print("Please enter 1 or 2 option ")


obj = Home()
obj.userMenu()
