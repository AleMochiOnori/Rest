from flask import Flask ,json ,request
from myJason import  JsonSerialize , JsonDeserialize


fileAnagrafe = "./anagrafe.json"
api = Flask(__name__)


@api.route("/add_cittadino" , methods=["POST"])
def gestisciCittadino():
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
    



@api.route("/modifica_cittadino", methods=["POST"])
def modificaCittadino():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json' :
       jRequest = request.json
       print(jRequest)
       sCodiceFiscale = jRequest["Codice Fiscale"]
       dAnagrafe : dict = JsonDeserialize(fileAnagrafe)

    






           

           








if __name__ == '__main__':
    api.run(host="127.0.0.1", port=8080)

