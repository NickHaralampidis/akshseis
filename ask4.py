num=[1000000,900000,500000,400000,100000,90000,50000,40000,10000,9000,5000,4000,1000,900,500,400,100,90,50,40,10,9,5,4,1]
rom=["-M","-C-M","-D","-C-D","-C","-X-C","-L","-X-L","-X","M-X","-V","M-V","M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
c=[]
a=input()
for i in range (0,25):
    if (a//num[i]):
        k=(a//num[i])*rom[i]
        c.append(k)
        a=a-(a//num[i])*num[i]
ap=''.join(c)
print ap