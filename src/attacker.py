import os, sys
sys.path.append((os.path.dirname(__file__)))
from utils.reserveMine import reserveMine
from utils.mineChooser import chooseMine
from utils.consts import *
from utils.funcs import *
from utils.config import *

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
    getLatestGameAttack(address=ADDRESS, teamId=teamId)

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


