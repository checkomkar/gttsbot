infile=open("myspeech.text","r")
data=infile.read()
wd1=data.split()
wd=len(data.split())
print(wd1)
print(wd)
fwd=wd1[0]
last=wd1[-1]
if(fwd=="Thakur" or last=="Thakur"):
    print("match found")
else:
    print("not found")
line_number=sum(1 for line in open("myspeech.text"))
print("Number of lines:",line_number)
