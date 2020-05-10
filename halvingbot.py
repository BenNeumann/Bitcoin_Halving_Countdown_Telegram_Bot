'''
Bitcoin halving telegram bot
'''

# Used for suspending executions.
import time
# Used for sending GET requests.
import requests
# used for html parsing.
from bs4 import BeautifulSoup


# Inputs
BOT_TOKEN = 'HERE'  # token here!!
BOT_CHAT_ID = 'HERE'  # chat id here!!!

#  Gif url's for the last 10 blocks countdown, you can change defult.
GIF_0 = 'https://media.giphy.com/media/JadMjOLosCNJ6/giphy.gif'
GIF_1 = 'https://media.giphy.com/media/H1BPj3Ormiv8yIxNEs/giphy.gif'
GIF_2 = 'https://media.giphy.com/media/3iCzQaHPgm3R1ESesa/giphy.gif'
GIF_3 = 'https://media.giphy.com/media/eexyt55mi2onEOF2rW/giphy.gif'
GIF_4 = 'https://media.giphy.com/media/l378kmO7gdbXaesXS/giphy.gif'
GIF_5 = 'https://media.giphy.com/media/HX3lSnGXZnaWk/giphy.gif'
GIF_6 = 'https://media.giphy.com/media/1pAeTfpHrQphR2hgeZ/giphy.gif'
GIF_7 = 'https://media.giphy.com/media/eHRfGFoEHmgxwBhlsz/giphy.gif'
GIF_8 = 'https://media.giphy.com/media/l3q2tkUqM3SangJj2/giphy.gif'
GIF_9 = 'https://media.giphy.com/media/26gsjCWitFy3euTeM/giphy.gif'
GIF_10 = 'https://media.giphy.com/media/xLQNZswBn8RYk/giphy.gif'

# Some constants.
API = 'https://api.telegram.org/bot'
CON = [API, BOT_TOKEN, BOT_CHAT_ID]
GIF_L = [GIF_0, GIF_1, GIF_2, GIF_3, GIF_4, GIF_5,
         GIF_6, GIF_7, GIF_8, GIF_9, GIF_10]


def main_function(con, gif_l):
    '''
    Main loop.
    '''
    def send_text(con, msg):
        '''
        Function for sending message via telegrams api.
        '''
        phra = ['/sendMessage?&chat_id=', '&parse_mode=Markdown&text=']
        send = con[0] + con[1] + phra[0] + con[2] + phra[1] + msg
        try:
            requests.get(send)
        except:
            print("telegram request error ")

    def send_gif(con, gif, cap):
        '''
        Function for sending gifs.
        '''
        phr = ['/sendAnimation?&chat_id=', '&caption=', '&animation=']
        send = con[0] + con[1] + phr[0] + con[2] + phr[1] + cap + phr[2] + gif
        try:
            requests.get(send)
        except:
            print("telegram requests error ")

    def get_block_count():
        '''
        Function for getting blockheight from blockchain.info's API .
        '''
        try:
            response = requests.get("https://blockchain.info/q/getblockcount")
        except:
            print("requests error ")
        try:
            soup = BeautifulSoup(response.text, 'html.parser')
        except:
            print("BeautifulSoup error ")
        try:
            result = 630000-int(str(soup))
        except:
            print("value error")
            return False
        return result

    # Variables.
    block_count = -1
    pattern = " Blocks to Halving!!!"
    con = con
    gif_l = gif_l

    # Main loop
    while True:
        # Check for block current count
        current = get_block_count()
        # If there is a connection error than sleep for 2 minutes.
        if current is False:
            time.sleep(120)
        # If there is a new block found than assign to variable.
        if block_count != current:
            block_count = current
            # If new block equle to 0 countdown, send halving gif and break .
            if block_count <= 0:
                send_gif(con, gif_l[0], "H-A-L-V-I-N-G!")
                break
            # Else if new block less than 10, send gif from list.
            elif block_count <= 10:
                send_gif(con, gif_l[block_count], str(block_count) + pattern)
                time.sleep(15)
            # Else if new block less than 100, send memo every 10 blocks.
            elif block_count < 100:
                if block_count % 10 == 0:
                    send_text(con, str(block_count) + pattern)
                    time.sleep(120)
            # Else if new block more than 100, end memo every 50 blocks.
            else:
                if block_count % 50 == 0:
                    send_text(con, str(block_count) + pattern)
                    time.sleep(600)


main_function(CON, GIF_L)
