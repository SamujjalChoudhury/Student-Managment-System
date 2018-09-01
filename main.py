import sMod as s

fp = open('data.txt','r')

temp = fp.readlines()

for i in range(len(temp)):
    temp[i] = temp[i].replace('\n','')



for i in range(0,len(temp), 9):
    s.name.append(temp[i])
    s.roll.append(int(temp[i+1]))
    s.branch.append(temp[i+2])
    s.sem.append(int(temp[i+3]))
    s.sub1.append(int(temp[i+4]))
    s.sub2.append(int(temp[i+5]))
    s.sub3.append(int(temp[i+6]))
    s.sub4.append(int(temp[i+7]))
    s.sub5.append(int(temp[i+8]))


#calling of function s.calGrade which calculates the grades of the student
s.calGrade()


#begining of the system
s.frontPage()
