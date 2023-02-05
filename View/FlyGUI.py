# CornHacks 2023
# GUI window

import tkinter
import tkinter.filedialog

from watchdog.events import FileSystemEventHandler

from Controller.FileController import File
from Model.FlyModel import FlyGroup

class Handler(FileSystemEventHandler):
    def __init__(self, flyGui):
        self.flyGui = flyGui

    def on_modified(self, event):
        self.flyGui.updateGrid()

class FlyGUI:

    def openFileDialog(self):
        self.fileTest = tkinter.filedialog.askopenfilename()
        if self.fileTest.endswith(".txt"):
            self.event_handler = Handler(self)
            self.testFile = File(self.event_handler, self.fileTest)

    def updateGrid(self, width=4):
        # calculate top 25%
        testFlyGroup = FlyGroup(self.testFile.fileToArray())
        top25Array = testFlyGroup.top25P()
        top25Len = len(top25Array)
        for x in range(0, top25Len):
            # row = math.floor(x / width)
            row = x // width
            col = (2 * (x % width) + 1)
            tkinter.Label(self.grid_frame, text='YES' if top25Array[x][1] == 1 else '', width=5).grid(row=row,
                                                                                                       column=col)

        testFlyGroup.doRegression()

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
        self.main_window.title("Top 25% Fly Monitor")

        # Create the menu
        self.menubar = tkinter.Menu(self.main_window)
        self.menubar.add_command(label="LOAD",  command=self.openFileDialog)
        self.menubar.add_command(label="ABOUT", command=self.infoBox)
        self.menubar.add_command(label="EXIT", command=self.main_window.quit)
        self.main_window.config(menu=self.menubar)

        # Print the static fly grid indicators.
        self.grid_frame = tkinter.Frame(self.main_window)

        for row in range(0, 8):
            for col in range(0, 8):
                if col % 2 == 0:
                    tkinter.Label(self.grid_frame, text='Fly #%02d:' % (4*row+col//2+1), width=5).grid(row=row, column=col)
                else:
                    tkinter.Label(self.grid_frame, text='', width=5).grid(row=row, column=col)

        self.main_window.grid_columnconfigure(2, minsize=1000)

        self.event_handler = Handler(self)

        # for numTake in range(1, 4-(top25Len%4)+1):
        #     tkinter.Label(self.grid_frame, text='').grid(row=numRows+1, column=(col * 2 - 1))
        #     tkinter.Label(self.grid_frame, text='').grid(row=numRows+1, column=(col * 2))

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