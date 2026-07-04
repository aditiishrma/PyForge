# Structuring it using a while loop
option = "YES"
while option == "YES":

# Displaying a menu to the user asking his/her choice

 print("Welcome to one of the most perfect & beginner friendly calculator!")
 print("1.Addition")
 print("2.Subtraction")
 print("3.Multiplication")
 print("4.Division")
 choice=input("Enter the operation you want to perform on the numbers(1-4) : ")
 if choice not in ["1","2","3","4"] :
    print("Invalid Choice!")
    exit()

# Asking for the numbers 
 try :
    num1=float(input("Enter the first number : "))
    num2=float(input("Enter the second number : "))
 except ValueError:
    print("Invalid Input ! Please give a valid number.")
 else :  
    if choice == "1" :
       print("Addition of the two numbers is : ", num1+num2)
    elif choice == "2":
        print("Subtraction of the two numbers is : ",num1-num2)
    elif choice == "3":
        print("Multiplication of the two numbers is : ",num1*num2)
    elif choice == "4":
        if num2 == 0 :
          print("Denominator can't be zero! ")
        else :
            print("Division of the two numbers is : ",num1/num2)
    else :
        print("Please give your choice !")
   
    option=input("Do you want to do another calculation?(YES/NO) : ")
    print("Thank You for using the calculator!")