num1 = int(input("Dime un numero: "))

for i in range(1,num1 +1):
    if(num1%i==0):
        print(i,end=" ")