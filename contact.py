import mysql.connector
import time
from controllers import *

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='sarmadjkhan123',
    database='contact'
)

def intro():
    print("="*35)
    print("CONTACT")
    print("BOOK")
    print("PROJECT\n")
    print("MADE BY: Sarmad Junaid")
    print("="*35)
    print()
    time.sleep(2)

def main():
    intro()
    while True:
        print("\n MAIN MENU ")
        print("1. ADD NEW RECORD")
        print("2. SEARCH RECORD")
        print("3. DISPLAY ALL RECORDS")
        print("4. DELETE RECORD")
        print("5. MODIFY RECORD")
        print("6. EXIT")
        print()
        ch = int(input("Select Your Option (1-6): "))
        print()
        if ch == 1:
            print("ADD NEW RECORD")
            create_record(mydb)
        elif ch == 2:
            print("SEARCH RECORD BY NAME")
            name = input("Enter name: ")
            search(mydb, name)
        elif ch == 3:
            print("DISPLAY ALL RECORDS")
            display_all(mydb)
        elif ch == 4:
            print("DELETE RECORD")
            name = input("Enter name: ")
            delete_record(mydb, name)
        elif ch == 5:
            print("MODIFY RECORD")
            name = input("Enter name: ")
            modify_record(mydb, name)
        elif ch == 6:
            print("Thanks for using Contact Book")
            mydb.close()
            break
        else:
            print("Invalid Choice")

main()