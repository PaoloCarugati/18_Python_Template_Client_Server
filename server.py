import cherrypy
import json
from record import record
from pymongo import MongoClient

@cherrypy.expose
class MyController(object):
    records = [] #array che contiene i dati

    USR = "NOME_UTENTE"
    PWD = "PASSWORD"
    RLM = "NOME_APPLICAZIONE"

    def validate_password(self, username, password):
        if (username == MyController.USR and password == MyController.PWD):
            return True
        else:
            return False


    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["NOME_DB"]
        self.collection = self.db["NOME_COLLECTIOM"]
        #cancello tutto
        self.collection.delete_many({})
        #inserimento
        self.collection.insert_many(MyController.records)

    @cherrypy.tools.json_out() #NOTA: ricordarsi di aggiungere questo decoratore se vogliamo l'output in formato json!!!
    def GET(self, id=-1):
        #scrivi qui le istruzioni per restituire i document (oppure IL document se id <> -1) della collection


    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
        data = cherrypy.request.json
        #scrivi qui le istruzioni per inserire un nuovo document
        return 0


    @cherrypy.tools.json_out()
    #@cherrypy.tools.accept(media='text/plain')
    def PUT(self, id=-1):
        data = cherrypy.request.json
        disco = json.loads(data, object_hook=record)
        #scrivi qui le istruzioni per modificare un document esistente            

    @cherrypy.tools.json_out()
    def DELETE(self, id=-1):
        #scrivi qui le istruzioni per eliminare un document


#if __name__ == '__main__':
conf = {
    '/': {
        'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
        'tools.sessions.on': True,
        'tools.response_headers.on': True,
        'tools.response_headers.headers': [('Content-Type', 'application/json'), ('Access-Control-Allow-Origin', '*')],
        'tools.auth_basic.on': True,
        'tools.auth_basic.realm': MyController.RLM,
        'tools.auth_basic.checkpassword': MyController.validate_password
    }
}  

#cherrypy.quickstart(MyController(), '/dischi', conf)
cherrypy.quickstart(MyController(), '/', conf)