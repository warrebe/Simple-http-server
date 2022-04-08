# Author: Benjamin Warren
# Date: 01/11/2022
# Description: Creating a simple HTTP server

    # Citation for the following program:
      # Date: 01/11/2022
      # Based on: Real Python examples
      # Source URL: https://realpython.com/python-sockets/

import socket  # for socket

try:
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("\nSocket successfully created")
except socket.error as err:
    print("\nsocket creation failed with error %s" % (err))

port = 2000 #Socket Port custom
Host_name = 'localhost' #Host name for connection

try:
    host_ip = socket.gethostbyname(Host_name) #Convert host name to IP
except socket.gaierror:
    # Host name resolution error
    print("There was an error resolving the host")
    exit(1)
data =  b"HTTP/1.1 200 OK\r\n"\
                b"Content-Type: text/html; charset=UTF-8\r\n\r\n"\
                b"<html>Congratulations!  You've downloaded the first Wireshark lab file!</html>\r\n"
soc.bind((host_ip, port)) #Specifies network and port number
soc.listen(1)#Lets the server accept 1 connection
connect, address = soc.accept() #.accept returns tuple of host and port of connection
with connect:
    print('Connected by', address)
    receive = connect.recv(1024) # Initial receive
    print("Recevied:", receive.decode())
    print("Sending>>>>>\n", data.decode(),"\n<<<<<")
    connect.sendall(data) # Send data to client
    while True:
        incoming = connect.recv(1024) #Keeps connection with client while open
        if not incoming: #Ends server after client disconnects
            soc.close()
            break


