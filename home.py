from crudOperations import MyHospitalDB


class Home:

    def administration(self) :
       print("""
                1. Display the details
                2. Add a new member
                3. Delete a member
                4. Make an exit
                                         """)

       a =  int(input("Enter your choice please!! : "))
       crudObj = MyHospitalDB()

       # Display details
       if a == 1:
            print("""
                    1. Doctors Details
                    2. Nurse Details
                    3. Others
                                     """)
            b = int(input("Enter your choice please!! : "))

            # doctor details
            if b == 1 :
                crudObj.showDetails("doctorDet")
                print("Showed DOC DETAILS now exist \U0001f60A")
                exit(1) # later we remove  this and make continue


            # Nurse details
            elif b == 2 :
                crudObj.showDetails("nurseDet")
                print("Showed Nurse DETAILS now exist \U0001f60A")
                exit(1)

        #  Add a new member
       if a == 2:
            print("""
                     1. Add Doctors
                     2. Add Nurse
                     3. Add Others
                                      """)

            b = int(input("Enter your choice please!! : "))

            if b == 1 :
                    # enter doctor details
                    # will ASK THE DETAILS new addDetails() function otherwise i would ask here then i have to send all th cred from here.
                    crudObj.addDetails("doctor") # by this string in this function will identify to ask for doc or nurse

            elif b == 2 :
                    # enter nurse details
                    # will ASK THE DETAILS
                    crudObj.addDetails("nurse")


         # Delete a member
       elif a == 3:
            print("""
                     1. Delete Doctors 
                     2. Delete Nurse 
                     3. Delete Others
                                      """)
            b = int(input("Enter your choice please!! : "))
            if b == 1 :
                crudObj.deleteDetails("doctors")

            elif b == 2 :
                crudObj.deleteDetails("nurse")

        # Make an exit
       if a == 4:  # will implement later
           pass

    def userMenu(self):
        crudObj = MyHospitalDB() # so that we don't have to make this object in each condition for calling its functions.
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

                    a = int(input("ENTER YOUR CHOICE:"))

                    if a == 1:
                        self.administration()

                    if a == 2:
                        print("ttttttttttttttttttt")

                    if a == 3:
                        print("Thank you for your time!! :\U0001f643")
                        break

            else: # if username or password is wrong
                exit(0)

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
