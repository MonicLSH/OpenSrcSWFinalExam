
print("i\t\t\tm(i)")
for r in range(1,902,100):
    num = 4
    sign = 1
    for i in range(2,r+1,1):
        sign= -sign
        num = num + ( sign * 4 * ( 1 / (2*i-1) ) )
    print(r,"\t\t\t",num)

