import socket
import pickle


MAX_ROUTES = 10


routing_table = []

class RouteEntry:
    def __init__(self, destination, subnet_mask, gateway, interface, metric):
        self.destination = destination
        self.subnet_mask = subnet_mask
        self.gateway = gateway
        self.interface = interface
        self.metric = metric

def add_route(destination, subnet_mask, gateway, interface, metric):
    global routing_table
    if len(routing_table) < MAX_ROUTES:
        route = RouteEntry(destination, subnet_mask, gateway, interface, metric)
        routing_table.append(route)
        return True
    else:
        return False

def print_routing_table():
    print("Routing Table:")
    print("{:<15} {:<15} {:<15} {:<15} {:<15}".format("Destination", "Subnet Mask", "Gateway", "Interface", "Metric"))
    for route in routing_table:
        print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(route.destination, route.subnet_mask, route.gateway, route.interface, route.metric))

def server():
  
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind(('192.168.0.139', 8888))

   
    server_socket.listen(1)
    print("Server is listening on port 8888...")

    while True:
       
        client_socket, client_address = server_socket.accept()
        print("Connected to client:", client_address)

        data = client_socket.recv(1024)
        if not data:
            break

        route_info = pickle.loads(data)

     
        success = add_route(*route_info)

       
        if success:
            client_socket.send("Route added successfully.".encode())
        else:
            client_socket.send("Routing table full. Cannot add more routes.".encode())

        print_routing_table()

        
        client_socket.close()


    server_socket.close()

if __name__ == "__main__":
    
    server()
