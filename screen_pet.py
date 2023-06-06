from tkinter import HIDDEN, NORMAL,Tk, Canvas
def toggle_eyes():
    current_color = c.itemcget(eye_left, 'fill')
    new_color = c.body_color if current_color == 'white' else 'white'
    current_state = c.itemcget(pupil_left, 'state')
    new_state = NORMAL if current_state == HIDDEN else HIDDEN
    c.itemconfigure(pupil_left, state=new_state)
    c.itemconfigure(pupil_right, state=new_state)
    c.itemconfigure(eye_left, fill=new_color)
    c.itemconfigure(eye_right, fill=new_color)

def blink():
    toggle_eyes()
    root.after(300, toggle_eyes)
    root.after(1500, blink)
root=Tk()

c=Canvas(root, width=500, height=500)
c.configure(bg='light blue',highlightthickness=0)

c.body_color = 'grey'
body = c.create_oval(55, 40, 385, 370, outline=c.body_color, fill=c.body_color)
ear_left = c.create_polygon(95, 100, 95, 20, 175, 80, outline=c.body_color, fill=c.body_color)
ear_right = c.create_polygon(275, 65, 345, 20, 340, 90, outline=c.body_color, \
                             fill=c.body_color)

foot_left = c.create_oval(85, 340, 165, 380, outline=c.body_color, fill= c.body_color)
foot_right = c.create_oval(270, 340, 350, 380, outline=c.body_color, fill= c.body_color)
eye_left = c.create_oval(150, 130, 180, 190, outline='black', fill='white')
pupil_left = c.create_oval(160, 165, 170, 175, outline='blue', fill='blue')
eye_right = c.create_oval(250, 130, 280, 190, outline='black', fill='white')
pupil_right = c.create_oval(260, 165, 270, 175, outline='blue', fill='blue')
mouth_normal = c.create_line(190, 270, 220, 230, 250, 270, smooth=1, width=2, state=NORMAL)

mouth_happy = c.create_line(190, 270, 220, 302, 250, 270, smooth=1, width=2, state=HIDDEN)
mouth_sad = c.create_line(190, 270, 220, 252, 250, 270, smooth=1, width=2, state=HIDDEN)
cheek_left = c.create_oval(90, 200, 140, 250, outline='red', fill='hot pink', state=HIDDEN)
cheek_right = c.create_oval(300, 200, 350, 250, outline='red', fill='hot pink', state=HIDDEN)

c.pack()

root.after(1000, blink)
def show_happy(event):
    if (40 <= event.x <= 800) and (40 <= event.y <= 800):
        c.itemconfigure(cheek_left, state=NORMAL)
        c.itemconfigure(cheek_right, state=NORMAL)
        c.itemconfigure(mouth_happy, state=NORMAL)
        c.itemconfigure(mouth_normal, state=HIDDEN)
        c.itemconfigure(mouth_sad, state=HIDDEN)
    return
def hide_happy(event):
    c.itemconfigure(cheek_left, state=HIDDEN)
    c.itemconfigure(cheek_right, state=HIDDEN)
    c.itemconfigure(mouth_happy, state=HIDDEN)
    c.itemconfigure(mouth_normal, state=NORMAL)
    c.itemconfigure(mouth_sad, state=HIDDEN)
    return
c.bind('<Motion>', show_happy)
c.bind('<Leave>', hide_happy)
root.mainloop()


