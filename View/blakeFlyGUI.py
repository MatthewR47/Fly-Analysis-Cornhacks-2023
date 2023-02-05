# CornHacks 2023
# GUI window

import tkinter
import tkinter.filedialog
from Controller.FileController import File
from Model.FlyModel import FlyGroup
import math


class FlyGUI:

    def openFileDialog(self):
        self.fileTest = tkinter.filedialog.askopenfilename()
        if self.fileTest.endswith(".txt"):
            self.testFile = File(self.fileTest)
            self.makeGrid()

    def makeGrid(self, width=4):
        # calculate top 25%
        self.testFlyGroup = FlyGroup(self.testFile.fileToArray())
        self.top25Array = self.testFlyGroup.top25P()
        top25Len = len(self.top25Array)
        for x in range(0, top25Len):
            row = math.floor(x / width)
            col = x % width
            tkinter.Label(self.grid_frame, text='Fly #%02d:' % (x + 1)).grid(row=row, column=(col * 2))
            tkinter.Label(self.grid_frame, text='YES' if self.top25Array[x][1] == 1 else '').grid(row=row,
                                                                                               column=(col * 2 + 1))
    def loadText(self):
        #Calculations here:

        #LastMove_Min
        groupLength = len(self.testFlyGroup.flyArray)-1
        col = 0
        self.lastMoveMin = 9999
        for mv in self.testFlyGroup.flyArray[groupLength]:
            if col > 9:
                self.lastMoveMin = mv if int(self.lastMoveMin)>int(mv) else self.lastMoveMin
            col+=1
        #LastMove_Max
        col = 0
        self.lastMoveMax = 0
        for mv in self.testFlyGroup.flyArray[groupLength]:
            if col > 9:
                self.lastMoveMax = mv if int(self.lastMoveMax)<int(mv) else self.lastMoveMax
            col+=1
        #Top25%
        copy = self.testFlyGroup
        copy.doRegression(True)
        lastTop25 = (len(copy.indexedPredVals)-1)//4
        self.Top25P = copy.indexedPredVals[lastTop25][1]
        #---

        # Create the frames to display tkinter frames.
        self.row1_frame = tkinter.Frame(self.main_window)
        self.row2_frame = tkinter.Frame(self.main_window)
        self.row3_frame = tkinter.Frame(self.main_window)

    def infoBox(self):
        tkinter.messagebox.showinfo("CornHacks 2023",
                                    "GitHub Repository\nhttps://github.com/MatthewR47/Fly-Analysis-Cornhacks-2023\n\n"
                                    "John Behrens\thttps://github.com/jrbdino\n"
                                    "Blake Meyer\thttps://github.com/willblakemeyer\n"
                                    "John Reagan\thttps://github.com/binaryBronco\n"
                                    "Matt Rokusek\thttps://github.com/MatthewR47")

    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()
        self.main_window.title("Fly Analysis")

        # Create the menu
        self.menubar = tkinter.Menu(self.main_window)
        self.filemenu = tkinter.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="Load File", command=self.openFileDialog)
        self.filemenu.add_command(label="Exit", command=self.main_window.quit)
        self.menubar.add_command(label="About", command=self.infoBox)
        self.main_window.config(menu=self.menubar)

        # self.loadText()

        # Create and pack the 8 rows of flies, 4 columns each.
        # fly_label = list(range(1, 33))
        # fly_label = []
        # row_frame = list(range(1, 9))
        # row_frame = []

        self.grid_frame = tkinter.Frame(self.main_window)
        self.testFile = File()
        self.makeGrid(4)

        self.loadText()
        # for numTake in range(1, 4-(top25Len%4)+1):
        #     tkinter.Label(self.grid_frame, text='').grid(row=numRows+1, column=(col * 2 - 1))
        #     tkinter.Label(self.grid_frame, text='').grid(row=numRows+1, column=(col * 2))

        # Pack the frames.
        self.row1_frame.pack()
        self.row2_frame.pack()
        self.row3_frame.pack()
        self.grid_frame.pack()

        # Start the main loop.
        tkinter.mainloop()


# Create an instance of the FlyGUI class.
fly_gui = FlyGUI()

'''
def main():
    # Create the main window widget.
    main_window = tkinter.Tk()

    # Enter the tkinter main loop.
    tkinter.mainloop()

# Call the main function.
main()
'''
