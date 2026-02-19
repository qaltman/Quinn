name = "Quinn"
def say_goodbye(name): 
    print ("goodbye,",name)
say_goodbye(name)

def Circle_area(radius): 
    pi = 3.14 
    area = (pi * radius**2)
    print (area)

radius = 4 
Circle_area(radius)

def subtract(a,b):
    return a - b 

def multiply(a,b):
    return a * b 

def divide(a,b):
    return a/b

a=4
b=2

print (subtract (a,b))
print (multiply (a,b))
print (divide (a,b))

def wardrobe_calc(readings): 
    return (min(readings),max(readings))

readings = [15,14,17,20,23,28,20]
print (wardrobe_calc(readings))

def is_weekend(day): 
    if day == 6 or day == 7:
        return "It's the weekend!"
    else: 
        return "it's not the weekend!"
    
day = 7
print (is_weekend(day))

def fuel_efficency(miles, gallons):
    return miles/gallons

miles = 50 
gallons = 12 
print (fuel_efficency(miles, gallons))

def encrypt(n): 
    last = n % 10 
    rest = n // 10 
    return int(str(last)+str(rest))

print (encrypt(12345))

def power (x,y): 
    result = 1 
    for i in range (y): #multiplys the x varriable by itself y amount of times
        result *= x 
    return result 
print (power(2,16))

def min_find(nums): 
    m = nums[0] #index from the firsst value 
    for n in nums: 
        if n<m: 
            m=n
    return m 

print(min_find([8,5,6]))

def max_find(nums): 
    m = nums[0] #index from the firsst value 
    for n in nums: 
        if n>m: 
            m=n #index through values until you find one that is greater than the one before and that becomes the value then restarts until you find the greatest value. 
    return m 

def min_while(nums): 
    m = nums[0] #sets m to be the first element of the list 
    i = 0 #creates index varriable i starting at 0 or the first position in this list
    while i < len(nums): # starts a loop that runs as long as i is a valid index len is the number of items in the list so it keeps looking until we have reached every element. 
        if nums[i] < m: #looks at current element and if it is smaller than current minimum m, then we found a new smaller value 
            m = nums[i] # updates m to the smaller value 
        i += 1 #increases i by one so the loop moves to the next element 
    return m # after loop fininshes we know that m hold the smallest value found. 

# print (min_while([1,3,5,6,2]))
def max_while(nums): 
    m = nums[0] #sets m to be the first element of the list 
    i = 0 #creates index varriable i starting at 0 or the first position in this list
    while i < len(nums): # starts a loop that runs as long as i is a valid index len is the number of items in the list so it keeps looking until we have reached every element. 
        if nums[i] > m: #looks at current element and if it is larger than current minimum m, then we found a new smaller value 
            m = nums[i] # updates m to the larger value 
        i += 1 #increases i by one so the loop moves to the next element 
    return m # after loop fininshes we know that m hold the smallest value found. 
print(max_while([1,3,4,7,9]))


def int_sum(value): 
    sum_digits = 0 
    while value > 0: 
        sum_digits += value % 10 
        value //= 10 
    return sum_digits 

print (int_sum(2468))