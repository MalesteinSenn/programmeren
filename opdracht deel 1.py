
from turtle import *
import tkinter as tk
from tkinter import *



class tekenen():
    # wind = tk.Tk()
    def __init__(self, childFrame):
        self.cFrame = childFrame
        canvas = tk.Canvas(self.cFrame)
        canvas.config(width=1200, height=700, borderwidth=2, relief="solid")
        canvas.pack(side=tk.LEFT)
        self.myTurtle = RawTurtle(canvas)
        self.createField()

    # functions self.turtle movement
    def forward(self):
        self.myTurtle.forward(50)
    def forward_10(self): 
        self.myTurtle.forward(10)
    def turn_right_90(self):
        self.myTurtle.right(90)
    def turn_right_10(self):
        self.myTurtle.right(10)
    def turn_left_90(self):
        self.myTurtle.left(90)
    def turn_left_10(self):
        self.myTurtle.left(10)

    # functions pen changes
    def pen_size_up(self):
        pen_size = self.myTurtle.pensize()
        pen_size = pen_size + 5
        self.myTurtle.pensize(pen_size)
    def pen_size_down(self):
        pen_size = self.myTurtle.pensize()
        pen_size = pen_size - 5
        self.myTurtle.pensize(pen_size)
    def pen_up(self):
        self.myTurtle.penup()
    def pen_down(self):
        self.myTurtle.pendown()

    # functions self.turtle visible or invisible
    def hide_turtle(self):
        self.myTurtle.hideturtle()
    def show_turtle(self):
        self.myTurtle.showturtle()

    # functions utility
    def home(self):
        self.myTurtle.home()
    def turtle_clear(self):
        self.myTurtle.clear()
    def turtle_reset(self):
        self.myTurtle.reset()
    def turtle_undo(self):
        self.myTurtle.undo()

    # functions self.turtle shapes
    def circle(self):
        self.myTurtle.circle(20)

    def repeating_circle(self):
        rad = 10
        col = (self.myTurtle.pencolor)
        s = 1
        for i in range (100):
            # veranderen van kleur bij 0, 25, 50, 75
            if i < 25:
                self.myTurtle.pencolor("purple")
            elif i >= 25 and i < 50:
                self.myTurtle.pencolor("green")
            elif i >= 50 and i < 75:
                self.myTurtle.pencolor("blue")
            else:
                self.myTurtle.pencolor("red")
            # cirkels maken
            col()
            self.myTurtle.circle(rad)
            self.myTurtle.right(90)
            rad = rad + 10
            s = s + 10000
            self.myTurtle.speed(s)


        
  
    def createField(self):
        
        
        
        # self.turtle movement
        Label = tk.Label(self.cFrame, text="turtle movement", width=15, height=3)
        Label.pack()
        button = tk.Button(self.cFrame, text="forward 50", command=self.forward, width=15)
        button.pack()
        button = tk.Button(self.cFrame, text="forward 10", command=self.forward_10, width=15)
        button.pack()
        button = tk.Button(self.cFrame, text="turn right 90", command=self.turn_right_90, width=15)
        button.pack()
        button = tk.Button(self.cFrame, text="turn right 10", command=self.turn_right_10, width=15)
        button.pack()
        button = tk.Button(self.cFrame, text="turn left 90", command=self.turn_left_90, width=15)
        button.pack()
        button = tk.Button(self.cFrame, text="turn left 10", command=self.turn_left_10, width=15)
        button.pack()

        # self.turtle pen change
        Label = tk.Label(self.cFrame, text="pen size changes", width=15, height=3)
        Label.pack()
        button = tk.Button(self.cFrame, text="pen size up 5", command=self.pen_size_up, width=15)
        button.pack()
        button = tk.Button(self.cFrame, text="pen size down 5", command=self.pen_size_down, width=15)
        button.pack()
        button = tk.Button(self.cFrame, text="pen up", command=self.pen_up, width=15)
        button.pack()
        button = tk.Button(self.cFrame, text="pen down", command=self.pen_down, width=15)
        button.pack()

        # self.turtle visible or invisible
        Label = tk.Label(self.cFrame, text="turtle visibility", width=15, height=3)
        Label.pack()
        button = tk.Button(self.cFrame, text="hide turtle", command=self.hide_turtle, width=15)
        button.pack()
        button = tk.Button(self.cFrame, text="show turtle", command=self.show_turtle, width=15)
        button.pack()

        # self.turtle utility
        Label = tk.Label(self.cFrame, text="turtle utility", width=15, height=3)
        Label.pack()
        button = tk.Button(self.cFrame, text="home", command=self.home, width=15)
        button.pack()
        button = tk.Button(self.cFrame, text="clear", command=self.turtle_clear, width=15)
        button.pack()
        button = tk.Button(self.cFrame, text="reset", command=self.turtle_reset, width=15)
        button.pack()
        button = tk.Button(self.cFrame, text="undo", command=self.turtle_undo, width=15)
        button.pack()

        # self.turtle shapes
        Label = tk.Label(self.cFrame, text="Shapes", width=15, height=3)
        Label.pack()
        button = tk.Button(self.cFrame, text="circle", command=circle, width=15)
        button.pack()
        button = tk.Button(self.cFrame, text="repeating circle", command=self.repeating_circle, width=15)
        button.pack()    
    
    def returnFrame(self):
        return self.cFrame