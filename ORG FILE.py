import sqlite3

# import cursor as cursor

conn = sqlite3.connect("student_info.db")
c = conn.cursor()

def menu():
    print("----------STUDENT RECORD MANAGEMENT SYSTEM------------")
    print("Enter 1 for SELECT ")
    print("Enter 2 for INSERT ")
    print("Enter 3 for UPDATE ")
    print("Enter 4 for DELETE ")
    print("Enter 5 for EXIT ")

    return int(input("what would you like to do ?"))
   # print("----------STUDENT RECORD MANAGEMENT SYSTEM------------")




run = menu()

while True:
        if run == 1:
            a = int(input("Enter student ID to SELECT : "))
            c = conn.cursor()
            query = "SELECT * FROM student where student_ID= %d" % (a)
            c.execute(query)
            #print(c.fetchmany())
            b= c.fetchmany()
            if b != [] :
                print(b)
            else:
                print("data not found")
            conn.commit()
            q = input("Would you like to go back to menu ? (y/n)")
            if q == 'y':
                run = menu()
            else:
                print("----------THANK YOU!-----------")
                break


        elif run == 2:
            sid = int(input("Enter ID to INSERT : "))
            sname = input("Enter name : ")
            semail = input("Enter email : ")
            snumber = int(input("Enter ph_number :"))
            scity = input("Enter city :")
            sgender = input("Enter gender : ")
            sdob = int(input('Enter DOB : '))
            sdept = input("Enter department :")
            syop = int(input("Enter year of passing :"))
            ssem = int(input("Enter semester :"))
            sgrade = input("Enter grade :")
            sper = input("Enter percentage :")

            c = conn.cursor()

            # c.execute("INSERT INTO student (student_ID,Name,Email,Ph_No,City,Gender,Date_of_birth,Dept,Year_of_Passing,"
            #         "Semester,Grade,Percentage) VALUES (?,?,?,?,?,?,?,?,?,?,?,?); ",
            #        (sid, sname, semail, snumber, scity, sgender, sdob, sdept, syop, ssem, sgrade, sper))

            # print(c.fetchall())

            c.execute("INSERT INTO student (student_ID,Name,Email,Ph_No,City,Gender,Date_of_birth,Dept,Year_of_Passing,"
                      "Semester,Grade,Percentage) VALUES (?,?,?,?,?,?,?,?,?,?,?,?);",
                      (sid, sname, semail, snumber, scity, sgender, sdob, sdept, syop, ssem, sgrade, sper))

            # query = ("INSERT INTO student (student_ID, Name, Email, Ph_No, City, Gender, Date_of_birth, Dept, Year_of_Passing, Semester, Grade, Percentage) VALUES ('%d', '%s', '%s', '%d', '%s', '%s', '%d', '%s', '%d', '%d', '%s', '%s')")
            # c.execute(query %(sid, sname, semail, snumber, scity, sgender, sdob, sdept, syop, ssem, sgrade, sper))

            print(c.fetchall())
            conn.commit()

            print("INSERTION  IS SUCCESSFULL")
            # for row in result:
            #   print(row)

            q = input("Would you like to go back to menu ? (y/n)")
            if q == 'y':
                run = menu()
            else:
                print("----------THANK YOU!-----------")
                break


        elif run == 3:

            # uname = input("Enter name : ")
            # umail = input("Enter email : ")
            # unumber = int(input("Enter ph_number : "))
            # ucity = input("Enter city :")
            # sql = "SELECT * FROM students WHERE name ='uname', email ='umail' , ph_number ='unumber' , city ='ucity';"
            sid = int(input("Enter student ID to UPDATE : "))
            c = conn.cursor()
            query = "SELECT * FROM student where student_ID= %d" % (sid)
            c.execute(query)
            b = c.fetchmany()
            if b != []:
                print(b)
                mail = input("Enter new email :")
                number = int(input("Enter new ph_number :"))
                city = input("Enter new city :")
                sql = "UPDATE student SET  Email='%s', Ph_no='%d', City='%s' where student_ID= %d"
                # print(result)
                c.execute(sql % (mail, number, city, sid))
                #print(c.fetchall())
                # conn.commit()

                print("UPDATED SUCCESSFULLY")
                conn.commit()
                q = input("Would you like to go back to menu ? (y/n)")
                if q == 'y':
                    run = menu()
                else:
                    print("----------THANK YOU!-----------")
                    break


            else:
                print("THE ROW YOU ARE TRYING TO UPDATE IS NOT PRESENT IN THE database")

                q = input("would you like to go back to menu ? (y/n)")
                if q == 'y':
                    run = menu()
                else:
                    print("----------THANK YOU!-----------")
                    break
                #if choice() == 1:
                 #   break
                #else:
                 #   pass

            # c.execute("SELECT * FROM student WHERE Name ='uname',Email ='umail', Ph_No ='unumber', City ='ucity'")
            # result = c.fetchall()
            # print(result)

            #name = input("Enter new name :")

            # sql = "UPDATE students SET name ='Name(upname)', email='Email(upmail)', ph_number ='Ph_No(upnumber)',"\
            #  "city ='City(upcity)' WHERE name='uname', email ='umail' , ph_number ='unumber' , city ='ucity';"




        elif run == 4:
            a = int(input("Enter the ID to DELETE : "))
            c = conn.cursor()
            # c.execute("SELECT * FROM student WHERE student_ID='sid'")
            # print(c.fetchall())
            # query = "DELETE * FROM students where student_ID='student_ID';"
            # res = input("Do you want to delete this record ? (Y/N)")
            #query = "SELECT * FROM student where student_ID= %d" % (sid)
            #c.execute(query)
            #b = c.fetchmany()
            #if b != []:
            #print(b)
            query = "SELECT * FROM student where student_ID= %d" % (a)
            c.execute(query)
            b = c.fetchall()
            if b != []:
                print(b)
                query1 = "DELETE from student where student_ID = %d " %(a)
                c.execute(query1)
                print("DELETED SUCCESSFULLY")
            else:
                print("data not found")
            conn.commit()
            q = input("would you like to go back to menu ? (y/n)")
            if q == 'y':

                run = menu()
            else:
                print("----------THANK YOU!-----------")
                break

        elif run == 5:
            c = conn.cursor()
            print("---EXIT SUCCESSFUL---")
            exit("student_info.db")

            conn.commit()
            print("----------THANK YOU!-----------")
            break
        else:
            print("----------THANK YOU!-----------")
            break
            conn.close()