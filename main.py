from tkinter import *
from tkinter import ttk

import random
from colors import *

# importing all the Algos from diffrent directory
from Algos.BubbleSort import bubble_sort
from Algos.MergeSort import merge_sort
from Algos.InsertionSort import insertion_sort
from Algos.SelectionSort import Selection_sort
from Algos.HeapSort import heapSort


# creating a window
window = Tk()
window.title("Sorting Visualizer")
window.maxsize(1000, 700)
window.config(bg=WHITE)

algo_name = StringVar()
algo_list = ['Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Heap Sort']
# algo_list = ['Bubble Sort', 'Merge Sort', ,'Insertion Sort']

speed_name = StringVar()
speed_list = ['Fast', 'Medium', 'Slow']

array_set = StringVar()
array_list = ['25', '50', '75', '100']


data = []


# creating random values rectangles / bars
def drawdata(data, ColorArray):

    canvas.delete('all')

    canvas_width = 800
    canvas_heigth = 400
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2

    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_heigth - height * 390
        x1 = (i+1) * x_width + offset
        y1 = canvas_heigth

        # print(x1, y1)
        canvas.create_rectangle(x0, y0, x1, y1, fill=ColorArray[i])

    window.update_idletasks()



# it will create no. of bars by choosing the value in the combobox
def allow_no():
    if array_menu.get() == '25':
        return 25

    elif array_menu.get() == '50':
        return 50

    elif array_menu.get() == '75':
        return 75

    else:
        return 100


# it helps to generate a array and draw rectangles in Canvas
def generate():
    global data

    data = []

    hello = allow_no()

    for i in range(0, hello):
        random_value = random.randint(1, 80)
        data.append(random_value)

    # print(data)
    # print(len(data))

    drawdata(data, [BLUE for x in range(len(data))])


# function to control the speed of sorting process
def set_speed():
    if speed_menu.get() == 'Slow':
        return 0.3

    elif speed_menu.get() == 'Medium':
        return 0.1
    
    else:
        return 0.001


# here you can select the Sorting Algorithm
def sort():
    global data

    timeTick = set_speed()

    if algo_menu.get() == "Bubble Sort":
        bubble_sort(data, drawdata, timeTick)

    elif algo_menu.get() == "Heap Sort":
        heapSort(data, drawdata, timeTick)

    elif algo_menu.get() == 'Selection Sort':
        Selection_sort(data, drawdata, timeTick)

    elif algo_menu.get() == 'Insertion Sort':
        insertion_sort(data, drawdata, timeTick)

    elif algo_menu.get() == 'Merge Sort':
        merge_sort(data, 0, len(data) + 1, drawdata, timeTick)



# User Interface 

UI_Frame = Frame(window, width=900, height=300, bg=WHITE)
UI_Frame.grid(row=0, column=0, padx=10, pady=10)


# Dropdown to select sorting algo
l1 = Label(UI_Frame, text="Algorithm : ", bg=WHITE)
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)

algo_menu = ttk.Combobox(UI_Frame, textvariable = algo_name, values=algo_list)
algo_menu.grid(row = 0, column=1, padx=5, pady=5)
algo_menu.current(0)


# Dropdown to select sorting speed
l2 = Label(UI_Frame, text="Sorting Speed : ", bg=WHITE)
l2.grid(row=1, column=0, padx=10, pady=5, sticky=W)

speed_menu = ttk.Combobox(UI_Frame, textvariable = speed_name, values=speed_list)
speed_menu.grid(row = 1, column=1, padx=5, pady=5)
speed_menu.current(0)



# Dropdown to select No of array
l3 = Label(UI_Frame, text="Array List : ", bg=WHITE)
l3.grid(row=2, column=0, padx=10, pady=5, sticky=W)

array_menu = ttk.Combobox(UI_Frame, textvariable = array_set, values=array_list)
array_menu.grid(row = 2, column=1, padx=5, pady=5)
array_menu.current(0)


# sort button
b1 = Button(UI_Frame, text="Sort", command=sort, bg=LIGHT_GRAY)
b1.grid(row=4, column=1, padx=5, pady=5)

# generate array button
b2 = Button(UI_Frame, text='Generate Array', command=generate, bg=LIGHT_GRAY)
b2.grid(row=4, column=0, padx=5, pady=5)

# canvas to draw our array
canvas = Canvas(window, width=800, height=400, bg=LIGHT_GRAY)
# canvas = Canvas(window, width=800, height=400, bg=LIGHT_GREEN)
canvas.grid(row=1, column=0, padx=10, pady=5)

########################################################################################



window.mainloop()