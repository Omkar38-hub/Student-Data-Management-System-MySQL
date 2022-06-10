from tkinter import *
import mysql.connector
from tkinter import ttk
import pymysql 
from tkinter import messagebox
class student:
        def __init__(self,root):
                self.root=root
                self.root.title("Student Management System")
                self.root.geometry("1350x700+0+0")

                title=Label(self.root,text="Student management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="yellow",fg="red")
                title.pack(fill=X)

                #...logout button...#
                lgo_frame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
                lgo_frame.place(x=1400,y=27,width=87,height=32.5)
                logoutbtn=Button(lgo_frame,text="LogOut",command=self.logout_window,width=10,bg="red").grid(row=0,column=0)
                
                #..all vriables...#
                self.Roll_No_var=StringVar()
                self.name=StringVar()
                self.email=StringVar()
                self.gender=StringVar()
                self.contact=StringVar()
                self.dob=StringVar()
                self.search_by=StringVar()
                self.search_txt=StringVar()

        #    manage frame  #
                manage_frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
                manage_frame.place(x=20,y=100,width=550,height=670)
                m_title=Label(manage_frame,text="Manage students",bg="crimson",fg="white",font=("times new roman",25,"bold"))
                m_title.grid(row=0,columnspan=2,pady=20)
                #roll
                lbl_roll=Label(manage_frame,text="Roll Number",bg="crimson",fg="white",font=("times new roman",20,"bold"))
                lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky='w')
                txt_roll=Entry(manage_frame,textvariable=self.Roll_No_var,font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
                txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky='w')
                #name
                lbl_name=Label(manage_frame,text="Name",bg="crimson",fg="white",font=("times new roman",20,"bold"))
                lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky='w')
                txt_name=Entry(manage_frame,textvariable=self.name,font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
                txt_name.grid(row=2,column=1,pady=10,padx=20,sticky='w')
                #email-id
                lbl_email=Label(manage_frame,text="Email-Id",bg="crimson",fg="white",font=("times new roman",20,"bold"))
                lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky='w')
                txt_email=Entry(manage_frame,textvariable=self.email,font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
                txt_email.grid(row=3,column=1,pady=10,padx=20,sticky='w')
                #gender
                lbl_gen=Label(manage_frame,text="Gender",bg="crimson",fg="white",font=("times new roman",20,"bold"))
                lbl_gen.grid(row=4,column=0,pady=10,padx=20,sticky='w')
                combo_gen=ttk.Combobox(manage_frame,textvariable=self.gender,font=("times new roman",20,"bold"),state='readonly')
                combo_gen['values']=('Male','Female','Others')
                combo_gen.grid(row=4,column=1,pady=10,padx=20,sticky='w')

                #contact
                lbl_contact=Label(manage_frame,text="Contact",bg="crimson",fg="white",font=("times new roman",20,"bold"))
                lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky='w')
                txt_contact=Entry(manage_frame,textvariable=self.contact,font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
                txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky='w')
                #DOB
                lbl_dob=Label(manage_frame,text="D.O.B",bg="crimson",fg="white",font=("times new roman",20,"bold"))
                lbl_dob.grid(row=6,column=0,pady=10,padx=20,sticky='w')
                txt_dob=Entry(manage_frame,textvariable=self.dob,font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
                txt_dob.grid(row=6,column=1,pady=10,padx=20,sticky='w')
                #address
                lbl_addr=Label(manage_frame,text="Address",bg="crimson",fg="white",font=("times new roman",20,"bold"))
                lbl_addr.grid(row=7,column=0,pady=10,padx=20,sticky='w')
                self.txt_addr=Text(manage_frame,width=29,height=3,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
                self.txt_addr.grid(row=7,column=1,pady=10,padx=20,sticky='w')



        #......button frame....#
                btn_frame=Frame(manage_frame,bd=4,relief=RIDGE,bg="crimson")
                btn_frame.place(x=60,y=580,width=420)
                #add button
                addbtn=Button(btn_frame,text="Add",command=self.add_students,width=10).grid(row=0,column=0,padx=10,pady=10)
                upbtn=Button(btn_frame,text="Update",command=self.update_data,width=10).grid(row=0,column=1,padx=10,pady=10)
                delbtn=Button(btn_frame,command=self.delete_data,text="Delete",width=10).grid(row=0,column=2,padx=10,pady=10)
                clrbtn=Button(btn_frame,command=self.clear,text="Clear",width=10).grid(row=0,column=3,padx=10,pady=10)
                

        #    detail frame  #
                detail_frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
                detail_frame.place(x=600,y=100,width=900,height=670)

                lbl_search=Label(detail_frame,text="Search By",bg="crimson",fg="white",font=("times new roman",20,"bold"))
                lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky='w')
                
                combo_search=ttk.Combobox(detail_frame,textvariable=self.search_by,width=15,font=("times new roman",15,"bold"),state='readonly')
                combo_search['values']=('roll_no','name','email')
                combo_search.grid(row=0,column=1,pady=10,padx=20,sticky='w')

                
                txt_search=Entry(detail_frame,width=15,textvariable=self.search_txt,font=("times new roman",15,"bold"))
                txt_search.grid(row=0,column=2,pady=10,padx=20,sticky='w')
                searchbtn=Button(detail_frame,command=self.search_data,text="Search",width=15).grid(row=0,column=3,padx=10,pady=10)
                showbtn=Button(detail_frame,text="Show all",command=self.fetch_data,width=15).grid(row=0,column=4,padx=10,pady=10)

        #...... table frame ...#
                table_frame=Frame(detail_frame,bd=4,relief=RIDGE,bg="crimson")
                table_frame.place(x=20,y=70,width=850,height=560)

                #for scrollbar
                scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
                scroll_y=Scrollbar(table_frame,orient=VERTICAL)
                #for tree view ttk module is used
                self.student_table=ttk.Treeview(table_frame,columns=('roll','name','email','gender','contact',"dob",'Address'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)

                scroll_x.config(command=self.student_table.xview)
                scroll_y.config(command=self.student_table.yview)

                self.student_table.heading("roll",text="Roll No.")
                self.student_table.heading("name",text="Name")
                self.student_table.heading("email",text="Email-Id")
                self.student_table.heading("gender",text="Gender")
                self.student_table.heading("contact",text="Contact")
                self.student_table.heading("dob",text="D.O.B")
                self.student_table.heading("Address",text="Address")

                self.student_table['show']='headings'

                self.student_table.column("roll",width=100)#set the heading column
                self.student_table.column("name",width=150)
                self.student_table.column("email",width=150)
                self.student_table.column("gender",width=50)
                self.student_table.column("contact",width=150)
                self.student_table.column("dob",width=130)
                self.student_table.column("Address",width=150)
                self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
                self.student_table.pack(fill=BOTH,expand=1)# for expanding to whole screen
                
                self.fetch_data()


        def add_students(self):
                if self.name.get().isdigit()==True or self.contact.get().isdigit()==False:
                        messagebox.showerror("Error","Invalid Input")
                if self.Roll_No_var.get()=="" or self.name.get()=="" or self.email.get()=="" or self.gender.get()=="" or self.contact.get()=="" or self.dob.get()=="":
                        messagebox.showerror("Error","All Fields Are Required")
                else:
                        con=mysql.connector.connect(host="localhost",user="root",password="password",database="employee2")
                        cur=con.cursor()
                        cur.execute("insert into stm(roll_no,name,email,gender,contact,dob,address) values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                                self.name.get(),
                                                                                self.email.get(),
                                                                                self.gender.get(),
                                                                                self.contact.get(),
                                                                                self.dob.get(),
                                                                                self.txt_addr.get('1.0',END)
                                                                                ))#finds text from beginning to end
                        con.commit()
                        self.fetch_data()
                        self.clear()
                        con.close() 
                        messagebox.showinfo("Success","Record Has Been Inserted") 

        def fetch_data(self):
                con=mysql.connector.connect(host="localhost",user="root",password="password",database="employee2")
                cur=con.cursor() 
                cur.execute("select * from stm ORDER BY roll_no")
                rows=cur.fetchall()
                if len(rows)!=0:
                        self.student_table.delete(*self.student_table.get_children())
                        for row in rows:
                                self.student_table.insert('',END,values=row)
                        con.commit()
                con.close()
        

        def clear(self):
                self.Roll_No_var.set("")
                self.name.set(""),
                self.email.set(""),
                self.gender.set(""),
                self.contact.set(""),
                self.dob.set(""),
                self.txt_addr.delete('1.0',END)
                
        def get_cursor(self,ev):
                cursor_row=self.student_table.focus()
                content=self.student_table.item(cursor_row)
                row=content['values']
                self.Roll_No_var.set(row[0])
                self.name.set(row[1]),
                self.email.set(row[2]),
                self.gender.set(row[3]),
                self.contact.set(row[4]),
                self.dob.set(row[5]),
                self.txt_addr.delete('1.0',END),
                self.txt_addr.insert(END,row[6])
        
        def update_data(self):
                if self.name.get().isdigit()==True or self.contact.get().isdigit()==False:
                        messagebox.showerror("Error","Invalid Input")
                else:
                        con=mysql.connector.connect(host="localhost",user="root",password="password",database="employee2")
                        cur=con.cursor()
                        cur.execute("update stm set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(
                                                                                self.name.get(),
                                                                                self.email.get(),
                                                                                self.gender.get(),
                                                                                self.contact.get(),
                                                                                self.dob.get(),
                                                                                self.txt_addr.get('1.0',END),
                                                                                self.Roll_No_var.get()
                                                                                ))#finds text from beginning to end
                        con.commit()
                        self.fetch_data()
                        self.clear()
                        con.close() 
                        messagebox.showinfo("Success","Record Has Been Updated")

        def delete_data(self):
                con=mysql.connector.connect(host="localhost",user="root",password="password",database="employee2")
                cur=con.cursor() 
                cur.execute("delete from stm where roll_no=%s",self.Roll_No_var.get())
                con.commit()
                self.fetch_data()
                self.clear()
                con.close()
                messagebox.showinfo("Success","Record Has Been Deleted") 
        
        def search_data(self):
                con=mysql.connector.connect(host="localhost",user="root",password="password",database="employee2")
                cur=con.cursor() 
                cur.execute("select * from stm where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                        self.student_table.delete(*self.student_table.get_children())
                        for row in rows:
                                self.student_table.insert('',END,values=row)
                        con.commit()
                con.close()
        
        def logout_window(self):
                self.root.destroy()
                import Login

root=Tk()
ob=student(root)
root.mainloop()