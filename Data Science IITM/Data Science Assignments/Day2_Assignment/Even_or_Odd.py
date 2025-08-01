'''
creating a function to check weather the argument if even or odd
'''

def check_even_or_odd(number):
    try:
        if number%2==0:
            return "Even"
        elif number%2!=0:
            return "Odd"
        else:
            return "Invalid number"
    except Exception as e:
        print(e)
num=int(input("Enter a number:"))
result=check_even_or_odd(num)
print(f"{num} is an {result} number.")