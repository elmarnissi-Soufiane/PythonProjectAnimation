# -*- coding: utf-8 -*-
"""
Created on Fri May 21 13:49:09 2021

@author: Soufiane
"""
class Ball:


    def __init__(self,canvas,x,y,diameter,xVelocity,yVelocity,color):
        self.canvas = canvas
        self.obj = canvas.create_rectangle(x,y,diameter,diameter,fill=color)
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity

    def move(self):
        coordinates = self.canvas.coords(self.obj)

        if(coordinates[2]>=(self.canvas.winfo_width()) or coordinates[0]<0):
            self.xVelocity = -self.xVelocity
        if(coordinates[3]>=(self.canvas.winfo_height()) or coordinates[1]<0):
            self.yVelocity = -self.yVelocity

        self.canvas.move(self.obj,self.xVelocity,self.yVelocity)