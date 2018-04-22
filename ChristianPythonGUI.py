# CHRISTIAN BAEZA: GUI TO FIND VALUES FOR CERTAIN QUESTIONS
from tkinter import *
from math import sqrt
#import pdb
from rect import Rectangle


def checking(codeList):
    fcount=0
    for Rcode in codeList:
        if len(Rcode) !=10 \
           or Rcode[1] != '{'\
           or Rcode[0] in string.ascii_lowercase\
           or Rcode[3] != '*'\
           or Rcode[4] not in string.digits\
           or Rcode[5] in string.ascii_lowercase\
           or Rcode[6] in string.ascii_lowercase\
           or Rcode[9] in string.ascii_lowercase\
           or Rcode[8]  in string.ascii_lowercase\
           or Rcode[7] != '}' \
           or Rcode[2] in string.ascii_lowercase :
                fcount+=1
    return fcount

class RecCounter():
   def __init__(self):
      self.reset()
      
   def reset(self):
##      self.area = 0
##      self.count=0
##      self.max_diag = 0.0

      self.count  = 0
      self.countq1=0
      self.maximum=0
      self.totalq3=0
      self.countq3=0
      self.formatcountq4=0
      self.totalq5=0
      self.countq6=0
      self.countq7=0
      
   def add(self, rectangle):
      # print(rec)
##      self.area += rec.get_area()
##      self.count += 1
##      if self.max_diag < rec.get_diag():
##         self.max_diag = rec.get_diag()
      self.count += 1  # every time I add a Rectangle I add 1

      #q1
      if rectangle.getStat()=="Fog":  #Fog is the word I want to find in the stat field
         self.countq1=self.countq1+1
      #q2
      if rectangle.getValue()>self.maximum: # Finds the Maximum value in the column 
         self.maximum=rectangle.getValue()
      #q3
      self.totalq3=self.totalq3+1
      if rectangle.getWidth()>=11 and rectangle.getWidth()<=20:
         self.countq3=self.countq3+1

      #q4

      if checking(rectangle.getCode()) >1:
         self.formatcountq4=self.formatcountq4+1
            
      #q5
      if rectangle.getQuant() >= 602 and rectangle.getQuant()<= 2075:
         self.totalq5 += rectangle.getQuant()
         
      #q6
      if rectangle.getSwitch()=="On":
         self.countq6=self.countq6+1
         
      #7
      if rectangle.getValue()>692.74 or rectangle.getStat()=="Cloud":
         self.countq7=self.countq7+1
         
##   def get_max_diag(self): return self.max_diag
##   def get_area(self): return self.area
##   def get_count(self): return self.count

   def myq1(self):
      return ("(1) The number of times fog comes up is: %d " %(self.countq1))

   def myq2(self):
      return("(2) The maximum number in the field[value] is: %d " %(self.maximum))

   def myq3(self):
      return("(3) The percentage of the numbers in [width] lie between (11) and (20) inclusive : %6.2f " %((self.countq3/self.totalq3)*100))

   def myq4(self):
       return("(4)The values in the 'code' field do not match the format X{X*9XX}XX is: %d" %(self.formatcountq4))
      
   def myq5(self):
       return("(5)The sum of the numbers in field [quant] between (602) and (2075) inclusive : %d" %(self.totalq5))              
   
   def myq6(self):
      return("(6)The number of times On comes up is: %d " %(self.countq6))

   def myq7(self):
      return("(7)The lines where value is more than 692.74 *or* stat's have the value (Cloud): %d " %(self.countq7))



class RecReader():
   def __init__(self, filename, counter, recgui):
     
      self.gui = recgui
      self.counter = counter
      self.infile = open(filename, 'r')
      if not self.infile:
         self.gui.fileNotFound()    # this leads to studying exceptions
      else:
         self.run()         
         
   def run(self):
      
      firstline = True
      for line in self.infile:
         if firstline:
            firstline = False
            continue

         
