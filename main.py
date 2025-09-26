import tkinter as tk
from tkinter import ttk ,font,messagebox,PhotoImage



winndow=tk.Tk()
winndow.title("To-Do-App")
winndow.configure(bg="#F0F0F0")
winndow.geometry("500x600")

heaser_font=font.Font(family="Garamond",size=24,weight="bold")
header_label=tk.Label(winndow,text="To-Do-App",font=heaser_font,bg="#F0F0F0",fg="#333")
header_label.pack(pady=24)

frame= tk.Frame(winndow,bg="#F0F0F0")
frame.pack(pady=10)

task_entry=tk.Entry(frame,font=("Garamond",14),bg="white",fg="grey",width=30)
task_entry.insert(0,"Write Your Task")
task_entry.pack(side=tk.LEFT,padx=10)

add_button= tk.Button(frame,text="Add Task",bg="#4CAF50" , fg="white", height=1,width=15,font=("Roboto",11))
add_button.pack(side=tk.LEFT,pady=10)


winndow.mainloop()