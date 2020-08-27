import time
f = open("IOfile.txt", "w")
n=50000000
time1=time.time()
for num in range (1,n):
      f.write("Now the file has more content!\n")
f.close()
time2=time.time()
print("Input " +str(n)+ " sentences.")
print("time:" + str(time2-time1) +'s\n')

time3=time.time()
count=1
for count, line in enumerate(open(r"IOfile.txt",'rU')):
        pass
count+=1
print("Counted "+ str(count) +" lines.")
time4=time.time()
print("read time is:" + str(time4-time3) +'s')
