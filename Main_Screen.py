from tkinter import *

root = Tk()
root.geometry("350x450")  # width x height
root.title("SPACE INVADERS")
root.configure(bg="dark blue")

text = Label(root, text="πππππ πππππππ", padx=11, pady=11, bg="cyan", fg="black", font="helvetica,10,bold",
             borderwidth=2, relief=GROOVE)
text.pack()

photo = PhotoImage(file="project.png")
labelphoto = Label(root, image=photo)
labelphoto.pack()


def command():
    import Game_loop




btn = Button(root, text="πππ ππΌππ", bg="orange", padx=48, pady=12, font="Gotham,10,bold", command=command)
btn.pack()
btn1 = Button(root, text="ππππ", bg="orange", padx=80, pady=12, font="Gotham,10,bold", command=quit)
btn1.pack()

root.mainloop()
