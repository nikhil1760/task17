import threading 
import socket as s
import os
k=s.socket(s.AF_INET, s.SOCK_DGRAM)
own_ip=input("Enter the your ip ")
own_port=1234
other_ip=input("Enter the other ip ")
other_port=5678
k.bind((own_ip,own_port))
os.system("clear")
print("-------------------- Chat Program -----------------") 
def send():
	while True:
		mes=input("")
		mes=mes.encode()
		k.sendto(mes,(other_ip,other_port))
def recv():
	while True:
		x=k.recvfrom(10240)
		print("      Received message    "+x[1][0]+" " +x[0].decode())
t1=threading.Thread(target=send)
t2=threading.Thread(target=recv)
t1.start()
t2.start()

		
		
		
