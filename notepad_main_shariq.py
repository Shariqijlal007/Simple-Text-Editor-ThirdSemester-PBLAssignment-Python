''' creating GUI Interface to show frontend working of notepad '''

#importing required packages and libraries
import re
from tkinter import *
from tkinter.ttk import *
from datetime import datetime
from tkinter  import messagebox
from tkinter import filedialog,simpledialog
from tkinter.scrolledtext import ScrolledText

#creating the root widget
root = Tk()
root.title('SHARIQ IJLAL TAHIR NOTEPAD GUI INTERFACE TO DISPLAY WORKING OF FRONTEND PROGRAM.')
root.geometry("500x500")

#creating scrollable notepad window
notepad = ScrolledText(root, width = 1000, height = 50)
fileName = ''

#defining functions for commands
def cmdNew():     #file menu New option
    global fileName
    if len(notepad.get('1.0', END+'-1c'))>0:
        if messagebox.askyesno("Notepad", "Do you want to save changes?"):
            cmdSave()
        else:
            notepad.delete(0.0, END)
    root.title("Notepad")

def cmdOpen():     #file menu Open option
    fd = filedialog.askopenfile(parent = root, mode = 'r')
    t = fd.read()     #t is the text read through filedialog
    notepad.delete(0.0, END)
    notepad.insert(0.0, t)
    
def cmdSave():     #file menu Save option
    fd = filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt')
    if fd!= None:
        data = notepad.get('1.0', END)
    try:
        fd.write(data)
    except:
        messagebox.showerror(title="Error", message = "Not able to save file!")
     
def cmdSaveAs():     #file menu Save As option
    fd = filedialog.asksaveasfile(mode='w', defaultextension = '.txt')
    t = notepad.get(0.0, END)     #t stands for the text gotten from notepad
    try:
        fd.write(t.rstrip())
    except:
        messagebox.showerror(title="Error", message = "Not able to save file!")

def cmdExit():     #file menu Exit option
    if messagebox.askyesno("Notepad", "Are you sure you want to exit?"):
        root.destroy()

def cmdCut():     #edit menu Cut option
    notepad.event_generate("<<Cut>>")

def cmdCopy():     #edit menu Copy option
    notepad.event_generate("<<Copy>>")

def cmdPaste():     #edit menu Paste option
    notepad.event_generate("<<Paste>>")

def cmdClear():     #edit menu Clear option
    notepad.event_generate("<<Clear>>")
       
def cmdFind():     #edit menu Find option
    notepad.tag_remove("Found",'1.0', END)
    find = simpledialog.askstring("Find", "Find what:")
    if find:
        idx = '1.0'     #idx stands for index
    while 1:
        idx = notepad.search(find, idx, nocase = 1, stopindex = END)
        if not idx:
            break
        lastidx = '%s+%dc' %(idx, len(find))
        notepad.tag_add('Found', idx, lastidx)
        idx = lastidx
    notepad.tag_config('Found', foreground = 'white', background = 'blue')
    notepad.bind("<1>", click)

def click(event):     #handling click event
    notepad.tag_config('Found',background='white',foreground='black')

def cmdSelectAll():     #edit menu Select All option
    notepad.event_generate("<<SelectAll>>")
    
def cmdTimeDate():     #edit menu Time/Date option
    now = datetime.now()
    # dd/mm/YY H:M:S
    dtString = now.strftime("%d/%m/%Y %H:%M:%S")
    label = messagebox.showinfo("Time/Date", dtString)

def cmdAbout():     #help menu About option
    label = messagebox.showinfo("About Notepad", "Notepad by: - \nSHARIQ IJLAL TAHIR \nBEE-57 B \nMCS")

#notepad menu items
notepadMenu = Menu(root)
root.configure(menu=notepadMenu)

#file menu
fileMenu = Menu(notepadMenu, tearoff = False)
notepadMenu.add_cascade(label='File', menu = fileMenu)

#adding options in file menu
fileMenu.add_command(label='New', command = cmdNew)
fileMenu.add_command(label='Open...', command = cmdOpen)
fileMenu.add_command(label='Save', command = cmdSave)
fileMenu.add_command(label='Save As...', command = cmdSaveAs)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command = cmdExit)

#edit menu
editMenu = Menu(notepadMenu, tearoff = False)
notepadMenu.add_cascade(label='Edit', menu = editMenu)

