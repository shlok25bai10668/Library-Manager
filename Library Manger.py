import time
from tabulate import tabulate

#ESTABLISHING CONNECTIVITY BETWEEN MYSQL AND PYTHON
import mysql.connector as c1
pwd=input("Enter your MySQL password: ")
db=c1.connect(
    host="localhost",
    user="root",
    password=pwd
)
curs=db.cursor()
curs.execute("create database if not exists Library")

#CREATING TABLE
curs.execute("Use Library")
table=("create table if not exists Books("
"BookId integer primary key auto_increment," 
"Title varchar(255) not null," 
"Author varchar(255) not null," 
"Publishing_Date varchar(255) not null," 
"Publisher varchar(255) not null," 
"Category varchar(255) not null)"
)
curs.execute(table)

#FUNCTION TO ADD RECORD
def addlib():
    tit=str(input("Enter the name of the book: "))
    au=str(input("Enter the author's name: "))
    dat=str(input("Enter publishing date: "))
    pub=str(input("Enter the publisher's name: "))
    ge=str(input("Category of the book: "))
    line1="insert into Books(Title, Author, Publishing_Date, Publisher, Category) values(%s,%s,%s,%s,%s)"
    h1=(tit,au,dat,pub,ge)
    curs.execute(line1,h1)
    print("Adding Record...")
    time.sleep(2)
    print("Your record has been stored.")
    wait = input('\n\nPress any key to continue.')
    db.commit()

#FUNCTION TO VIEW BOOKS
def slib():
    se7="SELECT * FROM Books"
    curs.execute(se7)
    qq=curs.fetchall()
    if qq is None:
        print("Book not found.")
    else:
        print("\nBook Found.")
        headers=["BookID", "Title", "Author", "Publishing Date", "Publisher", "Category"]
        print(tabulate(qq, headers, tablefmt="grid"))
    input('\n\nPress any key to continue.')

#FUNCTION TO SEARCH BY CATEGORY
def scat():
    cat=input("Enter the category to search: ")
    query="Select * from Books where Category=%s"
    curs.execute(query, (cat,))
    results=curs.fetchall()
    
    if not results:
        print("No books found in this category.")
    else:
        headers=["BookID", "Title", "Author", "Publishing Date", "Publisher", "Category"]
        print(tabulate(results, headers, tablefmt="grid"))
    input('\n\nPress any key to continue.')

#FUNCTION TO REMOVE RECORD
def remrec():
    tit=input("Enter book name: ")
    qd="Delete from Books where Title=%s"
    curs.execute(qd,(tit,))
    print("Record has been removed.")
    wait = input('\n\nPress any key to continue.')
    db.commit()

def menu():
    while True:
        print("1. View books")
        print("2. Add book")
        print("3. Remove book")
        print("4. Search by Category")
        print("5. Exit")
        i1=int(input("Enter your selection: "))
        if i1==1:
            slib()
        elif i1==2:
            addlib()
        elif i1==3:
            remrec()
        elif i1==4:
            scat()
        elif i1==5:
            break
        else:
            print("Please select from the given options.")
menu()
