import os, sys, requests
sys.path.append(os.getcwd() + '/utils')
from utils.reserveMine import reserveMine
from utils.mineChooser import chooseMine
from utils.consts import *
from utils.funcs import *
from utils.config import *

def getTeamsInfo():
    availableTeamsUrl = f"https://idle-game-api.crabada.com/public/idle/teams?user_address={ADDRESS}&is_team_available=1"
    teamsData = requests.get(availableTeamsUrl, headers=HEADERS, timeout=10).json()["result"]["data"]
    if teamsData is None:
        return False
    teamsInfo = dict()
    for team in teamsData :
        if team["looting_point"] > 0:
            teamId = team["team_id"]
            attackFaction, attackPoint = team["faction"], team["battle_point"]
            teamsInfo[teamId] = {"faction": attackFaction, "attackPoint": attackPoint}
    return teamsInfo

def getLatestGameAttack(teamId):
    teamsUrl = f"https://idle-game-api.crabada.com/public/idle/teams?user_address={ADDRESS}&page=1&limit=10"
    teams = requests.get(teamsUrl, headers=HEADERS, timeout=10).json()["result"]["data"]
    for team in teams:
        if team["team_id"] == teamId:
            latestGameAttack = team["latest_game_attack"]
            sendAttackTx(address=ADDRESS, game=latestGameAttack)

def attack(teamsInfo):
    try:
        selectedMine = chooseMine(teamsInfo, data="WithHistory")
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        printn(exc_type, f"line:{exc_tb.tb_lineno}")
        sleepy(120)
        return 
    if not selectedMine:
        selectedMine = chooseMine(teamsInfo, data="")
        if not selectedMine:
            sleepy(30)
            return
    mineId, teamId = selectedMine[0], selectedMine[1]
    accessToken = getAccessToken(ADDRESS)
    reserveMine(accessToken, mineId, teamId)
    printn("mine reserved...")
    sleepy(10)
    getLatestGameAttack(teamId)

def main(address):
    global ADDRESS
    ADDRESS = address
    while True:
        try:
            teamsInfo = getTeamsInfo()
            if not teamsInfo:
                printn("no available team...")
                sleepy(60)
                continue
            attack(teamsInfo)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            printn(exc_type, fname, f"line:{exc_tb.tb_lineno}")
            printn(e.__class__)
            sleepy(120)

if __name__ == "__main__":
    main(sys.argv[1])


