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

# Split : out put in list : data type would be string for every character
# indexing & slicing
spl = "20-03-2024 14:45"
ine=spl.split(" ")
print(spl.split(" "))
print(type(spl.split(" ")))
print(ine[0])
print(type(ine[0]))

# tranformation

print("=="*20)
print("++"*30)

# slicing

text="Python"
print(text[0])  # extraction of first num
print(text[0:3])  # print from Star to 2nd chracter
print(text[1:4]) # print 1 to 3 rd character
print(text[1:5:2]) # print from 1st character to 4th character, exclude printing after 5th char and from i to 4 it exclude every 2nd charater
print(text[4:])  # print from 4th charater to last character
print(text[::-1])  # print from last character to first charter/ reverce
print(text[-3:-2]) # print left to right not vice versa

# strip : used to remove blanck spaces
print("##"*30)
testy= "   kaila sh ".rstrip()  ## remove white spaces from right
test1= "   kaila sh ".lstrip()  ## remove white spaces from left
test2= "   kaila sh ".strip()   ## remove white spaces from entire string
test3= "###kai#####".strip("#") ## remove specia charater specified in string
print(testy)
print(test1)
print(test2)
print(test3)
print("**"*30)
tett="  abcopl  "
print(len(tett))
print(len(tett.strip()))

print(f"while spaces : {(len(tett) - len(tett.strip()))}")
print(f"No while spaces in tett : {(len(tett) == len(tett.strip()))}")