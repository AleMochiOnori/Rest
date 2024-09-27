import json,requests


base_url = "http://127.0.0.1:8080"

def creaInterfaccia():
    print("Operazioni disponibili : ")
    print("1. Inserisci cittadino : ")
    print("2. Richiedi dati cittadino : ")
    print("3. Modifica dati cittadino : ")
    print("4. Elimina cittadino : ")
    print("5. Exit")


def richiediDatiCittadino():
    nome = input("inserisci nome cittadino : ")
    cognome = input("inserisci cognome cittadino : ")
    dataDiNascita = input("Inserisci data di nascita : ")
    codiceFiscale = input("inserisci codice fiscale : ")
    jRequest = {"nome : " : nome , "cognome : " : cognome , "Data Nascita : " : dataDiNascita , "Codice Fiscale : " : codiceFiscale}
    return jRequest



def richiediCodiceFiscale():
    codiceFiscale = input('Inserire il Codiece Fiscale : ')
    jRequest = {"Codice Fiscale" :  codiceFiscale}
    return jRequest



def modificaCittadino():
    richiesta = input("Seleziona cosa vuoi modificare : Nome , Cognome , Data di Nascita")
    
    




sOper = input("Seleziona operazione da 1 a 5 : ")
while (sOper != "5"):
    if sOper == "1":
        api_url = base_url + "/add_cittadino"
        jsonDataRequest = richiediDatiCittadino()
        try:
            response = requests.post(api_url,json=jsonDataRequest)
            print(response.status_code)
            print(response.headers["Content-Type"])
            data1 = response.json()
            print(data1)
        except:
            print("problemi di comunicazione con il server , riprovare più tardi")



    if sOper == "2":
        api_url = base_url + "/richiedi_dati_cittadino"
        jsonDataRequest = richiediCodiceFiscale()
        try :
            response = requests.post(api_url,json=jsonDataRequest)
            print(response.status_code)
            print(response.headers["Content-Type"])
            data1 = response.json()
            print(data1)
        except:
            print("problemi di comunicazione con il server , riprovare più tardi")

    creaInterfaccia()

    sOper = input("Seleziona operazione da 1 a 5 : ")



    if sOper == "3":
        api_url = base_url + "/richiedi_dati_cittadino"
        jsonDataRequest = richiediCodiceFiscale()
        try:


