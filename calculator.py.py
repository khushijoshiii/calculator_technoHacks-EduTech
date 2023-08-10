#for adding two numbers

def add(x,y):
    return x+y

#for subtracting two numbers

def subtract(x,y):
    return x-y

#for multiplying two numbers

def multiply(x,y):
     return x*y

#for dividing two numbers

def divide(x,y):
    return x/y


print("select operation")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")

while true:
    #user will give input
    choice=input("enter your choice(1/2/3/4):")

    #check if choice is one of the foue options
    if choice in('1','2','3','4'):
        try:
            num1=float(input("enter first number:"))
            num2=float(input("enter second number;"))

        except ValueError:
                print("invalid choice.please enter a valid choice")
                continue
        if choice=='1':
                print(num1,"+",num2,"=",add(num1,num2))
        if choice=='2':
                print(num1,"-",num2,"=",subtract(num1,num2))
        if choice=='3':
                print(num1,"*",num4,"=",multiply(num1,num2))
        if choice=='4':
                print(num1,"/",num2,"=",divide(num1,num2))
                
#check if user want to perform another calculation
#break the while loop if answer is no

        next_calculation=input("lets do next calculation?(yes/no):")
        if next_calculation=="no":
                break
        else:
            print("invalid input")
            
