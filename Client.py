# Définition d'un client réseau rudimentaire
# Ce client dialogue avec un serveur ad hoc

import socket, sys

HOST = 'localhost' #'192.168.1.44'
PORT = 50000

# 1) création du socket :
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2) envoi d'une requête de connexion au serveur :
try:
    mySocket.connect((HOST, PORT))
except socket.error:
    print("La connexion a échoué.")
    sys.exit()
print("Connexion établie avec le serveur.")


msgServeur = mySocket.recv(1024).decode("utf-8")

while 1:
    if msgServeur.upper() == "FIN" or msgServeur =="":
        break
    print(msgServeur)
    msgClient = str.encode("bonjour")
    msgClient = input("Ecrire :")

    mySocket.send(str.encode(msgClient))

    msgServeur = mySocket.recv(1024)
    msgServeur = msgServeur.decode("utf-8")

# 4) Fermeture de la connexion :
print("Connexion interrompue.")
mySocket.close()


#msg.decode("utf-8")
