l1=[2, 4, 2, 8, 4, 2, 8]

fre={}
for n in l1:
    if n in fre:
        fre[n]=fre[n]+1
    else:
        fre[n]=1

print("Frequency of elements is:",fre)            