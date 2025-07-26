import mysql.connector
from mysql.connector import Error

class DBUtility:
    def __init__(self) -> None:
        self.config = {'host': 'localhost',       # your MySQL host
                       'database': 'medextract',  # your database
                       'user': 'root',   # your MySQL username
                       'password': 'root'} # your MySQL password
        self.connection = None
        self.cursor = None

    def get_connection_cursor(self):
        try:
            connection = mysql.connector.connect(
                host = self.config['host'],
                database = self.config['database'],
                user = self.config['user'],
                password = self.config['password']
            )
            if connection.is_connected():
                self.connection = connection
                self.cursor = connection.cursor()
                print("Connected to db")
        except Error as e:
            print("Error in connecting to db")

    def update_table(self, table, data):
        if not self.connection:
            self.get_connection_cursor()
        try:
            if self.connection and self.cursor:
                print(data)
                if table == 'patient':
                    self.cursor.callproc('add_patient', data) # executing stored procedure
                if table == 'prescription':
                    self.cursor.callproc('add_prescription', data) # executing stored procedure
                self.connection.commit()
                print("Patient information stored successfully")
                return True
            else:
                print("Error in executing stored procedure")
                return False
        except Exception as e:
            print("Error in executing stored procedure", e)
            return False
        finally:
            if self.connection:
                self.connection.close()
            if self.cursor:
                self.cursor.close()


if __name__ == "__main__":
    dbutility = DBUtility()
    data = ('Jon snow', '1234567890', 'Fully Vaccinated', 'Hypertension', 'HealthCarePlus')
    dbutility.update_table(table='patient', data=data)
