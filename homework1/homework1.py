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
print (bool("")) # Flase, This is also an empty value 
print (bool(" ")) # true the space acts as a non empty value when used in the quotations
print (bool(())) # nothing in the parentheses acts as an empty value 
print (bool([])) # same as above false means nothing in the parentheses
print (bool({})) # False, it has no value or space in the parentheses 
print (bool(True and False)) # this is false because both statements must be true to be True 
print (bool(True and True)) # this is True because both statements are true 
print (bool(False and False)) # this is False both statements are False
print (bool(True or False)) # This prints true because of the or operator which prints true if at least one of the expressions is true
print (bool (True or True)) # both are true so it returns true 
print (bool (False or False)) # both are false so it returns false 
print (bool(not(False))) # not effectively flips the operator so in this case the line reuturns true 
print (bool(not(True))) # same as above the not operator flips from true to false 

# 1. This shows that bool will return a false or True response when the expressions are true or there is a non empty value in the command line
# 2. The expressions with empty commands returning false were the most suprising becuase it doesnt seem like that would return false but it makes a lot of sense. 
# 3. print (bool (524)) will reuturn true becuase the expression is a value and isnt an empty expression 
# 4. print (bool (10>3 and False)) not both statements are true so it will return false

print (10 + 5) # 15, the + preforms addition 
print (10 - 5) # 5, the - preforms subtraction 
print (2*4) # 8, the * performs multiplication 
print (6/3) # 2.0, the / performs division 
print (5 % 2) # 1, the percent sign performs the modulo and gives the remainder after division so 5 = 2*2 +1 
print (3**2) # 9, the ** is like a power operator 
print (15 // 2) # 7, this is floor division so it divides and drops the decimal so the .5 is dropped in this case. 
print ( 5 == 2 ) # false because 5 is not equal to 2 
print ( 10 != 10) # false because the command means not equal to and 10 is equal to 10 
print (2<5) # True because 2 is less than 5 
print (12 > 5) # true 
print (5<= 6) # true 5 is less than or equal to 6 
print ( 1>= 10) # false one is not greater than nor equal to 10 

# x = 5 
# print ( x += 5)
# print ( x -+ 4 )
# print (x *= 3 )
# all return invalid syntax and dont preform a function due to this 

# 1. and checks if both of the varriables are true for instance True and True returns true because both are true where True and False would return false because not both are true 
# 2. or is different where only one of the variables has to be true so for instance True and False would be Ture and False and False would be false. 
# 3. Not flips the script here, so a not false would return true and a not true would return false. 

#More Questions

# The difference between / which preforms regular division and // which preforms floor division and essentially drops the decimal or rounds down to the nearest whole number. 
# % and // differ because the % operator gives you the left overs in a way like if you need one more number to acieve the value like we did above it would return 1 or any other that is needed and not apart of the division where floor division just rounds down to the lowest number 
# For this you would use the % remember this gives the remainder of the division 
# for assignemnt variables printing the ones above gave a syntax error but if you arent printing and just do what is posted it essentially will preform the action on that variable and then assign the new value to that variable so like x += 5 would be equivalent to writing x = x +5

my_string = "hello" 
print (my_string)
print (my_string[0]) # first place value so therefore that would be h 
print (my_string[1]) # e 
print (my_string[2]) # l 
print (my_string[3]) # l 
print (my_string[4]) # o 
print (my_string[-1]) # prints the last value of the string 
print (my_string[1:3]) # prints one and two therefore it shows el 
print (my_string[ 0:5:2 ]) # this prints 0 to 5 or the last place but skips every two so it gives h l o 
print (len(my_string)) # there are 5 characters in the string 
print (my_string + "goodbye") # gives the two pasted together with no space in the middle 
print (my_string * 7) # now there are 7 hellos printed on the terminal 

# Questions 
# 1. Slicing is taking a piece using out of things like things using [start:stop:step]
# 2. 
# name = "Oski"
# print (f"Hello, my name is {name}")
# this essentially calls the name into the strong using a function 
# 3. 
#name = "Oski"
#print (f"Hello, my name is {name}")
# same as above but name in the strong and in the parentheses are different 
# 4. f strings build strings by embedding variables or expressions directly inside them. f before the quotes calls the fucntion using the {} to insert the variable 

#3.5 terminal commands 
# 1. you can comment out a command using a # and this makes it not contribute to the code any more 
# 2. you can use it using the # to comment out any command that you may need to use 
# 3. You can use # to help to define what you are coding and keep organization in your code 
# 4. I tried it out it is very similar 

# cd is call directory and it is how you call into a directory, example is if you are in user quinn and you want to open homewokr 1 folder you cd homework1 
#ls lists the folder within the directory, to use it you would just type ls and it will show you all the possible files and folders in your current directory 
# la -a shows everything including the hidden files and folders like ones that start with a dot. you just type ls -a and it will show you these folders 
# mkdir means make directory, it will allow you to make a directory in the directory you are currently in. exmple would be mkdir homework1 
# cat prints a files contents into the terminal. to use you would put cat and the file name to see the contents of that file 
# pwd means print working directory and will show you the current path you took to your directory. so if you need to know how you got to the directory pwd will show you this path 
# cd .. allows you to go back one directoy to its parent folder or directory. so if you need to leave one directory and access another you would use cd ..
#cd . allows you to go into the current directory. essentially just a command that would allow you to access the directory you are currently in 
# cd ~ will take you all the way back to the home parent directory. in most cases this may be the general folder on your computer like downloads or all of your file explorers 
# cp is used to coppy any file or folder in you directory. to use it you call cp then the folder and it will coppy then you can use other commands in order to coppy into other folders etc, 
# mv is used to move and or rename a file. you would use it by typing mv the folder name and then either the new folder name or an existing folder you want to move into 
# rm is used to remove or delete files and folders, it is permenent so once you call it with the file name after you wont be able to get that file or folder back 
# clear essentially clears your screen. it is used if you get junky in the terminal and want to make it look better to do work and clear all the BS you have before the current line of code 
# grep is used like command s to search for tect in specific files. to use it you call grep "something" then the file name 

# questions
#1. touch is used to create a new empty file similar to nano or others, you can also use echo to print any text into the perminal or overwrite a file with tect you just call the function and then include the text afterwards, finally you can use head or tail to look into the beginning or end of a file, this can be super helpful in identifying what files are which especially for very large files. 
#2. ls and ls -a differ because ls -a will show you hidden files or folders that ls would not show you 
#3. a hidden file is not shown by default by the terminal or system the names typically start with a . in front of them and are hiddent in your computers settings becuase you dont open them all the time 
#4.  -l is for long format and it shows basically a more detailed list of the files and their specs, -r is used with cp and others and it tells the command to work through the directories so if you want to coppy a folder and everything inside of it or if you want to look for a specific word in every file within a directory, -i is used for safety and it will propt you before overwriting or moving something especially with comands like rm or mv 































