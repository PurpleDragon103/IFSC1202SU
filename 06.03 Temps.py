
def FahrToCel(f):
    c = (float(f) - 32) * 5 / 9
    return c

#ftempsfile = open("/workspace/IFSC1202/Assignments/Unit 6 HW/Text Files/06.03 FTemps.txt", "r")
ftempsfile = open("/workspace/IFSC1202/06.03 FTemps.txt", "r")
f = ftempsfile.readline()
#ctempsfile = open("/workspace/IFSC1202/Assignments/Unit 6 HW/Text Files/06.03 CTemps.txt", "w")
ctempsfile = open("/workspace/IFSC1202/06.03 CTemps.txt", "w")
i = 0
while f != "":
    ctempsfile.write("{:.1f}\n".format(FahrToCel(f)))
    i += 1
    f = ftempsfile.readline()

ftempsfile.close()
ctempsfile.close()
print("{} records written".format(i))
