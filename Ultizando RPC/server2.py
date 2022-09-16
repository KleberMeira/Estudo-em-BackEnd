from xmlrpc.server import SimpleXMLRPCServer

def server2(n):
    print("Requisição recebida com o seguinte argumento: " + str(n))
    print("n" + n)
    return n.upper()

server = SimpleXMLRPCServer(("localhost", 8080))
print("Listening on port 8080...")
server.register_function(server2, "server2")
server.serve_forever()