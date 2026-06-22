# একটা list এ 10টা number আছে

numberlist = [5, -3, 0, 8, -1, 0, 4, -7, 2, 9]
#print(numberlist)
for number in numberlist:
    print(number)

# Positive, negative, zero আলাদা করে count করো
    if(number == 0):
        print(' Zero')
    elif (number <0 ):
        print("Negetive")
    else: print("Possitive")

# সবচেয়ে বড় আর ছোট number বের করো (max/min built-in ছাড়া)
largets = numberlist[0]
smallest = numberlist[0]


for number in numberlist:
    if number>largets:
        largets = number
    if number<smallest:
        smallest= number
print(f"largets: {largets}")
print(f"smallest: {smallest}")
