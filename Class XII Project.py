import mysql.connector as mysql

connect = mysql.connect(host='localhost', user='root', passwd='12345', database='lib')
cursor = connect.cursor()


def main():
    print('| Library Management System |')
    result = password()
    if result:
        while True:
            print('\nMenu\n',
                  '\t', '1.Issue Book', '\t\t', '2.Submit Book\n',
                  '\t', '3.Current Status', '\t', '4.History\n',
                  '\t', '5.Admin Block', '\t\t', '6.Quit\n', sep='')
            c = int(input('Choose from the above option : '))
            if c == 1:
                issue()
            elif c == 2:
                submit()
            elif c == 3:
                dispcurrent()
            elif c == 4:
                disphistory()
            elif c == 5:
                admin()
            elif c == 6:
                break
            else:
                print('\nWRONG INPUT.TRY AGAIN.')
        connect.close()
        print('\nend of Program.')


def password():
    while True:
        pw = input('\nEnter the password : ')
        if pw == '12345':
            return True
        else:
            c = input('\n|Wrong Password|\n\nDo you want to try again(Y/N) : ')
            if c != 'Y' and c != 'y':
                break
    return False


def dispcurrent():
    command = "SELECT * FROM current"
    cursor.execute(command)
    table = cursor.fetchall()
    print('\nCurrent status is as follows : ')
    print()
    print('\t', 'S.No.', ' ' * 6, 'S.Name', ' ' * 11, 'B.No.', ' ' * 5, 'B.Name', ' ' * 11, 'Date', sep='')
    for row in table:
        print('\t', row[0], ' ' * (11 - len(row[0])), row[1], ' ' * (17 - len(row[1])),
              row[2], ' ' * (10 - len(row[2])), row[3], ' ' * (17 - len(row[3])), row[4], sep='')


def disphistory():
    command = "SELECT * FROM history"
    cursor.execute(command)
    table = cursor.fetchall()
    print('\nHistory is as follows : ')
    print()
    print('\t', 'Action', ' ' * 6, 'S.No.', ' ' * 6, 'S.Name', ' ' * 11,
          'B.No.', ' ' * 5, 'B.Name', ' ' * 11, 'Date', sep='')
    for row in table:
        print('\t', row[0], ' ' * (12 - len(row[0])),
              row[1], ' ' * (11 - len(row[1])), row[2], ' ' * (17 - len(row[2])),
              row[3], ' ' * (10 - len(row[3])), row[4], ' ' * (17 - len(row[4])), row[5], sep='')


def admin():
    while True:
        print('\nAdmin Menu\n',
              "1.Book's Record\n", "2.Student's Record\n", '3.Return\n', sep='')
        c = int(input('Choose from the above option : '))
        if c == 1:
            books()
        elif c == 2:
            students()
        elif c == 3:
            return
        else:
            print('\nWRONG INPUT.TRY AGAIN.')


def books():
    while True:
        print('\nNow, what do you want to do?\n',
              '\t', '1.Add Book', '\t\t', '2.Delete Book\n',
              '\t', '3.Update Book', '\t\t', '4.Display All Book\n',
              '\t', '5.Return\n', sep='')
        c = int(input('Choose from the above option : '))
        if c == 1:
            add('book')
        elif c == 2:
            delete('book')
        elif c == 3:
            update('book')
        elif c == 4:
            disp('book')
        elif c == 5:
            return
        else:
            print('\nWRONG INPUT.TRY AGAIN.')


def students():
    while True:
        print('\nNow, what do you want to do?\n',
              '\t', '1.Add Student', '\t\t', '2.Delete Student\n',
              '\t', '3.Update Student', '\t', '4.Display All Student\n',
              '\t', '5.Return\n', sep='')
        c = int(input('Choose from the above option : '))
        if c == 1:
            add('student')
        elif c == 2:
            delete('student')
        elif c == 3:
            update('student')
        elif c == 4:
            disp('student')
        elif c == 5:
            return
        else:
            print('\nWRONG INPUT.TRY AGAIN.')


