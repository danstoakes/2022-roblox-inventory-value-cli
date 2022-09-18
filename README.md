# 2022-roblox-inventory-value-calculator
Works for Limited and Limited Unique items. (unfinished)

To do: Turn into a package. Use cache file for loading automatically. Can do a quick api call to get user inventory on load, strip ids and check if any are missing from the file (i.e. items sold) or if any ids are not in the file (i.e. items purchased). Also can utilise flags for user id, etc.

Need to check the tool when the user isn't logged in anywhere. may actually require http headers for authentication.

Need to start using the price history feature for the economy api, then can have a running tally for value over months for comparison.
