# loops are used to iterate over a sequence (like a list, tuple, or string) or to repeat a block of code multiple times.



# for loop : used specific times or over a sequence
# while loop : used infinite time iteration





# for loop example

#it's one of the most powerful tools for repeating tasks.

"""
            for loop syntax

        for variable in iterable :


"""


table_no = int(input("Enter which table u want:="))


for i in range(1,11):
    print(table_no, "*", i ,"=", table_no*i)
    

print("\n") #for new line after completion of code


# example forloop 2

print("=========================\n")
Roll_no = [1,2,3,4,5]


for i in Roll_no:
    print(i)
    
    
    
# while loop — it repeats a block of code as long as a condition is true.




