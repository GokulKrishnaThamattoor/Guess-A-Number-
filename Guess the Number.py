
import random
n=int(input("how many times going to try"))   # attempt you are going to play
N=random.randint(0, 9999999999999)            #Secret Numbers!!

G=0                                           # guess
T=0                                           #tries 
print ("enter the number buddy")
print ("0-9999999999999")

while G!= N and T<n-1:
    x=int(input("Guess the Number buddy:-) "))#number guessed by ourself
    if G>N:
        print("oops too high bruh :-(")       #if the guess of number is greater
        if G<N:
            print("bro you are too low in guessing :-|")# if the guess of number is low
            if G==N:
                print ("You have a lucky day;-)",N,"Enjoy!!!")#when miracle happens if the number is crct
    else:
        print (":-(  404 Error )-:")                            #when we prove we are programmers;-)

