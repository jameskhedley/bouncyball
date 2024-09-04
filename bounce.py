from tkinter import *   

DELAY = 10
#creating a simple canvas  
top = Tk()  
top.geometry("800x800")  
c = Canvas(top,bg = "pink",height = "800", width=800)  

def main():
    c.pack()
    c.after(0, move)

    top.mainloop()  

def move():
    BALL_RADIUS = 50
    HOW_MANY = 2000
    #SPEED = 3
    G=0.1
    speed = 0
    circ0 = None
    direction = "down"
    y = 50
    new_y = y
    i=0

    while i < HOW_MANY:
        if direction == "down":
            speed = speed + G
        else:
            speed = speed - G
        if direction == "down":
            new_y = new_y + (speed)
        else:
            new_y = new_y - (speed)

        if new_y > 800 - BALL_RADIUS:
            direction = "up"
            print("BOING (bottom)")

        if speed <= 0:
            direction = "down"
            speed = 0

        if circ0:
            c.delete(circ0)
        #print(new_y)
        circ0 = circle(c, x=400, y=new_y, r=BALL_RADIUS)
        i=i+1
        c.update()
        c.after(DELAY)

def circle(canvas,x,y, r):
   id = canvas.create_oval(x-r,y-r,x+r,y+r)
   return id

main()