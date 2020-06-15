#Importing the important libraries before doing this.
#If error occured then in CMD/terminal install it by pip

from tkinter import *  
from datetime import date


#For Canvas
root = Tk()
root.geometry("650x500")
root.title("Hamara Age Calculator")
root.configure(bg='#DCDCDC')


#For Top Photo
photo = PhotoImage(file="mine.png")
myimage = Label(image=photo)
myimage.grid(row=0, column=1)

#Custom Function to calculate age
def calculateAge():
    today = date.today()
    birthDate = date(int(yearEntry.get()), int(monthEntry.get()), int(dayEntry.get()))
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    Label(text=f"{nameValue.get()} your age is {age}").grid(row=6, column=1)


#Labels 
Label(root,text="Name :- ", font =( 'Verdana', 15,)).grid(row=1, column=0, padx=90)
Label(root,text="Year :- ", font =( 'Verdana', 15)).grid(row=2, column=0, padx=90)
Label(root,text="Month :- ", font =( 'Verdana', 15)).grid(row=3, column=0, padx=90)
Label(root,text="Day :- ", font =( 'Verdana', 15)).grid(row=4, column=0, padx=90)

nameValue = StringVar()
yearValue = StringVar()
monthValue = StringVar()
dayValue = StringVar()

#Texboxes
nameEntry = Entry(root,bg='#FCF5D8', fg='black', textvariable=nameValue)
yearEntry = Entry(root,bg='#FCF5D8', fg='black',  textvariable=yearValue)
monthEntry = Entry(root,bg='#FCF5D8', fg='black',  textvariable=monthValue)
dayEntry = Entry(root,bg='#FCF5D8', fg='black',  textvariable=dayValue)
nameEntry.grid(row=1, column=1, pady=10)
yearEntry.grid(row=2, column=1, pady=10)
monthEntry.grid(row=3, column=1, pady=10)
dayEntry.grid(row=4, column=1, pady=10)

#For Button inside image
photo2 = PhotoImage(file = "arrow.png")  # Make sure use differnt names either only one picture will be displayed
  
photoimage = photo2.subsample(3, 3) 

Button(root, text="  Calculate Age", command=calculateAge, image = photoimage,bg='brown', fg='white', font=('helvetica', 13, 'bold'), compound = LEFT).grid(row=5, column=1, pady=10)


root.mainloop()

#End
