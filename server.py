from flask import Flask , request
import json
from myJason import  JsonSerialize , JsonDeserialize
import jsonify


fileAnagrafe = "./anagrafe.json"
file_utenti = "./utenti.json"
api = Flask(__name__)





@api.route("/add_cittadino" , methods=["POST"])
def gestisciCittadino():
    utenti : dict = JsonDeserialize(file_utenti)
    if 
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        jRequest = request.json
        print(jRequest)
        sCodiceFiscale = jRequest["codice fiscale"] 
        dAnagrafe : dict = JsonDeserialize(fileAnagrafe)
        if sCodiceFiscale not in dAnagrafe :
            dAnagrafe[sCodiceFiscale] = jRequest
            JsonSerialize(dAnagrafe , fileAnagrafe)
            jResponse = {"ERROR" : "000" , "Msg" : "ok"}
            return json.dumps(jResponse) , 200
        else :
            jResponse = {"ERROR" : "001" , "Msg" : "codice fiscale già presente in anagrafe"}
            return json.dumps(jResponse) , 200
    else :
        return "Errore formato non riconosciuti", 401
    




@api.route("/richiedi_dati_cittadino", methods=["POST"])
def richiediDatiCittadino():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json' :
       jRequest = request.json
       print(jRequest)
       sCodiceFiscale = jRequest["Codice Fiscale"]
       dAnagrafe : dict = JsonDeserialize(fileAnagrafe)
       if sCodiceFiscale in dAnagrafe :
           dAnagrafe[sCodiceFiscale] = jRequest
           JsonSerialize(dAnagrafe , fileAnagrafe)
           jResponse = {"ERROR" : "000" , "Msg" : dAnagrafe[sCodiceFiscale]}
           return json.dumps(jResponse) , 200
       else :
            jResponse = {"ERROR" : "001" , "Msg" : "codice fiscale non presente in anagrafe"}
            return json.dumps(jResponse) , 200
    else :
        return "il file non è un file di tipo Json"
    



@api.route("/modifica_cittadino", methods=["PUT"])
def modificaCittadino():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json' :
       jRequest = request.json
       print(jRequest)
       sCodiceFiscale = jRequest["Codice Fiscale"]
       dAnagrafe : dict = JsonDeserialize(fileAnagrafe)
       if sCodiceFiscale in dAnagrafe:
            campoDaModificare = jRequest.get("campo")
            nuovoValore = jRequest.get("valore")
            dAnagrafe[sCodiceFiscale][campoDaModificare] = nuovoValore
            JsonSerialize(dAnagrafe, fileAnagrafe)
            jResponse = {"ERROR": "000", "Msg": "Modifica effettuata correttamente"}
            return json.dumps(jResponse), 200       
       else:
            jResponse = {"ERROR": "001", "Msg": "Codice fiscale non presente in anagrafe"}
            return json.dumps(jResponse), 200
    else:
        return "Errore: formato non riconosciuto", 401 
           
           
@api.route("/rimuovi_cittadino", methods=["DELETE"])
def rimuoviCittadino():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json' :
       jRequest = request.json
       print(jRequest)
       sCodiceFiscale = jRequest["Codice Fiscale"]
       dAnagrafe : dict = JsonDeserialize(fileAnagrafe)
       if sCodiceFiscale in dAnagrafe:
            campoDaEliminare = jRequest.get("campo")
            dAnagrafe[sCodiceFiscale].pop(campoDaEliminare)
            JsonSerialize(dAnagrafe, fileAnagrafe)
            jResponse = {"ERROR": "000", "Msg": "Modifica effettuata correttamente"}
            return json.dumps(jResponse), 200
       else:
            jResponse = {"ERROR": "001", "Msg": "Codice fiscale non presente in anagrafe"}
            return json.dumps(jResponse), 200
    else:
        return "Errore: formato non riconosciuto", 401 
           
file_path_users = "utenti.json"
utenti = JsonDeserialize(file_path_users)



@api.route("/login" , methods = ["POST"])
def primoLogin():

    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json' :
       jRequest : dict = request.json
       # Jrequest =  {username : mario  , "password" : "cikolino123"}
       print(jRequest)
       usernameInseritoDaClient = jRequest["username"]
       if usernameInseritoDaClient in utenti :
           passwordInseritaDalClient = jRequest["password"]
           if passwordInseritaDalClient == utenti[usernameInseritoDaClient]["password"]:
               privilegio = utenti[usernameInseritoDaClient]["privilegi"]
               return jsonify({"Esito" : "000" ,"MSG" : "Utente registrato" , "Privilegio" : privilegio})
           else : 
               return jsonify({"Esito" : "000" ,"MSG" : "Credenziali errate"})
           
       else : 
           return jsonify({"Esito" : "000" ,"MSG" : "Credenziali errate"})
    else :
        return jsonify({"Esito" : "000" ,"MSG" : "Formato dati errato"})

if __name__ == '__main__':
    api.run(host="127.0.0.1", port=8080)

