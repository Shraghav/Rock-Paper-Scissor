import random
a=0
b=0
t=0
n=0
time=int(input("Enter how many times you want to play:"))
while t<time:
    cool=['ROCK','PAPER','SCISSOR']
    rand=random.choice(cool)
    user=input("Enter rock/ paper/ scissor:").upper()
    print(rand)
    if user=="ROCK" and rand=="PAPER":
        print("COMPUTER WON!\n")
        a+=1
        t+=1
    elif user=="ROCK" and rand=="SCISSOR":
        print("YOU WON!!\n")
        b+=1
        t+=1
    elif user=="PAPER" and rand=="ROCK":
        print("YOU WON\n")
        b+=1
        t+=1
    elif user=="PAPER" and rand=="SCISSOR":
        print("COMPUTER WON\n")
        a+=1
        t+=1
    elif user=="SCISSOR" and rand=="ROCK":
        print("COMPUTER WON\n")
        a+=1
        t+=1
    elif user=="SCISSOR" and rand=="PAPER":
        print("YOU WON\n")
        b+=1
        t+=1
    elif user==rand:
        print("Neither won\n")
        n+=1
        t+=1
    else:
        print("Please enter correctly!!\n")
if b>a:
    print("HURRAY!! YOU WON",b,"OUT OF",t,"PLAYS")
elif a>b:
    print("BETTER LUCK NEXT TIME. COMPUTER WON",a,"OUT OF",t,"PLAYS AND",n,"DRAWS")
    
elif a==b:
    print("SINCE YOU AND COMPUTER SCORED EQUAL POINTS, PLAY 1 MORE TIME (LIKE SUPER OVER)")
    user=input("Enter rock/ paper/ scissor:").upper()
    print(rand)
    if user=="ROCK" and rand=="PAPER":
        print("COMPUTER WON !\n")
        a+=1
        t+=1
    elif user=="ROCK" and rand=="SCISSOR":
        print("YOU WON!!\n")
        b+=1
        t+=1
    elif user=="PAPER" and rand=="ROCK":
        print("YOU WON\n")
        b+=1
        t+=1
    elif user=="PAPER" and rand=="SCISSOR":
        print("COMPUTER WON\n")
        a+=1
        t+=1
    elif user=="SCISSOR" and rand=="ROCK":
        print("COMPUTER WON\n")
        a+=1
        t+=1
    elif user=="SCISSOR" and rand=="PAPER":
        print("YOU WON\n")
        b+=1
        t+=1
    elif user==rand:
        print("Neither won\n")
        t+=1
    else:
        print("Please enter correctly!!\n")