import requests
import time

import src.constant as const
import src.query_helper as helper

def retry_timer (t):
    while t:
        minutes, seconds = divmod(t, 60)
        print("Retrying in {:02d}:{:02d}".format(minutes, seconds), end="\r")
        time.sleep(1)
        t -= 1

def get_non_limited_asset_value(assetID):
    query = helper.construct_query(const.MKT_ENDPOINT, {
        "assetID": assetID,
    })

    response = requests.get(query)
    responseJSON = response.json()

    if "errors" not in responseJSON:
        return responseJSON["PriceInRobux"]
    else:
        sys.exit("Request failed: ({0}): {1}".format(responseJSON["errors"]["code"], responseJSON["errors"]["message"]))
    

def calculate(assets, limited_only, currentAssetIndex = 1):
    pricedAssets = []
    while (currentAssetIndex < len(assets)):
        asset = assets[currentAssetIndex]
    
        query = helper.construct_query(const.ECO_ENDPOINT, {
            "assetID": asset["id"],
           })

        response = requests.get(query)
        responseJSON = response.json()

        if "errors" not in responseJSON:
            asset["value"] = responseJSON["recentAveragePrice"]
            pricedAssets.append(asset)
            currentAssetIndex += 1
        else:
            match (responseJSON["errors"][0]["code"]):
                case 0:
                    if responseJSON["errors"][0]["message"] == "TooManyRequests":
                        print("Hit API request limit at index {0} for: {1}".format(currentAssetIndex, query))
                        retry_timer(30)
                    else:
                        sys.exit("Request failed: ({0})".format(responseJSON["errors"][0]["message"]))
                case 5:
                    if not limited_only:
                        asset["value"] = get_non_limited_asset_value(asset["id"])
                        pricedAssets.append(asset)
                        currentAssetIndex += 1

    return pricedAssets
