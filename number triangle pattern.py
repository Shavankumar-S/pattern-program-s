rows=6
for i in range(rows):
    num=1
    for j in range(rows,0,-1):
        if j>1:
            print("",end='')
        else:
            print(num,end='')
    print("")
