#  Lists, dictionaries, and operations

# list is mutable 

"""
List Methods Summary
Method	    Description                          Syntax                      Example 
append()	Add item to end                     var.append(value)           l1.append(6)
insert()	Add item at index                   var.insert(index,value)     l1.insert(0,0)
remove()	Remove by value                     var.remove(value)           l1.remove(6)
pop()	    Remove last / index item            var.pop() /var.pop(index)   l1.pop()/l1.pop(4)
sort()	    Sort list                           var.sort()                  l1.sort()
reverse()	Reverse order                       var.reverse()               l1.reverse()
len()	    Get length of list                  len(var)
clear()	    Remove all items
    
"""


l1 = [1,2,3,4,5]



print("initial list values:-",l1)



# append method 

l1.append(6)  # at end 

print("after append updated values are:=",l1)


# index 
# var.insert(index,value)




l1.insert(0,0)


print("after insert updated values are:=",l1)


# remove

l1.remove(6)

print("after remove updated values are..=",l1)

# pop 

l1.pop()

print("after pop updated values are...",l1)

# reverse 

l1.reverse()
print("after reverse updated values are..",l1)
# sort 

l1.sort()

print("after sort values are...")

# len

print("length of l1=",len(l1))

# clear()



print("before clearing list updated values are..",l1)

l1.clear()
print("before clearing list updated values are..",l1)


print("\n\n")
# DICTIONARY is also mutable — holds key-value pairs

"""
Dictionary Methods Summary

Method      Description                          Syntax                           Example
get()       Access value by key                  dict.get(key)                    person.get("name")
update()    Update or add key–value              dict.update({key: value})        person.update({"age": 25})
pop()       Remove item by key                   dict.pop(key)                    person.pop("role")
keys()      Get all keys                         dict.keys()
values()    Get all values                       dict.values()
items()     Get key-value pairs                  dict.items()
clear()     Remove all items                     dict.clear()
"""


d1 = { "name" : "prasad",
    "role" : "python dev",
    "age" : 23}



# get 

print("initial d1 values=",d1)

print("after get updated values=",d1.get("name"))



# update


d1.update({"age":22})


print("after updated age now d1=",d1)



# pop 


d1.pop("role")


print("updated values after pop role:",d1)


# key

print("d1 keys are...:",d1.keys())

# values

print("d1 values are...:",d1.values())

# item (key and values)

print("items are ",d1.items())


# clear 

print("before clear d1=",d1)


print("after clear d1=",d1.clear())




# list comprehension 
"""
[expression for item in iterable if condition]
    
"""

lc = [i**2 for i in range(10) if i%2==0]


print("Even squares",lc)




# dict comprehension

"""
{key_expression: value_expression for item in iterable if condition}
    
"""


dc  = {i : i**2 for i in range(1,10) if i%2!=0}


print("odd squares",dc)