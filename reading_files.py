#open("srujan.text","r") #read
#open("srujan.txt","w") #write


file=open("srujan.txt","r")
print(file.readline())
file=open("srujan.txt","w")
file.write("srujan is a good boy")
print(file.read())
file.close()

