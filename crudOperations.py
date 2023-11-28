from setupDB import getCursor


class MyHospitalDB:

    def showEnteredData(self, username, password):
        print(f"userName : {username}")
        print(f"password : {password}")

    def userLogin (self, userName, password):
        [cursor, conn] = getCursor()
        verifyUserNamePass = f"SELECT name FROM user_details WHERE name = '{userName}' and  password = '{password}'"
        cursor.execute(verifyUserNamePass)
        existingUserNamePass = cursor.fetchone()
        if existingUserNamePass :
            print("User verified!!!")
            print("You are successfully Logged in!!!")
        else:
            print("Username or password is WRONG!! ")

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
