HOST = '192.168.1.44' #'192.168.1.44'
PORT = 50000

import socket, sys, threading
import xmlManager as xmlM
from pair_utils import *
import os

xmlM.init()

class ThreadClient(threading.Thread):
    '''dérivation d'un objet thread pour gérer la connexion avec un client'''
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn

    def callBack(self, commande):
        cmd = commande.split()
        if cmd[0] == "getPhoneNum":
            num = xmlM.getNumberFromAlias(cmd[1])
            self.connexion.send(num.encode("utf-8"))
        elif cmd[0] == "getInvitationKey":
            print("getInvitationKey")
        elif cmd[0] == "signIn":
            if len(cmd) != 4:
                print("Bad Input: ...")
                return
            #verif cmd[3]la clé d'invition
            client_pair(cmd[1])
            cert_str = open(cmd[1]+"_crt.pem", 'rt').read()
            key_str = open(cmd[1]+"_key.pem", 'rt').read()

            xmlM.addUser(cmd[1], cmd[2], cert_str)

            keycert = cert_str + " " + key_str
            self.connexion.send(keycert.encode("utf-8"))
            os.remove(cmd[1]+"_crt.pem")
            os.remove(cmd[1]+"_key.pem")

        else:
            print("Invalid callBack")

    def run(self):
        # Dialogue avec le client :
        nom = self.getName()        # Chaque thread possède un nom
        while 1:
            msgClient = self.connexion.recv(1024)
            msgClient = msgClient.decode("utf-8")
            if msgClient.upper() == "FIN" or msgClient =="":
                msgtmp = str.encode("FIN")
                self.connexion.send(msgtmp)
                break
            self.callBack(msgClient)
            self.connexion.send(str.encode("RECU"))
            message = "%s> %s" % (nom, msgClient)
            print(message)
            # Faire suivre le message à tous les autres clients :
            #for cle in conn_client:
            #    if cle != nom:      # ne pas le renvoyer à l'émetteur
            #        conn_client[cle].send(str.encode(message))

        # Fermeture de la connexion :
        self.connexion.close()      # couper la connexion côté serveur
        del conn_client[nom]        # supprimer son entrée dans le dictionnaire
        print("Client déconnecté:", nom)
        # Le thread se termine ici


# Initialisation du serveur - Mise en place du socket :
try:
    open("ca_crt.pem", "r")
    open("ca_key.pem", "r")
except:
    CA_pair()

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mySocket.bind((HOST, PORT))
except socket.error:
    print("La liaison du socket à l'adresse choisie a échoué.")
    sys.exit()
print("Serveur prêt, en attente de requêtes ...")
mySocket.listen(500)

# Attente et prise en charge des connexions demandées par les clients :
conn_client = {}                # dictionnaire des connexions clients
while 1:
    connexion, adresse = mySocket.accept()
    # Créer un nouvel objet thread pour gérer la connexion :
    th = ThreadClient(connexion)
    th.start()
    # Mémoriser la connexion dans le dictionnaire :
    it = th.getName()        # identifiant du thread
    conn_client[it] = connexion
    print ("Client %s connecté, adresse IP %s, port %s." %(it, adresse[0], adresse[1]))
    # Dialogue avec le client :
    connexion.send(str.encode("Vous êtes connecté. Envoyez vos messages."))
