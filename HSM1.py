#import modules

from tkinter import *
import sqlite3
import  tkinter.messagebox

# connectr to database
conn=sqlite3.connect('database.db')
print("Succesfully Connected")
 #cursor to move around the database
c=conn.cursor()

#empty list to later append the ids from the  database
ids=[]


 #tkinter application
class Application :
    def __init__(self,master):
        self.master=master

    #creating frames in the master
        self.left=Frame(master,width=800,height=720,bg='blue')
        self.left.pack(side=LEFT)

        self.right=Frame(master,width=400,height=720,bg='blue')
        self.right.pack(side=RIGHT)

        #lables for the  window
        self.heading=Label(self.left,text='GWALIOR HOSPITAL APPOINTMENTS',font=('arial 25 bold'),fg='black',bg='blue')
        self.heading.place(x=0,y=0)

         #patients name

        self.name=Label(self.left,text="Patient's name",font=('arial 18 bold'),fg='black',bg='blue')
        self.name.place(x=0,y=100)

        # age

        self.age = Label(self.left, text="Patient's Age", font=('arial 18 bold'), fg='black', bg='blue')
        self.age.place(x=0, y=140)

        #gender

        self.gender= Label(self.left, text="Patient's gender", font=('arial 18 bold'), fg='black', bg='blue')
        self.gender.place(x=0, y=180)

        #location
        self.location = Label(self.left, text="Patient's Location", font=('arial 18 bold'), fg='black', bg='blue')
        self.location.place(x=0, y=220)

        #appointment time

        self.time = Label(self.left, text="Appointment Time", font=('arial 18 bold'), fg='black', bg='blue')
        self.time.place(x=0, y=260)

        #phone
        self.phone = Label(self.left, text="Phone Number", font=('arial 18 bold'), fg='black', bg='blue')
        self.phone.place(x=0, y=300)

        #apponintment date

        self.date = Label(self.left, text="Appointment Date", font=('arial 18 bold'), fg='black', bg='blue')
        self.date.place(x=0,y=340)

        #problem

        self.pro = Label(self.left, text="Problem", font=('arial 18 bold'), fg='black', bg='blue')
        self.pro.place(x=0, y=380)

        #department

        self.dep = Label(self.left, text="Department", font=('arial 18 bold'), fg='black', bg='blue')
        self.dep.place(x=0, y=420)


        #Entiries for all labels
        self.name_ent=Entry(self.left,width=30)
        self.name_ent.place(x=250,y=100)

        self.age_ent = Entry(self.left, width=30)
        self.age_ent.place(x=250, y=140)

        self.gender_ent = Entry(self.left, width=30)
        self.gender_ent.place(x=250, y=180)

        self.location_ent = Entry(self.left, width=30)
        self.location_ent.place(x=250, y=220)

        self.time_ent = Entry(self.left, width=30)
        self.time_ent.place(x=250, y=260)

        self.phone_ent=Entry(self.left,width=30)
        self.phone_ent.place(x=250,y=300)

        self.date_ent = Entry(self.left, width=30)
        self.date_ent.place(x=250, y=340)

        self.pro_ent = Entry(self.left, width=30)
        self.pro_ent.place(x=250, y=380)

        self.dep_ent = Entry(self.left, width=30)
        self.dep_ent.place(x=250, y=420)

        # button to perform a command
        self.submit=Button(self.left, text="Add Appointment",width=20,height=2,bg='steelblue',command=self.add_appontment)
        self.submit.place(x=300,y=460)

        # getting the number of appointments fixed to view in the log
        sql2 = "SELECT ID FROM appointments"
        self.result = c.execute(sql2)
        for self.row in self.result:
            self.id = self.row[0]
            ids.append(self.id)

        # ordering the  ids
        self.new = sorted(ids)
        self.final_id = self.new[len(ids) - 1]
        #displaying the logs in our right frame
        self.logs=Label(self.right,text="",font=('arial 28 bold'),fg='white',bg='blue')
        self.logs.place(x=0,y=0)


        self.box=Text(self.right,width=100,height=40)
        self.box.place(x=20,y=10)
        self.box.insert(END,"Total Appointments till now:"+" "+str(self.final_id))

    # fuction to call when the submit buttonself.box.insert(END, 'Appointment fixed' + " " + str(self.final_id)) is clicked
    def add_appontment(self):
     #geeting User Inputs
      self.val1=self.name_ent.get()
      self.val2=self.age_ent.get()
      self.val3=self.gender_ent.get()
      self.val4=self.location_ent.get()
      self.val5=self.time_ent.get()
      self.val6=self.phone_ent.get()
      self.val7=self.date_ent.get()
      self.val8=self.pro_ent.get()
      self.val9=self.dep_ent.get()

      #checking if the user input is empty
      if self.val1=='' or self.val2=='' or self.val3=='' or self.val4=='' or self.val5=='' :
          tkinter.messagebox.showinfo("Warming","Please Fill Up All Boxes")
      else:
          #now we add to database
          sql="INSERT INTO 'appointments'(name,age,gender,location,scheduledtime,phone,scheduleddate,problem,department) VALUES(?,?,?,?,?,?,?,?,?)"
          c.execute(sql,(self.val1,self.val2,self.val3,self.val4,self.val5,self.val6,self.val7,self.val8,self.val9))
          conn.commit()
          tkinter.messagebox.showinfo("Success","Appointment For"+" "+str(self.val1)+"has been created")

          self.box.insert(END, 'Appointment fixed for' + " " + str(self.val1)+" "+"at"+" "+str(self.val5))


#creating the object
root=Tk()
b=Application(root)
root.geometry("1200x720+0+0")
root.resizable(False,False)
root.mainloop()