def add(obj):
    if obj == 'book':
        o = 'b'
        no = input('\nEnter the 5 digit Book Number : ')
        if len(no) != 5 or not (no.isdigit()):
            print('\nThis is not a valid Book Number for our database. Try Again.')
            return
    if obj == 'student':
        o = 's'
        no = input('\nEnter the 6 digit Student Number : ')
        if len(no) != 6 or not (no.isdigit()):
            print('\nThis is not a valid Student Number for our database. Try Again.')
            return

    command = "SELECT {}no FROM {} WHERE {}no='{}'".format(o, obj, o, no)
    cursor.execute(command)
    val = cursor.fetchall()
    if val != []:
        print('\nThere is already a {} with this number. Try again.'.format(obj))
        return

    name = input('Enter the {} Name : '.format(obj.capitalize()))

    print('\nPlease check the details you have entered : \n')
    print('{} Number : '.format(obj.capitalize()), no, '\n{} Name : '.format(obj.capitalize()), name, sep='')
    c = input('\nDo you want to continue with these details(Y/N) : ')
    if c != 'Y' and c != 'y':
        print('\nTry Again.')
        return

    command = "INSERT INTO {} VALUES('{}','{}')".format(obj, no, name)
    cursor.execute(command)
    connect.commit()
    print('\n|{} added successfully|'.format(obj.capitalize()))


def delete(obj):
    print('\n1.Delete individual\n', '2.Delete all\n', sep='')
    c = int(input('Choose from the above option : '))
    if c == 1:
        if obj == 'book':
            o = 'b'
            no = input('\nEnter the 5 digit Book Number : ')
            if len(no) != 5 or not (no.isdigit()):
                print('\nThis is not a valid Book Number for our database. Try Again.')
                return
        if obj == 'student':
            o = 's'
            no = input('\nEnter the 6 digit Student Number : ')
            if len(no) != 6 or not (no.isdigit()):
                print('\nThis is not a valid Student Number for our database. Try Again.')
                return

        command = "SELECT {}no FROM {} WHERE {}no='{}'".format(o, obj, o, no)
        cursor.execute(command)
        val = cursor.fetchall()
        if val == []:
            print('\nNo such {} to delete. Try Again.'.format(obj))
            return

        command = "SELECT {}no FROM current WHERE {}no='{}'".format(o, o, no)
        cursor.execute(command)
        val = cursor.fetchall()
        if val == [(no,)]:
            if obj == 'book':
                print('\nThis book is currently issued to someone. Cannot Delete.')
                return
            if obj == 'student':
                print('\nThe student currently holds a book from our library. Cannot Delete.')
                return

        command = "SELECT {}name FROM {} WHERE {}no='{}'".format(o, obj, o, no)
        cursor.execute(command)
        val = cursor.fetchall()
        name = val[0][0]

        print('\nPlease check the details one last time : \n')
        print('{} Number : '.format(obj.capitalize()), no, '\n{} Name : '.format(obj.capitalize()), name, sep='')
        c = input('\nDo you want to continue with these details(Y/N) : ')
        if c != 'Y' and c != 'y':
            print('\nTry Again.')
            return

        command = "DELETE FROM {} WHERE {}no='{}'".format(obj, o, no)
        cursor.execute(command)
        connect.commit()
        print('\n|{} deleted successfully|'.format(obj.capitalize()))

    elif c == 2:
        c = input('\nDo you really want to delete all records(Y/N) : ')
        if c != 'Y' and c != 'y':
            print('\nTry Again.')
            return

        if obj == 'book':
            o = 'b'
        if obj == 'student':
            o = 's'

        command = "SELECT {}no FROM current".format(o)
        cursor.execute(command)
        val1 = cursor.fetchall()
        if len(val1) != 0:
            if obj == 'book':
                print('\nSome books are currently issued to some students.', end='')
                print('\nWe will not delete those records.')
            if obj == 'student':
                print('\nSome students currently hold some books from our library.', end='')
                print('\nWe will not delete those records.')

            c = input('\nDo you now want to continue(Y/N) : ')
            if c != 'Y' and c != 'y':
                print('\nTry Again.')
                return

        command = "SELECT {}no FROM {}".format(o, obj)
        cursor.execute(command)
        val2 = cursor.fetchall()
        for no2 in val2:
            flag = True
            no2 = no2[0]
            for no1 in val1:
                no1 = no1[0]
                if no2 == no1:
                    flag = False
            if flag:
                command = "DELETE FROM {} WHERE {}no='{}'".format(obj, o, no2)
                cursor.execute(command)
                connect.commit()
        print('\n|{}s are accordingly deleted successfully|'.format(obj.capitalize()))

    else:
        print('\nWrong input.Try Again.')
        return


