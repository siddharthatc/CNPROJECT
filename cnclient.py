import socket
import pickle

def client():

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    client_socket.connect(('192.168.0.139', 8888))

   
    destination = input("Enter destination: ")
    subnet_mask = input("Enter subnet mask: ")
    gateway = input("Enter gateway: ")
    interface = input("Enter interface: ")
    metric = input("Enter metric: ")

   
    metric = int(metric)

   
    route_info = (destination, subnet_mask, gateway, interface, metric)

  
    data = pickle.dumps(route_info)

 
    client_socket.send(data)

    
    response = client_socket.recv(1024)
    print("Server response:", response.decode())

   
    client_socket.close()

if __name__ == "__main__":
   
    client()
