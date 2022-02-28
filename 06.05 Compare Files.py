

#onefile = open("/workspace/IFSC1202/Assignments/Unit 6 HW/Text Files/06.05 CompareFileA.txt", "r")
#twofile = open("/workspace/IFSC1202/Assignments/Unit 6 HW/Text Files/06.05 CompareFileB.txt", "r")
onefile = open("/workspace/IFSC1202SU/06.05 CompareFileA.txt", "r")
twofile = open("/workspace/IFSC1202SU/06.05 CompareFileB.txt", "r")
a = onefile.readline()
b = twofile.readline()
line = 0
count = 0

while a != "":
    line += 1
    if a != b:
        count += 1
        print("Line: {} - File A: {}".format(line,a))
        print("Line: {} - File B: {}".format(line,b))
    a = onefile.readline()
    b = twofile.readline()
print("{} differences".format(count))
