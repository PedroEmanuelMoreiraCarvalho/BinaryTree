import math

def getDistanceOf(x,y,x2,y2):
    dist = math.sqrt( (x2 - x)**2 + (y2 - y)**2 )
    return dist

class BinaryTree():
    def __init__(self):
        self.root = None

    def add(self,value):
        if self.root == None:
            self.root = Node(value,300,100)#middle
            return
        self.root.addChild(value)

    def showValues(self):
        self.root.printValues()

    def render(self,canvas):
        canvas.delete("all")
        canvas.create_rectangle(0,0,602,402)
        if self.root != None:
            self.root.render(canvas)

    def moveClosestTo(self,x,y):
        closest = self.root.getClosest(x,y)
        if closest != None:
            closest.moveTo(x,y)

class Node():
    def __init__(self, value,x,y):
        self.value = value
        self.left = None
        self.right = None
        self.cell = Cell(value,x,y)
    
    def addChild(self,new_value):
        if new_value == self.value:
            return
        elif new_value < self.value:
            if(self.left == None):
                self.left = Node(new_value,self.cell.x-60,self.cell.y+60)
            else:
                self.left.addChild(new_value)
        else:
            if(self.right == None):
                self.right = Node(new_value,self.cell.x+60,self.cell.y+60)
            else:
                self.right.addChild(new_value)

    def printValues(self):
        if self.left != None:
            self.left.printValues()
        print(self.value)
        if self.right != None:
            self.right.printValues()

    def render(self,canvas):
        if self.left != None:
            canvas.create_line(self.cell.x,self.cell.y + 10,self.left.cell.x,self.left.cell.y, fill="red", width=5)
            self.left.render(canvas)
        self.cell.render(canvas)
        if self.right != None:
            canvas.create_line(self.cell.x,self.cell.y + 10,self.right.cell.x,self.right.cell.y, fill="red", width=5)
            self.right.render(canvas)

    def getClosest(self,x,y):
        if self == None:
            return None
        if getDistanceOf(x,y,self.cell.x,self.cell.y) <= 10:
            return self.cell
        else:
            left_cell = None
            right_cell = None
            if self.left != None:
                left_cell = self.left.getClosest(x,y)
            if self.right != None:
                right_cell = self.right.getClosest(x,y)
            if left_cell != None:
                return left_cell
            elif right_cell != None:
                return right_cell
            else:
                return None

class Cell():
    def __init__(self,value,x,y):
        self.x = x
        self.y = y
        self.value = value

    def moveTo(self,new_x,new_y):
        self.x = new_x
        self.y = new_y

    def render(self, canvas):
        canvas.create_text(self.x, self.y, text=self.value, fill="black", font=('Helvetica 15 bold'))