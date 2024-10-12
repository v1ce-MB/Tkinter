from tkinter import*
window= Tk()
window.geometry("220x350")
window.config(bg="teal")

example=Label(window, text="I like Nairobi city", bg="teal", fg="yellow")
example.pack()

def click():
    print("you opened!")

link=Button(window, text="open!",bg="red",fg="dark blue", command=click)
link.pack()






window.mainloop()