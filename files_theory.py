#Files

"""
Read --> 'r'
Write --> 'w'
Append --> 'a'
seek
tell

f.read(n) --> reads first n characters
f.readline() --> reads a singl line from the file
f.readlines() --> generates a list containing individual lines of the file

f.write()
f.close()

"""
f=open("text.txt","r")
text=f.read()

#f.readline()
#f.readlines()
#f.seek()
#f.tell()

f.write("text here")

# with open("text.txt",'r') as f:

