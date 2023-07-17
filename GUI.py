from tkinter import *
from tkinter import ttk
from wikiScraper import *
import numpy as np
import matplotlib.pyplot as plt
import wikiScraper as scp
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

champNames = getChampList()
champData = np.zeros((163, 1))
selectedNames = []
champListLabel = "No Champions Selected"

def plotChamp(inputDataFrame:ttk.Frame):
    #TODO: EDIT
    global selectedNames, champData
    fig = plt.figure()
    newPlot = fig.add_subplot(111)
    for i in range(len(selectedNames)):
        champStats = scp.getSpecChampStats(selectedNames[i])
        newPlot.plot(champStats)


    canvas = FigureCanvasTkAgg(fig, inputDataFrame)
    canvas.draw()
    canvas.get_tk_widget().pack()#grid(row=0, column=2, rowspan=10)

def selectButton(name:str, label:Label):
    global selectedNames, champListLabel
    selectedNames.append(name)
    champListLabel = "\n".join(selectedNames)
    label.config(text=champListLabel)
    print(champListLabel)

def clearButton(label:Label):
    global selectedNames, champListLabel
    selectedNames.clear()
    champListLabel = "Champions:\n"
    label.config(text=champListLabel)
    print("clear")

def genInterface():
    global champNames, selectedNames
    
    root = Tk()
    root.geometry("1200x500")
    root.title("LOL STATS")

    inputDataFrame = ttk.Frame(root)
    inputDataFrame.grid(row=0, column=0, sticky=(N, S, E, W))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    secTitle1 = Label(inputDataFrame, text="Select Champions").grid(row=0,column=0)
    statString = StringVar(value="Champion")
    statSelect = ttk.Combobox(inputDataFrame, textvariable=statString)
    statSelect.grid(row=1,column=0)
    statSelect['values'] = champNames
    #NOTE: cannot store the get() value of combobox in variable here for some reason... must get it """""fresh"""""

    charList = Label(inputDataFrame)
    charList.config(text=champListLabel)
    charList.grid(row=3,column=0, rowspan=5)
    
    Button(inputDataFrame, text="Select",
           command=lambda: selectButton(statSelect.get(), charList)).grid(row=1, column=1)
    
    Button(inputDataFrame, text="Graph",
           command=lambda: plotChamp(inputDataFrame)).grid(row=2, column=1)
    
    Button(inputDataFrame, text="Clear",
           command=lambda: clearButton(charList)).grid(row=3, column=1)
    
    root.mainloop()
    

genInterface()