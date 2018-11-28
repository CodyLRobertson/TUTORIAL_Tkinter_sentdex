#Tutorial Walkthrough with YouTube's Sentdex

#{Videos Complete:
#1




#{Link: https://pythonprogramming.net/object-oriented-programming-crash-course-tkinter/?completed=/tkinter-depth-tutorial-making-actual-program/}



import tkinter as tk 																#{NOTE: What is OOP?>Object Oriented Program uses Instances of Objects sometimes generated from Class templates.}
class SeaofBTCapp(tk.Tk): 															#{Inheritance goes here. Other Classes}	
	def __init__(self, *args, **kwargs):											#{*args = Short for Arguments, can pass any number of variables.; *qwargs = Usually for dictionaries. 99.9999999999999% of the time. } 
																					#We did not rename tk.Tk as Root, subsequently root does not equal r. Change later?

		tk.Tk.__init__(self, *args, **kwargs)											#{always use a container to populate.}
		container = tk.Frame(self)

		container.pack(side="top",fill="both",expand=True)

		container.grid_rowconfigure(0, weight=1)										#Weight = Priority
		container.grid_columnconfigure(0, weight=1)
		self.frames = {}																#

		frame = StartPage(container, self)

		self.frames[StartPage] = Frame

		frame.grid(row=0,column=0,sticky="nsew")



