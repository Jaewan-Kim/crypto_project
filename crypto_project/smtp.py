from socket import *
import base64
import ssl
import sys

email = sys.argv[1]
message = sys.argv[2]
msg = "\r\n " + message
endmsg = "\r\n.\r\n"

mailServer = ("smtp.gmail.com", 587)
# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect(mailServer)

recv = clientSocket.recv(1024)
#print recv
if recv[:3] != '220':
    print'220 reply not received from server.'

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print recv1
    
clientSocket.send('starttls\r\n')
recv1 = clientSocket.recv(1024)
print recv1
clientSocket = ssl.wrap_socket(clientSocket, ssl_version=ssl.PROTOCOL_SSLv23)

uname = "kim.palacios.contact@gmail.com"
passw = "crypto18"
cred = base64.b64encode("\x00"+uname+"\x00"+passw)
clientSocket.send("AUTH PLAIN "+cred+"\r\n")
recv = clientSocket.recv(1024)
print(recv)

# Send MAIL FROM command and print server response.
clientSocket.send("MAIL FROM:<kim.palacios.contact@gmail.com>\r\n")
print clientSocket.recv(1024)

# Send RCPT TO command and print server response.
mailTo = "RCPT TO:<" + email + ">\r\n"
clientSocket.send(mailTo)
print clientSocket.recv(1024)

# Send DATA command and print server response.
clientSocket.send("DATA\r\n")
print clientSocket.recv(1024)

# Send message data.
clientSocket.send(msg)
clientSocket.send(endmsg)

# Send QUIT command and get server response.
clientSocket.send("QUIT\r\n")
print clientSocket.recv(1024)
clientSocket.close()
