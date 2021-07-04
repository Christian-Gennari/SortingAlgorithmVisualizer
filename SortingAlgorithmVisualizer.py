import tkinter
import random
from tkinter.constants import HORIZONTAL, SW, W
from tkinter.ttk import Combobox
from typing import Text
import SortingAlgorithms

rootWindow = tkinter.Tk()
rootWindow.title("Sorting Algorithm Visualizer")
rootWindow.minsize(900, 540)
rootWindow.maxsize(900, 540)
rootWindow.tk_setPalette("lightgray")

# Variables
selected_Algorithm = tkinter.StringVar()
data = []


# Functions
def drawData(data, colorArray):
    # Resets the canvas
    canvas.delete("all")

    c_height = 380
    c_width = 900
    x_width = c_width / (len(data) + 1)
    offset = 20
    spacing = 10
    normalizedData = [i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        # top left corner
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        # bottom right corner
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        # Drawing data columns
        canvas.create_rectangle(x0, y0, x1,y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))

    rootWindow.update_idletasks()

def Generate():
    global data    
    # Getting the user input from the UI and storing it as int
    minValue = int(minEntry.get())
    maxValue = int(maxEntry.get())
    size = int(sizeEntry.get())

    # Creating a data list and adding values based on user input
    data = []
    for each in range(size):
        data.append(random.randrange(minValue, maxValue+1))

    drawData(data, ["lightblue" for x in range(len(data))])

def StartAlgorithm():
    global data
    if not data: return

    if (algorithmMenu.get() == "Quick Sort"):
        SortingAlgorithms.quick_sort(data, 0, len(data)-1, drawData, speedScale.get())

    elif (algorithmMenu.get() == "Bubble Sort"):
        SortingAlgorithms.bubble_sort(data, drawData, speedScale.get())
    
    elif (algorithmMenu.get() == "Merge Sort"):
        SortingAlgorithms.merge_sort(data, drawData, speedScale.get())
    
    drawData(data, ["lightgreen" for x in range(len(data))])

  

#Frame / base layout
UI_frame = tkinter.Frame(rootWindow, width =900, height=200)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = tkinter.Canvas(rootWindow, width=900, height=380, bg="WhiteSmoke")
canvas.grid(row=1, column=0, padx=0, pady=5)


# User Interface
# Row [0]
tkinter.Label(UI_frame, text="Selected algorithm: ").grid(row=0, column=0, padx=0, pady=5, sticky=W)
algorithmMenu = Combobox(UI_frame, textvariable=selected_Algorithm, values=["Bubble Sort", "Quick Sort", "Merge Sort"])
algorithmMenu.grid(row=0, column=1, padx=5, pady=5)
algorithmMenu.current(0)

speedScale = tkinter.Scale(UI_frame, from_=0.1, to=2.0, length=200, digits=2, resolution=0.1, orient=HORIZONTAL, label="Select Speed [operations/sec]")
speedScale.grid(row=0, column=2, padx=5, pady=5)

#Start Button
tkinter.Button(UI_frame, text="Start sorting!", command=StartAlgorithm, bg="lightgreen").grid(row=0, column=3, padx=5, pady=5)


# Row [1]
sizeEntry = tkinter.Scale(UI_frame, from_=3, to=25, resolution=1, orient=HORIZONTAL, label="Data Size")
sizeEntry.grid(row=1, column=0, padx=5, pady=5)

minEntry = tkinter.Scale(UI_frame, from_=0, to=10, resolution=1, orient=HORIZONTAL, label=" Minimum value")
minEntry.grid(row=1, column=1, padx=5, pady=5)

maxEntry = tkinter.Scale(UI_frame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="Maximum value")
maxEntry.grid(row=1, column=2, padx=5, pady=5)

# Generate button
tkinter.Button(UI_frame, text="Generate data", command=Generate, bg="lightblue").grid(row=1, column=3, padx=5, pady=5)


rootWindow.mainloop()