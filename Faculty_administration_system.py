
## wlecome message
from ctypes.wintypes import DOUBLE
from tkinter.tix import INTEGER


print("\t\twelcome To Faculty Administration System\n") 
## admin list  and student list
admins={"ahmed":11111111,"abdo":22222222,"hazem":33333333}
student={}
## atrbuite function
student_information={}

## add student function
def add_student(name,student_information):
    new_student={name:student_information}
    student.update(new_student)
    print(f"new student list = {student}")

## delete_student function

def delete_student(name):
    student.pop(name)
    print(f"{name} was deleted from student_list")
    print(f"new student list = {student}") 

## Update_student function

def Update_student(name,valuename,newvalue):
    
    student[name][valuename]=newvalue
    print(f"information about {name} was updated")
    print(f"new student list = {student}")

## view_student_info function

def view_student_info(student_name):
    print(f"Welcome {name}\n"+"your id = "+student[student_name]["id"]+"\nyour age = "+student[student_name]["age"]+" Years Old "+"\nyour college is "+student[student_name]["college"])
    print("your Email is "+student[student_name]["email"]+"\nyour Gpa = "+student[student_name]["gpa"]+"\nyour password = "+student[student_name]["password"])

## loop for repeate system
while True:
        
            department=input("""Which department do u want ?
            \n 1-admin \n 2-student \n 3-Exit\n""") 

        ## processing     
            if department=="1":
                     
                
                    admin_name=input("Enter Your Name :- ").strip()
                    if admin_name in admins:
                        try:
                            admin_password=int(input("Enter password :- "))
                            if admin_password==admins[admin_name]:
                                
                                while True:  
                                
                                        dicision=input("""\nwhat do u want ?
                                        \n 1-Add student \n 2-Update on student information\n 3-delete student \n 4- Exit\n""")
                                        if dicision=="1":
                                            try:

                                                name=input("Enter student name :- ").strip()
                                                id=INTEGER(input("Enter student id :- ")).strip()
                                                age=INTEGER(input("Enter student age :- ")).strip()
                                                college=input("Enter student college :- ").strip()
                                                email=input("Enter student email :- ").strip()
                                                Gpa=DOUBLE(input("Enter student Gpa :- ")).strip()
                                                password=input("Enter student password :- ").strip()
                                                add_student(name,{"id":id,"age":age,"college":college,"email":email,"gpa":Gpa,"password":password}) 
                                            except:
                                                print("invaild input")


                                        elif dicision=="2":
                                            upname=input("what is the name u will update ?").strip()
                                            if upname in student:
                                                valuename=input("which valuename will you update ?").strip()
                                                if valuename in student[name]:
                                                    newvalue=input("which newvalue will you added ?").strip()
                                                    Update_student(upname,valuename,newvalue)
                                                else:
                                                    print("The Value Name Is Not In Student List")    
                                            else :
                                                print("The User Name Is Not In Student List ! ")
                                        elif dicision=="3":
                                            delname=input("Enter student name :- ").strip()
                                            if delname in student:
                                                delete_student(delname)
                                            else:
                                                print("The Name Is Not In Student List")
                                        elif dicision=="4":
                                            break  

                                        else :
                                          print("invalid Order ! please try again")                         
                                    


                            else:
                                print("Invalid ! Please Enter The Correct Password ")   
                        except:
                            print("Invalid ! Please Enter The Correct Password")

                    else:
                        print("Invalid ! Please Enter The Correct User_Name ")           
                            
            elif department=="2":
                    student_name=input("Enter Your Name :- ").strip()   
                    if student_name in student.keys():
                        student_password=input("Enter password :- ").strip()
                        if student_password==student[student_name]["password"]:
                            while True:
                                   
                                        dicision=input("""\nwhat do u want ?
                                        \n 1-view your information \n 2-exit \n""")

                                        if dicision=="1":
                                            view_student_info(student_name)

                                        elif dicision=="2":
                                            break   

                                        else :
                                            print("invalid Order ! please try again") 
                                    


                        else: print("Invalid ! Please Enter Password again")            
                    else:
                            print("Invalid ! Please Enter User_Name ")   
            elif department=="3":
                print("\tThank You For Using This System \n`")   
                break          

            else :
                print("invalid Order ! please try again \n")

        


