'''
  Name: Jack Morgan, and Tyler DeClifford
  James Hargest College
  Programming Internal for 2.7 & 2.8 ~ 12 credits
  Due: 6 April 2023
  
  TIP: Use assessment guide to help guide you through this Internal '''
#                           IMPORTS
import tkinter as tk

# Ask for two input values
a = float(input("Enter the length of leg A: "))
b = float(input("Enter the length of leg B: "))
c = float(input("Enter the length of hypotenuse C: "))

   
# Creating a window
window = tk.Tk()
window.geometry("400x300")
window.config(bg="#F7DC6F")
window.resizable(width=False,height=False)
window.title('Right Angle Triangle Solver')

#Labels for Heading and Subheading of GUI
lb_heading = tk.Label(window,text="Right Angle Triangle Solver",font=("Arial",20),fg="black",bg="#F7DC6F")
lb_subheading = tk.Label(window,font=("Arial",12),text="Enter your Triangle side values ",fg="black",bg="#F7DC6F")

# labels for date, month and year
lb_lega = tk.Label(window,text = "Leg A: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")
lb_hypotenuse = tk.Label(window,text = "Hypotenuse: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")
lb_legb = tk.Label(window,text = "Leg B: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")
