#classe wrapper
#funzioni di connetti e di disconnetti + varie
#le variabili di istanza sono le 4 variabili per la connetti
#invece la connetti è una variabile di classe 

#importo il modulo 
import pymssql
from pymssql import output
from pymssql import _mssql

class WrapperDB:
    
    conn = 0
    
    #def __init__(self, server="192.168.40.16\\SQLEXPRESS", user="CRD2122",
    #def __init__(self, server="213.140.22.237\\SQLEXPRESS", user="CRD2122",
    #           password="xxx123##", database="CRD2122"):
    def __init__(self, server="localhost\SQLEXPRESS", user="sa", \
               password="Password1!", database="5DINF"):
        self._server=server
        self._user=user
        self._password=password
        self._database=database
        
        
    def connetti(self):
        #connessione
        try:
            WrapperDB.conn = pymssql.connect(server = self._server, user = self._user, \
                        password = self._password, database = self._database)
            #print(f"\nConnessione effettuata! (DB: {self._database})\n")
            return WrapperDB.conn	
        except:
            print(f"\nConnessione NON riuscita! (DB: {self._database})\n")
            return 0
        
            
    def disconnetti(self, co):
        #disconnessione	
        try:
            co.close()
            #print(f"\nCHIUSURA connessione! (DB: {self._database})\n") 
        except:
            print(f"\nCHIUSURA connessione NON riuscita! (DB: {self._database})\n")
            return 0
        

    def elencoDischi(self, as_dict = False):
        #restituisce una lista di tuple se as_dict = False
        #altrimenti restituisce una lista di coppie chiave/valore (dictionary)
        conn = self.connetti()
        lista = []
        try:
            cur = conn.cursor(as_dict = as_dict)
            sql = "SELECT Id, Artist, Title, [Year], Company FROM PC_Records"
            cur.execute(sql)
            lista = cur.fetchall()
        except:
            err = "Houston abbiamo un problema..."
            print(f"[elencoPost] {err}")
        self.disconnetti(conn)
        return lista

    
    def singoloDisco(self, id):
        #restituisce un singolo post
        ret = {}
        conn = self.connetti()
        try:
            cursore = conn.cursor(as_dict = True)
            sql = f"""
                SELECT Id, Artist, Title, [Year], Company 
                FROM PC_Records 
                WHERE id = {id}   
                """
            cursore.execute(sql)
            ret = cursore.fetchone()
        except:
            err = "Houston abbiamo un problema..."
            print(f"[singoloPost] {err}")
        self.disconnetti(conn)
        return ret    

    
    #def inserisciPost(self, autore, testo):
    def inserisciDisco(self, parametri):
        #inserisce un nuovo post
        #parametri: (autore, testo)
        try:
            c = self.connetti() 
            cursore = c.cursor()
            sql = "INSERT INTO PC_Records (Artist, Title, Year, Compant) VALUES (%s , %s, %d, %s)"
            cursore.execute(sql, parametri)
            c.commit()
            #print("INSERIMENTO DISCO AVVENUTO")
            self.disconnetti(c)
            return True            
        except:
            #print("\INSERIMENTO DISCO/i: Si sono verificati degli errori!")
            self.disconnetti(c)
            return False


    def inserisciDiscoSP(self, parametri):
        #inserisce un nuovo post
        #parametri: (autore, testo)
        try:
            #dichiaro id come valore di output per la SP
            id = output(int)
            #aggiungo id ai parametri
            parametri = parametri + (id,)
            c = self.connetti() 
            cursore = c.cursor()
            res = cursore.callproc('dbo.PC_InserisciDisco', parametri)
            c.commit()
            #print("INSERIMENTO DISCO AVVENUTO")
            #return True            
            return res[4]
        except _mssql.MssqlDatabaseException as e:
            print("A MSSQLDatabaseException has been caught.")
            print('Number = ',e.number)
            print('Severity = ',e.severity)
            print('State = ',e.state)
            print('Message = ',e.message)
            return -1
        except Exception as err:
            #print("\INSERIMENTO DISCO/i: Si sono verificati degli errori!")
            print(str(err))
            self.disconnetti(c)
            #return False
            return -1

    def eliminaDisco(self, id):
        #elimina un post
        try:
            c = self.connetti() 
            cursore = c.cursor()
            sql = "DELETE PC_Recordsss WHERE id = %d"
            cursore.execute(sql, id)
            c.commit()
            #print("ELIMINA DISCO AVVENUTO")
            self.disconnetti(c)
            return True            
            
        except:
            #print("\ELIMINA DISCO/i: Si sono verificati degli errori!")
            self.disconnetti(c)
            return False

    


	    