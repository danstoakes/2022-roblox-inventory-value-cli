import json
import requests
import sys

assetTypes = [
    "Hat",
    "Face",
    "HairAccessory",
    "FaceAccessory",
    "NeckAccessory",
    "ShoulderAccessory",
    "FrontAccessory",
    "BackAccessory",
    "WaistAccessory"
]

nextPageCursor = ""

assetTypesString = "{0}={1}".format("assetTypes", "," . join(assetTypes))
queryEndpoint = "https://inventory.roblox.com/v2/users/16922696/inventory?"

counter = 0
assetIds = []
while (nextPageCursor != None):
    cursorString = "&{0}={1}".format("cursor", nextPageCursor) if nextPageCursor != "" else ""
    queryArgumentsString = "&{0}&{1}{2}".format("limit=100", "sortOrder=Asc", cursorString)
    queryString = "{0}{1}{2}".format(queryEndpoint, assetTypesString, queryArgumentsString)
    
    response = requests.get(queryString)

    match (response.status_code):
        case 400:
            sys.exit("Request failed: bad request")
        case 403:
            sys.exit("Request failed: not authorised")
        case 404:
            sys.exit("Request failed: not found")

    nextPageCursor = response.json()["nextPageCursor"]
    data = response.json()["data"]

    for asset in data:
        assetIds.append({
            "id": asset["assetId"],
            "type": asset["assetType"],
            "value": 0
        })

for assetId in assetIds:
    queryString = "https://economy.roblox.com/v1/assets/{0}/resale-data".format(assetId["id"])

    response = requests.get(queryString)
    responseJson = response.json()

    if "errors" not in responseJson:
        assetIds[assetIds.index(assetId)]["value"] = responseJson["recentAveragePrice"]
    else:
        match (responseJson["errors"][0]["code"]):
            case 0:
                sys.exit("Request failed: bad request")
            case 5:
                assetIds.remove(assetId)

print(assetIds)
        
