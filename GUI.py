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
statList = ["Health", "Mana", "Health Regen", "Mana Regen", "Armor", "Attack", "Magic Resist"]
xlvls = np.arange(1,19)


def generateSubplots(fig:plt.figure):
    subplotList = []
    for i in range(numStats):
        newPlot = fig.add_subplot(3, 3, (i + 1))
        subplotList.append(newPlot)
    return subplotList

def plotChamp(inputDataFrame:ttk.Frame):
    #TODO: EDIT Get More Stats
    global selectedNames, champData, xlvls, statList
    fig = plt.figure(figsize=(10,8))
    subplotList = generateSubplots(fig)

    for c in range(len(selectedNames)):#TODO: EDIT THIS FOR MORE STATS
        champStats = scp.getSpecChampStats(selectedNames[c])

        for i in range(numStats):
            newPlot = subplotList[i]
            line, = newPlot.step(xlvls, champStats[:, i], where="pre")
            line.set_label(selectedNames[c])

            newPlot.legend()
            newPlot.set_title(statList[i])
            newPlot.set_xticks(range(0, 20))

    canvas = FigureCanvasTkAgg(fig, inputDataFrame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=2, rowspan=40)

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
    root.geometry("1200x800")
    root.title("LOL STATS")

    inputDataFrame = ttk.Frame(root)
    inputDataFrame.grid(row=0, column=0, sticky=(N, S, E, W))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    secTitle1 = Label(inputDataFrame, text="Select Champions").grid(row=0,column=0)
    statString = StringVar(value="Champion")
    champSelect = ttk.Combobox(inputDataFrame, textvariable=statString)
    champSelect.grid(row=1,column=0)
    champSelect['values'] = champNames
    #NOTE: cannot store the get() value of combobox in variable here for some reason... must get it """""fresh"""""

    charList = Label(inputDataFrame)
    charList.config(text=champListLabel)
    charList.grid(row=4,column=0, rowspan=5)
    
    Button(inputDataFrame, text="Select",
           command=lambda: selectButton(champSelect.get(), charList)).grid(row=1, column=1)
    
    Button(inputDataFrame, text="Graph",
           command=lambda: plotChamp(inputDataFrame)).grid(row=2, column=1)
    
    statSelect = ttk.Combobox(inputDataFrame, textvariable="Select Stat")
    statSelect.grid(row=2,column=0)
    statSelect['values'] = statList
    
    Button(inputDataFrame, text="Clear",
           command=lambda: clearButton(charList)).grid(row=3, column=1)
    
    root.mainloop()
    

genInterface()