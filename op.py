from tkinter import *
from tkinter import messagebox
import pymysql


db=pymysql.connect("localhost","root","root","bbms")

cursor=db.cursor()


top=Tk()
top.geometry("1920x1080")
Label(top,text="BLOOD BANK SYSTEM",bg="blue",font = "Helvetica 15 bold").pack(fill=X)

Label(top,text="Click to  enter the details of the donor",bg="white",font="Helvetica 12").place(x=500,y=100,w=300,h=40)

Button(top,text="Donor details",command=lambda:donordetails()).place(x=550,y=150)

Label(top,text="Click to  enter the details of the blood",bg="white",font="Helvetica 12").place(x=500,y=200,w=300,h=40)
Button(top,text="Blood details",command=lambda:blooddetails()).place(x=550,y=250)
Label(top,text="Click to make a request for blood",bg="white",font="Helvetica 12").place(x=500,y=300,w=300,h=40)
Button(top,text="Blood request",command=lambda:bloodrequest()).place(x=550,y=350)
Button(top,text="Exit",command=lambda:stop(top)).place(x=500,y=400)

v = StringVar()

def a():
    messagebox.showinfo('success',"data submitted")

def sel():
    selection = "You selected the option " + v.get()
    print(selection)

def stop(top):
    top.destroy()

def insertDonor(name,age,gender,address,contactno):
    insert = "INSERT INTO donors(name,age,gender,address,contactno) VALUES('"+name+"','"+age+"','"+gender+"','"+address+"',"+"'"+contactno+"')"
    try:
        cursor.execute(insert)
        db.commit()
    except:
        db.rollback()


def insertBlood(bloodgroup,platelet,rbc):
    insert= "INSERT INTO blood(bloodgroup,platelet,rbc) VALUES('"+bloodgroup+"','"+"','"+platelet+"','"+"','"+"','"+rbc+"')"
    try:
        cursor.execute(insert)
        db.commit()
        a()
    except:
        db.rollback()


def retrieve(bg):
    request="select * from donors inner join blood using(id) where bloodgroup='"+bg+"'"
    try:
        cursor.execute(request)
        rows=cursor.fetchall()
        db.commit()
        print(len(rows))
        return rows
    except:
        db.rollback()
      

def donordetails():
	top=Toplevel()
	top.title("BLOOD BANK")
	top.geometry("1024x768")
	top.configure(background='#FF8F8F')
	Label(top,text="Name:",bg='white').place(x=40,y=40)
	Label(top,text="Age:",bg='white').place(x=40,y=80)
	Label(top,text="Gender:",bg='white').place(x=40,y=120)
	Label(top,text="Address:",bg='white').place(x=40,y=220)
	Label(top,text="Contact:",bg='white').place(x=40,y=260)
	e1=Entry(top).place(x=120,y=40)
	e2=Entry(top).place(x=120,y=80)
	r1=Radiobutton(top,text="Male",variable=v,value="Male",command=sel).place(x=120,y=120)
	r2=Radiobutton(top,text="Female",variable=v,value="Female",command=sel).place(x=120,y=150)
	r3=Radiobutton(top,text="Other",variable=v,value="Other",command=sel).place(x=120,y=180)
	e4=Entry(top).place(x=120,y=220)
	e5=Entry(top).place(x=120,y=260)
	
	b2=Button(top,text="Back",command=lambda : stop(top)).place(x=120,y=300)
	
	b1=Button(top,text="Submit",command=lambda : insertDonor(e1.get(),e2.get(),gen,e4.get(),e5.get())).place(x=40,y=300)

	top.mainloop()



def blooddetails():
    top=Tk()
    top.title("BLOOD BANK")
    top.geometry("1024x768")
    top.configure(background='#FF8F8F')
    Label(top,text="Blood Group:").place(x=40,y=40,w=250,h=20)
    Label(top,text="PLatetelet count (in 100 thousands):").place(x=40,y=80,w=250,h=20)
    Label(top,text="RBC count (in millions):").place(x=40,y=120,w=250,h=20)
    e1=Entry(top).place(x=300,y=40)
    e2=Entry(top).place(x=300,y=80)
    e3=Entry(top).place(x=300,y=120)
    b1=Button(top,text="Back",command=lambda : stop(top)).place(x=200,y=160)
    b2=Button(top,text="Submit",command=lambda : insertBlood(e1.get(),e2.get(),e3.get())).place(x=100,y=160)	
    top.mainloop()


def grid1(bg):
    top=Tk()
    top.title("LIST OF MATCHING DONORS")
    top.geometry("750x500")
    rows=retrieve()
    x=0
    for row in rows:
        l1=Label(top,text=row[0],bg="#1EDEF2",font = "Verdana 15 bold").grid(row=x,column=0,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
        l2=Label(top,text=row[1],bg="#1EDEF2",font = "Verdana 15 bold").grid(row=x,column=1,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
        l3=Label(top,text=row[2],bg="#1EDEF2",font = "Verdana 15 bold").grid(row=x,column=2,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
        l4=Label(top,text=row[3],bg="#1EDEF2",font = "Verdana 15 bold").grid(row=x,column=3,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
        l5=Label(top,text=row[4],bg="#1EDEF2",font = "Verdana 15 bold").grid(row=x,column=4,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
        l6=Label(top,text=row[5],bg="#1EDEF2",font = "Verdana 15 bold").grid(row=x,column=5,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
        l7=Label(top,text=row[6],bg="#1EDEF2",font = "Verdana 15 bold").grid(row=x,column=6,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
        l8=Label(top,text=row[7],bg="#1EDEF2",font = "Verdana 15 bold").grid(row=x,column=7,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
        l9=Label(top,text=row[8],bg="#1EDEF2",font = "Verdana 15 bold").grid(row=x,column=8,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
        l10=Label(top,text=row[9],bg="#1EDEF2",font = "Verdana 15 bold").grid(row=x,column=9,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)


def bloodrequest():
    top=Tk()
    top.title("BLOOD BANK")
    top.geometry("1024x720")
    #top.configure(background='#FF8F8F')
    Label(top,text="Enter the blood group: ").place(x=40,y=40,w=250,h=20)
    e=Entry(top).place(x=250,y=40)
    b2=Button(top,text="Back",command=lambda : stop(top)).place(x=300,y=80)
    b=Button(top,text="ENTER",command=lambda : grid1(e.get())).place(x=200,y=80)
    top.mainloop()


top.mainloop()
		
	
