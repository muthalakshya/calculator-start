# calculator
from art import logo
from replit import clear

# add
def add(a,b):
   return a+b
# sub
def sub(a,b):
    return a-b
#  multiple
def multiple(a,b):
    return a*b
# division
def div(a,b):
    return a/b

operation = {
    "+":add,
    "-":sub,
    "*":multiple,
    "/":div
}
def calculator():
    print(logo)

    a = float( input (" Enter 1st no. "))
    
    
    for operator in operation:
        print(operator)
    operation_performed = input("Pick an operation from the line above ")
    
    b = float( input (" Enter 2nd no. "))
    
    
    performed= operation[operation_performed]
    first_answer = performed(a,b)
    print(f"{a} {operation_performed} {b} = {first_answer}")
    
    condition = True
    
    while condition:
        continue_y_or_n = input(f"Type 'y' to continue calculation with {first_answer} , or type 'n' to start new calculations.:") 
    
        
        if continue_y_or_n=="n":
            condition= False
            clear()
            calculator()
        else:
            operation_performed = input("Pick an operation from the  above ")
            performed= operation[operation_performed]
            c = float(input("What's the next no. "))
        
            second_answer = performed(first_answer,c)
        
            print(f"{first_answer} {operation_performed} {c} = {second_answer}")



calculator()