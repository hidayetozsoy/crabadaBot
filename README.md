
# Crabada Bot
Fully automatized Bot for Crabada Idle Game.

Crabada is a Play to Earn game on Swimmer (Subnet for Avalanche) Network.

This bot is for Idle part of Crabada. It can loot, mine and reinforce. 

The only thing you need to do is setting your private keys and addresses. 




## Set Up

Firstly, Python3 should be installed on your computer. You can download Python from the link below.

- https://www.python.org/downloads/

- The **web3.py** package should be installed. 

- Open **Terminal** or **Cmd**:

- For Mac:
```
pip3 install web3
```

- For Windows:
```
pip install web3
```

After that, you should set your **private keys and addresses** from **config.py** file which is under **src/utils** directory. You can set addresses as many as you desire.

![Screen Shot 2022-09-07 at 13 12 28](https://user-images.githubusercontent.com/60021484/188853312-2dfb3f6c-3731-4e7d-bb8a-f30bb626aaeb.png)

There is one more step left. We should get your access token.

- Open Google Chrome and go https://idle.crabada.com/

- Right click to screen and click 'Inspect', then select 'Network' from the top bar. 

- Refresh the page.

- Search for **'token?refreshToken'** request in the list at the right side of the page. **Click** it.

![Screen Shot 2022-09-05 at 14 50 18](https://user-images.githubusercontent.com/60021484/188851617-3758df42-c74f-49e4-9721-5e9e1f2318f4.png)


- Copy the value highligted with light blue in this request after **'token?refreshToken'**. As shown in the picture below. This is your access token.

 ![Screen Shot 2022-09-05 at 14 51 08](https://user-images.githubusercontent.com/60021484/188851673-0cdc1909-3a2e-43ce-97fb-f0443987f5dc.png)

- Open **config.py** in the project under **src/utils** directory and paste your access token to **BEARERS** dict.

![Screen Shot 2022-09-07 at 13 09 52](https://user-images.githubusercontent.com/60021484/188852841-34bb9eb8-939d-41e7-9d98-9f99dc8d252d.png)

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
