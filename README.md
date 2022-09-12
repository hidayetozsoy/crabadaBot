
# Crabada Idle Game Bot
Fully automatized Bot for Crabada Idle Game.

Crabada is a Play to Earn game on Swimmer (Subnet for Avalanche) Network.

This bot is for Idle part of Crabada. It can loot, mine and reinforce. 

The only thing you need to do is setting your private keys, addresses, and access tokens. 

## Set Up

 1. [Install Python](#install-python)
 2. [Get Your Address](#get-your-address)
 3. [Get Your Private Key](#get-your-private-key)
 4. [Set Addresses and Private Keys](#set-addresses-and-private-keys)
 5. [Get Your Access Token](#get-your-access-token)
 6. [Set Access Token](#set-access-token)
 7. [Run Program](#run-program)
 8. [How It Works](#how-it-works)
 
### Install Python

Firstly, Python3 should be installed on your computer. You can download Python from the link below.

- https://www.python.org/downloads/

Then **web3.py** package should be installed. 

- Open **Terminal** or **Cmd**:

- For Mac:
`pip3 install web3`


- For Windows:
`pip install web3`

### Get Your Address
- Open **Metamask** extension

- Click to the shown area. Your address will be copied to clipboard.

<img width="405" alt="Screen Shot 2022-09-12 at 11 21 46" src="https://user-images.githubusercontent.com/60021484/189613923-2d75d3a9-79d1-4d0e-a3ee-aeee7d0dfaaa.png">

### Get Your Private Key
- Open **Metamask** extension.

- Click **three dots** on the top right.

- Click **Account Details**.

- Click **Export Private Key**.

- Write your **Metamask password** to the area and click **Confirm**. You will see your private key.

- Copy your **private key**.
- Wait for GIF below.

![howToGetPrivateKey](https://user-images.githubusercontent.com/60021484/189709264-af5cb80f-b286-4d10-9720-f3bd27db6f59.gif)

### Set Addresses and Private Keys
- Open config.py under **src/utils** directory. You can use Visual Studio Code to edit the code, or Notepad will be useful.

- Put your addresses to the left side. Private keys should be put to the right side like below.

![Screen Shot 2022-09-12 at 19 15 12](https://user-images.githubusercontent.com/60021484/189705382-130065e0-ad06-4940-acea-a7cf8496bc83.png)

- If you want to add multiple addresses, you should put comma (,) end of every line.

### Get Your Access Token

- Open Google Chrome and go https://idle.crabada.com/

- Connect your wallet.

- Right click to screen and click 'Inspect'.

-<img width="711" alt="Screen Shot 2022-09-12 at 12 54 10" src="https://user-images.githubusercontent.com/60021484/189625811-215c98b0-6bee-4fc2-a0c2-6db27906ae36.png">

- Select 'Network' from the top bar. 

<img width="1440" alt="Screen Shot 2022-09-12 at 12 55 17" src="https://user-images.githubusercontent.com/60021484/189625878-ade631d0-b5ae-45a1-8ae9-93120cf3963e.png">

- **Refresh** the page.

- Look for **'token?refreshToken'** request in the list at the right side of the page. **Click** it.

![Screen Shot 2022-09-05 at 14 50 18](https://user-images.githubusercontent.com/60021484/188851617-3758df42-c74f-49e4-9721-5e9e1f2318f4.png)

- Copy the value highligted with light blue in this request after **'token?refreshToken'**. As shown in the picture below. This is your access token. It usually starts with "eyJhb"...

![Screen Shot 2022-09-05 at 14 51 08](https://user-images.githubusercontent.com/60021484/189710649-7cdac7ac-06bb-4ddf-b9c1-fb15c9520ad8.png)

### Set Access Token

- Open **config.py** in the project under **src/utils** directory and paste your access token in **ACCESS_TOKENS** dict next to your address.

![Screen Shot 2022-09-12 at 19 17 42](https://user-images.githubusercontent.com/60021484/189705432-d873ae80-932d-4719-9993-3fb62263abb5.png)

### Run program

- Open terminal in program's directory.

- For Mac

  ```python3 main.py```

- For Windows

  ```python main.py```

## How it works

- **main.py** is for running all programs on different terminal windows. If there is a problem with main.py or you don't want to run it, you can run programs manually.

- **src**
    - **attacker.py** is runned individually for every address. If you have 3 addresses, 3 attacker.py should be runned. Takes 1 parameter as the address. 
    - **looter.py** is for checking open loots. If there is an open loot, it takes care of the loot. Reinforces and settles the game. There should be just 1 **looter.py** running. All the addresses is checked from 1 app.
    - **mineFinder.py** is for finding mines to loot. It searches for suitable mines and opponents who didn't reinforced their last mine. Mines are saved to **attackableWithHistory.json** and **attackable.json**. Option for number of last mines that opponent didn't reinforce can be changed through **config.py** file.
    - **miner.py** is for checking open mines. Starts mines when team's looting point is 0. Reinforces if needed. Just 1 **miner.py** is used for all addresses, like **looter.py**.
    - **utils**
        - **attackable.json** and **attackableWithHistory.json** is used to save suitable mines. **attackableWithHistory** keeps the mines whose owner didn't reinforce last mine.
        - **config.py** is where you will set your addresses, private keys, access tokens, and other options about transactions.
        - **mineChooser.py** chooses a suitable mine from data. First looks **attackableWithHistory.json** for non-reinforced mines, if there is suitable mine, chooses it. If not, looks at **attackable.json**.
        - **reserveMine.py** sends PUT request to reserve a mine for given team.
