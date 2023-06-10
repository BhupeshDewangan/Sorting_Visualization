import time
from colors import *


# Function for Selection_Sort
def Selection_sort(data, drawdata, timetick):
    for i in range(len(data) - 1):
        min = i
        for k in range(i+1, len(data)):
            if data[k] < data[min]:
                min = k

        data[min], data[i] = data[i], data[min]
        drawdata(data, [YELLOW if x == min or x == i else PURPLE for x in range(len(data))])
        time.sleep(timetick)

    drawdata(data, [BLUE for x in range(len(data))])