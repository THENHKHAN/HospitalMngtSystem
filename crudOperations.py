from setupDB import getCursor


class MyHospitalDB :

   def showEnteredData (self, username, password):
        print(f"userName : {username}")
        print(f"password : {password}")

   def userData (self, username, password) :
       [cursor, conn] = getCursor()

       if username == "SELECT name FROM user_details" :
           print("User already Exist")

       else:
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
               """ )








