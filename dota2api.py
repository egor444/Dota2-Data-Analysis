import json

import requests

STEAMID = "76561198085227187"
STEAMID32 = 124961459

class URLBuilder():
    """
        This class builds the url for an API request,
        based on request type and parameters.
        The URL is build based on the following structure:
        http://api.steampowered.com/<IType>_570/<RequestType>/v1?key=<APIKey>&<OtherParameters>

        For further information visit the TF wiki:
        https://wiki.teamfortress.com/wiki/WebAPI#Dota_2
    """

    baseurl = "http://api.steampowered.com/"
    gameID = "570"
    reqType = ""
    key = ""
    params = {"key": key}
    itype = "IDOTA2Match"

    def __init__(self):
        # Read the private API key
        with open("private/steam_data.txt","r") as f:
            self.key = f.readline().lower()
        self.params["key"] = self.key

    def set_IType(self,itype):
        self.itype = itype
        return self

    def setReqestType(self, type):
        self.reqType = type
        return self

    def addParameter(self, param, argument):
        self.params[param]= argument
        return self

    def getURL(self):
        outURL = f"{self.baseurl}{self.itype}_{self.gameID}/{self.reqType}/v1?"
        for par, val in self.params.items():
            outURL += f"&{par}={val}"
        return outURL

    def __str__(self):
        return self.getURL()

def get_win_by_match(matchID):
    """ Weird helper function (unused). Returns if radiant won a match.
    Args:
        matchID (int): ID of the match.
    Returns:
        bool: True if radiant won this match, False otherwise.
    """
    url = URLBuilder().setReqestType("GetMatchDetails").addParameter("match_id",matchID)
    response = requests.get(url).json()
    win  = response["result"]["radiant_win"]
    return win

def fetch_match_by_id(match_id):
    """Fetches a match from the API and returns the information as a JSON object.
    Args:
       match_id (int): ID of the match.
    Returns:
        json: The match information as json.
    """
    url = URLBuilder().setReqestType("GetMatchDetails").addParameter("match_id",match_id)
    result = requests.get(url).json()["result"]
    return result

def jprint(obj):
    """
    ✦ Fancier ✦ way to print a json object. (With indents and everything)
    """
    print(json.dumps(obj, indent=4))



#### The following code is cancerous in nature and was used for multiple purposes,
#### which is why a lot of it is commented out. Use at own risk.



lossList = {}
for i in range(1,139):
    lossList[i] = 0

def get_losses_from_match(match):
    # Idk
    players = match["players"]
    matchID = match["match_id"]
    radiantWin = get_win_by_match(matchID)
    myTeam = -1
    win = False
    for player in players:
        if player["account_id"] == STEAMID32:
            myTeam = player["team_number"]
            win = (radiantWin and myTeam == 0) or not radiantWin and myTeam == 1
    if not win:
        for player in players:
            if player["team_number"] != myTeam:
                lossList[player["hero_id"]] += 1


matches = []


#getHeroesURL = URLBuilder().setReqestType("GetHeroes").set_IType("IEconDOTA2")
getItemsURL = URLBuilder().setReqestType("GetGameItems").set_IType("IEconDOTA2")

#matchHistoryURL = URLBuilder().setReqestType("GetMatchHistory").addParameter("account_id",
#    STEAMID).addParameter("matches_requested",100)

result = requests.get(getItemsURL)#.json()["result"]
print(getItemsURL)
#with open("data/items.json","x") as f:
#    json.dump(matches, f, indent=4)


#result = requests.get(matchHistoryURL).json()["result"]
#
#matches_list = result["matches"]
#
#for m in matches_list:
#    m_id = m["match_id"]
#    match_data = fetch_match_by_id(m_id)
#    matches.append(match_data)
#
#with open("data/match_data.json","w") as f:
#    json.dump(matches, f)
#    #f.write(matches)

# for match in matches:
#     getLossesFromMatch(match)
#
# newlosses = lossList.copy()
# for k, v in lossList.items():
#     if v == 0:
#         newlosses.pop(k)
# sortedLosses = sorted(newlosses.items(), key=lambda x:x[1], reverse=True)
#
# with open("heroeIDList.txt","r") as f:
#     data = f.read()
#     heroList = json.loads(data)
#
# for loss in sortedLosses:
#     lossI = loss[0]
#     hero = list(heroList.keys())[list(heroList.values()).index(lossI)]
#     print(f"{hero}: {loss[1]}")

