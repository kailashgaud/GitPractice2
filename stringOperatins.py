name = "kailash"
age = 24
print( type(name))
print(type(age))
print("Your name is " + name +"  and age is " + str(age))

print(len(name))

if len(name) < 5:
    print("Name is short")
else:
    print("Name is sufficient")
## count function
text1= """
I love Python
I am Python
Are u python
"""

print(text1.count("python"))

## Replace : replacing string values/ char

abc= "23/90/2089"
print(abc.replace("/","-"))

cd= "kai$hai$"
print(cd.replace("$",""))

phno= "+49 (186) 123-4568"
print(phno.replace("+","00").replace(" ",""
).replace("-","").replace("(","").replace(")",""))

#f formating

s1="kailash"
s2=32
is_married=True
print(f"My name is {s1} and my age is {s2} and my martial status is married {is_married}")
print(f"{{this is me}}")
print(f"2+6 = {2+6}")