#adding options in edit menu
editMenu.add_command(label='Cut', command = cmdCut)
editMenu.add_command(label='Copy', command = cmdCopy)
editMenu.add_command(label='Paste', command = cmdPaste)
editMenu.add_command(label='Delete', command = cmdClear)
editMenu.add_separator()
editMenu.add_command(label='Find...', command = cmdFind)
editMenu.add_separator()
editMenu.add_command(label='Select All', command = cmdSelectAll)
editMenu.add_command(label='Time/Date', command = cmdTimeDate)

#help menu
helpMenu = Menu(notepadMenu, tearoff = False)
notepadMenu.add_cascade(label='Help', menu = helpMenu)

#adding options in help menu
helpMenu.add_command(label='About Notepad', command = cmdAbout)

notepad.pack()
root.mainloop()


'''
    Creating the MAIN PROGRAM which will show the backend working of notepad
    NOTE:
          1. THE MAIN PROGRAM IS MENU BASED BACKEND PROGRAM PROMPTING THE USER TO SELECT AN OPTION FROM A GIVEN MENU.
          2. THE MAIN PROGRAM WILL START RUNNING AFTER THE GUI INTERFACE IS CLOSED. 
          3. THE USER CAN CHOOSE TO EXPLORE BACKEND OR FRONTEND WORKING OF NOTEPAD DEPENDING ON HIS/HER PREFERENCE.
          4. BOTH PROGRAMS ARE NOT INDEPENDENT. I.E. THE BACKEND PROGRAM WILL RUN AFTER THE FRONTEND PROGRAM. 
''' 

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext 



class Node2Way(Node):
    def __init__(self,initdata):
        Node.__init__(self,initdata)
        self.previous = None

    def getPrevious(self):
        return self.previous

    def setPrevious(self,newprevious):
        self.previous = newprevious



