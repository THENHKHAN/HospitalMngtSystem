from crudOperations import MyHospitalDB


class Home:

    def userMenu(self):

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
            crudObj = MyHospitalDB()
            crudObj.userLogin(username, password)


        elif (choice == 2):  # for Registration
            print("Wao, you selected Registration !")
            print('''
                ================================
           !!!!!!!!!!!! Register Yourself Please !!!!!!!!!!!!
                ================================
             ''')
            username = input("Input your username please !!: ")
            password = input("Input the password (Password must be strong!!! : ")

            crudObj = MyHospitalDB()
            crudObj.showEnteredData(username, password)
            crudObj.userData(username, password)


        else:
            print("Please enter 1 or 2 option ")


obj = Home()
obj.userMenu()
