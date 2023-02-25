myfile=open("newText.txt",'w')

myfile.write('hello there')
myfile.close()

myfile=open('newText.txt','a')
myfile.write(" some other text.")
myfile.close()

myfile=open('newText.txt','r+')
text=myfile.read(100)
print(text)