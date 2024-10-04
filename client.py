import json
import requests



base_url = "http://127.0.0.1:8080"


def effettuaPrimoLogin():
    
    global username , password , privilegio , primoLoginEffetuato
    username = input("inserisci username")
    password = input("inserisci la password")
    jRequest = {"username " : username , "password" : password}
    try:
        api_url = base_url + "/login"
        response = requests.post(api_url,json=jRequest)
        if response.status_code == 200 :
            jResponse = response.json
            if jResponse["ERROR"] == "000":
                privilegio : str = jResponse["Privilegio"]
                primoLoginEffetuato = 1 
                
    except:
        print("Attenzione problemi con il server")

username: str = ""
password : str = ""
primoLoginEffetuato = 0
privilegio : str = ""
while primoLoginEffetuato == 0 :
    primoLoginEffetuato = effettuaPrimoLogin()


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

    richiestaModifica = input("Seleziona cosa vuoi modificare : Nome , Cognome , Data di Nascita (Scrivere solo Data) :  ")
    split = richiestaModifica.split()
    for parola in split:
        if parola == "Nome" :
            richiestaNome = input("inserire il nome modificato : ")
            return {"campo": "nome", "valore": richiestaNome}
        if parola == "Cognome" :
            richiestaCognome = input("inserire il Cognonome modificato : ")
            return {"campo": "cognome", "valore": richiestaCognome}
        if parola == "Data":
            richiestaData = input("inserire la data modicata : ")
            return {"campo": "data di nascita", "valore": richiestaData}
    


def eliminaCittadino():
    richiestaModifica = input("Seleziona cosa vuoi eliminare : Nome , Cognome , Data di Nascita (Scrivere solo Data) :  ")
    split = richiestaModifica.split()
    for parola in split:
        if parola == "Nome" :
            richiestaNome = input("inserire il nome da eliminare : ")
            return {"campo": "nome", "valore": richiestaNome}
        if parola == "Cognome" :
            richiestaCognome = input("inserire il Cognonome da eliminare : ")
            return {"campo": "cognome", "valore": richiestaCognome}
        if parola == "Data":
            richiestaData = input("inserire la data da eliminare: ")
            return {"campo": "data di nascita", "valore": richiestaData}


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
        api_url = base_url + "/modifica_cittadino"
        jsonDataRequest = richiediCodiceFiscale()
        try :
            response = requests.post(api_url,json=jsonDataRequest)
            if response.status_code == 200 :
                data1 = response.json()
                print(response.status_code)
                print(response.headers["Content-Type"])
                if data1["ERROR"] == "000":
                    print("Il codice fiscale esiste")
                    richiestaModifica = modificaCittadino()
                    if richiestaModifica :
                        jsonDataRequest.update(richiestaModifica)
                        response = requests.post(api_url,json=jsonDataRequest)
                        print(response.status_code)
                        print(response.headers["Content-Type"])
                        data1 = response.json()
                        print(data1)
                    else :
                        print("inserire prima i campi") 
                else :
                    print("Il codice fiscale non esiste")

            else:
                print("il server non ha risposto")
                            
        except:
            print("problemi di comunicazione con il server , riprovare più tardi")




    if sOper == "4":
        api_url = base_url + "/rimuovi_cittadino"
        jsonDataRequest = richiediCodiceFiscale()
        try :
            response = requests.post(api_url,json=jsonDataRequest)
            if response.status_code == 200 :
                data1 = response.json()
                print(response.status_code)
                print(response.headers["Content-Type"])
                if data1["ERROR"] == "000":
                    print("Il codice fiscale esiste")
                    richiestaEliminazione = eliminaCittadino()
                    if richiestaEliminazione :
                        jsonDataRequest.update(richiestaEliminazione)
                        response = requests.post(api_url,json=jsonDataRequest)
                        print(response.status_code)
                        print(response.headers["Content-Type"])
                        data1 = response.json()
                        print(data1)
                    else :
                        print("inserire prima i campi") 
                else :
                    print("Il codice fiscale non esiste")

            else:
                print("il server non ha risposto")
                            
        except:
            print("problemi di comunicazione con il server , riprovare più tardi") 







