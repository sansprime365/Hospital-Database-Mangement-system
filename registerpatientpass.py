from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import tkinter

class patientloginID:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x600+0+0")
        self.root.title("Patient ID")

        self.var_username=StringVar()
        self.var_securityq=StringVar()
        self.var_securityans=StringVar()
        self.var_Setpass=StringVar()
        self.var_Confirmpass=StringVar()

        main_frame=Frame(self.root,bd=2,bg="powder blue")
        main_frame.place(x=0,y=0,width=900,height=600)

        main_frame=Frame(main_frame,bd=2,bg="black")
        main_frame.place(x=45,y=110,width=800,height=370)

        label=Label(main_frame,text="Patient UserID Registration",font=("times new roman",30,"bold"),bg="black",fg="white")
        label.place(x=160,y=0,width=480,height=60)

        name1=Label(main_frame,text="Patient User Name",font=("times new roman",15,"bold"),bg="black",fg="white")
        name1.place(x=60,y=60,width=200,height=60)
        name=ttk.Entry(main_frame,textvariable=self.var_username,font=("times new roman",15,"bold"),width=20)
        name.place(x=80,y=100)

        security1=Label(main_frame,text="Security Question:",font=("times new roman",15,"bold"),bg="black",fg="white")
        security1.place(x=60,y=140,width=200,height=60)
        security_combo=ttk.Combobox(main_frame,textvariable=self.var_securityq,font=("times new roman",15,"bold"),state="readonly",width=20)
        security_combo["values"]=("Select Question","bestie's name","nickname","pet's name","school name","favorite song","favourite colour")
        security_combo.current(0)
        security_combo.place(x=80,y=180)

        security2=Label(main_frame,text="Security Answer:",font=("times new roman",15,"bold"),bg="black",fg="white")
        security2.place(x=405,y=140,width=200,height=60)
        securitypa=ttk.Entry(main_frame,textvariable=self.var_securityans,font=("times new roman",15,"bold"),width=20)
        securitypa.place(x=430,y=180)

        pass1=Label(main_frame,text="Set Password",font=("times new roman",15,"bold"),bg="black",fg="white")
        pass1.place(x=70,y=210,width=140,height=60)
        passwrd=ttk.Entry(main_frame,textvariable=self.var_Setpass,font=("times new roman",15,"bold"),width=20)
        passwrd.place(x=80,y=250)

        pass1=Label(main_frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="black",fg="white")
        pass1.place(x=405,y=210,width=200,height=60)
        passwrd=ttk.Entry(main_frame,textvariable=self.var_Confirmpass,font=("times new roman",15,"bold"),width=20)
        passwrd.place(x=430,y=250)

        rgstrbtn1=Button(main_frame,text="Register",command=self.registerdata,width=11,font=("times new roman",16,"bold"),bg="powder blue",fg="black",activebackground="white",borderwidth=0)
        rgstrbtn1.place(y=320,x=480)

        loginbtn1=Button(main_frame,text="Login",command=self.LoginBackButton,width=11,font=("times new roman",16,"bold"),bg="powder blue",fg="black",activebackground="white",borderwidth=0)
        loginbtn1.place(y=320,x=620)

    def registerdata(self):
        if self.var_username.get()=="" or self.var_securityq.get()=="" or self.var_securityans.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif self.var_Setpass.get()!=self.var_Confirmpass.get():
            messagebox.showerror("Error","Password must be same!")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Sh@15062005",database="project_database")
            my_cursor=conn.cursor()
            query=("select * from patientuserid where username=%s")
            value=(self.var_username.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","UserID already exists use another one")
            else:
                my_cursor.execute("insert into patientuserid values(%s,%s,%s,%s,%s)",(
                                                                                        self.var_username.get(),
                                                                                        self.var_securityq.get(),
                                                                                        self.var_securityans.get(),
                                                                                        self.var_Setpass.get(),
                                                                                        self.var_Confirmpass.get()
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registered patient data")
    def LoginBackButton(self):
        self.Exit=tkinter.messagebox.askyesno("SAGE AI MANAGEMENT SYSTEM","Do you want to return to login page?",parent=self.root)
        if self.Exit >0:
            self.root.destroy()
        else:
            return



if __name__ =="__main__":
    root=Tk()
    obj=patientloginID(root)
    root.mainloop()