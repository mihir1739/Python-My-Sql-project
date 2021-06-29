#Computer Science Project developed by Mihir
import mysql.connector as m
import function as fun
con=m.connect(host='localhost',user='root',password='root',database='KV2')
z=0
s=0
while z<9:
    print('👨‍🎓🚍welcome to student data management system👩‍🏫👨‍🏫')
    print('1. Create Table')
    print('2.Add ')
    print('3.Update one details')
    print('4.Update all deatils ')
    print('5.Transfer')
    print('6.Delete')
    print('7.View Details')
    print('8.Show the details of All students')
    print('9.EXIT ')
    z=int(input('Enter your choice'))
    
    if z==1:
        if s==0:
            fun.Create()
            print('the Tables have been created')
        else:
            print('The tables has already be created')
    
    elif z==2:
        a=int(input('Enter Roll_no'))
        b=input('Enter name')
        c=int(input('Enter class -in integer'))
        d=int(input('enter marks Out of 100'))
        e=input('enter stream in maximum 6 Characters')
        f=int(input('enter age'))
        fun.add(a,b,c,d,e,f)
        print('Data added in database KV2')
    
    elif z==3:
        print('1. To update roll_no')
        print('2. To update Name')
        print('3. To update Class -in integer')
        print('4. To update Marks')
        print('5. To update Stream')
        print('6. To update age')
        t=int(input('Enter Your Choice'))
        b=input('Enter name')
        c=int(input('Enter Class'))
        try:
            fun.updaone(t,b,c)
            print('operation sucessfull')
        except:
            print('Data not found')
    
    elif z==4:
        b=input('Enter name')
        c=int(input('Enter Class -in integer'))
        a=int(input('Enter NEW Roll_no'))
        d=int(input('enter NEW marks'))
        e=input('enter NEW stream')
        f=int(input('enter NEW age'))
        try:
            fun.upda(a,b,c,d,e,f)
            print('operation sucessfull')
        except:
            print('Details Could Not be Found')
        
    elif z==5:
        b=input('Enter name')
        c=int(input('Enter class -in integer'))
        try:
            fun.transfer(b,c)
            print('Details Shifted To Other Table ')
        except:
            print('Details Could Not be Found')
    
    elif z==6:
        b=input('Enter name')
        c=int(input('Enter class -in integer'))
        try:
            fun.delete(b,c)
            print('operation sucessful')
        except:
            print('data doesnot exist')
    
    elif z==7:
        b=input('Enter name')
        c=int(input('Enter class -in integer'))
        try:
            fun.show(b,c)
        except:
            print('data doesnot exist')
        
    elif z==8:
        print('1 for primary ')
        print('2 for secondry')
        print('3 for senior secondry')
        c=int(input('enter your choice'))
        fun.Showall(c)
    elif z==56:
        c=int(input('enter class '))
        print('enter 1 to sort by Roll_no')
        print('enter 2 to sort by name')
        print('enter 3 to sort by class')
        print('enter 4 to sort by marks')
        print('enter 5 to sort by stream')
        print('enter 6 to sort by age')
        d=int(input('enter your choice'))
        if d==1:
            s='r_no'
            fun.sortby(c,s)
        if d==1:
            s='name'
            fun.sortby(c,s)
        if d==1:
            s='class'
            fun.sortby(c,s)
        if d==1:
            s='marks'
            fun.sortby(c,s)
        if d==1:
            s='stream'
            fun.sortby(c,s)
        if d==1:
            s='age'
            fun.sortby(c,s)
        
con.close()
print('Thank you 👍👍')