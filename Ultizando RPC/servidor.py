from xmlrpc.server import SimpleXMLRPCServer
import sys
import xmlrpc.client

def is_even(n):
    print("Requisição recebida com o seguinte argumento: " + str(n))
    print("n" + n)
    with xmlrpc.client.ServerProxy("http://localhost:8080/") as proxy:
        resultado = proxy.server2(n)
    return resultado



server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(is_even, "is_even")
server.serve_forever()

#####SERVIDOR

####import socket
####HOST = ''              # Endereco IP do Servidor
####PORT = 9008            # Porta que o Servidor esta
####tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
####orig = (HOST, PORT)
####tcp.bind(orig)
####tcp.listen(1)
####def soma(a, b): return a + b
    
####while True:
####    con, cliente = tcp.accept()
####    print 'Concetado por', cliente
####    while True:        
        ####a = int(con.recv(1))
        ####b = int(con.recv(1))
        ####result = soma(a, b)
        ####print result
        ####con.send(str(result))
####print 'Finalizando conexao do cliente', cliente
####con.close()