def create_record(mydb):
    name = input("Enter name: ")
    address = input("Enter address: ")
    mobile = input("Enter mobile: ")
    email = input("Enter email: ")
    mycursor = mydb.cursor()
    sql = "INSERT INTO book(name,address,mobile,email) VALUES (%s,%s,%s,%s)"
    record = (name,address,mobile,email)
    mycursor.execute(sql, record)
    mydb.commit()
    mycursor.close()
    print("Record Entered Successfully\n")

def search(mydb, name):
    mycursor = mydb.cursor()
    sql = 'SELECT * FROM book WHERE name = %s'
    value = (name,)
    mycursor.execute(sql, value)
    record = mycursor.fetchone()
    if record == None:
        print("No such record exists")
    else:
        print("\nRESULT OF SEARCH ")
        print("-"*35)
        print('Name: ', record[0])
        print('Address: ', record[1])
        print('Mobile: ', record[2])
        print('Email: ', record[3])
        print("-"*35)

def display_all(mydb):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM book")
    print("="*80)
    print('{0:20}{1:30}{2:15}{3:30}'.format('NAME', 'ADDRESS', 'MOBILE NO', 'E-MAIL'))
    print("="*80)
    for record in mycursor:
        print('{0:20}{1:30}{2:15}{3:30}'.format(record[0], record[1], record[2], record[3]))
        print("-"*80)
    print("="*80)
    mycursor.close()

def delete_record(mydb, name):
    mycursor = mydb.cursor()
    sql = 'DELETE FROM book WHERE name = %s'
    value = (name,)
    mycursor.execute(sql, value)
    mydb.commit()
    if mycursor.rowcount == 0:
        print("Record not found")
    else:
        print("Record deleted successfully")

def modify_record(mydb, name):
    mycursor = mydb.cursor()
    sql = 'SELECT * FROM book WHERE name = %s'
    value = (name,)
    mycursor.execute(sql, value)
    record = mycursor.fetchone()
    if record is None:
        print("No such record exists")
    else:
        while True:
            print('\nPress the option you want to edit: ')
            print("1. Name")
            print("2. Address")
            print("3. Mobile")
            print("4. BACK")
            print()
            ch = int(input("Select your option (1-4): "))
            if ch == 1:
                new_name = input("Enter new Name: ")
                sql = 'UPDATE book SET name = %s WHERE name = %s'
                values = (new_name, name)
                mycursor.execute(sql, values)
                mydb.commit()
                print(mycursor.rowcount, "record updated successfully")
            elif ch == 2:
                new_address = input("Enter new Address: ")
                sql = 'UPDATE book SET address = %s WHERE name = %s'
                values = (new_address, name)
                mycursor.execute(sql, value)
                mydb.commit()
                print(mycursor.rowcount, "record updated successfully")
            elif ch == 3:
                new_mobile = input("Enter new Mobile: ")
                sql = 'UPDATE book SET mobile = %s WHERE name = %s'
                values = (new_mobile, name)
                mycursor.execute(sql, value)
                mydb.commit()
                print(mycursor.rowcount, "record updated successfully")
            elif ch == 4:
                break
            else:
                print("Invalid choice !!!\n")
        mycursor.close()