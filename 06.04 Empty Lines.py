#inputfile = open("/workspace/IFSC1202/Assignments/Unit 6 HW/Text Files/06.04 EmptyLinesInput.txt", "r")
#outputfile = open("/workspace/IFSC1202/Assignments/Unit 6 HW/Text Files/06.04 EmptyLinesOutput.txt", "w")
inputfile = open("/workspace/IFSC1202/06.04 EmptyLinesInput.txt", "r")
outputfile = open("/workspace/IFSC1202/06.04 EmptyLinesOutput.txt", "w")

# Read the first line of the input file
x = inputfile.readline()
r = 0
w = 0
# Read until the input is empty
while x != "":
     r += 1
     if x != "\n":
          outputfile.write(x)
          w += 1
# Read the next line of the input file
     x = inputfile.readline()

# Close both files
inputfile.close()
outputfile.close()
print("{} records read".format(r))
print("{} records written".format(w))