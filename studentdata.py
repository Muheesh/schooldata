import sqlite3
from prettytable import PrettyTable
data = sqlite3.connect("school.db")
table = data.execute("select name from sqlite_master where type='table' and name='student'").fetchall()
if table!=[]:
    print("Table already created.")
else:
    data.execute('''create table student(
                            sname text,
                            rollno integer,
                            admno integer,
                            examname text,
                            eng integer,
                            math integer,
                            phy integer,
                            chem integer,
                            bio integer );''')
    print("Table created")

while True:
    print("Select an option from the given list")
    print("1.Add student data")
    print("2.View all students data")
    print("3.Search a student using their partial name")
    print("4.Search a student using Admisiion number or Rollnumber")
    print("5.Update a student using Admission number")
    print("6.Delete the  student data using Admission number")
    print("7.Display the topper student in physics")
    print("8.Display the total number of students")
    print("9.Display the average marks in english")
    print("10.Display the students who scored below average marks in mathematics")
    print("11.Display the students scored above average in chemistry")
    print("12.Exit")

    a=int(input("Enter the choice to be executed"))

    if a==1:    #add
        getSname = input("Enter the student name:")
        getRollno = input("Enter the rollnumber:")
        getAdmno = input("Enter the Admission number:")
        getExamname = input("Enter the examination name:")
        getEng = input("Enter the marks secured in English:")
        getMat = input("Enter the marks secured in mathematics:")
        getPhy = input("Enter the marks secured in Physics:")
        getChe = input("Enter the marks secured in Chemistry:")
        getBio = input("Enter the marks secured in Biology:")
        data.execute("insert into student (sname,rollno,admno,examname,eng,math,phy,chem,bio) \
        values('"+getSname+"',"+getRollno+","+getAdmno+",'"+getExamname+"','"+getEng+"','"+getMat+"','"+getPhy+"',\
        '"+getChe+"','"+getBio+"')")
        data.commit()
        print("Added student data successfully")
    elif a==2:    #view
        result=data.execute("select * from student")
        table = PrettyTable(["Studentname","Rollno","AdmnNo","Examname","Englishmark","Mathsmark","Physicsmark","Chemistrymark","Biologymark"])
        for i in result:
            table.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]])
        print(table)
    elif a==3:   #search
        getSname = input("Enter the partial name of the student:")
        result=data.execute("select * from student where sname like '%" + getSname + "%'")
        table = PrettyTable(["Studentname", "Rollno", "AdmnNo", "Examname", "Englishmark", "Mathsmark", "Physicsmark", "Chemistrymark","Biologymark"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]])
        print(table)
    elif a==4:   #search
        getAdmno = input("Enter the admission number:")
        getRollno = input("Enter the rollnumber:")
        result = data.execute("select * from student where admno="+getAdmno+" or rollno ="+getRollno)
        table = PrettyTable(["Studentname", "Rollno", "AdmnNo", "Examname", "Englishmark", "Mathsmark", "Physicsmark", "Chemistrymark","Biologymark"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]])
        print(table)
    elif a==5:  #update student
        getAdmno = input("Enter the admission number:")
        getSname = input("Enter the new student name:")
        getRollno = input("Enter the new rollnumber:")
        getExamname = input("Enter the new examination name:")
        getEng = input("Enter the new marks secured in English:")
        getMat = input("Enter the new marks secured in mathematics:")
        getPhy = input("Enter the new marks secured in Physics:")
        getChe = input("Enter the new marks secured in Chemistry:")
        getBio = input("Enter the new marks secured in Biology:")
        data.execute("update student set sname='"+getSname+"',rollno="+getRollno+",examname='"+getExamname+"',eng="+getEng+",\
                math="+getMat+",phy="+getPhy+",chem="+getChe+",bio="+getBio+"")
        data.commit()
        print("updated student details successfully")
    elif a==6: #delete student
        getAdmno = input("Enter the admission number to be deleted:")
        data.execute("delete from student where admno="+getAdmno)
        data.commit()
        print("Deleted successfully")
    elif a==7:
        result=data.execute("select max(phy) as phy from student")

        for i in result:
            print("Marks",i[0])
    elif a==8:
        result = data.execute("select count(*) as count from student")
        for i in result:
            print("Total students:",i[0])
    elif a==9:
        result = data.execute("select avg(eng) as eng from student")
        for i in result:
            print("average",i[0])
    elif a==10:
        result=data.execute("select * from student where math< (select avg(math) as math from student)")
        table = PrettyTable(["Studentname", "Rollno", "AdmnNo", "Examname", "Englishmark", "Mathsmark", "Physicsmark", "Chemistrymark","Biologymark"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]])
        print(table)
    elif a==11:
        result=data.execute("select * from student where chem>(select avg(chem) as chem from student)")
        table = PrettyTable(["Studentname", "Rollno", "AdmnNo", "Examname", "Englishmark", "Mathsmark", "Physicsmark", "Chemistrymark","Biologymark"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]])
        print(table)
    elif a==12:
        data.close()
        print("Exited")
        break
    else:
        print("Invalid selection reconsider!")







