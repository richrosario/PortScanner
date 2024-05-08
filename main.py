import socket

#Our goal here is to find open ports on a target; NMAP is way easier but this is good for practice!
##We could introdue a more efficient multi-thread version here as well

targetIP = "IP.IP.IP.IP"

def portscan():
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect((targetIP,port))
		return True
	except:
		return False

for port in range(1,1023) #well-known ports
	result = portscan(port)
    if(result): #if the function above is true
        print("Port {} is open!".format(port))
    else:
        print("Port {} is closed!".format(port))