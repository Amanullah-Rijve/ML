'''
File Handeling
r- raead
w-write
a - append
r+ -- read + write
'''
# write
with open("data.txt","w") as f:
    f.write("hello , world! \n")
    f.write("I am learning ML")
#read
with open("data.txt","r") as f:
    content = f.read()
    print(content)