def update(obj):
    if obj == 'book':
        o = 'b'
        no = input('\nEnter the 5 digit Book Number : ')
        if len(no) != 5 or not (no.isdigit()):
            print('\nThis is not a valid Book Number for our database. Try Again.')
            return
    if obj == 'student':
        o = 's'
        no = input('\nEnter the 6 digit Student Number : ')
        if len(no) != 6 or not (no.isdigit()):
            print('\nThis is not a valid Student Number for our database. Try Again.')
            return

    command = "SELECT {}no,{}name FROM {} WHERE {}no='{}'".format(o, o, obj, o, no)
    cursor.execute(command)
    val = cursor.fetchall()
    if val == []:
        print('\nNo such {} to update. Try again.'.format(obj))
        return

    name = val[0][1]

    command = "SELECT {}no FROM current WHERE {}no='{}'".format(o, o, no)
    cursor.execute(command)
    val = cursor.fetchall()
    if val == [(no,)]:
        if obj == 'book':
            print('\nThis book is currently issued to someone. Cannot Update.')
            return
        if obj == 'student':
            print('\nThe student currently holds a book from our library. Cannot Update.')
            return

    if obj == 'book':
        nno = input('\nEnter the new 5 digit Book Number (if necessary, otherwise enter old) : ')
        if len(nno) != 5 or not (nno.isdigit()):
            print('\nThis is not a valid Book Number for our database. Try Again.')
            return
    if obj == 'student':
        nno = input('\nEnter the new 6 digit Student Number (if necessary, otherwise enter old) : ')
        if len(nno) != 6 or not (nno.isdigit()):
            print('\nThis is not a valid Student Number for our database. Try Again.')
            return

    if no != nno:
        command = "SELECT {}no FROM {} WHERE {}no='{}'".format(o, obj, o, nno)
        cursor.execute(command)
        val = cursor.fetchall()
        if val == [(nno,)]:
            print('\nLibrary already holds a {} with this number. Try Again.'.format(obj))
            return

    nname = input('Enter new {} Name : '.format(obj.capitalize()))

    print('\nPlease check the final details : \n')
    print('{} Number : '.format(obj.capitalize()), 'old-> ', no, ', ', 'new-> ', nno,
          '\n{} Name : '.format(obj.capitalize()), 'old-> ', name, ', ', 'new-> ', nname, sep='')

    c = input('\nDo you want to continue with these details(Y/N) : ')
    if c != 'Y' and c != 'y':
        print('\nTry Again.')
        return

    command = "UPDATE {} SET {}no='{}',{}name='{}' WHERE {}no='{}'".format(obj, o, nno, o, nname, o, no)
    cursor.execute(command)
    connect.commit()
    print('\n|{} details updated successfully|'.format(obj.capitalize()))


def disp(obj):
    if obj == 'book':
        o = 'B'
    if obj == 'student':
        o = 'S'

    command = "SELECT * FROM {}".format(obj)
    cursor.execute(command)
    table = cursor.fetchall()
    print('\nDetails of all {}s are as follows : '.format(obj))
    print()
    print('\t', '{}.No.'.format(o), ' ' * 7, '{}.Name'.format(o), sep='')
    for row in table:
        print('\t', row[0], ' ' * (12 - len(row[0])), row[1], sep='')


