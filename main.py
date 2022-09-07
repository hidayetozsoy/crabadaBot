import os, platform, sys
from time import sleep
from src.utils.config import PRIVATE_KEYS

MAIN_PATH = os.path.dirname(__file__)

def macCloseTerminals():
    os.system('''killall "Terminal" ''')

def runMacCommand(command):
    os.system( f'''/usr/bin/osascript -e  'tell application "Terminal" to do script with command "{command}"' ''')

def runMacMiner():
    command = f"cd {MAIN_PATH}/src/ && python3 {MAIN_PATH}/src/miner.py"
    runMacCommand(command)

def runMacLooter():
    command = f"cd {MAIN_PATH}/src/ && python3 {MAIN_PATH}/src/looter.py"
    runMacCommand(command)

def runMacMineFinder():
    command = f"cd {MAIN_PATH}/src/ && python3 {MAIN_PATH}/src/mineFinder.py"
    runMacCommand(command)

def runMacAttackers():
    for address in PRIVATE_KEYS.keys():
        command = f"cd {MAIN_PATH}/src/ && python3 attacker.py {address}"
        runMacCommand(command)
        sleep(3)
   
def runWinCommand(command):
    os.system(f'start cmd.exe /k "{command}"')

def runWinMiner():
    command = f"cd {MAIN_PATH}/src/ && python {MAIN_PATH}/src/miner.py"
    runWinCommand(command)

def runWinLooter():
    command = f"cd {MAIN_PATH}/src/ && python {MAIN_PATH}/src/looter.py"
    runWinCommand(command)

def runWinMineFinder():
    command = f"cd {MAIN_PATH}/src/ && python {MAIN_PATH}/src/mineFinder.py"
    runWinCommand(command)

def runWinAttackers():
    for address in PRIVATE_KEYS.keys():
        command = f"cd {MAIN_PATH}/src/ && python attacker.py {address}"
        runWinCommand(command)
        sleep(3)
   
def win():
    runWinMiner()
    sleep(3)
    runWinLooter()
    sleep(3)
    runWinMineFinder()
    sleep(3)
    runWinAttackers()

def mac():
    macCloseTerminals()
    sleep(5)
    runMacMiner()
    sleep(3)
    runMacLooter()
    sleep(3)
    runMacMineFinder()
    sleep(3)
    runMacAttackers()

if __name__ == "__main__":
    if platform.system() == "Darwin":
        mac()
    elif platform.system() == "Windows":
        win() 
    else:
        print("Operating system is not suitable. Please run the app manually")
