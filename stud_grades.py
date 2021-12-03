def grade(s):
    if(91<=s<=100):
        g=10
    elif(81<=s<=90):
        g=9
    elif(71<=s<=80):
        g=8
    elif(61<=s<=70):
        g=7
    elif(51<=s<=60):
        g=6
    elif(41<=s<=50):
        g=5
    return g
def calGPA(num):
    s1=int(input("enter subject1 marks:"))
    s2=int(input("enter subject2 marks:"))
    s3=int(input("enter subject3 marks:"))
    s4=int(input("enter subject4 marks:"))
    s5=int(input("enter subject5 marks:"))
    s6=int(input("enter subject6 marks:"))
    c1=int(input("enter subject1 credit:"))
    c2=int(input("enter subject2 credit:"))
    c3=int(input("enter subject3 credit:"))
    c4=int(input("enter subject4 credit:"))
    c5=int(input("enter subject5 credit:"))
    c6=int(input("enter subject6 credit:"))
    if((s1>100 or s1<0) or (s2>100 or s2<0) or (s3>100 or s3<0) or (s4>100 or s4<0) or (s5>100 or s5<0) or (s6>100 or s6<0)):
        print(" Enter correct marks!!!")
    elif((41<=s1<=100) and (41<=s2<=100) and (41<=s3<=100) and (41<=s4<=100) and (41<=s5<=100) and (41<=s6<=100)):
        gpa=(grade(s1)*c1+grade(s2)*c2+grade(s3)*c3+grade(s4)*c4+grade(s5)*c5+grade(s6)*c6)/(c1+c2+c3+c4+c5+c6)
        print(gpa)
    else:
        print("FAIL")
students=[]
stud_gpa={}
lower=int(input("enter first num in class:"))
upper=int(input("enter last num in class:"))
for i in range(lower,upper+1):
    print("HI",i)
    print(calGPA(i))
