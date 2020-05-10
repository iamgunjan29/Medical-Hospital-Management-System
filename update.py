#update the appointments
from tkinter import  *
import tkinter.messagebox
import sqlite3

conn=sqlite3.connect('database.db')
c=conn.cursor()

class Application:
   def __init__(self,master):
       self.master=master
       #heading label
       self.heading= Label(master,text="Update Appointments",fg='steelblue',font=('arial 40 bold'))
       self.heading.place(x=150,y=0)

       #search criteria-->name
       self.name=Label(master,text="Enter Patient's name",font=('arial 18 bold'))
       self.name.place(x=0,y=60)

       #entry for the name
       self.namenet=Entry(master,width=30)
       self.namenet.place(x=280,y=62)

       #search button
       self.search=Button(master,text='Search',width=12,height=1,bg='steelblue',command=self.search_db)
       self.search.place(x=350,y=102)

    #function to search
   def search_db(self):
       self.input=self.namenet.get()
       #execute sql

       sql="SELECT * FROM appointments WHERE name LIKE ?"
       self.res=c.execute(sql,(self.input,))
       for self.row in self.res:
         self.name1=self.row[1]
         self.age=self.row[2]
         self.gender=self.row[3]
         self.location=self.row[4]
         self.time=self.row[5]
         self.phone=self.row[6]
         self.date=self.row[7]
         self.pro=self.row[8]
         self.dep=self.row[9]
         self.doc=self.row[10]

       #creating the update form
       self.uname=Label(self.master,text="Patient's Name",font=('arial 18 bold'))
       self.uname.place(x=0,y=140)

       self.uage = Label(self.master, text="Age", font=('arial 18 bold'))
       self.uage.place(x=0, y=180)

       self.ugender = Label(self.master, text="Gender", font=('arial 18 bold'))
       self.ugender.place(x=0, y=220)

       self.ulocation = Label(self.master, text="Location", font=('arial 18 bold'))
       self.ulocation.place(x=0, y=260)

       self.utime = Label(self.master, text="Appointment Time", font=('arial 18 bold'))
       self.utime.place(x=0, y=300)

       self.uphone = Label(self.master, text="Phone Number", font=('arial 18 bold'))
       self.uphone.place(x=0, y=340)

       self.udate = Label(self.master, text="Appointment date", font=('arial 18 bold'))
       self.udate.place(x=0, y=380)

       self.upro = Label(self.master, text="Problem", font=('arial 18 bold'))
       self.upro.place(x=0, y=420)

       self.udep = Label(self.master, text="Department", font=('arial 18 bold'))
       self.udep.place(x=0, y=460)

       self.udoc = Label(self.master, text="Consult Doctor", font=('arial 18 bold'))
       self.udoc.place(x=0, y=500)

       #enteries for each label======================================
       #    filing the search result in the entry box to update
       self.ent1=Entry(self.master,width=30)
       self.ent1.place(x=300,y=140)
       self.ent1.insert(END,str(self.name1))

       self.ent2 = Entry(self.master, width=30)
       self.ent2.place(x=300, y=180)
       self.ent2.insert(END, str(self.age))

       self.ent3 = Entry(self.master, width=30)
       self.ent3.place(x=300, y=220)
       self.ent3.insert(END, str(self.gender))

       self.ent4 = Entry(self.master, width=30)
       self.ent4.place(x=300, y=260)
       self.ent4.insert(END, str(self.location))

       self.ent5 = Entry(self.master, width=30)
       self.ent5.place(x=300, y=300)
       self.ent5.insert(END, str(self.time))

       self.ent6 = Entry(self.master, width=30)
       self.ent6.place(x=300, y=340)
       self.ent6.insert(END, str(self.phone))

       self.ent7 = Entry(self.master, width=30)
       self.ent7.place(x=300, y=380)
       self.ent7.insert(END, str(self.date))

       self.ent8 = Entry(self.master, width=30)
       self.ent8.place(x=300, y=420)
       self.ent8.insert(END, str(self.pro))

       self.ent9 = Entry(self.master, width=30)
       self.ent9.place(x=300, y=460)
       self.ent9.insert(END, str(self.dep))

       self.ent10 = Entry(self.master, width=30)
       self.ent10.place(x=300, y=500)
       self.ent10.insert(END, str(self.doc))

       #button  to execute update
       self.update=Button(self.master,text="Update",width=20,height=2,bg='lightblue',command=self.update_db)
       self.update.place(x=400,y=540)

       #button to delete appointment
       self.delete=Button(self.master,text="Delete",width=20,height=2,bg='red',command=self.delete_db)
       self.delete.place(x=150,y=540)

       #button to show all patients
       # self.all = Button(self.master, text="All Patients", width=20, height=2, bg='blue', command=self.all_db)
       # self.all.place(x=700, y=380)

   def update_db(self):
        self.var1=self.ent1.get()#update name
        self.var2=self.ent2.get()#uppdate age
        self.var3=self.ent3.get()# update gender
        self.var4=self.ent4.get() #update locatin
        self.var5=self.ent5.get()#updated phone
        self.var6=self.ent6.get()#updated time
        self.var7=self.ent7.get()#updatedate
        self.var8=self.ent8.get()#updatepro
        self.var9=self.ent9.get()#updatedep
        self.var10=self.ent10.get()#updatedoc

        query="UPDATE appointments SET name=?,age=?,gender=?,location=?,phone=?,scheduledtime=?,scheduleddate=?,problem=?,department=?,doctor=? WHERE name LIKE ?"
        c.execute(query,(self.var1,self.var2,self.var3,self.var4,self.var5,self.var6,self.var7,self.var8,self.var9,self.var10,self.namenet.get()))
        conn.commit()
        tkinter.messagebox.showinfo("Update","Sucessfully Updated.") #tom shrama #Tom Hank

   def delete_db(self):
       sql2="DELETE FROM appointments WHERE name LIKE ?"
       c.execute(sql2,(self.namenet.get(),))
       conn.commit()
       tkinter.messagebox.showinfo("Success","Deleted Successfully")
       self.ent1.destroy()
       self.ent2.destroy()
       self.ent3.destroy()
       self.ent4.destroy()
       self.ent5.destroy()
       self.ent6.destroy()
       self.ent7.destroy()
       self.ent8.destroy()
       self.ent9.destroy()
       self.ent10.destroy()

  #def all_db(self):
       #sql3="SELECT * FROM appointments"
       #c.execute(sql3)
      # conn.commit()

#creating object
root=Tk()
b=Application(root)
root.geometry("1200x720+0+0")
root.resizable(False,False)
root.mainloop()