class CursorBasedList(object):
    
    def __init__(self):
        ''' Creates an empty cursor-based list.'''
        self.head = Node2Way(None)
        self.tail = Node2Way(None)
        self.tail.setPrevious(self.head)
        self.current = None
        self.size = 0

    def hasNext(self):
        ''' Will return True if the current item has a next item.
            Precondition:  the list is not empty.'''
        
        if self.isEmpty():
            raise AttributeError("list is empty")
        else:
            return self.current.getNext() != self.tail
        

    def hasPrevious(self):
        ''' Will return True if the current item has a previous item.
            Precondition:  the list is not empty.'''
        if self.isEmpty():
            raise AttributeError("list is Empty ")
        return self.current.getPrevious() != self.head
    
    def first(self):
        ''' Will move the cursor to the first item
            if there is one.
            Precondition:  the list is not empty.'''
        if self.isEmpty():
            print('The list is empty')
        else:
            self.current=self.head.getNext()
        
    def last(self):
        ''' Will move the cursor to the last item
            if there is one.
            Precondition:  the list is not empty.'''
        if self.isEmpty():
            print('The list is empty')
        else:
            self.current=self.tail.getPrevious()

    def next(self):
        ''' Precondition: hasNext returns True.
            Postcondition: The current item is has moved to the right one item'''
        if (self.hasNext() is None):
            print('No item at next position')
        else:
            self.current=self.current.getNext()

    def previous(self):
        ''' Precondition: hasPrevious returns True.
            Postcondition: The current item is has moved to the left one iten'''
        if not (self.hasPrevious()):
            print('No item at previous position')
        else:
            self.current=self.current.getPrevious()

    def insertAfter(self, item):
        ''' Will insert item after the current item, as the only item if the list is empty.  The new item is the
            current item.'''
        new=Node2Way(item)
        if (self.isEmpty()):
            self.head.setNext(new)
            new.setPrevious(self.head)
            new.setNext(self.tail)
            self.tail.setPrevious(new)
            self.current=new
            self.size+=1
        elif(self.current.getNext() is  self.tail):
            self.current.setNext(new)
            new.setPrevious(self.current)
            new.setNext(self.tail)
            self.tail.setPrevious(new)
            self.current=new
            self.size+=1
        else:
            per=self.current
            top=self.current.getNext()
            per.setNext(new)
            new.setNext(top)
            top.setPrevious(new)
            new.setPrevious(per)
            self.current=new
            self.size+=1

    def insertBefore(self, item):
        ''' Will insert item before the current item, as the only item if the list is empty.  The new item is the
            current item.'''
        new=Node2Way(item)
        if (self.isEmpty()):
            print('empty list')
        elif(self.current.getPrevious() is self.head):
            self.head.setNext(new)
            self.current.setPrevious(new)
            new.setNext(self.current)
            new.setPrevious(self.head)
            self.size+=1
        else:
            per=self.current.getPrevious()
            per.setNext(new)
            new.setNext(self.current)
            new.setPrevious(per)
            self.current.setPrevious(new)
            self.size+=1

    def getCurrent(self):
        ''' Will return the current item without removing it or changing the current position.
            Precondition:  the list is not empty'''
        if self.isEmpty():
            print('empty list')
        else:
         return(self.current.getData())

    def remove(self):
        ''' Will remove and return the current item. Making the next item
            the current item if one exists; otherwise the tail item in the
            list is the current item.
            Precondition: the list is not empty.'''
        if self.isEmpty():
            print('empty list')
        else:
            per=self.current.getPrevious()
            top=self.current.getNext()
            per.setNext(top)
            top.setPrevious(per)
            self.current=per
            self.size-=1

    def replace(self, value):
        ''' Will replace the current item by the newItemValue.
            Precondition: the list is not empty.'''
        new=Node2Way(value)
        if self.isEmpty():
            print("empty list")
        else:
            per=self.current.getPrevious()
            top=self.current.getNext()
            per.setNext(new)
            top.setPrevious(new)
            new.setNext(top)
            new.setPrevious(per)
            self.current=new

    def isEmpty(self):
        if(self.head.getNext() is None):
            return True
        else:
            return False

    def len(self):
        ''' Will return the number of items in the list.'''
        # replace below
        n=self.size
        return n

    def str(self):
        ''' Will include items from first through last.'''
        # replace below
        if self.isEmpty():
            print("Empty list")
        else:
         a="  "
         b=self.head.getNext()
         while b.getNext() is not None:
            a=a+" "+(str(b.getData()))
            b=b.getNext()
         return a
        #TEST BENCH
    def testList():
     print("\nMAIN PROGRAM which will show the backend working of notepad\nNOTE:\n1. THE MAIN PROGRAM IS A MENU BASED BACKEND PROGRAM PROMPTING THE USER TO SELECT AN OPTION FROM THE GIVEN MENU.\n2. THE MAIN PROGRAM WILL START RUNNING AFTER THE GUI INTERFACE IS CLOSED.\n3. THE USER CAN CHOOSE TO EXPLORE BACKEND OR FRONTEND WORKING OF NOTEPAD DEPENDING ON HIS/HER PREFERENCE.\n4. BOTH PROGRAMS ARE NOT INDEPENDENT. I.E. THE BACKEND PROGRAM WILL RUN AFTER THE FRONTEND PROGRAM.")
     print("\n===============================================================")
     print("\nYou may type word(s) or you may type full sentence(s)")
     myList = CursorBasedList()
     while True:
        print("\n===============================================================")
        print("Current List:",myList.str())
        if myList.isEmpty():
            print("Empty list")
        else:
            print("length:",myList.len(), " Current item:", myList.getCurrent())
            print("\n===============================================================")
        print("\n===============================================================")
        print("\nTest Positional List Menu:")
        print("A - Insert After")
        print("B - Insert Before")
        print("C - Get Current")
        print("E - Is Empty")
        print("F - First")
        print("L - Last")
        print("N - Next")
        print("P - Previous")
        print("R - Remove")
        print("U - Replace")
        print("X - Exit Backend Program")
        print("\n===============================================================")
        response = input("Menu Choice? ").upper()
        print("\n===============================================================")
        if response == 'A':
         item = input("Enter the new item to insertAfter: ")
         print("\n===============================================================")
         r=''
         a=0
         g=len(item)
         for u in item:
          r=r+u
          a+=1
          if(u==" " or a==g):
           myList.insertAfter(r)
           r=''    
        elif response == 'B':
         item = input("Enter the new item to insertBefore: ")
         print("\n===============================================================")
         r=''
         a=0
         g=len(item)
         for u in item:
          r=r+u
          a+=1
          if(u==" " or a==g):
           myList.insertBefore(r)
           r=''
        elif response == 'C':
            item = myList.getCurrent()
            print("The current item in the list is:",item)
            print("\n===============================================================")
        elif response == 'E':
            print("isEmpty returned:", myList.isEmpty())
            print("\n===============================================================")
        elif response == 'F':
            myList.first()
            print("\n===============================================================")
        elif response == 'L':
            myList.last()
            print("\n===============================================================")
        elif response == 'N':
            myList.next()
            print("\n===============================================================")
        elif response == 'P':
            myList.previous()
            print("\n===============================================================")
        elif response == 'R':
            item = myList.remove()
            print("item removed:",item)
            print("\n===============================================================")
        elif response == 'U':
            item = input("Enter replacement item: ")
            myList.replace(item)
            print("\n===============================================================")
        elif response == 'X':
            break

        else:
            print("Invalid Menu Choice!")
            print("\n===============================================================")

CursorBasedList.testList() 


        
