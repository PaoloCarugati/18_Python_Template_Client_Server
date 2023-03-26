import cherrypy
#import cherrypy_cors
import json
from WrapperDB import WrapperDB
from record import record

@cherrypy.expose
class MyController(object):
    wrp = WrapperDB()

    @cherrypy.tools.json_out() #NOTA: ricordarsi di aggiungere questo decoratore se vogliamo l'output in formato json!!!
    def GET(self, id=-1):
        dischi = self.wrp.elencoDischi(as_dict=True)

        if (int(id) == -1):
            return dischi
        else:
            #return self.dischi[int(id)]
            disco = [d for d in dischi if d["id"] == int(id)]
            if (len(disco) == 1):
                return (disco[0])
            else:
                cherrypy.response.status = 404
                return {} 


    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
        #self.dischi.append(data)
        #return {}
        data = cherrypy.request.json
        disco = json.loads(data, object_hook=record)
        res = self.wrp.inserisciDiscoSP(disco)
        return res


    @cherrypy.tools.json_out()
    #@cherrypy.tools.accept(media='text/plain')
    def PUT(self, id=-1):
        data = cherrypy.request.json
        disco = json.loads(data, object_hook=record)
        res = self.wrp.aggiornaDisco(id)
        if (bool(res)):
            return id;
        else:
            cherrypy.response.status = 404
            return {} 
            

    @cherrypy.tools.json_out()
    def DELETE(self, id=-1):
        index = -1
        for d in range(0, len(self.dischi)) :
            if self.dischi[d]["id"] == int(id):
                index = d
                break
        if index != -1:
            self.dischi.pop(index)
        return 0


#if __name__ == '__main__':
conf = {
    '/': {
        'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
        'tools.sessions.on': True,
        'tools.response_headers.on': True,
        #'tools.response_headers.headers': [('Content-Type', 'application/json')]
        #devo aggiungere l'header "Access-Control-Allow-Origin" per abilitare le richieste da un dominio differente
        'tools.response_headers.headers': [('Content-Type', 'application/json'), ('Access-Control-Allow-Origin', '*')]
    }
}  

cherrypy.quickstart(MyController(), '/dischi', conf)