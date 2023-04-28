import requests
#import json
from requests.auth import HTTPBasicAuth

USR = "Paolo"
PWD = "Password123"

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




url = 'http://127.0.0.1:8080/dischi'
#print("url: " + url)


callGET(1)

callGET()

disco = {
            "id": 5,
            "title": "Duke",
            "artist": "Genesis",
            "year": 1980,
            "company": "A&M"      
        }

callPOST(disco)

callGET()

callDELETE(5)

callGET()
