#Pasha Ahmadi 9816683

import pyshark
import time

print("====== *[{ Start Capturing ...}]* ======")
capture = pyshark.LiveCapture(interface='lo' ,bpf_filter='port 4040' )
begin=time.time()

capture.sniff(timeout=10)
packet_amount=len(capture)
sum=0
counter=0
print("====== *[{ End Capturing ...}]* ======")
for item in range(0,len(capture)):
    print(capture[item])
    sum+=len(capture[item])
    str_packet=str(capture[item])
    if str_packet.find('retransmission') !=-1:
        counter+=1

end=time.time()



print("*******************************************************************************\n")
print("                  number of receiving packets: ",packet_amount)
print("\n*********************************************************************************")
print("\n                average throughtput of sender :",(sum/(end-begin))/(10**6),"Mbit/s")
print("\n*********************************************************************************")
print("                  number of retransmission TCP packet : ",counter)
print("\n*********************************************************************************")
