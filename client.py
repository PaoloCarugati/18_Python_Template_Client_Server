import requests
from requests.auth import HTTPBasicAuth

#questi devono essere uguali a quelli del server :-)
USR = "NOME_UTENTE"
PWD = "PASSWORD"

basicauth = HTTPBasicAuth(USR, PWD)


def callGET(id=None):
    print("***** GET *****")
    if (id == None):
        getUrl = url
    else:
        getUrl = url + "/" + str(id)
    print("url: " + getUrl)
    response = requests.get(getUrl, auth=basicauth)
    print("status code: " + str(response.status_code))
    #print(response.content)
    json = response.json()
    print("response content:")
    print(json)
    print("***************")
    print("")
    print("")
    print("")


def callPOST(disco):
    print("***** POST *****")
    print("url: " + url)

    headers={
        'Content-type':'application/json', 
        'Accept':'application/json'
    }

    response = requests.post(
        url, 
        json=disco,
        headers=headers, 
        auth=basicauth
    )
    print("status code: " + str(response.status_code))
    #print("response content:")
    #print(response.content)
    print("***************")
    print("")
    print("")
    print("")

    
def callPUT(record):
    print("***** POST *****")
    print("url: " + url)

    headers={
        'Content-type':'application/json', 
        'Accept':'application/json'
    }

    response = requests.put(
        url, 
        json=record,
        headers=headers, 
        auth=basicauth
    )
    print("status code: " + str(response.status_code))
    #print("response content:")
    #print(response.content)
    print("***************")
    print("")
    print("")
    print("")    

"""
#utilizza questa se nella PUT del server hai definito il parametro id
def callPUT(record, id):
    print("***** POST *****")
    putUrl = url + "/" + str(id)
    print("url: " + putUrl)

    headers={
        'Content-type':'application/json', 
        'Accept':'application/json'
    }

    response = requests.put(
        putUrl, 
        json=record,
        headers=headers, 
        auth=basicauth
    )
    print("status code: " + str(response.status_code))
    #print("response content:")
    #print(response.content)
    print("***************")
    print("")
    print("")
    print("")    
"""
    
    
def callDELETE(id):
    print("***** DELETE *****")
    deleteUrl = url + "/" + str(id)
    print("url: " + deleteUrl)
    response = requests.delete(deleteUrl, auth=basicauth)
    print("status code: " + str(response.status_code))
    #print(response.content)
    print("***************")
    print("")
    print("")
    print("")




#url = 'http://127.0.0.1:8080/qualcosa'
url = 'http://127.0.0.1:8080'



