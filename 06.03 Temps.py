
def FahrToCel(f):
    c = (f - 32) * 5 / 9
    return c

#ftempsfile = open("/workspace/IFSC1202/Assignments/Unit 6 HW/Text Files/06.03 FTemps.txt", "r")
ftempsfile = open("/workspace/IFSC1202SU/06.03 FTemps.txt", "r")
f = float(ftempsfile.readline())
#ctempsfile = open("/workspace/IFSC1202/Assignments/Unit 6 HW/Text Files/06.03 CTemps.txt", "w")
ctempsfile = open("/workspace/IFSC1202SU/06.03 CTemps.txt", "w")
i = 0
while f != "":
    ctempsfile.write("{:.1f}\n".format(FahrToCel(f)))
    i += 1
    f = float(ftempsfile.readline())
print("{} records written".format(i))
ftempsfile.close()
ctempsfile.close()
