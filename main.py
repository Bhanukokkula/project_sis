import sqlite3
conn = sqlite3.connect("student_info.db")
c = conn.cursor()


#def switch(case):
 #   case1: int(input("enter 1 for SELECT:"))
  #  case2: int(input("enter 2 for INSERT: "))
   # case3: int(input("enter 3 for UPDATE:"))
   # case4: int(input("enter 4 for DELETE:"))
   # case5: int(input("enter 5 for EXIT:"))

def run():
    menu = int(input("enter 1 for SELECT:"))
    menu = int(input("enter 2 for INSERT:"))
    menu = int(input("enter 3 for UPDATE:"))
    menu = int(input("enter 4 for DELETE:"))
   # menu = int(input("enter 5 for EXIT:"))

    return menu


menu = run()


while True:

    if menu == 1:

        try:
            sid = input("Enter student ID : ")

            ins_cur = conn.cursor()

            query = 'SELECT student_ID FROM student '
            print(c.fetchall())

            ins_cur.execute(query)

            conn.commit()

            menu = run()

        except :
            print('e')

        finally:
            conn.close()
            ins_cur.close()

    if menu == 2:
        ins_cur = conn.cursor()

        query = 'INSERT INTO student(student_ID, Name, Email,'\
                ' Ph_No,City,Gender,Date_of_birth,Dept,Year_of_Passing,Grade,Percentage)'

        ins_cur.execute(query)

        conn.commit()

        menu = run()

    if menu == 3:
        ins_cur = conn.cursor()

        query = 'UPDATE student(student_ID,Name,Email,Ph_No,City,Gender,Date_of_birth,Dept,Year_of_Passing,Grade,Percentage)'

        ins_cur.execute(query)

        conn.commit()

        menu = run()

    if menu == 4:
        try:
            emp_no = int(input())

            del_cur = conn.cursor()

            query = 'DELETE FROM student where student_ID = %d student_ID'

            del_cur.execute(query)

            conn.commit()

        except sqlite3.data as e:
            print(e)

        finally:
            del_cur.close()
            conn.close()
            menu = run()

    if menu == 5:
        ins_cur = conn.cursor()

        exit('student.db')

        conn.commit()

        menu = run()

    break
conn.close()
