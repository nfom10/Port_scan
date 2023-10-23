# Nombre - Escaneando Puertos.py
# Python Version -  3.5

import socket

p_abiertos = 0
# Diccionario de Puertos
puertos = dict()
puertos = {
        20: "FTP Data", 21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS", 59: "DCC",
        79: "Finger", 80: "HTTP", 110: "POP3", 113: "IDENT", 119: "NNTP", 135: "NetBIOS",
        139: "NetBIOS", 143: "IMAP", 389: "LDAP", 443: "HTTPS", 445: "MSFT DS", 563: "POP3 SSL",
        993: "IMAP4 SSL", 995: "POP3 SSL", 1080: "Proxy", 1723: "PPTP", 3306: "MySQL", 5000: "UPnP",
        8080: "Proxy Web"
    }

print("#"*49)
print("#"+(" "*9)+"Escaner de Puertos con Python"+(" "*9)+"#")
print("#"*49)

# Entrada Direccion IP
host = input("# IP > ")
print("# ")
if len(host.split('.')) == 4 or len(host.split('.')) == 3:
    # Creacion del socket
    socket = socket.socket()

    # Comprobar todos los puertos
    for puerto,nombre in puertos.items():
        
        try:
            socket.connect((host,puerto))
            print("# Puerto %s - %s Abierto" %(puerto,nombre) )
            p_abiertos += 1
            socket.close()
        except :
            socket.close()

    print("# ")
    if p_abiertos != 0:
        print("# Direccion IP o Host : "+host+" tiene "+str(p_abiertos)+" puertos abiertos")
    else:
        print("# Direccion IP o Host : "+host+" No Tiene Puertos Abiertos")
else:
    print("# Direccion IP o Host NO Valido")

print("#"*49)
