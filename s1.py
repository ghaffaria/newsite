i=0
j=1
o=0
n=1
while o==0:
    print(i,len(str(i)),'\n')
    print(j,len(str(j)),'\n')



    i=i+j
    n += 1
    if len(str(i))==1000:
        o=1
        break
    j=i+j
    n += 1
    if len(str(j))==1000:
        o=1
        break


print('i=',i,len(str(i)))
print('j=',j,len(str(j)))
print(n)



