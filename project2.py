import mysql.connector
print("""
WELCOME TO BOOK INVENTORY MANAGEMENT SYSTEM
""")
mydb = mysql.connector.connect(host ="localhost", user ='root', passwd= 'root')
mycursor = mydb.cursor()
mycursor.execute("create database if not exists book_store3")
mycursor.execute("use book_store3")
mycursor.execute("create table if not exists login(username varchar(25)not null, password varchar(25) not null) ")
mycursor.execute("create table if not exists purchase(odate date not null, name varchar(25)not null, pcode int not null, amount int not null)")
mycursor.execute("create table if not exists stock( pcode int not null, pname varchar(25)not null, quantity int not null, price int not null)")
mydb.commit()
z=0
mycursor.execute("select * from login")
for i in mycursor:
    z+=1
if (z==0):
    mycursor.execute("insert into login values('username','123')")
    mydb.commit()
while True:
    print("""1. Admin
2. Customer
3. Exit
""")
    ch= int(input("enter your choice::"))
    if(ch==1):
        passs=input("enter password::")
        mycursor.execute("select * from login")
        for i in mycursor:
            username,password=i
        if(passs==password):
            print("welcome TO My Book Store")
            loop2='y'
            while(loop2=='y' or loop2=='Y'):
                print("""1. add new book
            2. update price
            3. delete book
            4. display all books
            5. change password
            6. log out
  """)
                ch= int(input("enter your choice::"))
                if(ch==1):
                    loop='y'
                    while(loop=='y' or loop=='Y'):
                      pcode=int(input("enter book code::"))
                      pname =input("enter book name::")
                      quantity=int(input("enter book quantity::"))
                      price=int(input("enter book price::"))
                      mycursor.execute("insert into stock values('"+str(pcode)+"', '"+pname+"','"+str(quantity)+"','"+str(price)+"')")
                      mydb.commit()
                      print("record successfully Updated")
                      loop=input("Do you want to enter more items(y/n)::")
                    loop2=input("Do you want to continue editing stock(y/n)::") 
                elif(ch==2):
                    loop='y'
                    while(loop=='y' or loop=='Y'):
                      pcode=int(input("enter book code::"))
                      new_price=int(input("enter new price::"))
                      mycursor.execute("update stock set price ='"+str(new_price)+"' where pcode='"+str(pcode)+"'")
                      mydb.commit()
                      loop=input("Do you want to change price of any other item(y/n):")
                    loop2=input("Do you want to continue editing stock(y/n)::")
                elif(ch==3):
                   loop='y'
                   while(loop=='y' or loop=='Y'):
                     pcode=int(input("enter book code::"))
                     mycursor.execute("delete from stock where pcode='"+str(pcode)+"'")
                     mydb.commit()
                     print("record successfully gets Deleted")
                     loop=input("Do you want to delete any other data(y/n)::")
                   loop2=input("Do you want to continue editing stock(y/n)::")
                elif(ch==4):
                    mycursor.execute("select * from stock")
                    print("pcode||pname||quantity||price")
                    for i in mycursor:
                        t_code,t_name,t_quan,t_price=i
                        print(f"{t_code}||{t_name}||{t_quan}||{t_price}")
                elif(ch==5):
                    old_pass=input("enter new password::")
                    mycursor.execute("select * from login")
                    for i in mycursor:
                        username,password=i
                    if(old_pass==password):
                        new_pass=input("enter new password::")
                        mycursor.execute("update login set password='"+new_pass+"'")
                        mydb.commit()
                elif(ch==6):
                   break
       
        
                



                    


                        
                        
                

        else:
            print("wrong password")


#################################customer section###############################################################
    elif(ch==2):
       print(""" 1. Books available
2. payment
3. view available books
4. go back
""")
       ch2 =int(input("enter your choice::"))
       if(ch2==1):
           name= input("enter your name::")
           pcode=int(input("enter book code:"))
           quantity=int(input("enter product quantity"))
           mycursor.execute("select * from stock where pcode ='"+str(pcode)+"'")
           for i in mycursor:
               t_code,t_name,t_quan,t_price=i
           amount=t_price*quantity
           net_quan=t_quan-quantity
           mycursor.execute("update stock set quantity ='"+str(net_quan)+"'where pcode='"+str(pcode)+"'")
           mycursor.execute("insert into purchase values(now(),'"+name+"','"+str(pcode)+"','"+str(amount)+"')")
           mydb.commit()
       elif(ch2==2):
          print(f"amount to be paid {amount}")
       elif(ch2==3):
          print("CODE||NAME||PRICE")
          mycursor.execute("select * from stock")
          for i in mycursor:
             t_code,t_name,t_quan,t_price=i
             print(f"{t_code}||{t_name}||{t_price}")
       elif(ch2==4):
           break
    elif(ch==3):
       break
             
             
        
        

           
        
         
        
                
        
