import csv
import mysql.connector


class Employee():

    host = "localhost"
    port = "3307"
    username = "root"
    password = "usbw"
    db = "northwind"

    def __init__(self, row):
        self.employeeid = row['EmployeeID']
        self.lastname = row['LastName']
        self.firstname = row['FirstName']
        self.title = row['Title']
        self.titleofcourtesy = row['TitleOfCourtesy']
        self.birthdate = row['BirthDate']
        self.hiredate = row['HireDate']
        self.address = row['Address']
        self.city = row['City']
        self.region = row['Region']
        self.postalcode = row['PostalCode']
        self.country = row['Country']
        self.homephone = row['HomePhone']
        self.extension = row['Extension']
        self.photo = row['Photo']
        self.notes = row['Notes']
        self.reportsto = row['ReportsTo']
        self.photopath = row['PhotoPath']
        self.salary = row['Salary']

    @staticmethod
    def parse(rownumber):
        count = 1
        with open('employees.csv', 'r') as f:
            reader = csv.DictReader(f,delimiter = ";")
            for row in reader:
                count += 1
                if count == rownumber:
                    tester = Employee(row)
                    return tester

    @staticmethod
    def persist():
        connection = mysql.connector.connect(user=Employee.username, password=Employee.password, host=Employee.host,port=Employee.port,database=Employee.db)
        cursor = connection.cursor(buffered = True)

        print(tester.lastname)


Employee.persist()