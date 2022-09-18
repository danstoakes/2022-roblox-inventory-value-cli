import requests
import sys

import src.constant as const
import src.parse_cache as cache
import src.query_helper as helper

def collect(userID, disable_cache):
    if not disable_cache:
        return cache.load(userID)

    nextPageCursor = ""
    query = helper.construct_query(const.INV_ENDPOINT, {
        "userID": userID,
	"nextPageCursor": nextPageCursor
    })

    assets = []
    while (nextPageCursor != None):
        query = helper.construct_query(const.INV_ENDPOINT, {
            "userID": userID, 
            "nextPageCursor": nextPageCursor
        })

        response = requests.get(query)

        if response.status_code == 200:
            responseJSON = response.json()

            nextPageCursor = responseJSON["nextPageCursor"]
            data = responseJSON["data"]
	
            for asset in data:
                assets.append({
                    "id": asset["assetId"],
                    "type": asset["assetType"],
                    "value": 0
                })		
        else:
            sys.exit("Request failed ({0}): {1}".format(response.status_code, response.reason))

    return assets
