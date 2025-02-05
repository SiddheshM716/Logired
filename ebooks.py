import csv
flag=0
price=[400,440,380,460,500,470,600,550,520]
tot=0
one='''"To Kill a Mockingbird" by Harper Lee'''
two='''"1984" by George Orwell'''
three='''"Pride and Prejudice" by Jane Austen'''
four='''"The Great Gatsby" by F. Scott Fitzgeral'''
five='''"The Lord of the Rings" by J.R.R. Tolkien'''
six='''"Harry Potter" series by J.K. Rowling'''
seven='''"The Diary of Anne Frank" by Anne Frank'''
eight='''"War and Peace" by Leo Tolstoy'''
nine='''"The Little Prince" by Antoine de Saint-Exupéry'''
prd={one:400,two:440,three:380,four:460,five:500,six:470,seven:600,eight:550,nine:520}

car={}
def login():
    global flag
    f=open('login.csv','r')
    r=list(csv.reader(f))
    ui=input("Enter your username:")
    flag=0
    for i in r:
        if i[0]==ui:
            pa=input("Enter your password:")
            if i[1]==pa:
                flag=1
        else:
            break

def signin():
    global flag
    f=open('login.csv','a')
    ui=input("Enter your username:")
    pa=input("Enter your password:")
    obj=csv.writer(f)
    obj.writerow([ui,pa])
    print("user created successfully")
    flag=1

def buybooks():
    login()
    global flag
    if flag==0:
         print("user does not exist")
         ch=input('Create new user?(Y/N)')
         if ch=='y' or ch=="Y":
            signin()
         elif ch=='n' or ch=='N':
            return
    if flag==1:
           print("Confirm purchase:(Y/N):")
           ch=input()
           if ch=='y' or ch=="Y":
               print('''
============================================================================

Purchase Sucessful
Enjoy your reading time!!!

============================================================================''')
               car={}
               homepage()
           if ch=='n' or ch=='N':
               return

               
def cart():
    while True:
        print('''
============================================================================''')
        print("%-70s%-5s"%('Book name','Price'))
        for i in car:
            print("%-70s%-5s"%(i,car[i]))
        print('''
Total amount=%s
C.Checkout
B.Back
============================================================================'''%(tot))
        ch=input("Enter your Choice:")
        if ch=="c" or ch=='C':
            buybooks()
        if ch=="b" or ch=='b':
            break

def showbook(a):
    a='book'+str(a)+'.txt'
    f=open(a,'r')
    rev=f.read()
    f.close()
    print("============================================================================================================================")
    print(rev)
    print('''
Price=%s
C.Buy book
A.Add to cart
V.View Cart
B.Back

============================================================================================================================'''%(price[int(c)-1]))
    ch=input("Enter your choice:")
    while(True):
        if ch=='C' or ch=='c':
            buybooks()
        elif ch=='a' or ch=='A':
            for i in prd:
                if prd[i]==price[int(c)-1]:
                    name=i
            global tot
            car.update({name:price[int(c)-1]})
            print("Added to cart")
            tot=tot+price[int(c)-1]
            break
        elif ch=="v" or ch=="V":
            cart()
        elif ch=='n' or 'N':
            break
        
def homepage():            
    while (True):
        print('''
============================================================================
                                LOGIRED
                                =======

                                 Home
                                 ====

Bestsellers:
1. %s
2. %s
3. %s
4. %s
5. %s
6. %s
7. %s
8. %s
9. %s

C.View your cart
E.Exit
============================================================================
Enter your choice to proceed:'''%(one,two,three,four,five,six,seven,eight,nine),end='')
        global c
        c=input()
        if c in ['1','2','3','4','5','6','7','8','9']:
            showbook(c)
        elif c=='c' or c=='C':
            cart()
        elif c=='e' or c=='E':
            break
homepage()
