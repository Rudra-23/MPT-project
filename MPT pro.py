from os import system, name
def screen_clear():
   if name == 'nt':
      _ = system('cls')
   else:
      _ = system('clear')
def decor(func):
    def wrap(x):
        print("\n"+"-"*100)
        func(x)
        print("\n"+"-"*100)
    return wrap
def Correct(s):
    a=s[0].upper()
    b=s[1:].lower()
    c=a+b
    return c

def check(atn,sy,name):
    arr=[atn,Correct(sy),Correct(name)]
    file=open("Elements.txt","r")
    for line in file:
        str=line.split(" ")
        if int(str[0])==arr[0]:
            if str[1]==arr[1] and str[2]==arr[2]:
                flag=1
                break
            else:
                flag=0
                break
        elif str[1]==arr[1]:
            if int(str[0])==arr[0] and str[2]==arr[2]:
                flag=1
                break
            else:
                flag=0
                break
        elif str[2]==arr[2]:
            if int(str[0])==arr[0] and str[1]==arr[1]:
                flag=1
                break
            else:
                flag=0
                break
        else:
            flag=1
    file.close()
    return flag
            



def create():
    screen_clear()
    var='y'
    file=open("Elements.txt","a")
    at=input("Enter the Atomic Number of the Element\n")
    if at.isdigit():
        at=int(at)
    else:
        screen_clear()
        print("\nWrong Input Entered\n")
        return
    sy=input("Enter the Symbol of the Element\n")
    if not((len(sy)==1 or len(sy)==2) and sy.isalpha()==True):
        screen_clear()
        print("\nWrong Input Entered\n")
        return
    name=input("Enter the name of the Element\n")
    if name.isalpha()==False:
        screen_clear()
        print("\nWrong Input Entered\n")
        return
    flag=check(int(at),Correct(sy),Correct(name))
    if flag==1:
        while var=='y' or var=='Y':
            prop=input("Enter the property of the Element\n")
            file.write(str(at)+" "+Correct(sy)+" "+Correct(name)+" "+prop+"\n")
            print("\nElement has updated succesfully!")
            var=input("\nEnter Y or y to continue entering properties! \n")
        screen_clear()
    else:
        print("\n\n Any one of the INFO in incorrect!\n\n")
    file.close()
@decor    
def searchBYnum(x):
    screen_clear()
    flag=0
    file=open("Elements.txt","r")
    for line in file:
        arr=line.split(" ")
        if int(arr[0])==x:
            break
    else:
        flag=1
        print("NO ELEMENT FOUND!")
    if flag==0:
        print("Element is "+arr[2].upper())
        print("\nAtomic number is "+arr[0])
        print("\nSymbol is "+arr[1])
        print("\nIts properties are :")
        file.close()
        file=open("Elements.txt","r")
        count=1
        for line in file:
            arr=line.split(" ")
            if int(arr[0])==x:
                print(str(count)+") ",end="")
                print(" ".join(arr[3:]),end="")
                count +=1
        
    
@decor
def searchBYchar(s):
    screen_clear()
    flag=0
    file=open("Elements.txt","r")
    for line in file:
        arr=line.split(" ")
        if (arr[1])==s:
            break
    else:
        flag=1
        print("NO ELEMENT FOUND!")
    if flag==0:
        print("Element is "+arr[2].upper())
        print("\nAtomic number is "+arr[0])
        print("\nSymbol is "+arr[1])
        print("\nIts properties are :")
        file.close()
        file=open("Elements.txt","r")
        count=1
        for line in file:
            arr=line.split(" ")
            if arr[1]==s:
                print(str(count)+") ",end="")
                print(" ".join(arr[3:]),end="")
                count +=1
    
@decor
def searchBYname(s):
    screen_clear()
    flag=0
    file=open("Elements.txt","r")
    for line in file:
        arr=line.split(" ")
        if (arr[2])==s:
            break
    else:
        flag=1
        print("NO ELEMENT FOUND!")
    if flag==0:
        print("Element is "+arr[2].upper())
        print("\nAtomic number is "+arr[0])
        print("\nSymbol is "+arr[1])
        print("\nIts properties are :")
        file.close()
        file=open("Elements.txt","r")
        count=1
        for line in file:
            arr=list(line.split(" "))
            if arr[2]==s:
                print(str(count)+") ",end="")
                print(" ".join(arr[3:]),end="")
                count +=1
   
            
while True:
    print("\n\n\npress 1 to create a element info")
    print("press 2 to search a element by its number")
    print("press 3 to search a element by its symbol")
    print("press 4 to search a element by its name")
    print("press 0 to exit\n\n\n")
    num=input("enter the number from the options\n")
    if num.isdigit()==False:
        print("Thankyou For Using!!!\nClosing....")
        break
    else:
        num=int(num)
    if num==1:
        create()
    elif num==2:
        x=input("Enter the atomic number you want to search !\n")
        if x.isdigit():
            x=int(x)
            searchBYnum(x)
        else:
            screen_clear()
            print("\nEnter a Number (not character)\n")

    elif num==3:
        s=input("Enter the atomic symbol you want to search !\n")
        if (len(s)==2 or len(s)==1) and s.isalpha()==True:
            s=Correct(s)
            searchBYchar(s)
        else:
            screen_clear()
            print("\nWrong Symbol Format\n")
    elif num==4:
        s=input("Enter the atomic name you want to search !\n")
        if s.isalpha()==True:
            s=Correct(s)
            searchBYname(s)
        else:
            screen_clear()
            print("\nEnter Proper Name!\n")
    else:
        print("Thank you for using !!\nClosing....")
        break
        