import mysql.connector as j
con=j.connect(host='localhost',user='root',password='root',database='KV2')
def Create():
#function to create table in mySQL
    k='''create table primary1 (r_no int,
    name varchar(15) unique,
    class int,
    marks int,
    stream varchar(6),
    age int)'''
    f='''create table secondary (r_no int,
    name varchar(15) unique,
    class int,
    marks int,
    stream varchar(6),
    age int)'''
    v='''create table sr_secondary (r_no int,
    name varchar(15) unique,
    class int,
    marks int,
    stream varchar(6),
    age int)'''
    cr=con.cursor()
    cr.execute(k)
    cr.execute(f)
    cr.execute(v)
    con.commit()

def add(a,b,c,d,e,f):
#function to add values to the table in mySQL
    if c<=5:
        cr=con.cursor()
        k='''insert into primary1 values (%d,'%s',%d,%d,'%s',%d)'''%(a,b,c,d,e,f)
        cr.execute(k)
        con.commit()
    elif c>5 and c<11:
        k='''insert into secondary values (%d,'%s',%d,%d,'%s',%d)'''%(a,b,c,d,e,f)
        cr=con.cursor()
        cr.execute(k)
        con.commit()
    else:
        k='''insert into sr_secondary values (%d,'%s',%d,%d,'%s',%d)'''%(a,b,c,d,e,f)
        cr=con.cursor()
        cr.execute(k)
        con.commit()

def upda(a,b,c,d,e,f):
#function to update table in mySQL
    if c<=5:
        k='''update primary1 set r_no="%d",age="%d",marks="%d",stream="%s",class="%d" where name="%s"'''%(a,f,d,e,c,b)
        cr=con.cursor()
        cr.execute(k)
        con.commit()
    elif c>5 and c<11:
        k='''update secondary set r_no="%d",age="%d",marks="%d",stream="%s",class="%d" where name="%s"'''%(a,f,d,e,c,b)
        cr=con.cursor()
        cr.execute(k)
        con.commit() 
    else:
        k='''update sr_secondary set r_no="%d",age="%d",marks="%d",stream="%s",class="%d" where name="%s"'''%(a,f,d,e,c,b)
        cr=con.cursor()
        cr.execute(k)
        con.commit()

def updaone(d,b,c):
    if c<=5:
        if d==1:
            h=int(input('enter New Roll no.'))
            k='''update primary1 set r_no="%d"where name="%s"'''%(h,b)
            cr=con.cursor()
            cr.execute(k)
            con.commit()
        elif d==2:
            h=int(input('enter New Name no.'))
            k='''update primary1 set name="%s"where name="%s"'''%(h,b)
            cr=con.cursor()
            cr.execute(k)
            con.commit()
        elif d==3:
            h=int(input('enter New class.'))
            k='''update primary1 set class="%d"where name="%s"'''%(h,b)
            cr=con.cursor()
            cr.execute(k)
            con.commit()
        elif d==4:
            h=int(input('enter New Marks'))
            k='''update primary1 set marks="%d"where name="%s"'''%(h,b)
            cr=con.cursor()
            cr.execute(k)
            con.commit()
        elif d==5:
            h=input('enter New stream')
            k='''update primary1 set stream="%s"where name="%s"'''%(h,b)
            cr=con.cursor()
            cr.execute(k)
            con.commit()
        elif d==6:
            h=int(input('enter New age'))
            k='''update primary1 set age="%d"where name="%s"'''%(h,b)
            cr=con.cursor()
            cr.execute(k)
            con.commit()
    elif c>5 and c<11:
        if d==1:
            h=int(input('enter New Roll no.'))
            k='''update secondary set r_no="%d"where name="%s"'''%(h,b)
            cr=con.cursor()
            cr.execute(k)
            con.commit()
        elif d==2:
            h=int(input('enter New Name .'))
            k='''update secondary set name="%s"where name="%s"'''%(h,b)
            cr=con.cursor()
            cr.execute(k)
            con.commit()
        elif d==3:
            h=int(input('enter New class.'))
            k='''update secondary set class="%d"where name="%s"'''%(h,b)
            cr=con.cursor()
            cr.execute(k)
            con.commit()
        elif d==4:
            h=int(input('enter New Marks'))
            k='''update secondary set marks="%d"where name="%s"'''%(h,b)
            cr=con.cursor()
            cr.execute(k)
            con.commit()
        elif d==5:
            h=input('enter New stream')
            k='''update secondary set stream="%s"where name="%s"'''%(h,b)
            cr=con.cursor()
            cr.execute(k)
            con.commit()
        elif d==6:
            
            k='''update secondary set age="%d"where name="%s"'''%(h,b)
            cr=con.cursor()
            cr.execute(k)
            con.commit()
    else:
        if d==1:
            h=int(input('enter New Roll no.'))
            k='''update sr_secondary set r_no="%d"where name="%s"'''%(h,b)
            cr=con.cursor()
            cr.execute(k)
            con.commit()
        elif d==2:
            h=int(input('enter New Name no.'))
            k='''update sr_secondary set name="%s"where name="%s"'''%(h,b)
            cr=con.cursor()
            cr.execute(k)
            con.commit()
        elif d==3:
            h=int(input('enter New class.'))
            k='''update sr_secondary set class="%d"where name="%s"'''%(h,b)
            cr=con.cursor()
            cr.execute(k)
            con.commit()
        elif d==4:
            h=int(input('enter New Marks'))
            k='''update sr_secondary set marks="%d"where name="%s"'''%(h,b)
            cr=con.cursor()
            cr.execute(k)
            con.commit()
        elif d==5:
            h=input('enter New stream')
            k='''update sr_secondary set stream="%s"where name="%s"'''%(h,b)
            cr=con.cursor()
            cr.execute(k)
            con.commit()
        elif d==6:
            h=int(input('enter New age'))
            k='''update sr_secondary set age="%d"where name="%s"'''%(h,b)
            cr=con.cursor()
            cr.execute(k)
            con.commit()
