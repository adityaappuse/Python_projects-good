from tkinter import *
import os
import shutil
from tkinter import filedialog
from tkinter import messagebox

root = Tk()
root.title("file organizer")
root.geometry("200x100")

#To create a window and choose the folder
def click():
    
    root.filename = filedialog.askdirectory(title="Select the folder for organization")
    myButton.pack_forget()
    source = root.filename
    
    #Create button again for executing the above given thing
    global myButton2
    myButton2 = Button(main_frame,text="Execute",command=lambda:organize_files(source),bg="#D1BEB0",fg="#7A4419")
    myButton2.pack(anchor=CENTER)

#Function to control organize the files in a folder

def organize_files(dest):
    #Created the organize_files to add different types in a list 
    files=os.listdir(dest)
    types=[]
    txt_output = Text(main_frame, height=5, width=30)
    for file in files:
        ext=os.path.splitext(file)[1]
        if ext not in types:
            types.append(ext)
    actual_organize(dest,types)

    #actual process occurs her
def actual_organize(destination,types):
    list_of_files=os.listdir(destination)
    for type in types: 
        file_name=type[1:]
        folder_name=os.path.join(destination,f"{file_name} files")
        os.makedirs(folder_name,exist_ok=True)
        counter=0
        #take file check extension if same then paste it on new folder
        for file in list_of_files:
            if(file.endswith(type)):
                src = os.path.join(destination,file)
                dest =os.path.join(destination,folder_name)
                final_dest = os.path.join(dest,file)
                if os.path.exists(final_dest):
                    counter+=1
                    shutil.move(src,final_dest+counter)
                else:
                    shutil.move(src,final_dest)
        result = messagebox.askquestion(title="Completed succesfully",message="Task succesfully completed")
        if result =="yes":
            root.destroy()
        else:
            return None

#Create a frame to contain the button correctly and almost middle
main_frame = LabelFrame(root,pady=40,bg="#0e1116")
main_frame.pack(fill=BOTH,expand=True)

    
# Create button that leads to window where folder is selected
myButton = Button(main_frame,text="Click to Start",command=click,bg="#D1BEB0",fg="#7A4419")
myButton.pack(anchor=CENTER)
root.mainloop()