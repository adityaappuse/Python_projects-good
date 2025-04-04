from tkinter import *
from tkinter import ttk
import pandas as pd
import os
import datetime
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame(columns=["Money Spent","Expense type"])

def passonthevalue():

    moneySpent = myinput1.get()
    expense = myinput2.get()
    myinput1.delete(0,END)
    myinput2.selection_clear
    myinput2.set("Select the type of expense") 
    addToDatabase(moneySpent,expense)


def addToDatabase(moneySpent,expense):


    
    data =[[moneySpent,expense,datetime.date.today()]]


# creating a table like structure to add the values
    new_data = pd.DataFrame(data,columns=["Money Spent","Expense type","Date"])
    new_data = new_data.reset_index(drop=True)
    new_data.index.name ="Index"

#adding the value to the og table
    
    
    filepath = "money_tracker.csv"
    if(os.path.exists(filepath)and os.path.getsize(filepath)>0):
        main_df = pd.read_csv(filepath)
    else:
        main_df = pd.DataFrame(columns=["Money Spent","Expense type","Date"])    
    
    
    main_df =pd.concat([main_df,new_data],axis=0,ignore_index=True)
    main_df.index.name = "Index"
   
    main_df.index +=1
    main_df.to_csv("money_tracker.csv",index=False)

def clearTable():
    filename = "money_tracker.csv"
    f = open(filename,"w+")
    f.close()

def showPieChart():
    InitialChartFile = pd.read_csv("money_tracker.csv")
    #Use groupby to aggregate similar values
    summedFile = InitialChartFile.groupby("Expense type").sum().reset_index()
    #convert to a string to be used for pie chart
    Expenses = summedFile["Expense type"].to_list()
    cashSpent = summedFile["Money Spent"].to_list()
    

    sns.color_palette("Set2")
    plt.pie(cashSpent,labels=Expenses)
    plt.show()

root =Tk()
root.geometry("400x400")
tkvar = StringVar(value="rent")
choices=["rent","food","transportation","clothes","personal care","miscellaneous"]

main_frame = LabelFrame(root,pady=40,bg="#46351D")
main_frame.pack(fill=BOTH,expand=True)

myLabel1 = Label(main_frame,text="Type how much money was spent there",fg="#F9DEC9",bg="#46351D")
myLabel1.place(x=10,y=20)

myinput1 =  Entry(main_frame,width=50,bg="#646F4B")
myinput1.place(x=20,y=40)


myLabel2 = Label(main_frame,text="What activity was the money spent for???",fg="#F9DEC9",bg="#46351D")
myLabel2.place(x=10,y=90)

combostyle = ttk.Style()
combostyle.theme_create('combostyle', parent='alt', settings={
    'TCombobox': {
        'configure': {
            'selectbackground': '#646F4B',  # Background of selected item
            'fieldbackground': '#646F4B',  # Background of the entry box
            'background': '#46351D',  # Dropdown menu background
        }
    }
})
combostyle.theme_use('combostyle')  # Apply the new style
#combobox
myinput2 = ttk.Combobox(main_frame,values=choices,width=23)
myinput2.set("Select the type of expense")
myinput2["state"]="readonly"
myinput2.place(x=20,y=110)



myButton = Button(main_frame,text="Submit",bg="#99B2DD",padx=10,pady=10,command=passonthevalue)
myButton.place(x=40,y=140)

clearButton = Button(main_frame,text="Clear the table",bg="#99B2DD",padx=10,pady=10,command=clearTable)
clearButton.place(x=110,y=140)

tableButton = Button(main_frame,text="View Expense Breakdown",bg="#99B2DD",padx=10,pady=10,command=showPieChart)
tableButton.place(x=45,y=190)

root.mainloop()

def createPiChart():
    
    InitialChartFile = pd.read_csv("money_tracker.csv")
    sns.color_palette("pastel")[0:5]
    plt.pie()
    