##         fields = line.split(',')
##         width = int(fields[0].strip())
##         height= int(fields[1].strip())
##         self.counter.add( Rectangle(width,height))

         line = line.strip ()
         fields = line.split (",")           #mapping each of the colums in the excel spreadsheet to their field name this makes it easier for me to type their column name instead of their position again 
         stat = str( fields [0])
         value = float(fields [1])
         width = int(fields [2])
         code = fields [3]
         quant = int(fields [4])
         switch =  str(fields [5])
             # then I pass a complete Rectangle to the counter object 
         self.counter.add( Rectangle(stat, value, width, code, quant, switch))
         
         
      self.infile.close()
      self.gui.notify()
      

class RecGUI():
   def __init__(self, root):
      self.ok = False # indicate if there has been a valid read
      self.counter = RecCounter()
      
      Label(root,font="mono -36 bold", justify="center", 
             text="Christian's GUI Program").grid(row=0, column=0, columnspan=3, sticky=N)
           
      Label(root, text="Enter Filename: ", width=15).grid(row=1, column=0, sticky=E)
      self.flname = Entry(root, width=15, bg="white")

      self.flname.grid(row=1, column=1, stick=W)
      Button(root,text="GO!!", command=self.process_file).grid(row=1,column=2)
#q1
      Label(root, text="Question 1:", width=10).grid(row=2, column=1, sticky=E)
      self.q1= Label(root, width=80)
      self.q1.grid(row=2,column=2, sticky=W)
#q2
      Label(root, text="Question 2:", width=10).grid(row=3, column=1, sticky=E)
      self.q2=Label(root, width=80)
      self.q2.grid(row=3,column=2, sticky=W)
#q3
      Label(root, text="Question 3:", width=10).grid(row=4, column=1, sticky=E)
      self.q3=Label(root, width=80)
      self.q3.grid(row=4,column=2, sticky=W)
#q4
      Label(root, text="Question 4:", width=10).grid(row=5, column=1, sticky=E)
      self.q4= Label(root, width=80)
      self.q4.grid(row=5,column=2, sticky=W)
#q5
      Label(root, text="Question 5:", width=10).grid(row=6, column=1, sticky=E)
      self.q5= Label(root, width=80)
      self.q5.grid(row=6,column=2, sticky=W)
#q6
      Label(root, text="Question 6:", width=10).grid(row=7, column=1, sticky=E)
      self.q6= Label(root, width=80)
      self.q6.grid(row=7,column=2, sticky=W)
#q7
      Label(root, text="Question 7:", width=10).grid(row=8, column=1, sticky=E)
      self.q7= Label(root, width=80)
      self.q7.grid(row=8,column=2, sticky=W)

      #self.maxDgLbl.grid(row=4,column=2, sticky=W)
      #self.mssg=Label(root)
      #self.mssg.grid(row=5,column=0,columnspan=3)
       
      
   def process_file(self, ev=None):
      filename = self.flname.get()
      
      if len(filename) > 4:    #chance it may be ok
         self.ok = True
         self.counter.reset()
         self.reader=RecReader(filename, self.counter, self)
      
   def fileNotFound(self):
      self.ok = False
      
   def message(self, amssg):
      self.mssg['text']=amssg
      
   def notify(self):
      if self.ok:
         self.q1['text'] = str(self.counter.myq1())
         self.q2['text'] = str(self.counter.myq2())
         self.q3['text'] = str(self.counter.myq3())
         self.q4['text'] = str(self.counter.myq4())
         self.q5['text'] = str(self.counter.myq5())
         self.q6['text'] = str(self.counter.myq6())
         self.q7['text'] = str(self.counter.myq7())
 
   ##########################
   ### It all starts here ###
   ##########################
      
if __name__ == "__main__":
   top = Tk()
   top.geometry("750x300")#GUI WINDOW SIZE 
   top.title("Christian Baeza's GUI Program") 
   top.grid()
   
   app = RecGUI(top)
   
   top.mainloop()
      
