###TASK: Input then execute the following expressions (note: you will have to re-enter each expression separately). Ensure you understand each operator and the result produced.

def calculator():
    while True:
        operation=input("please enter operation : ")
        print(eval(operation))
        again=input("are ypu sure to continue:yes/no : ").lower()
        if again !="yes":
            break

if __name__=="__main__":
    calculator()

