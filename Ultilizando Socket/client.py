############CLI
import socket
HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 9008         # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print 'Para sair use CTRL+X\n'
msg = raw_input()
tcp.send (msg)
result = tcp.recv(2)
print result
tcp.close()