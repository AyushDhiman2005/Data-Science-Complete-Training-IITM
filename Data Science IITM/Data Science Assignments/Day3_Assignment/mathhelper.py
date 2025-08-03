'''
1. prime check
2. factorial
3. fibonacci
'''

def prime_check(number):
    #importing math module to use sqrt function
    import math as m

    #There is no need to traverse till the n-1 value as the factors repreat after square root

    try:
        if number==2 or number==3:
            return True
        elif number==1 or number==0:
            return False
        

        else:
            start_value=2
            stop_value= int(m.sqrt(number) +1)
            for i in range(start_value,stop_value):
                if number%i==0:
                    return False
            return True
    except Exception as e:
        return e
        
def factorial(n): 
    '''
    factorial function returns the factorial value
    '''
    #First checking weather the number is negative integer or not
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    #handling 0,1,2 cases
    if n==1 or n==0:
        return 1

    else:
        if n>100:
            #if number exceeding 100 then, using iterative approach
            result=1
            for i in range(2,n+1):
                result=result*i
            return result
        
        else:
            #otherwise using recursive approach
            return n * factorial(n-1)

 


def prime_list(number_range):
    '''
    This function returns a list of the prime numbers till the given range
    '''
    myList=[]
    for i in range(number_range):
        if prime_check(i)==True:
            myList.append(i)
    return myList


def fiboList(n):
    try:
        if n==1:
            return [0]
        elif n==2:
            return [0,1]
        else:
            mylist = [0,1]
            for i in range(n-2):
                mylist.append(mylist[-1] + mylist[-2])
            return mylist
   

    except Exception as e:
        return e

print(fiboList(-15))