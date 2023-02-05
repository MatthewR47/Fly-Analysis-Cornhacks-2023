from Model.FlyModel import FlyGroup
from Controller.FileController import File

file = File()
group = FlyGroup(file.fileToArray())

result = group.top25P()
print(result)