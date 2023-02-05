import os
from Model.FlyModel import FlyGroup
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class File:

    # init method or constructor
    def __init__(self, event_handler, path=""):
        # Using above file path as testing only. Can input other file path instead if necessary.
        self.path = path
        self.array2D = []

        script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
        rel_path = self.path
        abs_file_path = os.path.join(script_dir, rel_path)
        self.file = open(abs_file_path, 'r')
        self.flyModel = FlyGroup(self.fileToArray())
        self.event_handler = event_handler
        self.observe = Observer()
        filename = rel_path.split("/")[len(rel_path.split("/"))-1]
        self.observe.schedule(self.event_handler, path=abs_file_path.replace(filename, "")[:-1], recursive=False)

        self.observe.start()

    def unregisterFile(self):
        self.observe.stop()

    # Sample Method
    def readFile(self):
        # grab information about the flies given a path.
        #     Read through file

        lines = self.file.readlines()

        count = 0
        # Strips the newline character
        for line in lines:
            count += 1
            print("Line{}: {}".format(count, line.strip()))

    def fileToArray(self):
        self.array2D = []

        with open(self.path, 'r') as f:
            for line in f.readlines():
                self.array2D.append(line.split('\t'))
        return self.array2D

    def changePath(self, path):
        self.path = path


# print("default (relative) file path test:")
# p = File()
# p.fileToArray()
#
# print("absolute/input file path test:")
# p = File("C:\\Users\\willb\\PycharmProjects\\CornHacks2023\\Fly-Analysis\\Resources\\Hardening Experiments\\DAM2_6hr_39\\10252022CtM001.txt")
# p.fileToArray()


# Reverse read file in case we need it
# def read_reverse_order(file_name):
#     # Open file for reading in binary mode
#     with open(file_name, 'rb') as read_obj:
#         # Move the cursor to the end of the file
#         read_obj.seek(0, os.SEEK_END)
#         # Get the current position of pointer i.e eof
#         pointer_location = read_obj.tell()
#         # Create a buffer to keep the last read line
#         buffer = bytearray()
#         # Loop till pointer reaches the top of the file
#         while pointer_location >= 0:
#             # Move the file pointer to the location pointed by pointer_location
#             read_obj.seek(pointer_location)
#             # Shift pointer location by -1
#             pointer_location = pointer_location - 1
#             # read that byte / character
#             new_byte = read_obj.read(1)
#             # If the read byte is new line character then it means one line is read
#             if new_byte == b'\n':
#                 # Fetch the line from buffer and yield it
#                 yield buffer.decode()[::-1]
#                 # Reinitialize the byte array to save next line
#                 buffer = bytearray()
#             else:
#                 # If last read character is not eol then add it in buffer
#                 buffer.extend(new_byte)
#         # As file is read completely, if there is still data in buffer, then its the first line.
#         if len(buffer) > 0:
#             # Yield the first line too
#             yield buffer.decode()[::-1]

