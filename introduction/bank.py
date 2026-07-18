input("Your fullname : ")
a=int(input("Your current account balance in DA : "))
b=int(input("How much money you'd like to withdrawl : "))
c=int(input("How many withdrawals attempts you'd like to make : "))

if a>=0 :
    for i in range (c): 
     a=a-b
     print(a)        
     breakpoint 
    print ("Task done successfully")
    breakpoint
      
elif a-(b*c)<0 : 
        print("No enough money in the bank")

        
    

    
