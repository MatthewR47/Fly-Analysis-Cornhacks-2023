import time

file = open("..\\Controller\\10252022CtM001.txt", "r")
simulatedNewFile = open("..\\Resources\\simulatedFlyData.txt", "w")


lines = file.readlines()

for line in lines:
    print(line)
    simulatedNewFile = open("..\\Resources\\simulatedFlyData.txt", "a")
    simulatedNewFile.writelines(line)
    simulatedNewFile.close()
    time.sleep(1)
file.close()