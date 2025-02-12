def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2



while True:
    print('Calculator')
    print("1: Add")
    print("2: Subtract")
    print("3: Multiplication")
    print("4: Division")
    print("5: Quit")

    option = input("Select your option: 1,2,3,4,5:")

    if option == '5':   #5 is also wrttn as string coz input is strng
        print("Exiting Program...!")
        break  #we used brk so ve to put n a whileloop
    if option in ('1', '2', '3', '4'):
        num1 = float(input("Enter your first no:"))
        num2 = float(input("Enter your second no:"))

        if option == '1':
            print("Result:", add(num1,num2))
        elif option == '2':
            print("Result:", sub(num1,num2))
        elif option == '3':
            print("Result:", mul(num1,num2))
        elif option == '4':
            print("Result:", div(num1,num2))
    else:
        print("Invalid option selected")