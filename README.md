
# Crabada Bot
Fully automatized Bot for Crabada Idle Game.

Crabada is a Play to Earn game on Swimmer (Subnet for Avalanche) Network.

This bot is for Idle part of Crabada. It can loot, mine and reinforce. 

The only thing you need to do is setting your private keys and addresses. 




## Set Up

Firstly, Python3 should be installed on your computer. You can download Python from the link below.

https://www.python.org/downloads/

The **web3.py** package should be installed. 

Open **Terminal** or **Cmd**:

For Mac:
```
pip3 install web3
```

For Windows:
```
pip install web3
```

After that, you should set your **private keys and addresses** from **config.py** file which is under **src/utils** directory.

There is one more step left. We should get your access token.

Open Google Chrome and go https://idle.crabada.com/

Right click to screen and click 'Inspect', then select 'Network' from the top bar. 

Refresh the page.

Search for **'token?refreshToken'** request in the list at the right side of the page. **Click** it.

resim

Copy the value in this request after 'token?refreshToken'. As shown in the picture below. This is your access token.

resim 

Open **config.py** in the project and paste your access token to **BEARERS** dict.

It should be seen like below. 

resim
## How it works

- **main.py** is for running all programs on different terminal windows. If there is a problem with main.py or you don't want to run it, you can run programs manually.

- **src**
    - **attacker.py** is runned individually for every address. If you have 3 addresses, 3 attacker.py should be runned. Takes 1 flag as the address. 
    - **looter.py** is for checking open loots. If there is an open loot, it takes care of the loot. Reinforces and settles the game. There should be just 1 **looter.py** running. All the addresses is checked from 1 app.
    - **mineFinder.py** is for finding mines to loot. It searches for suitable mines and opponents who didn't reinforced their last mine. Mines are saved to **attackableWithHistory.json** and **attackable.json**. Option for number of last mines that opponent didn't reinforce can be changed through **config.py** file.
    - **miner.py** is for checking open mines. Starts mines when team's looting point is 0. Reinforces if needed. Just 1 **miner.py** is used for all addresses, like **looter.py**.
    - **utils**
        - **attackable.json** and **attackableWithHistory.json** is used to save suitable mines. **attackableWithHistory** keeps the mines whose owner didn't reinforce last mine.
        - **config.py** is where you will set your addresses, private keys, bearers, and other options about transactions.
        - **mineChooser.py** chooses a suitable mine from data. First looks **attackableWithHistory.json** for non-reinforced mines, if there is suitable mine, chooses it. If not, looks at **attackable.json**.
        - **reserveMine.py** sends PUT request to reserve a mine for given team.