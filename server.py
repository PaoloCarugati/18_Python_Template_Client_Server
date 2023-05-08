import cherrypy
import json
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


def __init__(self, url="mongodb://localhost:27017", db="MyDB", collection="MyCollection"):
        #definisco delle variabili di istanza
        self.client = MongoClient(url)
        self.db = self.client[db]
        self.collection = self.db[collection]
        self.projection = {"_id": 0}
        #cancello tutto
        self.collection.delete_many({})
        #inserimento
        self.collection.insert_many(MyController.records)

        
    @cherrypy.tools.json_out() #NOTA: ricordarsi di aggiungere questo decoratore se vogliamo l'output in formato json!!!
    def GET(self, id=-1):
        #scrivi qui le istruzioni per restituire i document (oppure IL document se id <> -1) della collection
        return []
        #ricordati di gestire il 404!


    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
        data = cherrypy.request.json
        #scrivi qui le istruzioni per inserire un nuovo document
        return 0 #in realtà devo ritornare l'id dell'elemento inserito


    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def PUT(self):
        data = cherrypy.request.json
        #scrivi qui le istruzioni per modificare un document esistente            
        return 0
        #ricordati di gestire il 404!

    @cherrypy.tools.json_out()
    def DELETE(self, id=-1):
        #scrivi qui le istruzioni per eliminare un document
        return 0
        #ricordati di gestire il 404!

        
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

#eventualmente utilizzare questa per cambiare la porta
#cherrypy.config.update({'server.socket_port': 80})

#cherrypy.quickstart(MyController(), '/qualcosa', conf)
cherrypy.quickstart(MyController(), '/', conf)
