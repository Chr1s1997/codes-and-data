import time
number = 5000
time1=time.time()
b = 10**number
x1 = b*4//5
x2 = b// -239
he = x1+x2
number *= 2
for i in range(3,number,2):
    x1 //= -25
    x2 //= -57121
    x = (x1+x2) // i
    he += x
pai = he*4
paistring=str(pai)
result=paistring[0]+str('.')+paistring[1:len(paistring)]
print("result£º\n\n%s"%result)
time2=time.time()
print('\ntime:' + str(time2 - time1) + 's')

