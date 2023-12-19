from setupDB import getCursor
import psycopg2
from prettytable import PrettyTable


class MyHospitalDB:

    def userData(self, username, password):
        [cursor, conn] = getCursor()
        checkUsername = f"SELECT name FROM user_details WHERE name = '{username}' "  # this will get all name. Here PW not required bcz there can with diff. username have same pw
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

    def userLogin(self, userName, password):
        [cursor, conn] = getCursor()
        verifyUserNamePass = f"SELECT name FROM user_details WHERE name = '{userName}' and  password = '{password}'"  # username and with this password in this table must match both.
        cursor.execute(verifyUserNamePass)
        existingUserNamePass = cursor.fetchone()
        flag = True
        if existingUserNamePass:
            print("User verified!!!")
            conn.close()
        else:
            print("Username or password is WRONG :\U0001f612, Please try again!! ")
            flag = False
            conn.close()
        return flag

    def doctorDetails(self, docTableName):
        try:
            cursor, conn = getCursor()
            select_query = f"SELECT * FROM {docTableName}"
            cursor.execute(
                select_query)  # but if you will write directly inside execute() then always use '{}' i.e. under single quote
            allDoc = cursor.fetchall()
            print("Here are doctor details: ")
            print("Total rows In the Table are:  ", len(allDoc))

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

            # Get column names from cursor description
            column_names = [col[0] for col in cursor.description]  # here we are getting cols name from DB
            table = PrettyTable()  # this will print like a table
            # Cols = ["Id", "Name", "Specialization", "Age", "Address", "Contact", "Fee",
            #                      "Monthly_Salary"] # here we are hard coding col name
            table.field_names = column_names
            # Populate the table with rows
            for row in allDoc:
                table.add_row(row)  # working as well
                # table.add_row([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]]) # # working as well

            # Print the formatted table
            print(table)

        except psycopg2.Error as error:
            print("Failed to read data from table", error)
        finally:
            if conn:
                conn.close()
                cursor.close()
                print("The Postgresql connection inside Show doctor details is closed")

    def nurseDetails(self, nurseTableName):
        try:
            cursor, conn = getCursor()
            selectQuery = f"SELECT * FROM {nurseTableName}"
            cursor.execute(selectQuery)
            allNurses = cursor.fetchall()
            print("Here are Nurses details: ")
            print("Total rows are:  ", len(allNurses))
            # Get column names from cursor description
            column_names = [col[0] for col in cursor.description]  # here we are getting cols name from DB dynamically
            table = PrettyTable()
            table.field_names = column_names  # making fields as table columns
            for row in allNurses:
                table.add_row(row)

            # Print the formatted table
            print(table)

        except psycopg2.Error as error:
            print("Failed to read data from table", error)
        finally:
            if conn:
                conn.close()
                cursor.close()
                print("The Postgresql connection inside Show nurse details is closed")

    def patientDetails(self, patientTableName):
        cursor, conn = getCursor()
        try:
            selectQuery = f"SELECT * from {patientTableName};"
            cursor.execute(selectQuery)
            allPatient = cursor.fetchall()
            print("Here are the Patient details: ")
            print("Total rows are:  ", len(allPatient))
            # Get column names from cursor description
            column_names = [col[0] for col in cursor.description]  # here we are getting cols name from DB dynamically
            table = PrettyTable()
            table.field_names = column_names  # making fields as table columns
            for row in allPatient:
                table.add_row(row)
            # Print the formatted table
            print(table)
        except psycopg2.Error as error:
            print("Failed to read data from table", error)

        finally:
            if conn:
                conn.close()
                cursor.close()
                print("The Postgresql connection inside Show Patient details is closed")

    def addDoctor(self, docTableName, docCredList):
        # AllCOl: ['id', 'name', 'specialisation', 'age', 'address', 'contact', 'fee', 'monthly_salary']
        try:
            [name, spe, age, addr, cont, fees,
             mSalary] = docCredList  # unpacking list of creds so that i can insert all in table
            cursor, conn = getCursor()
            query = f"SELECT * FROM {docTableName}"  # doing to get all the columns name of table
            cursor.execute(query)  # it does not return anything
            docDet = cursor.fetchall()  # comes details into cursor
            column_names = [col[0] for col in
                            cursor.description]  # In order to work this, you have to execute above two line.

            print(f"All Columns in {docTableName} : {column_names}")
            # Construct the INSERT query without single quotes around the table and column names
            # insertDetsQuery = f'''
            # INSERT INTO {docTableName} (name, specialisation, age, address, contact, fee, monthly_salary)
            #         VALUES ('{name}', '{spe}', '{age}', '{addr}', '{cont}', '{fees}', '{mSalary}')
            # '''
            insertDetsQuery = f'''
                    INSERT INTO doctor_details ({column_names[1]}, {column_names[2]}, {column_names[3]}, {column_names[4]}, {column_names[5]}, {column_names[6]}, {column_names[7]})
                    VALUES ('{name}', '{spe}', '{age}', '{addr}', '{cont}', '{fees}', '{mSalary}')
                '''

            cursor.execute(insertDetsQuery)
            conn.commit()
            print(f"Data INSERTED SUCCESSFULLY in  table:{docTableName} ")

        except psycopg2.Error as error:
            print(f"Failed to INSERT data in table:{docTableName} ,", error)

        finally:
            if conn:
                conn.close()
                cursor.close()
                print("The Postgresql connection is closed")
                input("Press Enter key to continue!!")

    def addNurse(self, nurseTableName, nurseCredList):
        try:
            [name, age, addr, cont, mSalary] = nurseCredList
            cursor, conn = getCursor()
            getAllColNames = f'SELECT * FROM {nurseTableName}'
            cursor.execute(getAllColNames)
            nurseDet = cursor.fetchall()  # does not need to store in any variable bcz we'll use cursor only.
            column_names = [col[0] for col in
                            cursor.description]  # getting this table(nurse_details) columns name by using list comprehension
            print(f"All Columns in {nurseTableName} : {column_names}")
            insertDetsQuery = f""" INSERT INTO {nurseTableName} ( {column_names[1]}, {column_names[2]}, {column_names[3]}, {column_names[4]}, {column_names[5]})
                                    VALUES ('{name}', '{age}', '{addr}', '{cont}', '{mSalary}')
                            """

            cursor.execute(insertDetsQuery)
            conn.commit()
            print(f"Data INSERTED SUCCESSFULLY in  table:{nurseTableName} ")

        except psycopg2.Error as error:
            print(f"Failed to INSERT data in table:{nurseTableName} ,", error)

        finally:
            if conn:
                conn.close()
                cursor.close()
                print("The Postgresql connection is closed")
                input("Press Enter key to continue!!")

    def addPatient(self, patientTableName, patientCredsList):
        cursor, conn = getCursor()
        try:
            [name, sex, addr, cont] = patientCredsList
            getAllCol = f"SELECT * FROM {patientTableName}"
            cursor.execute(getAllCol)  # it does not return anything
            cursor.fetchall()
            column_names = [col[0] for col in cursor.description]
            print(f"All Columns in {patientTableName} : {column_names}")

            insertQuery = f""" INSERT INTO {patientTableName} ({column_names[1]}, {column_names[2]}, {column_names[3]}, {column_names[4]} )
                                VALUES ( '{name}', '{sex}', '{addr}', '{cont}' )
                         """
            cursor.execute(insertQuery)
            conn.commit()
            print(f"Data INSERTED SUCCESSFULLY in  table: {patientTableName} ")
            self.patientDetails(patientTableName)

        except psycopg2.Error as error:
            print(f"Failed to INSERT data in table: {patientTableName} ,", error)

        finally:
            if conn:
                conn.close()
                cursor.close()
                print("The Postgresql connection is closed")
                input("Press Enter key to continue!!")

    def deleteDoc(self, docTableName, userName):
        cursor, conn = getCursor()
        try:
            cursor, conn = getCursor()
            # Using a parameterized query to prevent SQL injection
            delQuery = f"DELETE FROM {docTableName} WHERE name = %s RETURNING *;"  # By RETURNING * this : it will return deleted record.
            # Execute the query with the parameter
            cursor.execute(delQuery, (userName,))
            '''
            In this example, %s is a placeholder for the parameter in the DELETE query, and the actual value 
            is provided as a tuple (userName,) in the execute method. This approach helps to prevent SQL injection.
            '''
            # Fetch the deleted record (if needed)
            deleted_record = cursor.fetchone()
            conn.commit()
            print(f"You have deleted doctor : {deleted_record}")
            print("Remaining Doctors are :", end=" ")
            selectQuery = self.doctorDetails(docTableName)

        except psycopg2.Error as error:
            print(f"Failed to DELETE data in table:{docTableName} ,", error)

        finally:
            if conn:
                conn.close()
                cursor.close()
                print("The Postgresql connection inside delete record is closed")

    def deleteNurse(self, nurseTableName, nurseName):
        cursor, conn = getCursor()
        try:
            query = f'''
                        DELETE FROM {nurseTableName} WHERE name = %s ;
                '''
            cursor.execute(query, (nurseName,))
            # Fetch the deleted record (if needed)
            deleted_record = cursor.fetchone()
            print(f"You have deleted doctor : {deleted_record}")
            conn.commit()
            self.nurseDetails(nurseTableName)  # by this we can see the remaining nurses in the table

        except psycopg2.Error as error:
            print(f"Failed to DELETE data in table:{nurseTableName} ,", error)

        finally:
            if conn:
                conn.close()
                cursor.close()
                print("The Postgresql connection inside delete record is closed")

    def deletePatient(self, patientTableName, patientName):
        cursor, conn = getCursor()
        try:
            findPatient = f"SELECT * FROM {patientTableName} WHERE name = %s ;"
            cursor.execute(findPatient, (patientName, ))
            record = cursor.fetchall()
            print("So you want to discharge this patient: ", record)
            bill = input("Has he paid all the bills? (y/n):")
            if bill.lower() == "y":
                delQuery = f"DELETE FROM {patientTableName} WHERE name = '{patientName}'" # always use single quote outside the {} like '{python_variable}'. When you try to enter columns value/python variable use single qoute with that.
                '''         
The issue here is related to SQL syntax. When you are using a variable in a SQL query, especially for string values, 
it should be enclosed in single quotes. In your case, you need to modify the DELETE query to properly handle the patientName variable. So the CORRECT IS :  '{patientName}'
                '''
                cursor.execute(delQuery)
                print(f"You have deleted doctor : {record}")
                conn.commit()
                print("Remaining Doctors are :", end=" ")
                self.nurseDetails(patientTableName)  # by this we can see the remaining nurses in the table

            else:
                print("Bill not paid : Pay the bill please")

        except psycopg2.Error as error:
            print(f"Failed to DELETE data in table: {patientTableName} ,", error)

        finally:
            if conn:
                conn.close()
                cursor.close()
                print("The Postgresql connection inside delete record is closed")

    def updateDoctor(self, docTableName, userId, colName, data):
        try:
            cursor, conn = getCursor()
            # Update single record now
            updateQuery = f""" UPDATE {docTableName} 
                                    SET {colName.lower()} = %s WHERE id = %s
                            """
            cursor.execute(updateQuery, (data, userId))
            conn.commit()
            count = cursor.rowcount
            print(f"******* {count} Record Updated successfully *******  ")


        except psycopg2.Error as error:
            print(f"Failed to UPDATE data in table:{docTableName} ,", error)
        finally:
            if conn:
                conn.close()
                cursor.close()
                print("The Postgresql connection inside Update record is closed")

    def updateNurse(self, nurseTableName, userId, colName, data):
        cursor, conn = getCursor()
        try:
            updateQuery = f""" UPDATE {nurseTableName} 
                                SET {colName.lower()} = %s WHERE id = %s """
            cursor.execute(updateQuery, (data, userId))
            conn.commit()
            count = cursor.rowcount  # it will count total number of rows
            print(f"******* {count} Record Updated successfully *******  ")

        except psycopg2.Error as error:
            print(f"Failed to UPDATE data in table:{nurseTableName} ,", error)
        finally:
            if conn:
                conn.close()
                cursor.close()
                print("The Postgresql connection inside Update record is closed")

    def showEnteredData(self, username, password):
        print(f"userName : {username}")
        print(f"password : {password}")

    # common show , add, delete and update functionality and then based on the user choice making for particular entity
    def showDetails(self, doc="", nurse="", patient="", others=""):
        if doc == "doctorDet":
            docTableName = "doctor_details"
            self.doctorDetails(docTableName)
        elif nurse == "nurseDet":
            nurseTableName = "nurse_details"
            self.nurseDetails(nurseTableName)

        elif patient == "patient":
            patientTableName = "patient_details"
            self.patientDetails(patientTableName)

    def addDetails(self, doc="", nurse="", patient="",
                   others=""):  # given default arg so that i can send from where this fun is getting a single arg according to the doc or nurse or other. and below in this function bodu i can verify what arg got passed in this function.
        if doc == "doctor":
            # enter doctor details
            # ASKING THE DETAILS
            name = input("Enter the doctor's name:  ")
            spe = input("Enter the specialization:  ")
            age = input("Enter the age:  ")
            addr = input("Enter the address:  ")
            cont = input("Enter Contact Details:  ")
            fees = input("Enter the fees:  ")
            mSalary = input("Enter the monthly Salary:  ")
            docCredList = [name, spe, age, addr, cont, fees, mSalary]
            docTableName = "doctor_details"
            self.addDoctor(docTableName, docCredList)


        elif nurse == "nurse":
            name = input("Enter the nurse's name:  ")
            age = input("Enter the age:  ")
            addr = input("Enter the address:  ")
            cont = input("Enter Contact Details:  ")
            mSalary = input("Enter the monthly Salary:  ")
            nurseCredList = [name, age, addr, cont, mSalary]
            nurseTableName = "nurse_details"
            self.addNurse(nurseTableName, nurseCredList)

        elif patient == "patient":
            name = input("Enter the patient's name:  ")
            sex = input("Enter the sex:  ")
            addr = input("Enter the address:  ")
            cont = input("Enter Contact Details:  ")
            patientCredsList = [name, sex, addr, cont]
            patientTableName = "patient_details"
            self.addPatient(patientTableName, patientCredsList)

    def deleteDetails(self, doc="", nurse="", patient="", others=""):
        if doc == "doctors":
            docTableName = "doctor_details"
            print("Here are the Details of all Doctor: ")
            self.doctorDetails(docTableName)
            print("Enter the Doctor's name of which you want to remove : ",
                  end=" ")  # id and username both are unique so we can anyone.username seems more intuitive
            docName = input()
            self.deleteDoc(docTableName, docName)

        elif nurse == "nurse":
            nurseTableName = "nurse_details"
            print("Here are the Details of all Nurses: ")
            self.nurseDetails(nurseTableName)
            nurseName = input("Enter the Nurse's name of which you want to remove : ")
            self.deleteNurse(nurseTableName, nurseName)

        elif patient == "patient" :
            patientTableName = "patient_details"
            print("Here are the Details of all Patients: ")
            self.patientDetails(patientTableName)
            patientName = input("Enter the Patient's name of which you want to remove : ")
            self.deletePatient(patientTableName, patientName)

    def updateDetails(self, doc="", nurse="", patient="", others=""):
        if doc == "doctors":
            docTableName = "doctor_details"
            print("All Doctor *** BEFORE UPDATE *** : ")
            self.doctorDetails(docTableName)
            # print(" and the column name and update value (except ID): ", end=" ")  # id and username both are
            # unique so we can use anyone.username seems more intuitive
            userId = input("Enter the Doctor's ID of which you want to Update: ")
            colName = input("Enter the Column name that you want to update in : ")
            data = input("Enter the value that you want to update: ")

            self.updateDoctor(docTableName, userId, colName, data)

            print("All Doctor *** AFTER UPDATE *** : ")
            self.doctorDetails(docTableName)

        elif nurse == "nurse":
            nurseTableName = "nurse_details"
            print("All Nurses *** BEFORE UPDATE *** : ")
            self.nurseDetails(nurseTableName)
            userId = input("Enter the Nurse's ID of which you want to Update: ")
            colName = input("Enter the Column name that you want to update in : ")
            data = input("Enter the value that you want to update: ")
            self.updateNurse(nurseTableName, userId, colName, data)

            print("All Nurse *** AFTER UPDATE *** : ")
            self.nurseDetails(nurseTableName, )
