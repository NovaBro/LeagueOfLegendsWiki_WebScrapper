from tkinter import *
from tkinter import ttk
from wikiScraper import *
import numpy as np
import matplotlib.pyplot as plt
import wikiScraper as scp

champNames = getChampList()

def generateGraph1(data:np.array):
    #TODO: EDIT
    
    print(data[0,:,0])
    for champion in data:
        plt.plot(champion[:,0])

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
    statSelect.get()
    

    
    Button(inputDataFrame, text="Make Graph",
           command=lambda: generateGraph1(scp.getChampStats(10))).grid(row=6, column=2)




    root.mainloop()

genInterface()