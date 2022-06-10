from tkinter import*
import mysql.connector
import pymysql #pip install pymysql
from tkinter import messagebox

class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("login Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")
        #Background colour
        left_lbl=Label(self.root,bg="#08A3D2",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=600)

        right_lbl=Label(self.root,bg="#031F3C",bd=0)
        right_lbl.place(x=600,y=0,relheight=1,relwidth=1)
        
        #frame
        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=170,y=150,width=800,height=500)
        title=Label(login_frame,text="LOGIN HERE",font=("times new roman",30,"bold"),bg="white",fg="#08A3D2").place(x=250,y=50)
        
        email=Label(login_frame,text="EMAIL ADDRESS",font=("times new roman",18,"bold"),bg="white",fg="gray").place(x=250,y=150)
        self.txt_email=Entry(login_frame,font=("times new roman",20,),bg="lightgray")
        self.txt_email.place(x=250,y=180,width=350,height=35)
        
        pass_=Label(login_frame,text="PASSWORD",font=("times new roman",20,"bold"),bg="white",fg="gray").place(x=250,y=250)
        self.txt_pass_=Entry(login_frame,font=("times new roman",20,),bg="lightgray",show='*')
        self.txt_pass_.place(x=250,y=280,width=350,height=35)
        #button
        btn_reg=Button(login_frame,cursor="hand2",command=self.register_window,text="Register new Account?",font=("times new roman",14),bg="white",bd=0,fg="#B00857").place(x=250,y=320)
        btn_login=Button(login_frame,text="Login",command=self.login,font=("times new roman",20,"bold"),fg="white",bg="#B00857",cursor="hand2").place(x=250,y=360,width=180,height=40)
    
    # close frame ....#
        close_frame=Frame(self.root,bg="white")
        close_frame.place(x=1170,y=300,width=300,height=200)
        title1=Label(close_frame,text="Close From Here",font=("times new roman",30,"bold"),bg="red",fg="#08A3D2").place(x=0,y=0)
        title2=Label(close_frame,text="Close the window\n if it is not Required\n now",font=("times new roman",15,"bold")).place(x=60,y=60)
        close_btn=Button(close_frame,text="Close",command=self.close,font=("times new roman",20,"bold"),fg="white",bg="#B00857",cursor="hand2").grid(row=6,column=2,pady=140,padx=110)

    def close(self):
        self.root.destroy()
    #def check(self): 
        #messagebox.askquestion("Form", 
                          #"are you 18+",  
                          #icon ='question')

    #clear output after clicking ok
    def clear(self):
        self.txt_email.delete(0,END)
        self.txt_pass_.delete(0,END)
        

    def register_window(self):
        self.root.destroy()
        import register

    def student_window(self):
        self.root.destroy()
        import student

    def login(self):
        if self.txt_email.get()=="" or self.txt_pass_.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                # mydb = mysql.connector.connect(
                # host="localhost",
                # user="root",
                # password=""
                # )
                con=mysql.connector.connect(host="localhost",user="root",password="password",database="employee2")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s and password=%s",(self.txt_email.get(),self.txt_pass_.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Email-Id or Password",parent=self.root)
                else:
                    messagebox.showinfo("Success","Welcome!!\n You are successfully logged in",parent=self.root)
                    con.close()
                    self.clear()
                    self.student_window()
            except Exception as es:
                messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)
           
root=Tk()
obj=Login_window(root)
root.mainloop()