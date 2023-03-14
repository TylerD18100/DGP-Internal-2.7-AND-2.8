'''
  Name: Jack Morgan, and Tyler DeClifford
  James Hargest College
  Programming Internal for 2.7 & 2.8 ~ 12 credits
  Due: 6 April 2023
  
  TIP: Use assessment guide to help guide you through this Internal '''
from datetime import date
# used to create a custom window for age calculator
import tkinter as tk


#                      FUNCTION
def get_age():
    # gets the three entries
    a= int(e_date.get())
    b=int(e_month.get())
    h=int(e_year.get())

def find_age(d, m, y):    
    # find the age ( difference between current and date of birth )
    age = today.year-y-((today.month, today.day)<(m,d))
    return age

def display_calc_age(age):    
    tbox_age.config(state='normal')
   
    #age calculated is inserted into the text box after clearing the previous info in the textbox.
    tbox_age.delete('1.0', tk.END)
    tbox_age.insert(tk.END,age)
    tbox_age.config(state='disabled')

def exit():
    window.destroy()

#                      MAIN
# Create a object which stores today's whole date using datetime function
today = date.today()

# Creating a custom window

window = tk.Tk()
window.geometry("600x300")
window.config(bg="#F7DC6F")
window.resizable(width=False,height=False)
window.title('Right Angle triangle solver')

#Labels for Heading and Subheading of GUI
lb_heading = tk.Label(window,text="Right Angle Triangle Solver",font=("Arial",20),fg="black",bg="#F7DC6F")
lb_subheading = tk.Label(window,font=("Arial",12),text="Enter your Triangle Side Values!",fg="black",bg="#F7DC6F")

# labels for date, month and year
lb_date = tk.Label(window,text = "Leg A: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")
lb_month = tk.Label(window,text = "Leg B: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")
lb_year = tk.Label(window,text = "Hypotenuse: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")

# Entry boxes for date, month and year
e_date = tk.Entry(window,width=5)
e_month = tk.Entry(window,width=5)
e_hypotenuse = tk.Entry(window,width=5)

# Button to calculate age
btn_calculate_age = tk.Button(window,text="Solve",font=("Arial",13), command=get_age)


lb_calculated_age = tk.Label(window,text="The Solved Triangle",font=("Arial",12,"bold"),fg="darkgreen",bg="#F7DC6F") 
tbox_age=tk.Text(window,width=5,height=0,state="disabled")


btn_exit = tk.Button(window,text="Exit Application!",font=("Arial",13),command=exit)


lb_heading.place(x=110,y=5)
lb_subheading.place(x=135,y=40)
lb_date.place(x=100,y=70)
lb_month.place(x=100,y=95)
lb_year.place(x=100,y=120)
e_date.place(x=240,y=70)
e_month.place(x=240,y=95)
e_hypotenuse.place(x=240,y=120)
btn_calculate_age.place(x=140,y=150)
lb_calculated_age.place(x=50,y=200)
tbox_age.place(x=240,y=203)
btn_exit.place(x=100,y=230)