# File: homework1. py 
#--- Variables and Data Types ---
a = 10 
print (a)
print(type(a)) # a is an interger, whole number with no decimal 

b=1.5 
print (b) 
print(type(b)) # b is float, or a fractional number 

c= 3j 
print (c)
print(type(c)) # c is complex, or a number with both real and imaginary parts

d = "hello"
print(d)
print(type(d)) # d is a string, or a quoted word or letters

e = [1,2,3]
print (e) 
print(type(e)) # e is a list, a mutable ordered senquecne of elements

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print (f)
print(type(f)) #a dictoonary type is a data type that stores a collection of items in key-value pairs. 

g = (1,2)
print(g) 
print(type(g)) # g is a tuple, or a variable to store multiple items

h = ["apple", "banna", "strawberry"]
print (h) 
print(type(h)) # h is a list similar to e but it doenst have to be numbers 

i = True 
print (i) 
print(type(i)) # i is a bool or boolian, used ot represent true or false 

j = None 
print (j)
print(type(j)) # j is NoneType, which is used for the constant none. represents tha basence of a value or a null value

k = [True, "blue", 12]
print (k) 
print(type(k)) #k is still a list like before doesnt matter what values are in the corresponding list

l = str(14)
print (l)
print(type(l)) # a string is a data thype the stores numbers, variables, letters or characters. 

m = 1e4
print (m) 
print(type(m)) # m is a float used to represent real numbers with fractional components e i think acts as a base 10 like on a calucaltor. 

# 1. it looks like I found 9 different data types
# 2. interger, float, complex, string, list, dict, tuple, bool, nonetype 
# 3. f,h,k are all lists, and b and m are floats.
# 4. l was a string which is not an interger becuase it is actually storing that number as text kinda like the quoted things we would do
# 5. a set is written with curly brackets for example x = {"apple", "banna", "cherry"} and its purpose it to stroe an unordered collection of unique items. 

print (10 > 9) # true 10 is greater than 9 
print (10 == 9 ) # flase becuase 10 does not equal 9 
print (10<=9) # flase 10 is not less than or equal to 9 
print (bool("abc")) # true because abc is not an empty statement nor is it zero
print (bool(123)) # again like I said this is not an emptry value so it is true 
print (bool(["apple","cherry","banna"])) # True again because a string is not an empty value 
print (bool(True)) # True is not an empty value either 
print (bool(False)) # False is not a truthy value so it is considered an empty value is this case which is what bool is looking for in order to print false 
print (bool(0)) # False, 0 is an empty value so it returns false. 













