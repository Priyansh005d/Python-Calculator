#PYTHON CALCULATOR

operator = input("Enter a operator(+ - / *) : ")
num1 = int(input("Enter a number : "))
num2 = int(input("Enter another number : "))

if(operator == '+'):
    print(f"{num1}+{num2}={num1 + num2}")
elif(operator == '-'):
    print(f"{num1}-{num2}={num1 - num2}")    
elif(operator == '/'):
    print(f"{num1}/{num2}={num1 / num2}")    
elif(operator == '*'):
    print(f"{num1}X{num2}={num1 * num2}") 
else:
    print("invalid choice") 

print("Thanks for using my Calculator... ")    


        

