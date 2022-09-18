import src.calculate_value as value
import src.collect_inventory as inventory

def calculate(userID, limited_only, disable_cache):
    print(userID)
    print(limited_only)
    print(disable_cache)

    assets = inventory.collect(userID, disable_cache)

    print("Found a total of {0} assets".format(len(assets)))

    assets = value.calculate(assets, limited_only)

    print(assets)
