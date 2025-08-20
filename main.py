import random
print("-1 is for snake, 0 is for water and 1 for gun")
computer = random.choice([-1,0,1])
user= int(input("enter the choice you want to make:"))


reverse_choice={-1:"snake",0:"water",1:"gun"}

print(f"user choice is {reverse_choice[user]} and computer choose{reverse_choice[computer]}")

if(computer == user):
    print("match is drawn")

else:
    if(computer== -1 and user==0):
        print("computer won")
    
    elif(computer== -1 and user==1):
        print("you won")

    elif(computer==1 and user==0):
        print("you won")    

    elif(computer== 1 and user== -1):
        print("computer won")    

    elif(computer==0 and user==1):
        print("computer won")    

    elif(computer== 0 and user==-1):
        print("user won")    