import requests,time
url='https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=AIzaSyAMgRgY5IpN5c6mdUiGNikEplBAcos_y8E'
i=0
time1=time.time()
for num in range (5000):
    response=requests.get(url)
    if (response.status_code)==200:
        i=i+1
        #print(response.status_code)
        if (i%50==0):
            print('This is No. '+str(i)+ ' calls.')
time2=time.time()
print('\ntime:'+str(time2-time1)+'s')
print('Total '+str(i)+' calls')

