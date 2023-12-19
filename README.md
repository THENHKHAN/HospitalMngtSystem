## Hospital Management System in Python
#### Tech Stack :
1 - `Python`<br>
2 - `PostgreSQL`<br>
3 - `Pycharm IDE`

We are going to learn the entire process step by step. We are going to learn starting from the Registration to the discharge of the patient 
using Python Programming Language.

>We all are aware of the Hospital management work. There comes the registration of new patients, the bed, the doctor’s details, and the medicines information. The nurses’ and the worker’s details and lastly the discharge summary of the patient

## Important INFO:
```
1. Installing PostgreSql Database and PostgreSql-connector-python as psycopg2.
2. Import the module and perform database connectivity
3. Perform New Registration
4. Display the list of options the user wants to select
5. Adding the data of the administration staff
6. Updating and Deleting the details of the administration staff 
7. Displaying the patient’s information and adding the new patients
8. Discharge process of the patient and accounting of the bills
```
### Features and Benefits of Hospital Management System in Python
Here as we are using PostgreSQL for database creation in Hospital Management, we are able to
* Register new Staff/Patient
* View the staff, patient information, discharge, and bill payment summary details.
* Update and Delete the details.
* We can add, delete and modify and view the details of the doctors, nurses, and workers.

### DB Setup :
```Python
import psycopg2

try :
    conn = psycopg2.connect(database="Demo",
                            host="localhost",
                            user="postgres",
                            password="password",
                            port="5432")

except Exception as error :
    print(error)

cursor = conn.cursor()
# Most importantly: ALWAYS make commit after executing query. Like this conn.commit()
```
## Important for writing variable inside sql query string:
Problem:
```python
 delQuery = f"DELETE FROM {patientTableName} WHERE name = {patientName}"
                cursor.execute(delQuery)
Failed to DELETE data in table: patient_details , column "rohan" does not exist
LINE 1: DELETE FROM patient_details WHERE name = rohan

Mine Question:
                but this name is exist
                 [(6, 'rohan', 'm', 'mm-445 , ffdf, sf mumbai', '113399')]
 
```
Solution:
```python
The issue here is related to SQL syntax. When you are using a variable in a SQL query, especially for string values, it should be enclosed in single quotes.
In your case, you need to modify the DELETE query to properly handle the patientName variable.

Here's the corrected code:

delQuery = f"DELETE FROM {patientTableName} WHERE name = '{patientName}'"
cursor.execute(delQuery)
```
Focus here **`'{patientName}'`** </br>

##### Another Syntax:
```python
        query = f'''
                    DELETE FROM {nurseTableName} WHERE name = %s ;
            '''
        cursor.execute(query, (nurseName,))
```
#####  WARNING:
```commandline
Always be cautious about SQL injection vulnerabilities when concatenating variables into SQL queries. If the variable comes from user input,
consider using parameterized queries or proper escaping mechanisms to prevent potential security risks.
```


