import src.constant as const

def construct_query (endpoint, args = {}):
    match (endpoint):
        case const.ECO_ENDPOINT:
            endpoint = const.ECO_ENDPOINT

            return endpoint.format(args["assetID"])
        case const.INV_ENDPOINT:
            cursorString = "&{0}={1}".format("cursor", args["nextPageCursor"]) if args["nextPageCursor"] != "" else ""
            
            return "{0}{1}{2}".format(
                endpoint.format(args["userID"]), 
                "{0}={1}".format("assetTypes", "," . join(const.ASSET_TYPES)), 
                "&{0}&{1}{2}".format("limit=100", "sortOrder=Asc", cursorString)
            )
        case const.MKT_ENDPOINT:
            endpoint = const.MKT_ENDPOINT
            
            return endpoint.format(args["assetID"])
