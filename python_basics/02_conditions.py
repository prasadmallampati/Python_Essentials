# they let  you execute only if certain condition are true 

# if
#else
#elif 


# example of if 
age = 18
if age>=18:
    print(f"age if {age} eligible for  voting...")

    
    


# example of if and else 
age = int(input("Enter your age:="))


if age>=18:
    print(f"age if {age} eligible for  voting...")
else:
    print(f"wait for  {18-age} years cast your vote")



# example  for if - elif - else



marks  = int(input("Enter Your marks...= "))



if marks>=90:
    print("Grade A ")
elif marks>=80:
    print("Grade B")
    
elif marks>=70:
    print("Grade C")
    
elif marks>60:
    print("Grade C")
elif marks>=50:
    print("Grade D")
    
elif marks>=40:
    print("Grade E")
    
else:
    print(f"Fail u need {40-marks} to pass the  exam..")