def transfer(b,c):
#function to tranfer data from one table to another in mySQL
    if c<=5:
        k='''insert into secondary select * from primary1 where name="%s"'''%(b)
        g='''delete from primary1 where name="%s"'''%(b)
        f='''update secondary set class="%d"name="%s"'''%(c+1,b)  
        cr=con.cursor()
        cr.execute(k)
        cr.execute(g)
        con.commit()
    elif c>5 and c<11:
        k='''insert into sr_secondary select * from secondary where name="%s"'''%(b)
        g='''delete from secondary where name="%s"'''%(b)  
        f='''update secondary set class="%d"name="%s" '''%(c+1,b)  
        cr=con.cursor()
        cr.execute(k)
        cr.execute(g)
        cr.execute(f)
        con.commit()

def delete(b,c):
#function to delete values from table in mySQL
    if c<5:
        k='''delete from primary1 where name="%s"'''%(b)
        cr=con.cursor()
        cr.execute(k)
        con.commit()
    elif c>5 and c<11:
        k='''delete from secondary where name="%s"'''%(b)
        cr=con.cursor()
        cr.execute(k)
        con.commit()          
    else:
        k='''delete from sr_secondary where name="%s" '''%(b)
        cr=con.cursor()
        cr.execute(k)
        con.commit()

def show(b,c):
#function to view details of a student from mySQL
    if c<=5:
        k='''select * from primary1 where name="%s"'''%(b)
        cr=con.cursor()
        cr.execute(k)
        r=cr.fetchall()
        print(r[0])
          
    elif c>5 and c<11:
        k='''select * from secondary where name="%s"'''%(b)
        cr=con.cursor()
        cr.execute(k)
        r=cr.fetchall()
        print(r[0])
        
    else:
        k='''select * from sr_secondary where name="%s"'''%(b)
        cr=con.cursor()
        cr.execute(k)
        r=cr.fetchall()
        print(r[0])
        
def Showall(j):
#function to view table from mySQL
    if j==1:
        k='''select * from  primary1 '''
        cr=con.cursor()
        cr.execute(k)
        r=cr.fetchall()
        for i in r:
            for j in i:
                print(j,end=' ')
            print()
                
    elif j==2:
        k='''select * from  secondary '''
        cr=con.cursor()
        cr.execute(k)
        r=cr.fetchall()
        for i in r:
            for j in i:
                print(j,end=' ')
            print()
        
    else:
        k='''select * from  sr_secondary '''
        cr=con.cursor()
        cr.execute(k)
        r=cr.fetchall()
        for i in r:
            for j in i:
                print(j,end=' ')
            print()

def sortby(c,s):
    if c<5:
        k='''select * from primary1 sort by "%s" '''(s)
        cr=con.cursor()
        cr.execute(k)
        r=cr.fetchall()
        for i in r:
            for j in i:
                print(j,end=' ')
            print()
    elif c>5 and c<11:
        k='''select * from secondary sort by "%s" '''(s)
        cr=con.cursor()
        cr.execute(k)
        r=cr.fetchall()
        for i in r:
            for j in i:
                print(j,end=' ')
            print()
    else:
        k='''select * from secondary sort by "%s" '''(s)
        cr=con.cursor()
        cr.execute(k)
        r=cr.fetchall()
        for i in r:
            for j in i:
                print(j,end=' ')
            print()
con.close()          