from tkinter import *
from tkinter import ttk
from wikiScraper import *
import numpy as np
import matplotlib.pyplot as plt

champNames = getChampList()

def generateGraph(data:np.array):
    #TODO: EDIT 
    plt.plot(data)
    plt.show()



def genInterface():
    global champNames
    root = Tk()
    root.geometry("800x500")
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

    root.mainloop()

genInterface()