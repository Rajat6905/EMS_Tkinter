import re
import tkinter as tk
from bean import emp
from ui_Services import main
from tkinter import messagebox
from tkinter import ttk
import csv
from fpdf import FPDF


class MyFirstGUI:
    def __init__(self, master,top):
        self.top=top
        self.master = master
        
    def mainWindow(self):
        self.master.geometry("1000x600")    
        self.master.title("Employee Management System")
        bar=tk.Menu(self.master)
        fileMenu = tk.Menu(bar ,tearoff =0)
        fileMenu.add_command(label="Add Users",font=('arial', 14),command=lambda:self.manage_users())
        fileMenu.add_command(label="Search User",font=('arial', 14),command=lambda:self.search_user_ui())
        fileMenu.add_command(label="View User",font=('arial', 14),command=lambda:self.view_user())
        fileMenu.add_command(label="Delete User",font=('arial', 14),command=lambda:self.delete_ui())
        fileMenu.add_command(label="Edit User",font=('arial', 14),command=lambda:self.edit_ui())

        bar.add_cascade(label="Manage Users",font=('arial', 14),menu=fileMenu)
        
        reportMenu=tk.Menu(bar,tearoff=0)
        reportMenu.add_command(label="User Reports",font=('arial', 14),command=lambda:self.table())
        bar.add_cascade(label="Reports",font=('arial', 14),menu=reportMenu)
        bar.add_command(label="Exit",font=('arial', 14),command=self.logout)
        self.master.config(menu=bar)
    def manage_users(self):
        for obj in self.master.winfo_children():
            obj.destroy()
        self.mainWindow()
        tk.Label(self.master, text="Manage users").grid(row=0,padx=10,pady=10)
        tk.Label(self.master, text="Company Inof---").grid(row=1,padx=10,pady=10)
        tk.Label(self.master, text="User Id").grid(row=2)
        tk.Label(self.master, text="User Name").grid(row=3,pady=10)
        tk.Label(self.master, text="Password ").grid(row=4,pady=10)
        tk.Label(self.master, text="Confirm Password ").grid(row=5,pady=10)
        
        tk.Label(self.master, text="User Type ").grid(row=6,pady=10)
        tk.Label(self.master, text="User Status ").grid(row=7,pady=10)
        self.id=tk.Label(self.master,text=main.returnid())
        self.id.grid(row=2, column=2)
        self.name = tk.Entry(self.master,width=20, font=('arial', 12))
        self.name.grid(row=3, column=2)
        self.password = tk.Entry(self.master,width=20, font=('arial', 12))
        self.password.grid(row=4, column=2)
        
        self.confirm_password = tk.Entry(self.master,width=20, font=('arial', 12))
        self.confirm_password.grid(row=5, column=2)
        
        self.v = tk.IntVar()
        self.v.set(2)
        tk.Radiobutton(root, text="Admin", variable=self.v, value=1).grid(row=6,column=2)
        tk.Radiobutton(root, text="User", variable=self.v, value=2).grid(row=6,column=3)
        
        
        self.ty = tk.IntVar()
        self.ty.set(1)
        tk.Radiobutton(root, text="Active", variable=self.ty, value=1).grid(row=7,column=2)
        tk.Radiobutton(root, text="Inactive", variable=self.ty, value=2).grid(row=7,column=3)
        tk.Label(self.master, text="Personal Inof---").grid(row=8,padx=10,pady=10)   
        tk.Label(self.master, text="Mobile Number ").grid(row=9,pady=10)
        tk.Label(self.master, text="DOB ").grid(row=10,pady=10)
        tk.Label(self.master, text="Email ").grid(row=11,pady=10)
        
        self.contact = tk.Entry(self.master,width=20, font=('arial', 12))
        self.contact.grid(row=9, column=2)
        
        self.DOB=tk.Entry(self.master,width=20, font=('arial', 12))
        self.DOB.grid(row=10,column=2)
        
        self.email=tk.Entry(self.master,width=20, font=('arial', 12))
        self.email.grid(row=11,column=2)
        tk.Button(self.master, text='Save',
                  command=lambda:self.addButton(),height=2).grid(row=14,column=1,padx=20,pady=20 )
        
    
    def add(self):
        
        u_id=str(self.id.cget("text"))
        usertype= self.v.get()
        if usertype==1:
            usertype="Admin"
        else:
            usertype="User"
            
        userStatus=self.ty.get()
        if userStatus==1:
            userStatus="Active"
        else:
            userStatus="Inactive"
        obj=emp()
        obj.setId(u_id)
        obj.setName(self.name.get())
        obj.setPassword(self.password.get())
        obj.setuser_type(usertype)
        obj.setuser_status(userStatus)
        obj.setcontact(self.contact.get())
        obj.setdob(self.DOB.get())
        obj.setemail(self.email.get())
        return obj
    def addButton(self):
        objadd=self.add()
        if len(objadd.getName())==0:
            tk.messagebox.showerror("Error", "Please Enter your UserName")
        elif len(objadd.getPassword())==0:
              tk.messagebox.showerror("Error", "Please Enter your Password")
            
        elif len(objadd.getcontact())<10:
            tk.messagebox.showerror("Error", "Please Enter your Valid Mobile Number")
        elif len(objadd.getdob())==0:
            tk.messagebox.showerror("Error", "Please Enter your DOB")
        elif len(objadd.getemail())==0:
            tk.messagebox.showerror("Error", "Please Enter your Email Id")
        
        elif not re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',objadd.getemail()):
            tk.messagebox.showerror("Error", "Please Enter Valid Email_ID")
        elif len(self.confirm_password.get())==0:
            tk.messagebox.showerror("Error", "Please Enter Confirm Password")
        elif self.confirm_password.get() != objadd.getPassword():
            tk.messagebox.showerror("Error", "Password And Confirm Password must be same")
    
        elif main.addUsers(objadd):
             tk.messagebox.showinfo("Info","Sucessfully Added")
             for obj in self.master.winfo_children():
                 obj.destroy()
             self.manage_users()
             
        else:
            tk.messagebox.showerror("Error","Failed")    
    def mm(self):
        tk.Label(self.master, text="User Id").grid(row=3,column=1,pady=6)
        tk.Label(self.master, text="User Name").grid(row=4,column=1,pady=6)
        tk.Label(self.master, text="User Type ").grid(row=5,column=1,pady=6)
        tk.Label(self.master, text="User Status ").grid(row=6,column=1,pady=6)
        tk.Label(self.master, text="Contact ").grid(row=7,column=1,pady=6)
        tk.Label(self.master, text="DOB ").grid(row=8,column=1,pady=6)
        tk.Label(self.master, text="Email").grid(row=9,column=1,pady=6)
        
        
    def view_user(self,i=0):
        for obj in self.master.winfo_children():
            obj.destroy()
        self.mainWindow()
        _users=main.all_user()
        if i==len(_users)-1 :
            self.mm()
            tk.Label(self.master, text=_users[i][0]).grid(row=3,column=2,pady=6)
            tk.Label(self.master, text=_users[i][1]).grid(row=4,column=2,pady=6)
            tk.Label(self.master, text=_users[i][2]).grid(row=5,column=2,pady=6)
            tk.Label(self.master, text=_users[i][3]).grid(row=6,column=2,pady=6)
            tk.Label(self.master, text=_users[i][4]).grid(row=7,column=2,pady=6)
            tk.Label(self.master, text=_users[i][5]).grid(row=8,column=2,pady=6)
            tk.Label(self.master, text=_users[i][6]).grid(row=9,column=2,pady=6)
            tk.Button(self.master, text='Prev <<',command=lambda:self.view_user(i-1),height=2).grid(row=11,column=2,pady=20,padx=20)
            tk.Button(self.master, text="Edit ",command=lambda:self.editbtn(_users[i][0]),height=2).grid(row=12,column=2,pady=20,padx=20)
        
        elif i>0:
            self.mm()
            tk.Label(self.master, text=_users[i][0]).grid(row=3,column=2,pady=6)
            tk.Label(self.master, text=_users[i][1]).grid(row=4,column=2,pady=6)
            tk.Label(self.master, text=_users[i][2]).grid(row=5,column=2,pady=6)
            tk.Label(self.master, text=_users[i][3]).grid(row=6,column=2,pady=6)
            tk.Label(self.master, text=_users[i][4]).grid(row=7,column=2,pady=6)
            tk.Label(self.master, text=_users[i][5]).grid(row=8,column=2,pady=6)
            tk.Label(self.master, text=_users[i][6]).grid(row=9,column=2,pady=6)
            tk.Button(self.master, text='Next >>',command=lambda:self.view_user(i+1),height=2).grid(row=11 ,column=1,pady=20,padx=20)
            tk.Button(self.master, text='Prev <<',command=lambda:self.view_user(i-1),height=2).grid(row=11,column=2,pady=20,padx=20)
            tk.Button(self.master, text="Edit ",command=lambda:self.editbtn(_users[i][0]),height=2).grid(row=12,column=2,pady=6)
        else:
            self.mm()
            tk.Label(self.master, text=_users[i][0]).grid(row=3,column=2,pady=6)
            tk.Label(self.master, text=_users[i][1]).grid(row=4,column=2,pady=6)
            tk.Label(self.master, text=_users[i][2]).grid(row=5,column=2,pady=6)
            tk.Label(self.master, text=_users[i][3]).grid(row=6,column=2,pady=6)
            tk.Label(self.master, text=_users[i][4]).grid(row=7,column=2,pady=6)
            tk.Label(self.master, text=_users[i][5]).grid(row=8,column=2,pady=6)
            tk.Label(self.master, text=_users[i][6]).grid(row=9,column=2,pady=6)
            tk.Button(self.master, text='Next >>',command=lambda:self.view_user(i+1),height=2).grid(row=11,column=1,pady=6)
            tk.Button(self.master, text="Edit ",command=lambda:self.editbtn(_users[i][0]),height=2).grid(row=12,column=2,pady=6)
    
    
    def delete_ui(self):

        for obj in self.master.winfo_children():
            obj.destroy()
        self.mainWindow()
         
        tk.Label(self.master,text="User Id").grid(row=0,padx=10,pady=20)
        self.del_id=tk.Entry(self.master,width=20, font=('arial', 12))
        self.del_id.grid(row=0, column=2)
        self.del_id.bind('<Return>',self.delete)
        
    def delete(self,event):
        s_id=self.del_id.get()
        if main.delete(s_id):
            tk.messagebox.showinfo("Sucess","Deleted")
            self.del_id.delete(0,'end')
            
        else:
            tk.messagebox.showerror("Error","Invalid Id")
            self.del_id.delete(0,'end')
       
        
    def search_user_ui(self):
         for obj in self.master.winfo_children():
            obj.destroy()
         self.mainWindow()
         tk.Label(self.master, text="Enter User ID").grid(row=0,padx=10,pady=20)
         tk.Label(self.master, text="Company Inof---").grid(row=1,padx=10,pady=10)
         tk.Label(self.master, text="User Name").grid(row=3,pady=10)
         tk.Label(self.master, text="User Type ").grid(row=4,pady=10)
         tk.Label(self.master, text="User Status ").grid(row=5,pady=10)
         tk.Label(self.master, text="Contact ").grid(row=6,pady=10)
         tk.Label(self.master, text="DOB ").grid(row=7,pady=10)
         tk.Label(self.master, text="Email").grid(row=8,pady=10)
         self.search_id = tk.Entry(self.master,width=20, font=('arial', 12))
         self.search_id.grid(row=0, column=2)
         self.search_id.bind('<Return>',self.search)
    def editbtn(self,i):
        for obj in self.master.winfo_children():
            obj.destroy()
        self.mainWindow()
        self.edit_ui(i)
    def edit_ui(self,u_id=None):
        for obj in self.master.winfo_children():
            obj.destroy()
        self.mainWindow()
        if u_id !=None:
        
           self.del_id = tk.Entry(self.master,width=20, font=('arial', 12))
           self.del_id.grid(row=0, column=3)
           self.del_id.insert("end",u_id)
           self.edit_info()
           
           
        else:
            self.del_id = tk.Entry(self.master,width=20, font=('arial', 12))
            
            self.del_id.grid(row=0, column=3)
            self.edit_user_i()
            self.del_id.bind('<Return>',self.edit)
            
        self.del_id.bind('<Return>',self.edit)
    
    
    def update(self):
        bb=self.update_btn()
    
        if main.update(bb):
            tk.messagebox.showinfo("Sucess","Updated")
            self.del_id.delete(0,'end')
            self.edit_user_i()
        else:
            tk.messagebox.showerror("Error","No user found")
            self.edit_user_i()
      
    def edit(self,event):
        self.edit_user_i()
        self.edit_info()
        
        
    def edit_user_i(self):
        tk.Label(self.master, text="Enter User ID").grid(row=0,padx=10,pady=20)
        tk.Label(self.master, text="Company Inof---").grid(row=1,padx=10,pady=10)
        tk.Label(self.master, text="User Name").grid(row=2,pady=10)
            
        tk.Label(self.master, text="User Status ").grid(row=3,pady=10)
        tk.Label(self.master, text="Contact ").grid(row=4,pady=10)
        tk.Label(self.master, text="DOB ").grid(row=5,pady=10)
        tk.Label(self.master, text="Email").grid(row=6,pady=10)
        tk.Button(self.master, text='Save',
                     command=lambda:self.update(),height=2).grid(row=7,column=1,padx=20 )
        self.u_s = tk.IntVar()
        self.u_s.set(1)
        tk.Radiobutton(root, text="Active", variable=self.u_s, value=1).grid(row=3,column=3)
        tk.Radiobutton(root, text="Inactive", variable=self.u_s, value=2).grid(row=3,column=4)
        
        self.name_=tk.Entry(self.master,width=20, font=('arial', 12))
        self.name_.grid(row=2,column=3)
        self.contact_=tk.Entry(self.master,width=20, font=('arial', 12))
        self.contact_.grid(row=4,column=3)
        self.dob_=tk.Entry(self.master,width=20, font=('arial', 12))
        self.dob_.grid(row=5,column=3)
        self.email_=tk.Entry(self.master,width=20, font=('arial', 12))
        self.email_.grid(row=6,column=3)
        
    def edit_info(self):
        self.edit_user_i()
    
        d_id=self.del_id.get()
        if main.search(d_id):
            val=main.search(self.del_id.get())
            self.name_.delete(0,'end')
            self.name_.insert('end',val[0])
            if val[2]=="Active":
                self.u_s.set(1)
            else:
                self.u_s.set(2)
                
            userStatus=self.u_s.get()
            if userStatus==1:
                userStatus="Active"
            else:
                userStatus="Inactive"
            self.contact_.delete(0,'end')
            self.contact_.insert('end',val[3])
            self.dob_.delete(0,'end')
            self.dob_.insert('end',val[4])
            self.email_.delete(0,'end')
            self.email_.insert('end',val[5])
   
        else:
            tk.messagebox.showerror("Error","No user found")
            self.edit_ui()
            
    def update_btn(self):
        userStatus=self.u_s.get()
        if userStatus==1:
            userStatus="Active"
        else:
            userStatus="Inactive"
        obj1=emp()
        obj1.setId(self.del_id.get())
        obj1.setName(self.name_.get())
        obj1.setuser_status(userStatus)
        obj1.setcontact(self.contact_.get())
        obj1.setdob(self.dob_.get())
        obj1.setemail(self.email_.get())
        return obj1
    
    def search(self,event):
        s_id=self.search_id.get()
        if main.search(s_id):
            c=main.search(self.search_id.get())
            
            tk.Label(self.master, text=c[0]).grid(row=3,column=2)
            tk.Label(self.master, text=c[1]).grid(row=4,column=2)
            tk.Label(self.master, text=c[2]).grid(row=5,column=2)
            tk.Label(self.master, text=c[3]).grid(row=6,column=2)
            tk.Label(self.master, text=c[4]).grid(row=7,column=2)
            tk.Label(self.master, text=c[5]).grid(row=8,column=2)
            
        else:
            tk.messagebox.showerror("Error","No User Found")
            self.search_user_ui()

    def logout(self):
        self.master.destroy()
    
    def login(self):
        top.geometry("500x250")
        top.title("Login")
        tk.Label(self.top, text="User ID",width=20, font=('arial', 12)).grid(row=0,padx=30,pady=20)
        tk.Label(self.top, text="Password",width=20, font=('arial', 12)).grid(row=1,padx=30,pady=20)
        
        self.e1 = tk.Entry(self.top,width=20, font=('arial', 12))
        self.e2 = tk.Entry(self.top,show='*',width=20, font=('arial', 12))
        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        tk.Button(self.top, text='Quit', command=lambda:self.command2(),height=2).grid(row=5,column=0,padx=30)
        tk.Button(self.top, text='Login', command=lambda:self._login_btn_clicked(),height=2).grid(row=5,column=1,pady=30 )
    def _login_btn_clicked(self):
        obj3=emp()
        obj3.setId(self.e1.get())
        obj3.setPassword(self.e2.get())
         
        if len(self.e1.get()) == 0:
            messagebox.showerror("Login error", "Please Enter your UserName")
        elif len(self.e2.get())==0:
            messagebox.showerror("Login error", "Please Enter your Password")
        
        elif main.checkuser(obj3):
            
            messagebox.showinfo("Login info","Welcome "+main.checkuser(obj3))
            
            self.e1.delete(0,'end')
            self.e2.delete(0,'end')
            self.master.deiconify()
            self.top.destroy()
            self.mainWindow()
        else:
            messagebox.showerror("Login error","Incorrect username,password")
            
            self.e1.delete(0,'end')
            self.e2.delete(0,'end')
    def command2(self):
        self.top.destroy() 
        self.master.destroy()
    def table(self):
        print("table")
        for obj in self.master.winfo_children():
            obj.destroy()
        self.mainWindow()
        data=main.all_user()
        self.treeview = ttk.Treeview(self.master)
        self.treeview.grid(columnspan=2)
        self.treeview["columns"] = ("one", "two", "three","four","five","six")
    
        self.treeview.heading("one", text="ID")
        self.treeview.heading("two", text="Name")
        self.treeview.heading("three", text="Status")
        self.treeview.heading("four", text="Contact")
        self.treeview.heading("five", text="DOB")
        self.treeview.heading("six", text="Email")
        
        for index, dat in enumerate(data): 
            self.treeview.insert("",index,  text=index, values=(dat[0], dat[1],dat[3],dat[4],dat[5],dat[6]))
        
        
        tk.Button(self.master, text='Save as CSV', command=lambda:self.savecsv(),height=2).grid(row=14,column=0,padx=20,pady=10 )
        tk.Button(self.master, text='Save as Pdf', command=lambda:self.savepdf(),height=2).grid(row=12,column=0,padx=20,pady=10 )
        
    def savecsv(self):
        data=main.all_user()
        
        with open("out.csv", "w", newline='') as csv_file:
             
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(data)
        tk.messagebox.showinfo("Sucess","Sucesssfully saved")
        
        
        
    def savepdf(self):
        pdf=FPDF(format='letter', unit='in')
        pdf.add_page()
        pdf.set_font('Times','',10.0) 
        pdf.ln(0.5)
        epw = pdf.w - 2*pdf.l_margin
       
        data=main.all_user()
        col_width = epw/len(data[0])
        pdf.set_font('Times','B',14.0) 
        pdf.cell(epw, 0.0, 'User data', align='C')
        pdf.set_font('Times','',10.0) 
        pdf.ln(0.5)
        th = pdf.font_size
        for row in data:
            
            for datum in row:
                
                pdf.cell(col_width, th, str(datum), border=1)
         
            pdf.ln(th)
        pdf.output('out.pdf','F')
        tk.messagebox.showinfo("Sucess","Sucesssfully saved")
 

if __name__=="__main__":
    root = tk.Tk()
    top = tk.Toplevel()
    
    menu =MyFirstGUI(root,top)
    menu.login()
    
    root.withdraw()
    root.mainloop()
    
    
