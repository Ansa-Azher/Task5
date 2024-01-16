
#    **********Pseudo-code*********
#This is the pseudo-code is for two financial calculator:an investment calculator and a home loan repayment calculator
#It will first show the user a small menu where user will choose an option what they want to do either they want to use  calculator for investment money or
#for home loan repayment

#If user choose investment, the program will take the user to investment plan 
#Where user will be asked about to enter some information to perform calculation

#For investment program have two investment types 'simple' or 'compound'

#If user choose simple investment plan it will calculate the simple investment plan and display the interest with the simple investment
#(simple interest is continually  calculated on intial amount invested and calculated only once in a year. This interest amount is than added to the intial 
#amount that you invested known as principal amount)

#If user choose compound investment option than it will calculate compound investment interest rate (Compound interest rate is different:
#in that the interest is calculated on the current total known as the accumulated amount)and show to the user as output

#Or if user choose bond option, than it will take to home loan repayment plan 
#Where program will ask user to input some information to calculate home loan and display the user home loan repayment interest rate

#python file added to perform calculation
import math

# Print function is used to display the menu to user to choose option 
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

# check variable will save information that user will choose from menu
check=input("Enter either 'investment' or 'bond' from the above menu to proceed:")

# lower() fuction is used to conver user input into lower aplhabets as user will not feel hesitate about case senstivity 
check1=check.lower()

#if control structure is used to compare the user input with the 'investment' , if it matches with the user input it will perform calculation for investment plan
if (check1 == "investment"):
    
    #Here it will take  the money to deposit, interest rae as well as number of year that for how many years user wants to invest 
    #float function is used to convert user input into float to perform calculation
    # (as python take information in form of string and arithmetic function cannot be performen on string)
    deposit_money=float(input("Please enter the amount of deposit money to invest"))
    interest_rate=float(input("Please enter the intrest rate , dont't worry about the '%'"))
    no_of_year=float(input("Please enter the number of amount that you plan to invest"))
    
    #Here user will choose either he want simple or compound investment method
    interest=input("Which type of interest you want, 'simple'or 'compound'")
    
    # go to line 34
    interest1=interest.lower()
    
    #if control structure is used to match the user inputwith 'simple' , if it matches it will calculate simple investement plan 
    if (interest1 == "simple"):
        
        # r variable is used to store the result of interest rate devided by 100
        r=interest_rate / 100
        
        # Here is the formula to calculate simple interest
        simple_interest = deposit_money * (1 + r * no_of_year)
        
        # print will show the simple interest rate on investment
        print("{}is simple interest rate".format(simple_interest))
        
     # elif condition will be executed if user choose compound interest option otherwise not  
    elif (interest == "compound"):
        
        # r variable is used to store the result of interest rate devided by 100
        r=interest_rate / 100
        
        #Here is the formula to calculate compound interest rate and math.pow function is used to perform power calculation
        compound_interest = deposit_money * math.pow ( ( 1 + r ) , no_of_year )
        
        #print fuction is used to show the compound interest rate
        print("{} is compound interest  rate".format(compound_interest))
    
    # elif block will executed if user will choose home loan repayment plan by rntering the word 'bond' otherwise this block will not executed
elif(check == "bond"):
    
    #Here user will enter some information to perform calculation
    present_house_value=float(input("please enter present house value"))
    bond_interest_rate=float(input("Please enter the interest rate"))
    no_of_month=float(input("Please enter the number of month that you plan to take to repay the bond"))
    
    #Here is the formula to calculate repayment installment
    i = bond_interest_rate / 100
    i = i / 12
    repayment = (i * present_house_value) / ( 1 - ( 1 + i)**( - no_of_month))
    
    #print function is used to display the repayment amount for home loan
    print("Repayment amount for home loan  is  {}".format(repayment))
    
#else block will executed to tell the user that you entered invalid input(if he entered)
else:
    print("invalid input")
    
