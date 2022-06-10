from tkinter import*
#from PIL import Image,ImageTk #pip install pillow
from tkinter import messagebox
import mysql.connector
import pymysql #pip install pymysql
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registerartion Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #background image

        left_lbl=Label(self.root,bg="#08A3D2",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=600)

        right_lbl=Label(self.root,bg="#031F3C",bd=0)
        right_lbl.place(x=600,y=0,relheight=1,relwidth=1)
        #self.bg=ImageTk.PhotoImage(file="bg2.jpeg")
        #bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)
        #self.left=ImageTk.PhotoImage(file="bg1.jpeg")
        #left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)
        #register frame
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)
        
        title=Label(frame1,text="Register Here",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)
        
        #1st row
        f_name=Label(frame1,text="First name",font=("times new roman",15,"bold"),bg="white",fg="grey").place(x=50,y=100)
        self.txt__fname=Entry(frame1,font=("times new roman",20),bg="lightgrey")
        self.txt__fname.place(x=50,y=130,width=250)
        
        l_name=Label(frame1,text="Last name",font=("times new roman",15,"bold"),bg="white",fg="grey").place(x=370,y=100)
        self.txt__lname=Entry(frame1,font=("times new roman",20),bg="lightgrey")
        self.txt__lname.place(x=370,y=130,width=250)
        
        #2nd row
        contact=Label(frame1,text="Contact number",font=("times new roman",15,"bold"),bg="white",fg="grey").place(x=50,y=170)
        self.txt__contact=Entry(frame1,font=("times new roman",20),bg="lightgrey")
        self.txt__contact.place(x=50,y=200,width=250)
        
        email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="grey").place(x=370,y=170)
        self.txt__email=Entry(frame1,font=("times new roman",20),bg="lightgrey")
        self.txt__email.place(x=370,y=200,width=250)
        
        #third row
        password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="grey").place(x=50,y=240)
        self.txt__password=Entry(frame1,font=("times new roman",20),bg="lightgrey",show='*')
        self.txt__password.place(x=50,y=270,width=250)
        
        cpassword=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="grey").place(x=370,y=240)
        self.txt__cpassword=Entry(frame1,font=("times new roman",20),bg="lightgrey",show='*')
        self.txt__cpassword.place(x=370,y=270,width=250)
        
        #terms
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Terms & Conditions",variable=self.var_chk,cursor="hand2",onvalue=1,offvalue=0,font=("times new roman",12),bg="white").place(x=50,y=310)
        btn_register=Button(frame1,text="Register Now",bg="#B00857",cursor="hand2",command=self.register_data,font=("times new roman",20,"bold")).place(x=270,y=390)
        
        lb=Label(self.root,text="If You already Have An Account Then Sign In",font=("times new roman",16,"bold"),fg="grey").place(x=50,y=350)
        btn_log=Button(self.root,text="Sign In",bg="red",command=self.login_window,cursor="hand2",font=("times new roman",20,"bold")).place(x=200,y=390,width=180)
    
    def login_window(self):
        self.root.destroy()
        import Login
    #to clear inputs after registeration
    def clear(self):
        self.txt__fname.delete(0,END)
        self.txt__lname.delete(0,END)
        self.txt__contact.delete(0,END)
        self.txt__email.delete(0,END)
        self.txt__password.delete(0,END)
        self.txt__cpassword.delete(0,END)
        
    def register_data(self):
        if self.txt__fname.get().isdigit()==True or self.txt__lname.get().isdigit()==True or self.txt__contact.get().isdigit()==False:
            messagebox.showerror("Error","Invalid Input",parent=self.root)
        if self.txt__fname.get()=="" or self.txt__contact.get()=="" or self.txt__email.get()=="" or self.txt__password.get()=="" or self.txt__cpassword.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif self.txt__password.get()!=self.txt__cpassword.get():
            messagebox.showerror("Error","Password & Confirm Password should be same",parent=self.root)
        elif self.var_chk.get()==0:#if not checked checkbox
            messagebox.showerror("Error","Please Agree our Terms & Conditions",parent=self.root)   
        else:
            try:
                con=mysql.connector.connect(host="localhost",user="root",password="password",database="employee2")
                cur=con.cursor()
                # sql = """SELECT * FROM `steps` WHERE stepNo = %s"""
                cur.execute("select * from employee where email= %s",(self.txt__email.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already Exist,Please try with another email",parent=self.root)
                else:    
                    cur.execute("insert into employee(f_name,l_name,contact,email,password)values(%s,%s,%s,%s,%s)",
                                (self.txt__fname.get(),
                                 self.txt__lname.get(),
                                 self.txt__contact.get(),
                                 self.txt__email.get(),
                                 self.txt__password.get()
                                ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Registered Successfully",parent=self.root)
                    self.clear()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to :{str(es)}",parent=self.root) 
                           
root=Tk()
obj=Register(root)
root.mainloop()