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


def plotChamp(data:np.array, inputDataFrame:ttk.Frame):
    #TODO: EDIT
    fig = plt.figure()
    newPlot = fig.add_subplot(111)
    newPlot.plot(data)

    canvas = FigureCanvasTkAgg(fig, inputDataFrame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=2)



def genInterface(name:str):
    global champNames, selectedNames
    selectedNames.append(name)
    
    
    root = Tk()
    root.geometry("1200x500")
    root.title("LOL STATS")

    inputDataFrame = ttk.Frame(root)
    inputDataFrame.grid(row=0, column=0, sticky=(N, S, E, W))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    secTitle1 = Label(inputDataFrame, text="Individual Stats").grid(row=0,column=0)
    statString = StringVar(value="Champion Stat")
    statSelect = ttk.Combobox(inputDataFrame, textvariable=statString)
    statSelect.grid(row=0,column=0)
    statSelect['values'] = champNames
    #NOTE: cannot store the get() value of combobox in variable here for some reason... must get it """""fresh"""""
    Button(inputDataFrame, text="Select",
           command=lambda: plotChamp(scp.getSpecChampStats(statSelect.get()), inputDataFrame)).grid(row=0, column=1)
    
    Button(inputDataFrame, text="Graph",
           command=lambda: plotChamp(scp.getSpecChampStats(statSelect.get()), inputDataFrame)).grid(row=0, column=1)
    
    
    root.mainloop()
    

genInterface()