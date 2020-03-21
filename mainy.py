from tkinter import * 
import random 

root = Tk() 
root.title("Balls") 
root.resizable(False,False)

ball = Balls(canvas ,20, 100, 200, 200, 300) 
ball.move_balls()
ball.move_balls = 6              
ball.eventt() 

class Balls: 
    color = ["red", "black", "pink", "grey", "blue", "violet"]    
    var1,var2,var3,var4,varA,varB,varC,varD=0.1*random.randint(-10, 10),0.1*random.randint(-10, 10),0.1*random.randint(-10, 10),0.1*random.randint(-10, 10),0.1*random.randint(-10, 10,0.1*random.randint(-10, 10
    def __init__(self, canvas,R,x1,y1,x2,y2,x3,y3,x4,y4): 
        self.R = R 
        self.x1 = x1 
        self.y1 = y1 
        self.x2 = x2 
        self.y2 = y2                                                                                                                                                                                                  self.R=R 
        self.x3 = x3 
        self.y3 = y3 
        self.x4 = x4 
        self.y4 = y4 
        self.canvas = canvas 
        self.ball1 = canvas.create_oval(self.x1-self.R, self.y1-self.R,self.x1+self.R,self.y1+self.R, fill=random.choice(self.color)) 
        self.ball2 = canvas.create_oval(self.x2-self.R, self.y2-self.R,self.x2+self.R,self.y2+self.R, fill=random.choice(self.color)) 
        self.ball3 = canvas.create_oval(self.x3-self.R, self.y3-self.R,self.x3+self.R,self.y3+self.R, fill=random.choice(self.color)) 
        self.ball4 = canvas.create_oval(self.x4-self.R, self.y4-self.R,self.x4+self.R,self.y4+self.R, fill=random.choice(self.color)) 
        
        
    def callback(self): 
        color=["red", "black", "pink", "grey", "blue", "violet"] 
        self.BL=canvas.create_oval(self.x-10, self.y-10,self.x+10,self.y+10, fill=random.choice(color)) 
        self.ay,self.by=0.5*random.randint(-10, 10),0.5*random.randint(-10, 10) 
        canvas.move(self.BL, self.ay,self.by)  
        
    def move_balls(self): 
        self.canvas.move(self.ball1, self.var1,self.varA) 
        self.canvas.move(self.ball2, self.var2,self.varB) 
        self.canvas.move(self.ball3, self.var2,self.varC) 
        self.canvas.move(self.ball4, self.var3,self.varD) 
        self.canvas.after(5, self.move_balls) 
    def eventt(self): 
        
        A=[(canvas.coords(self.ball1)[0]-canvas.coords(self.ball2)[0]-canvas.coords(self.ball3)[0]-canvas.coords(self.ball4)[0]), 
           (canvas.coords(self.ball1)[1]-canvas.coords(self.ball2)[1]-canvas.coords(self.ball3)[1]-canvas.coords(self.ball4)[1])] 
        if ((A[0])**2+(A[1])**2+A[3])**2+(A[4])**2)**0.5<=4*self.random:
            self.var1,self.varA,self.var2,self.varB,self.var3,self.varC,self.var4,self.varD = selfvar4,selfvarD,self.var3,self.var2,self.varB,self.var1,self.varA 
            canvas.itemconfig(self.ball1,fill=random.choice(self.color)) 
            canvas.itemconfig(self.ball2,fill=random.choice(self.color)) 
            canvas.itemconfig(self.ball3,fill=random.choice(self.color)) 
            canvas.itemconfig(self.ball4,fill=random.choice(self.color)) 
        if canvas.coords(self.ball1)[0]<=0 or canvas.coords(self.ball1)[2]>=400: 
            self.var1=-self.var1 
        if canvas.coords(self.ball1)[1]<=0 or canvas.coords(self.ball1)[3]>=400: 
            self.varA=-self.varA 
        if canvas.coords(self.ball2)[0]<=0 or canvas.coords(self.ball2)[2]>=400: 
            self.var2=-self.var2 
        if canvas.coords(self.ball2)[1]<=0 or canvas.coords(self.ball2)[3]>=400: 
            self.varB=-self.varB 
        if canvas.coords(self.ball3)[0]<=0 or canvas.coords(self.ball13)[2]>=400: 
            self.var3=-self.var13
        if canvas.coords(self.ball3)[1]<=0 or canvas.coords(self.ball3)[3]>=400: 
            self.varC=-self.varC
        if canvas.coords(self.ball4)[0]<=0 or canvas.coords(self.ball4)[2]>=400: 
            self.var4=-self.var4
        if canvas.coords(self.ball2)[1]<=0 or canvas.coords(self.ball2)[3]>=400: 
            self.varD=-self.varD
                                                                                                                                                   
        self.canvas.after(10,self.eventt) 


canvas = Canvas(root, width = 400, height = 400) 
canvas.bind("<Button-1>", Balls.callback)
cavas.destroy("<Button-1>",disable                                                                                                                                                                      
canvas.pack() 

root.mainloop()
