# -*- coding: utf-8 -*-
'''
Created on 2016. febr. 23.

Implementation of application interface:

Create Class Application
    Class should contain the following methods
    __init__ constructor to describe the atrributes:    
        canvas , title , entry, labels
    
    draw_gallow() method to draw the gallow. It would
    be nice to solve it from pictures
    
    erase_all() method when starting a new section
    
    missed_letters method to show the missed thing.
    
The following methods should be included from Hangman_BSW file


Need to Fix:

Create buttons for inputs too and for missed letters
@author: SzuroveczD
'''

from Tkinter import *
import Hangman_BSW
import tkMessageBox
from PIL import Image, ImageTk
from doctest import master


 
class Application(Tk):
    
   
    def __init__(self):
        
        Tk.__init__(self, master)
        self.configure(background='white')
        #self.name = Label(self, text = u"A K A S Z T Ó F A", font = 15, padx=10, pady=10, fg = "red", bg = "white").pack()
        self.topic_and_word = Hangman_BSW.tell_secret_word()
        self.topic = Label(self, text = u'Téma: '+ self.topic_and_word[0], font = 10, padx=5, pady=5, bg = "white")
        self.can =  Canvas (self, width = 250, height = 350, bg = "white")
        self.title(u'Akasztófa')
        # Create the main sections of the layout,and lay them out
        self.top = Frame(self)
        self.bottom = Frame(self)
        self.new = Frame(self)
        self.top.pack(side=BOTTOM, padx=5,pady=5)
        self.bottom.pack(side=BOTTOM,padx=5,pady=5)
        self.new.pack(side=BOTTOM)
        # The list of the images has been defined
        self.my_images = []
        self.my_images.append(PhotoImage(file = "man1.gif"))
        self.my_images.append(PhotoImage(file = "man2.gif"))
        self.my_images.append(PhotoImage(file = "man3.gif"))
        self.my_images.append(PhotoImage(file = "man4.gif"))
        self.my_images.append(PhotoImage(file = "man5.gif"))
        self.my_images.append(PhotoImage(file = "man6.gif"))
        self.my_images.append(PhotoImage(file = "man7.gif"))
        self.my_images.append(PhotoImage(file = "man8.gif"))
        self.my_image_number = 0
        self.image_on_canvas = self.can.create_image(0, 0, anchor = NW, image = self.my_images[self.my_image_number])
        self.topic.pack()
        self.show_data()
        
    def show_data(self):
        # Choose a random word from the random topic
        self.secret_word =self.topic_and_word[1]
        # Split the words like that ['h','e', 'l', 'o']
        self.seperate_word = list(self.secret_word)
        # Determine the length of the word
        self.lengthof_seperate_word = len(self.seperate_word)
        # Draw a line line '- - - - - '
        self.show_line = list(self.lengthof_seperate_word * '-')
        # Set starting variables and let the game begin
        self.missed_words = 0 
        self.missed_letters = ''
        self.counter = 1
        self.game_begin()
        
    def game_begin(self):
       
        # Set to StringVar the secret word
        self.Line = self.set_to_stringvar(''.join(self.show_line))
        # Get the StringVar secret word 
        self.secret_line = Label(self,font=("Helvetica",25,"bold"), bg = 'white')
        self.secret_line.configure(text=self.get_variable(self.Line)) 
        # Set to StringVar the Missed Letters
        self.missed_text = self.set_to_stringvar(u'Tévesztett betűk:' + self.missed_letters)
        # Get the StringVar variable  
        self.dynamic_missed_text = Label(self, font = 15)
        self.dynamic_missed_text.configure(text = self.missed_text.get(),bg = 'white')
        self.dynamic_missed_text.pack()   
        '''Pack the canvas here'''
        self.can.pack()
        self.secret_line.pack()
        '''http://stackoverflow.com/questions/2261191/how-can-i-put-2-buttons-next-to-each-other'''
        self.Letters = ['A',u'Á','B','C', 'D', 'E',u'É', 'F', 'G','H', 'I',u'Í','J','K','L','M','N','O',u'Ó',u'Ö',u'Ő','P','Q','R','S','T','U',u'Ú',u'Ü',u'Ű','V','W','X','Y','Z']
        for i in range (0,len(self.Letters)/2):
            self.button_pointer(i,self.bottom)
        for i in range (len(self.Letters)/2,len(self.Letters)):
            self.button_pointer(i,self.top)
        #Button (self.new,text = u'Új Játék').grid(row = 1,column = 2)
        
                
       
   
        
    def game_decide(self):
        # This part of code will be updated every time when the user choose a letter
        # pushes the next button
        self.update_idletasks() 
        self.input_data = self.input.lower()
                 
        self.linespprove = Hangman_BSW.safety_input(self.input_data, self.missed_letters)
        # If the input is incorrect
        if self.linespprove != True:
            tkMessageBox.showwarning('HIBA', self.linespprove)
        # if the input is correct  
        else:
            
            result =  Hangman_BSW.check_if_guessed(self.input_data, self.seperate_word)
            # If missed a letter
            if result == [] :
               
                self.counter += 1
                # Increment Number of missed words by and a missed letters to the list
                self.missed_words += 1
                self.missed_letters += self.input_data
                # Update Text of missed letters
                self.missed_text = (u'Tévesztett betuk:' + ' '.join(self.missed_letters))
                self.dynamic_missed_text.configure (text =self.missed_text)
                '''Change The Picture'''
                self.my_image_number += 1
                if self.my_image_number == len(self.my_images):
                    self.my_image_number = 0
                self.can.itemconfig(self.image_on_canvas, image = self.my_images[self.my_image_number])
                if self.counter == 7:
                    self.my_image_number += 1
                    '''REPAIR THIS METHOD DUPLICATED'''
                    self.can.itemconfig(self.image_on_canvas, image = self.my_images[self.my_image_number])
                    self.secret_line.configure( text = self.secret_word)
                    self.messagebox_ask(u':S Sajnos nem nyert', u'Sajnos ez most nem sikerült akarsz újat játszani ?')
            # If the user found a relevant letter    
            else:
                # Show the letters what the user found instead of lines : e-mple
                self.show_secret_word = ''.join (Hangman_BSW.print_table(self.show_line, result, self.input_data))
                # Refresh the line
                self.secret_line.configure( text = self.show_secret_word)
                # If the user Win
                if self.secret_word == self.show_secret_word:
                    self.messagebox_ask(u"GRATULÁLOK NYERTÉL!!!!", u"Szeretnél újra játszani?")
                         
                
             
               
    
         
    def image(self, nameofpic):
        image = Image.open(nameofpic)
        photo = ImageTk.PhotoImage(image)
        label = Label(self, image=photo)
        label.image = photo
        label.pack()
    
    def set_to_stringvar(self,name):
        temp = StringVar()
        temp.set(name)
        return temp 
    
    def get_variable(self, name):
        return name.get()
    
    def button_pointer(self,i, arrange):
        Button(arrange,text = self.Letters[i],command =lambda: self.test(self.Letters[i]),width=3 ).pack(side =LEFT)
        return
    
   
    
    def test(self,i):
        self.input = i
        self.game_decide()
        return 
        
    
    def stringvar_to_widget(self,label,name):
        label = Label(self)
        label.configure(text=self.get_variable(name)) 
        label.pack()
        return
    
    
    def callback(self,*args):
        print "variable changed!"
        var = StringVar()
        var.trace("w", self.secret_line)
        var.set("hello")
    
    def messagebox_ask (self,title,message):
        decide = tkMessageBox.askyesno(title, message)
        if decide != True:
            self.quit()
        else:
            self.destroy()
            self.__init__()
        
            
def main():
   
    app = Application ()
    app.mainloop()    

def main_destroy():
    main.app.destroy()
    
if __name__ == "__main__":
    main()
    
   
        
        
