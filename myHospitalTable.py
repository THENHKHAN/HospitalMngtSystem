from setupDB import getCursor


# creating user_data (it will have : doctor , nurse , patient , others)

def userTable(cursor, conn): # this is like main user who can act as a receptionist  perform operation on doctor ,
    # nurse, patient,others
    table_query = '''   
            CREATE TABLE IF NOT EXISTS user_details (  
                id SERIAL PRIMARY KEY,
                name VARCHAR(30) NOT NULL,
                password VARCHAR(30) NOT NULL                     
            );    
    '''
    cursor.execute(table_query)
    conn.commit()


def doctorTable(cursor, conn):
    table_query = '''

            CREATE TABLE IF NOT EXISTS doctor_details (          
                id SERIAL PRIMARY KEY ,
                name VARCHAR (30) NOT NULL ,
                specialisation VARCHAR (30) NOT NULL,
                age INT NOT NULL ,
                address VARCHAR (60)  NOT NULL, 
                contact VARCHAR (15) NOT NULL ,
                fee INT,
                monthly_salary INT
            );
    '''
    cursor.execute(table_query)
    conn.commit()


def nurseTable(cursor, conn):
    table_query = '''

            CREATE TABLE IF NOT EXISTS nurse_details (
                id SERIAL PRIMARY KEY ,
                name VARCHAR (30) NOT NULL ,
                age INT NOT NULL ,
                address VARCHAR (60) NOT NULL , 
                contact VARCHAR (15) NOT NULL ,
                monthly_salary INT 
            );
    '''
    cursor.execute(table_query)
    conn.commit()


def patientTable(cursor, conn):
    table_query = '''

            CREATE TABLE IF NOT EXISTS patient_details (
                id SERIAL PRIMARY KEY ,
                name VARCHAR (30) NOT NULL ,
                sex VARCHAR (30) NOT NULL ,
                address VARCHAR (60) NOT NULL , 
                contact VARCHAR (15) NOT NULL 
            );              
    '''
    cursor.execute(table_query)
    conn.commit()


def otherWorkerTable(cursor, conn):
    table_query = '''

            CREATE TABLE IF NOT EXISTS other_worker_details (
                id SERIAL PRIMARY KEY ,
                name VARCHAR (30) NOT NULL ,
                address VARCHAR (60) NOT NULL , 
                contact VARCHAR (15) NOT NULL ,  
                monthly_salary INT 
            );           
    '''
    cursor.execute(table_query)
    conn.commit()


[cursor, conn] = getCursor() # returing cursor and connection so receing as list so these variable work equavalent to the returned.
userTable(cursor, conn)
doctorTable(cursor, conn)
nurseTable(cursor, conn)
patientTable(cursor, conn)
otherWorkerTable(cursor, conn)

print("All 5 table created ")

cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
tables = cursor.fetchall()
print("Tables: ",
      tables)  # [('user_details',), ('doctor_details',), ('nurse_details',), ('patient_details',), ('other_worker_details',)]
table_names = [table[0] for table in
               tables]  # ['user_details', 'doctor_details', 'nurse_details', 'patient_details', 'other_worker_details']
print("Tables: ", table_names)

for table in table_names:
    print(table)
cursor.close()
conn.close()
