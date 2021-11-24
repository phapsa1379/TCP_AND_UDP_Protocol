
#Pasha Ahmadi 9816683

import json
import matplotlib.pyplot as plt

#*******************************client*****************************
#   
f1 = open('client.json',)
  

data1 = json.load(f1)

throughput_client=[] 
time_client=[]

for i in data1['intervals']:
    for j in i['streams']:
        throughput_client.append(float(j['bits_per_second']))

for ii in data1['intervals']:
    for jj in ii['streams']:
        time_client.append(float(jj['end']))

plt.title("Avg Throughput Of Client")
plt.xlabel('time')
plt.ylabel('Throughput')
plt.plot(time_client, throughput_client, marker = 'o', c = 'g')
  
plt.show()  
f1.close()


#*******************************************server******************************************
f2 = open('server.json',)
  

data2 = json.load(f2)

throughput_server=[] 
time_server=[]

for i in data2['intervals']:
    for j in i['streams']:
        throughput_server.append(float(j['bits_per_second']))

for ii in data2['intervals']:
    for jj in ii['streams']:
        time_server.append(float(jj['end']))

plt.title("Avg Throughput Of Server")
plt.xlabel('time')
plt.ylabel('Throughput')
plt.plot(time_server, throughput_server, marker = 'o', c = 'g')
  
plt.show()  
f2.close()