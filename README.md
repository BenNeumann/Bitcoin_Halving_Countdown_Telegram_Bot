# Bitcoin Halving Countdown Telegram Bot
Telgram bot that perform a countdown (with cool gifs) to the bitcoin third halving.

## About the Bot

The bot will check for blockhieght on blockchaininfo API and calculate the amount of blocks until halving.
if there is more than 100 blocks to go until the halving, the bot will send you a reminder every 50 blocks.
if there is less than 100 blocks to go until the halving, the bot will send you a reminder every 10 blocks.
if there is less than 10 blocks to go until the halving, the bot will send you a reminder every block with a nice gif.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine.


### Prerequisites

- you should install python 3 and pip3 (Python Package Installer)
- than install the packages beautiful soup 4 and requests by:


```
pip3 install bs4 requests
```

### Installing

#### create a telegram bot:

1. add the bot father to telegram by clicking the link https://t.me/botfather

2. send the bot father the message - /newbot

3. choose a name for your bot.

4. choose a username for your bot.

5. add your bot to telegram by clicking the reply link from bot father.

6. send your bot the message "hi" or add the bot to your telegram group.

7. copy the api token from bot father reply.

8. found out your group chat id or private chat id by entering the link -<br>
 https://api.telegram.org/botXXX:YYYY/getUpdates
replace XXX:YYYY with your bot token, replace XXX:YYYY with your bot token.

9. Look for “chat”:{“id”:-zzzzzzzzzz,<br>-zzzzzzzzzz is your chat id (with the negative sign) and copy it.

#### deploy the script:

1. clone the repository or download the python script.

2. past you bot token in the python script where it say "token here!!".

3. past you bot chat id or group id where it say "chat id here!!!".

4. run the code with python

```
python3 halvingbot.py
```

## Running the tests
its a simple script so no testing, sorry about that.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

