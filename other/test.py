import tkinter as t

tk = t.Tk()
w = t.Button()
canvas = t.Canvas(tk, bg="#000000", bd=3, width=480, height=360)
velx = 0
vely = 0
x = 240
y = 50
# img = t.PhotoImage(file="puppy.jpg")
# canvas.create_image(x, 200, image=img)
id = canvas.create_rectangle(x, y, 10, 10, fill="red")


def move():
    global x
    global y
    # canvas.delete("all")
    x += velx
    y += vely
    # canvas.create_image(x, 200, image=img)
    # canvas.create_rectangle(x, y, 10, 10, fill="red")
    canvas.move(id, velx, vely)
    tk.after(10, move)


def clear_board():
    # canvas.delete("all")
    pass


def key_press(event):
    global velx
    global vely
    print(event)
    keysym = event.keysym
    pr = event.char
    if pr == "a":
        velx = -5
    if pr == "d":
        velx = 5
    if pr == "w":
        vely = -5
    if pr == "s":
        vely = 5


def key_release(event):
    global velx
    global vely
    print(event)
    # velx = 0
    # vely = 0
    keysym = event.keysym
    pr = event.char
    if pr == "a":
        velx = 0
    if pr == "d":
        velx = 0
    if pr == "w":
        vely = 0
    if pr == "s":
        vely = 0


w = t.Button(tk, command=clear_board, activebackground="#000000", activeforeground="#FFFFFF", bd=3, fg="#000000",
             bg="#FFFFFF", text="Clear", relief="groove")

canvas.focus_set()
canvas.bind("<KeyPress>", key_press)
canvas.bind("<KeyRelease>", key_release)

move()
w.pack()
canvas.pack()
tk.mainloop()
