from sqlalchemy import create_engine,MetaData,Table,Column,Integer,String,Float

from sqlalchemy.orm import registry, sessionmaker

DB_URL = 'mysql://root:root@localhost:3306/sqlalchemy1'

ENG = create_engine(DB_URL)

class Student():
    def __init__(self,roll,name,marks):
        self.roll=roll
        self.name=name
        self.marks=marks

    def __str__(self):
        return f'{self.roll}  {self.name}  {self.marks}'
    
md=MetaData()

tb = Table('stu', md,
           Column('roll', Integer , primary_key=True),
           Column('name', String(20)),
           Column('marks', Float),
           )
           
reg_obj = registry()

reg_obj.map_imperatively(Student,tb)

#md.create_all(ENG)
#print("table created")

session = sessionmaker(bind=ENG)
sess=session()

def conformation():
    user_roll=int(input("enter roll number:"))
    student=sess.query(Student).filter(Student.roll==user_roll)
    try:
        data=student.one()
    except:
        print("enter valid roll number")
        return False
    else:
        return student
    

def add_student():
    roll=int(input("enter your roll:"))
    name=input("enter your name:")
    marks=float(input("enter marks here:"))
    obj=Student(roll=roll,name=name,marks=marks)
    sess.add(obj)
    sess.commit()
    print("student added")

    
def show_student():
    data=sess.query(Student)
    for student in data:
        print(student)

def update_student():
    result=conformation()
    if result:
        ch=int(input("enter choice\n"\
                     "1.update name\n"\
                     "2.update marks"))
        match ch:
            case 1:
                newname=input("enter new name:")
                result.update({Student.name:newname})

            case 2:
                newmarks=float(input("enter new marks:"))
                result.update({Student.marks:newmarks})
        print("record updated")

def delete_student():
    result=conformation()
    if result:
        result.delete()
        print("record deleted")
                
    

while True:
    ch = int(input("enter choice:\n"\
                   "1.add student\n"\
                   "2.show student\n"\
                   "3.update student\n"\
                   "4.delete student\n"\
                   "5.exit"))
    match ch:
        case 1:
            add_student()

        case 2:
            show_student()

        case 3:
            update_student()

        case 4:
            delete_student()

        case 5:
            print("existing.....")
            break

        case _:
            print("invalid choice...")
        
sess.close()            
