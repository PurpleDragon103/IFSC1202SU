
def percentchange(x,b):
    p = (x - b) / b * 100
    return p

#stockfile = open("/workspace/IFSC1202/Assignments/Unit 6 HW/Text Files/06.02 Stock.txt", "r")
stockfile = open("/workspace/IFSC1202/06.02 Stock.txt", "r")
x = float(stockfile.readline())
b = x
print("{0:^10}{1:^10}".format("Price","Change"))
print("{:^10}".format(x))
x = float(stockfile.readline())

while x != "":
    print("{:^10.2f}{:10.2f}%".format(x,percentchange(x,b)))
    b = x
    x = stockfile.readline()
    if x != "":
        x = float(x)    
x = stockfile.close()
