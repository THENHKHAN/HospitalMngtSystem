from setupDB import getCursor
import psycopg2
from prettytable import PrettyTable
class MyHospitalDB:

    def doctorDetails(self,docTableName):
        try :
                cursor , conn = getCursor()
                select_query = f"SELECT * FROM {docTableName}"
                cursor.execute(select_query)
                allDoc = cursor.fetchall()
                print("Total rows are:  ", len(allDoc))
                print("Here are doctor details: ")
                # print("Printing each row")
                # for row in allDoc:
                #     print("Id: ", row[0])
                #     print("Name: ", row[1])
                #     print("specialisation: ", row[2])
                #     print("age: ", row[3])
                #     print("address: ", row[4])
                #     print("contact: ", row[5])
                #     print("fee: ", row[6])
                #     print("monthly_salary: ", row[7])
                #     print("\n")
                table = PrettyTable() # this will print like a table
                table.field_names = ["Id", "Name", "Specialization", "Age", "Address", "Contact", "Fee",
                                     "Monthly_Salary"]

                # Populate the table with rows
                for row in allDoc:
                    table.add_row(row) # working as well
                    # table.add_row([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]]) # # working as well

                # Print the formatted table
                print(table)

                print("Total rows are: ", len(allDoc))
                cursor.close()

        except psycopg2.Error as error:
            print("Failed to read data from table", error)
        finally:
            if conn:
                conn.close()
                print("The Postgresql connection is closed")
    def showEnteredData(self, username, password):
        print(f"userName : {username}")
        print(f"password : {password}")

    def userLogin (self, userName, password):
        [cursor, conn] = getCursor()
        verifyUserNamePass = f"SELECT name FROM user_details WHERE name = '{userName}' " # and  password = '{password}' dont need pw
        cursor.execute(verifyUserNamePass)
        existingUserNamePass = cursor.fetchone()
        if existingUserNamePass :
            print("User verified!!!")
        else:
            print("Username or password is WRONG!! ")
        return True
    def userData(self, username, password):
        [cursor, conn] = getCursor()
        checkUsername = f"SELECT name FROM user_details WHERE name = '{username}' "  # this will get all name
        cursor.execute(checkUsername)
        existingUser = cursor.fetchone()  # it will get one

        if (existingUser):  # it will return true if username of same already exist in the user_details table
            print("User already Exist")
            # Additional logic for handling existing user

        else:  # '{username}' single quote is must while using any variable in ''' quote
            query = f'''
                        INSERT INTO user_details (name , password)
                        VALUES ('{username}' , '{password}') 
           '''
            cursor.execute(query)
            conn.commit()
            cursor.close()
            conn.close()
            print("""
                    ============================================
                    !!Well Done!!Registration Done Successfully!!
                    ============================================
               """)

    def showDetails(self,doc = "doctorDet" , nurse = "nurseDet", patient = "patientDet"):
        if doc == "doctorDet" :
            docTableName =  "doctor_details"
            self.doctorDetails(docTableName)
        if nurse == "nurseDet" :
            nurseTableName = "nurse_details"
            # self.nurseDetails(nurseTableName)