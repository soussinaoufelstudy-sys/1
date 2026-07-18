a=int(input("Input the temperature: "))
C =  ((a-32)*5)/9
F = ((9*a)/5)+32
b=(input('''- Input F if it's in Celsius and you want it in Fahrenheit.
         Or input C if it's in Fahrenheit and you want in Celsius : '''))

if b.upper()=="F":
    print ( "Temperature in Celsius is : " + str(C) )
elif b.upper()=="C":
    print("Temparature in Fahrenheir is : " + str(F))
else : 
    print("Invalid")



