import os

#initialisations of all the lists
name = []
roll = []
branch = []
sem = []
sub1 = []
sub2 = []
sub3 = []
sub4 = []
sub5 = []
grade = []



#initialisation of a dictionary
mark = {'a':90, 'b':'80', 'c':70, 'd':50, 'e':30, 'f':0}



#defination of function calGrade which calculates the grades of the students
def calGrade():
    global sub1
    global sub2
    global sub3
    global sub4
    global sub5
    global grade
    for i in range(len(sub1)):
        grade.append((int(sub1[i])+int(sub2[i])+int(sub3[i])+int(sub4[i])+int(sub5[i]))//5)




#defination of function topper which prints the roll numbers and names of the students of the wanted grade
#and the the starting percentage of every grades should be passed
def topper(g):
    #calGrade()
    temp = []
    if g==90:
        for i in range(len(grade)):
            if grade[i]>=90:
                temp.append(i)

    elif g==80:
        for i in range(len(grade)):
            if grade[i]>=80 and grade[i]<90:
                temp.append(i)

    elif g==70:
        for i in range(len(grade)):
            if grade[i]>=70 and grade[i]<80:
                temp.append(i)

    elif g==50:
        for i in range(len(grade)):
            if grade[i]>=50 and grade[i]<70:
                temp.append(i)

    elif g==30:
        for i in range(len(grade)):
            if grade[i]>=30 and grade[i]<50:
                temp.append(i)

    else:
        for i in range(len(grade)):
            if grade[i]<30:
                temp.append(i)

    if len(temp)==0:
        print("\nNo result found")
        return
    print("Roll Number\t\t\t\t\tName")
    print("============\t\t\t\t=====\n")
    for i in range(len(temp)):
        print(roll[temp[i]],'\t\t\t\t\t\t   ',name[temp[i]])





#defination of the function search which basically searches for the student with the given roll number
def search(a):
    flag = 0
    for i in range(len(roll)):
        if roll[i]==a:
            flag = 1
            break

    if flag == 1:
        print("\nName : ",name[i])
        print("Roll Number : ",roll[i])
        print("Branch : ", branch[i])

    else:
        print("No result found")





#defination of function pageOne which handles if the input from the frontPage is '1'
def pageOne():
    os.system('cls')
    temp = input("Enter the roll number of the student you are looking for : ")
    if temp.isdigit():
        search(int(temp))
    else:
        print("Wrong input. Try again\n\n")
        pageOne()
    input("\n\n\n\n\nPress enter to goto the main menu")
    frontPage()




#defination of function pageTwo which handles if the input from the frontPage is '2'
def pageTwo():
    os.system("cls")
    global mark
    grd = input("Enter the grade you want to check for (A/B/C/D/E/F) : ")
    if grd.isalpha():
        grd.lower()
        if grd=='a' or grd=='b' or grd=='c' or grd=='d' or grd=='e' or grd=='f':
            topper(int(mark[grd]))
        else:
            print("Wrong input. Try again")
            pageTwo()
    else:
        print("Wrong input. Try again")
        pageTwo()
    input("\n\n\n\n\nPress enter to goto the main menu")
    frontPage()



#defination of the function frontPage which is nothing but the default page
def frontPage():
    os.system('cls')
    print("Welcome to student managment system\n===================================\n")
    print("1. Search for student\n2. List of students of a particular grade\n3. Exit\n")
    temp = input("Enter your choice(1/2/3) : ")
    if temp == '1':
        pageOne()
    elif temp == '2':
        pageTwo()
    elif temp == '3':
        exit(0)
    else:
        print("Wrong input. Try again\n\n\n")
        frontPage()

