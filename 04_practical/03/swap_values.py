a = 47
b = 85

# swap without temp keyword
# print(f"Before A is {a} B is {b}")
# a,b = b, a
# print(f"After A is {a} B is {b}")
                
# swap using temp 
print(f"Before A is {a} B is {b}")        
temp = a
a = b
b = temp
print(f"After A is {a} B is {b}")