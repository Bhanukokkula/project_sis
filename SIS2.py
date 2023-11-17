import sqlite3

#import cursor as cursor

conn = sqlite3.connect("student_info.db")
c = conn.cursor()

print("----------STUDENT RECORD MANAGEMENT SYSTEM------------")
print("Enter 1 for SELECT ")
print("Enter 2 for INSERT ")
print("Enter 3 for UPDATE ")
print("Enter 4 for DELETE ")
print("Enter 5 for EXIT ")
print("Enter(1-5) : ")
n = int(input())


def values():
    pass


if n == 1:
    sid = input("Enter student ID : ")

    c = conn.cursor()

    #query = 'SELECT student_ID FROM students '
    #result = cursor.fetchall()
    #return result

    c.execute("SELECT * FROM student")
    print(c.fetchone())
    #for row in result:
     #   print(row)

    conn.commit()

elif n == 2:
    sid = int(input("Enter ID : "))
    sname = input("Enter name : ")
    semail = input("Enter email : ")
    snumber = int(input("Enter ph_number :"))
    scity = input("Enter city :")
    sgender = input("Enter gender : ")
    sdob = input('Enter DOB : ')
    sdept = input("Enter department :")
    syop = int(input("Enter year of passing :"))
    ssem = int(input("Enter semester :" ))
    sgrade = input("Enter grade :")
    sper = input("Enter percentage :")

    c.execute("INSERT INTO student (student_ID,Name,Email,Ph_No,City,Gender,Date_of_birth,Dept,Year_of_Passing,"
              "Semester,Grade,Percentage) VALUES (?,?,?,?,?,?,?,?,?,?,?,?); ",
              (sid, sname, semail, snumber, scity, sgender, sdob, sdept, syop, ssem, sgrade, sper))
    print(c.fetchall())
    print("Insertion is successful")
    #for row in result:
     #   print(row)
    conn.commit()

elif n == 3:

    uname = input("Enter name : ")
    umail = input("Enter email : ")
    unumber = int(input("Enter ph_number : "))
    ucity = input("Enter city :")
    #sql = "SELECT * FROM students WHERE name ='uname', email ='umail' , ph_number ='unumber' , city ='ucity';"
    c = conn.cursor()
    #c.execute("SELECT * FROM student WHERE Name ='uname',Email ='umail', Ph_No ='unumber', City ='ucity'")
    result = c.fetchall()
    print(result)

    name = input("Enter new name :")
    mail = input("Enter new email :")
    number = int(input("Enter new ph_number :"))
    city = input("Enter new city :")
   # sql = "UPDATE students SET name ='Name(upname)', email='Email(upmail)', ph_number ='Ph_No(upnumber)',"\
        #  "city ='City(upcity)' WHERE name='uname', email ='umail' , ph_number ='unumber' , city ='ucity';"

    sql = "UPDATE student SET Name ='name', Email='mail' ,Ph_No ='number', City ='city' WHERE Name='uname'"
    ",Email ='umail' , Ph_No ='unumber' , City ='ucity'"
    #print(result)
    c.execute(sql)
    print(c.fetchall())
    # conn.commit()

    print("Updated successfully")
    conn.commit()

elif n == 4:
    sid = int(input("Enter the ID : "))
    c = conn.cursor()
    #c.execute("SELECT * FROM student WHERE student_ID='sid'")
    #print(c.fetchall())


   # query = "DELETE * FROM students where student_ID='student_ID';"
    #res = input("Do you want to delete this record ? (Y/N)")

    sql = "DELETE FROM student WHERE student_ID ='+sid+'"
    c.execute(sql)
    print(c.fetchall())
    #if res == 'Y':
        #try:
    # c.execute(sql)
            #conn.commit()
    print("Successfully Deleted")
    conn.commit()
        #except :
           # print("error in delete operation")
           # conn.rollback()

elif n == 5:
    c = conn.cursor()

    exit("student_info.db")

    conn.commit()
else:
    print("----------THANK YOU!-----------")
conn.close()




