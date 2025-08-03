'''
A calculator that handles division by zero
Handle invalid input gracefully
Use try-except blocks

'''

def numerical_input():
    try:
        num1=float(input("Enter first number:"))
        num2=float(input("Enter second number:"))
        return num1,num2
    except Exception as e:
        print(e)
        return 0.0,0.0

def operator_choice():
    choice=input('''
1. Addition:  + 
2. Subtraction: -
3. Multiplication: *
4. Division: /
                 
Enter your choice: ''')
    return choice

def calculator(a=0,b=0,choice=''):
    if a==0 and b==0:
        a,b=numerical_input()
    choice=str(choice)
    if choice=='':
        choice = operator_choice()
    if '+' in choice:
        return a+b
    elif '-' in choice:
        return a-b
    elif '*' in choice:
        return a*b
    elif '/' in choice:
        try:
            return a/b
        except Exception as e:
            print(f"Error : {e}")
            return "oo"    


number1 = 15
number2 = 20
number3=0

print(f"{number1} + {number2} = {calculator(number1,number2,'+')}")

print(f"{number1} / {number3} = {calculator(number1,number3,'/')}")

