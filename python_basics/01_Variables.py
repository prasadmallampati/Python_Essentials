# A variable is a name that refers to a value in memory.
# You can store and manipulate data using variables.

#  Rules for variable names:
# - Must start with a letter or underscore (_)
# - Case-sensitive (Name and name are different)
# - Cannot use Python reserved keywords

#  Invalid examples:
# 2name = "Prasad"     # Starts with number
# my-name = "he"      # Contains a dash
# class = "python"       # 'class' is a keyword

#  Valid examples
no = 1                # Integer variable
pi = 3.14             # Float variable
is_alive = True       # Boolean variable
name = "Prasad"       # String variable

# Variables can be reassigned or combined
names = name + " M"

#  Print the variables
print("no:", no)
print("pi:", pi)
print("is_alive:", is_alive)
print("name:", name)
print("names:", names)


# type of variable 

print("type of no:", type(no))
print("type of pi:", type(pi))
print("type of is_alive:", type(is_alive))
print("type of name:", type(name))
print("type of names:",type(names))



# we can read dynamically also using input() ...


input_name =input("Enter your name:= ")



