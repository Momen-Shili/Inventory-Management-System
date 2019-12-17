#Inventory Management System 2
#SaurontheMighty


#Dictionaries
unit_price={}
description={}
stock={}

#Open file with stock
details = open("stock.txt","r")

#First line of the file is the number of items
no_items  = int((details.readline()).rstrip("\n"))

#Add items to dictionaries
for i in range(0,no_items):
    line  = (details.readline()).rstrip("\n")
    x1,x2 = line.split("#")
    x1=int(x1)
    x2=float(x2)
    unit_price.update({x1: x2})

for i in range(0,no_items):
    line  = (details.readline()).rstrip("\n")
    x1,x2 = line.split("#")
    x1=int(x1)
    description.update({x1: x2})

for i in range(0,no_items):
    line  = (details.readline()).rstrip("\n")
    x1,x2 = line.split("#")
    x1=int(x1)
    x2=int(x2)
    stock.update({x1: x2})

details.close()

#List to store the items purchased
cart=[]

c="y" #Runs the while loop as long as user wants


#Instructions
print("Welcome to IMS")
print()
print("A-Add an item")
print("R-Remove an item")
print("E-Edit specifics of an item")
print("L-List all items")
print("I-Inquire about a part")
print("P-Purchase")
print("C-Checkout")
print("S-Show all parts purchased")
print("Q-Quit")
print("remove-Remove an item from the cart")
print("help-See all commands again")
print()


total_cost=0 
flag=0 #To check if they have checked out


while(c!= "q" or c!= "Q"):
    c= input("What would you like to do? ")
    
    if(c=="q" or c=="Q"):
        break
        
    elif(c=="A" or c=="a"):#Add a part
        p_no = int(input("Enter part number: "))
        p_pr = float(input("Enter part price: "))
        p_desc = input("Enter part description: ")
        p_stock = int(input("Enter part stock: "))
        
        m=0
        for i in range(0,len(unit_price)):
            if(p_no in unit_price):
                p_no+=1
                m=1
        if(m==1):
            print()
            print("That part number already exists :(, changing value to ",p_no)
                
        unit_price.update({p_no: p_pr})
        description.update({p_no: p_desc})
        if(p_stock > -1):
            stock.update({p_no: p_stock})
        else:
            p_stock = 0
            stock.update({p_no: p_stock})
            print("The stock of an item cannot be negative, the stock has been set to 0.")
        print()
        print("Part number: ",p_no," Description: ",description.get(p_no)," Price: ",unit_price.get(p_no)," Stock: ",stock.get(p_no))
        print("Part was added successfully!")
        print()
        
    elif(c=="E" or c=="e"):#Edit a part
        print()
        p_no = int(input("Enter part number: "))
        if(p_no in unit_price):
            p_pr = float(input("Enter part price: "))
            p_desc = input("Enter part description: ")
            p_stock = int(input("Enter part stock: "))
                
            unit_price.update({p_no: p_pr})
            description.update({p_no: p_desc})
            stock.update({p_no: p_stock})
            
        else:
            print("That item does not exist, to add an item use a")
        print()
    
            
    elif(c=="R" or c=="r"):#Remove a part
        print()
        p_no = int(input("Enter part number: "))
        if(p_no in unit_price):
            are_you_sure = input("Are you sure you want to remove that item(y/n)? ")
            if(are_you_sure=="y" or are_you_sure=="Y"):
                unit_price.pop(p_no)
                description.pop(p_no)
                stock.pop(p_no)
                print("Item successfully removed!")
            print()
        else:
            print("Sorry, we don't have such an item!")
            print()
        
    elif(c=="L" or c=="l"):#List all the parts
        print()
        print("Parts and their prices: ",unit_price)
        print("Descriptions: ",description)
        print("Stock left of Item: ",stock)
        print()

    elif(c=="I" or c=="i"):#Inquire about a part
        print()
        p_no=int(input("Enter Part Number: "))
        if(p_no in unit_price):
            print()
            print("Part number: ",p_no," Description: ",description.get(p_no)," Price: ",unit_price.get(p_no)," Stock: ",stock.get(p_no))
            if(stock.get(p_no)<3 and stock.get(p_no)!=0):
                print("Only ",stock.get(p_no)," remaining! Hurry!")
            print()
        else:
            print("Sorry we don't have such an item!")
            print()
        
    elif(c=="P" or c=="p"):#Purchase a part
        print()
        p_no = int(input("Enter Part number: "))
        if(p_no in unit_price):
            if(flag==1):
                flag=0
            stock_current = stock.get(p_no)
            if(stock_current>0):
                stock_current = stock.get(p_no)
                stock[p_no] = stock_current-1
                item_price = unit_price.get(p_no)
                total_cost = total_cost+item_price
                print(description.get(p_no),"added to cart: ","$",item_price)
                cart.append(p_no)#Stores item in cart
            else:
                print("Sorry! We don't have that item in stock!")
        else:
                print("Sorry! We don't have such an item!")
        print()
        
    elif(c=="C" or c=="c"):#Check out
        print()
        print("You bought the following parts: ",cart)
        print("Total: ","$",round(total_cost,2))
        tax= round(0.13*total_cost,2)
        print("Tax is 13%: ","$",tax)
        total = round(total_cost+tax,2)
        print("After Tax: ","$",total)
        total_cost=0
        flag=1
        print()
        print("You can still purchase items after check out, your cart has been reset. To quit press q")
        print()
        
    elif(c=="help"):#Display all commands
        print()
        print("Help Centre")
        print("A-Add an item")
        print("R-Remove an item")
        print("E-Edit specifics of an item")
        print("L-List all items")
        print("I-Inquire about a part")
        print("P-Purchase")
        print("C-Checkout")
        print("S-Show all parts purchased")
        print("remove-Remove an item from the cart")
        print("help-See all commands again")
        print("If you have any other questions or concerns please contact the manager.")
        print()
        
    elif(c=="remove" or c=="Remove"):#To remove an item from the cart
        print()
        are_you_sure = input("Are you sure you want to remove an item from the cart(y/n)? ")
        if(are_you_sure=="y"):
            p_no = int(input("Enter part number to remove from cart: "))
            if(p_no in cart):
                stock_current = stock.get(p_no)
                stock[p_no] = stock_current+1
                item_price = unit_price.get(p_no)
                total_cost = total_cost-item_price
                j=0
                for i in range(0,len(cart)):#To find the index of the part in the list cart
                    if(i==p_no):
                        j=i

                cart.pop(j)
                print(description.get(p_no),"removed from cart: ")
                print()
            else:
                print()
                print("That item is not in your cart!")
                print()
                
    elif(c=="s" or c=="S"):#prints list cart
        print()
        print(cart)
        print()
        
    else:
        print()
        print("ERROR! Contact manager for help!")
        print()


#Outputs total if the user quits without checking out
if(total_cost>0 and flag==0):
    print()
    print("You bought: ",cart)
    print("Total: ","$",round(total_cost,2))
    tax= round(0.13*total_cost,2)
    print("Tax is 13%: ","$",tax)
    total = round(total_cost+tax,2)
    print("After Tax: ","$",total)
    
print()
print("Thank you for using IMS")

#Write the updated inventory to the file
details = open("stock.txt","w")
no_items=len(unit_price)
details.write(str(no_items)+"\n")
for i in range(0,no_items):
    details.write(str(i+1)+"#"+str(unit_price[i+1])+"\n")
    
for i in range(0,no_items):
    details.write(str(i+1)+"#"+description[i+1]+"\n")
    
for i in range(0,no_items):
    details.write(str(i+1)+"#"+str(stock[i+1])+"\n")
    
details.close()
