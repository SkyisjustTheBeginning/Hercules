import os
print("Notepad")
name = input("Name of Notepad File: ")
handle = open(name+".txt","w")
num = input("Number of lines:")
for i in range(int(num)):
    line = input("Text for line:")
    handle.write(line)
    handle.write("\n")
print("Opening note")
os.startfile(name+".txt")