import requests
#import json


def callGET(id=None):
    print("***** GET *****")
    if (id == None):
        getUrl = url
    else:
        getUrl = url + "/" + str(id)
    print("url: " + getUrl)
    response = requests.get(getUrl)
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
        headers=headers
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
    response = requests.delete(deleteUrl)
    print("status code: " + str(response.status_code))
    #print(response.content)
    print("***************")
    print("")
    print("")
    print("")




url = 'http://localhost:8080/dischi'
#print("url: " + url)
callGET(1)
callGET()

disco = {
            "title": "Duke",
            "artist": "Genesis",
            "year": 1980,
            "company": "A&M"      
        }

#callGET()
#callPOST(disco)
#callGET()
#callDELETE(5)
#callGET()
