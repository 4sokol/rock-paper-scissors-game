print ("Hello World")
print ("------------")
#--------------------------
#variables
#--------------------------
num1 = 3
num2 = 5
num3 = num4 = 6
num5, num6 = 8, 9

result_sum = num1 + num2
resulm_min = num1 - num2
resulm_mul = num1 * num2
resulm_slh = num2 / num1

print (result_sum)
print (resulm_min)
print (resulm_mul)
print (resulm_slh)
print (num3)
print (num4)
print (num1, num2, num3, num4)
print (num5, num6)
print ("------------")
#ARG (*) - associates all the values which ar not assigned to other vars, e.g. if
#you want to take only 1st & last values from the values list, then:
z, *x, c = [1, 2, 3, 4, 5]
print (z)
print (x)
print (c)
print ("------------")
#--------------------------
# variables & functions - is the peace of code which runs only if it was called, we define the function with 'def'
# 'inputs' help you to interract with the user

def greeting():
    return 'Hello'

# to call the function you just need to specify the functions name
response = greeting()
print(response)

# dictionary - used to store data in key-value pair, the value could be a variable
dict = {'name': 'Bean', 'color': 'blue', 'variable': choices}

