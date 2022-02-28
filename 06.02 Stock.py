
def percentchange(x,b):
    x = float(x)
    p = (x - b) / b * 100
    return p

#stockfile = open("/workspace/IFSC1202/Assignments/Unit 6 HW/Text Files/06.02 Stock.txt", "r")
stockfile = open("/workspace/IFSC1202/06.02 Stock.txt", "r")
x = float(stockfile.readline())

print("{0:^10}{1:^10}".format("Price","Change"))
print("{:^10}".format(x))
while x != "":
    b = x
    x = float(stockfile.readline())
    print("{:^10.2f}{:10.2f}%".format(x,percentchange(x,b)))
x = stockfile.close()
