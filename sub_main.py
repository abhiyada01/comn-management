from tkinter import *
from tkinter import messagebox
import os
import sqlite3 as sl
import sys



def main():
    root = Tk()
    root.iconbitmap('icon.ico')
    root.title('Componenet Management')
    root.geometry('1350x750+0+0')
    app = window1(root)
    root.mainloop()

    

class window1:

    def __init__(self,master, *arg, **kwarg):
        self.master = master
        mainframe = Frame (self.master)
        mainframe.pack()
        topframe = Frame(mainframe)
        topframe.grid(row=0,column = 0, columnspan=2)
        def iexit():
            master.destroy()
            sys.exit()
        
        statusframe = Frame(mainframe)
        statusframe.grid(row=1,column = 0)
        
        listframe = Frame(mainframe)
        listframe.grid(row = 1,column =1)
        
        buttonframe = Frame(mainframe)
        buttonframe.grid(row = 2,column =0, columnspan=2)
#===========================Variable=========================================
        var1 = StringVar()
        var2 = StringVar()
        var3 = StringVar()
        var4= StringVar()
        var5 = StringVar()
        var6 = StringVar()
        
#====================================Function=========================================
        def file_dir():
            diri = "C:\\Users\\Abhishek Kumar\\Desktop\\Project\\Pro2\\com_database.db"
            return diri
        def iclear():
            ent1.delete(0, 'end')
            ent2.delete(0, 'end')
            ent3.delete(0, 'end')
            ent4.delete(0, 'end')
            ent5.delete(0, 'end')
            ent6.delete(0, 'end')
        def caps(event):
            var1.set(ent1.get().upper())
            var2.set(ent2.get().upper())
            var3.set(ent3.get().upper())
            var4.set(ent4.get().upper())
            var5.set(ent5.get().upper())
            

        def com_display():
            file = file_dir()
            conn = sl.connect(file)
            c = conn.cursor()
            c.execute('SELECT * FROM component')
            data = c.fetchall()
            com_list.delete(0, 'end')
            for row in data:
                com_list.insert('end', row, str('|'))
            conn.close()
        def com_search():
            if (len(ent1.get())) != 0 or (len(ent2.get())) != 0 or (len(ent3.get())) != 0 or (len(ent4.get())) != 0 or (len(ent5.get())) != 0 or (len(ent6.get())) != 0:
                file = file_dir()
                conn = sl.connect(file)
                c = conn.cursor()
                c.execute('SELECT * FROM component WHERE (part_name = ? OR part_num= ? OR pcbname= ? OR pcbnum= ? OR box_num= ?)',(ent1.get(),ent2.get(),ent3.get(),ent4.get(),ent5.get()))
                data = c.fetchall()
                com_list.delete(0, 'end')
                for row in data:
                    com_list.insert('end', row, str('|'))
                conn.close()
            else:
                messagebox.showerror('warning','Atleast One should be filled except description')

        def com_rec(event):
            try:
                serrec = com_list.curselection()[0]
                data_r = com_list.get(serrec)
                
                ent1.delete(0, 'end')
                var1.set(data_r[0])
                
                ent2.delete(0, 'end')
                var2.set(data_r[1])
                
                ent3.delete(0, 'end')
                var3.set(data_r[2])
                
                ent4.delete(0, 'end')
                var4.set(data_r[3])
                
                ent5.delete(0, 'end')
                var5.set(data_r[4])
                
                ent6.delete(0, 'end')
                var6.set(data_r[5])
                
                return data_r[0]
            except:
                pass


#=============================Label=========================================
        
        lbl = Label(topframe, text = 'Component Management System', font = ('arial',35,'bold'))
        lbl.pack()

        label1 = Label(statusframe, text = 'Part Name', font = ('arial',18,'bold'))
        label1.grid(row = 0, column=0,padx=10, pady = 30)
        ent1 = Entry(statusframe, textvariable = var1)
        ent1.grid(row = 0, column=1,padx=10, pady = 30)
        ent1.bind("<KeyRelease>", caps)

        label2 = Label(statusframe, text = 'Part Number', font = ('arial',18,'bold'))
        label2.grid(row = 1, column=0,padx=10, pady = 30)
        ent2 = Entry(statusframe, textvariable = var2)
        ent2.grid(row = 1, column=1,padx=10, pady = 30)
        ent2.bind("<KeyRelease>", caps)

        label3 = Label(statusframe, text = 'PCB Name', font = ('arial',18,'bold'))
        label3.grid(row = 2, column=0,padx=10, pady = 30)
        ent3 = Entry(statusframe, textvariable = var3)
        ent3.grid(row = 2, column=1,padx=10, pady = 30)
        ent3.bind("<KeyRelease>", caps)

        label4 = Label(statusframe, text = 'PCB Number', font = ('arial',18,'bold'))
        label4.grid(row = 3, column=0,padx=10, pady = 30)
        ent4 = Entry(statusframe, textvariable = var4)
        ent4.grid(row = 3, column=1,padx=10, pady = 30)
        ent4.bind("<KeyRelease>", caps)

        label5 = Label(statusframe, text = 'Box Name', font = ('arial',18,'bold'))
        label5.grid(row = 4, column=0,padx=10, pady = 30)
        ent5 = Entry(statusframe, textvariable = var5)
        ent5.grid(row = 4, column=1,padx=10, pady = 30)
        ent5.bind("<KeyRelease>", caps)

        label6 = Label(statusframe, text = 'Description', font = ('arial',18,'bold'))
        label6.grid(row = 5, column=0,padx=10, pady = 30)
        ent6 = Entry(statusframe, textvariable = var6)
        ent6.grid(row = 5, column=1,padx=10, pady = 30)
        
    
#============================================Listbox============================
        scroll = Scrollbar(listframe)
        scroll.pack(side='right',fill=Y)
        com_list = Listbox(listframe,setgrid= True,width = 60,selectmode = 'single',font =('arial', 20, 'bold'), yscrollcommand = scroll.set)
        com_list.pack()
        com_list.bind("<<ListboxSelect>>", com_rec)
        scroll.config( command = com_list.yview )

#====================================Button==============================
        but1 = Button(buttonframe, text = 'Search',font = ('arial',20,'bold'), command = com_search)
        but1.grid(row=0, column=0, padx=110,pady =10)
        
        but2 = Button(buttonframe, text = 'Clear',font = ('arial',20,'bold'), command = iclear)
        but2.grid(row=0, column=1, padx=110, pady =10)
        
        but3 = Button(buttonframe, text = 'Display',font = ('arial',20,'bold'), command = com_display)
        but3.grid(row=0, column=2, padx=110, pady =10)
        
        but4 = Button(buttonframe, text = 'Exit',font = ('arial',20,'bold'),command = iexit)
        but4.grid(row=0, column=3, padx=110, pady =10)
        
        

if __name__ == '__main__':
    main()
