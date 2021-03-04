# Définition d'un client réseau rudimentaire
# Ce client dialogue avec un serveur ad hoc

import socket, sys


def receive():
    msg = mySocket.recv(1024).decode("utf-8").split("_|_")
    if msg == "":
        return
    while msg[-1] != "END_COMMUNICATION":
        msg += mySocket.recv(1024).decode("utf-8").split("_|_")
    return msg

def send(msg):
    msg += "_|_END_COMMUNICATION"
    mySocket.send(msg.encode("utf-8"))


HOST = 'localhost' #'192.168.1.44'
PORT = 50000


mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



try:
    mySocket.connect((HOST, PORT))
except socket.error:
    print("La connexion a échoué.")
    sys.exit()
print("Connexion établie avec le serveur.")


msgServeur = receive()
while 1:
    if msgServeur[0].upper() == "FIN":
        break
    print(msgServeur)
    msgClient = input("Ecrire :")

    send(msgClient)

    msgServeur = receive()



# 4) Fermeture de la connexion :
print("Connexion interrompue.")
mySocket.close()


#msg.decode("utf-8")
