'''
We know the formula for factorial

n! = n*(n-1)!

ex: 5! = 5 * (5-4)! = 5 * 4!
'''

def factorial(number):
    if number==0 or number==1:
        return 1
    else:
        result = number * factorial(number-1)
        return result
    
num = int(input("Enter a number:"))
print(f"{num}! = {factorial(num)}")