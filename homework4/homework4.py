#print("Hello,world) # this gave a syntax error because I did not close the parentheses 
#print(name) this gives a name error because the name does not exist and to fix it one would need to define the varible name
#age = "22"
#print (age+1) #this gives a type error becuase the age is listed as a string and not an interger so you cannot add the strong and the integer together.
favorite_foods = ["potatoes", "carrots", "steak", "grapes","tuna"]
print (favorite_foods[1])
print (favorite_foods[-1])
favorite_foods.append("chicken")
print (favorite_foods)
favorite_foods.insert(0,"apple")
print (favorite_foods)
favorite_foods.remove("steak")
print(len(favorite_foods))
for food in favorite_foods: 
    print(food.upper())
#------------------------------------------------------------------------------------------------------------------------------------
first_and_last = favorite_foods[:1] + favorite_foods[-1:]
print (first_and_last)

if "potato" in favorite_foods: 
    print ("A potato!")
else: 
    print ("no potato!")

numbers = list(range(21))

def get_first_15(numbers): 
    return numbers[:15]

def get_every_5th(numbers): 
    return numbers[::5]

def reverse_and_stride(numbers): 
    return numbers[::-1]

print ("numbers", numbers)
print ("first 15",get_first_15(numbers))
print (get_every_5th(numbers))
print (reverse_and_stride(numbers))
#---------------------------------------------------------------------------------------------------------------------------------------
numbers = [[1,2,3], [4,5,6],[7,8,9]]
print (numbers[2])
print(numbers[1][1])
numbers.append([10,11,12])
print(numbers)

def sum_nested(lst): 
    total = 0 
    for row in lst: 
        for num in row: 
            total += num 
    return total

print (sum_nested(numbers))

def make_5x5(): 
    grid = []
    num = 1 
    for i in range(5):
        row = []
        for i in range (5):
            row.append(num)
            num += 1 
        grid.append(row)
    return grid

def replace_multiples(grid):
    new_grid = []
    for row in grid: 
        new_row = [] 
        for i, val in enumerate(new_row): 
            if val % 3 == 0: 
                new_row[i] = "?"
        new_grid.append(new_row)
    return new_grid

def sum_not_qmark(grid): 
    total = 0 
    for row in grid: 
        for val in row: 
            if isinstance(val, int): 
                total += val 
    return total
#----------------------------------------------------------------------------------------------

ages = {"Katie": 30, "Mariam": 42, "Safia": 25, "Mira":48}
print (ages["Katie"])
ages["Mira"] = 100 
ages["Milana"]=52
ages.pop("Mariam")

for name, age in ages.items():
    print(name,age)