def issue():
    sno = input('\nEnter the 6 digit Student Number : ')
    if len(sno) != 6 or not (sno.isdigit()):
        print('\nThis is not a valid Student Number for our database. Try Again.')
        return

    command = "SELECT sno FROM student WHERE sno='{}'".format(sno)
    cursor.execute(command)
    val = cursor.fetchall()
    if val == []:
        print('\nNo such student with this Student Number in our record. Try Again.')
        return

    command = "SELECT sno FROM current WHERE sno='{}'".format(sno)
    cursor.execute(command)
    val = cursor.fetchall()
    if val == [(sno,)]:
        print('\nPreviously issued book has not been submitted yet by this student. Please inquire.')
        return

    command = "SELECT sname FROM student WHERE sno='{}'".format(sno)
    cursor.execute(command)
    val = cursor.fetchall()
    sname = val[0][0]

    bno = input('Enter the 5 digit Book Number : ')
    if len(bno) != 5 or not (bno.isdigit()):
        print('\nThis is not a valid Book Number for our database. Try Again.')
        return

    command = "SELECT bno FROM book WHERE bno='{}'".format(bno)
    cursor.execute(command)
    val = cursor.fetchall()
    if val == []:
        print('\nNo such book with this Book Number in our record. Try Again.')
        return

    command = "SELECT bno FROM current WHERE bno='{}'".format(bno)
    cursor.execute(command)
    val = cursor.fetchall()
    if val == [(bno,)]:
        print('\nThis book was already issued to someone else. Please inquire.')
        return

    command = "SELECT bname FROM book WHERE bno='{}'".format(bno)
    cursor.execute(command)
    val = cursor.fetchall()
    bname = val[0][0]

    date = input('Enter the date of issue in format (YYYY-MM-DD) : ')
    if len(date) > 10:
        print('\nWrong format of date. Try Again.')
        return

    print('\nPlease check the details you have entered : \n')
    print('Student Number : ', sno, '\nStudent Name : ', sname,
          '\nBook Number : ', bno, '\nBook Name : ', bname, '\nDate : ', date, sep='')

    c = input('\nDo you want to continue with these details(Y/N) : ')
    if c != 'Y' and c != 'y':
        print('\nTry Again.')
        return

    command = "INSERT INTO current VALUES('{}','{}','{}','{}','{}')".format(sno, sname, bno, bname, date)
    cursor.execute(command)
    connect.commit()

    command = "INSERT INTO history VALUES('{}','{}','{}','{}','{}','{}')".format('issued', sno, sname, bno, bname, date)
    cursor.execute(command)
    connect.commit()

    print('\n|Book issued successfully|')


def submit():
    sno = input('\nEnter the 6 digit student number : ')
    if len(sno) != 6 or not (sno.isdigit()):
        print('\nThis is not a valid Student Number for our database. Try Again.')
        return

    command = "SELECT sno FROM student WHERE sno='{}'".format(sno)
    cursor.execute(command)
    val = cursor.fetchall()
    if val == []:
        print('\nNo such student with this Student Number in our record. Try Again.')
        return

    command = "SELECT sno FROM current WHERE sno='{}'".format(sno)
    cursor.execute(command)
    val = cursor.fetchall()
    if val == []:
        print('\nNo book has been issued to this student. Please inquire.')
        return

    bno = input('Enter the Book Number : ')
    if len(bno) != 5 or not (bno.isdigit()):
        print('\nThis is not a valid Book Number for our database. Try Again.')
        return

    command = "SELECT bno FROM current WHERE sno='{}'".format(sno)
    cursor.execute(command)
    val = cursor.fetchall()
    if val != [(bno,)]:
        print('\nThis is not the Book issued to this student. Please inquire.')
        return

    command = "SELECT sname FROM current WHERE sno='{}'".format(sno)
    cursor.execute(command)
    val = cursor.fetchall()
    sname = val[0][0]

    command = "SELECT bname FROM current WHERE sno='{}'".format(sno)
    cursor.execute(command)
    val = cursor.fetchall()
    bname = val[0][0]

    date = input('Enter the date of submission in format (YYYY-MM-DD) : ')
    if len(date) > 10:
        print('\nWrong format of date. Try Again.')
        return

    days = int(input('Enter the number of days from the date of issue to the date of submission : '))

    print('\nPlease check the details one last time : \n')
    print('Student Number : ', sno, '\nStudent Name : ', sname,
          '\nBook Number : ', bno, '\nBook Name : ', bname, '\nDate : ', date, sep='')

    if days > 15:
        print('\nLate Submission : Student is submitting book after 15 days.')
        print('Fine = Rs.', (days - 15) * 10, 'at the rate of Rs. 10 per day after 15 days.')

    c = input('\nDo you want to continue with these details(Y/N) : ')
    if c != 'Y' and c != 'y':
        print('\nTry Again.')
        return

    command = "DELETE FROM current WHERE sno='{}'".format(sno)
    cursor.execute(command)

    command = "INSERT INTO history VALUES('{}','{}','{}','{}','{}','{}')".format('submitted', sno, sname, bno, bname, date)
    cursor.execute(command)
    connect.commit()

    print('\n|Book submitted successfully|')

#----------------------------------------------------------------------------
main()
#----------------------------------------------------------------------------