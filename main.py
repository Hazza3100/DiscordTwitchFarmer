import time
import json
import requests


with open('config.json') as f:
    cfg = json.load(f)
    token = cfg['token']
    channelID = cfg['channel_id']
    message = cfg['message']


def count_down(times):
    while times:
        minutes, seconds = divmod(times, 60)
        timer = '{:02d}:{:02d}'.format(minutes, seconds) # from somewhere
        print(f"Time Until Next Message > {timer}")
        time.sleep(1)
        times -= 1 
    print('Sent message!')



count = int(input("How often to send the message (Seconds)>  "))


def do():
    headers = {
        'authority': 'discord.com','accept': '*/*','accept-language': 'en-GB,en-US;q=0.9,en;q=0.8','authorization': token,'origin': 'https://discord.com','referer': f'https://discord.com/channels/@me/{channelID}','sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36','x-debug-options': 'bugReporterEnabled','x-discord-locale': 'en-GB','x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLUdCIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNS4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA1LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL3d3dy5nb29nbGUuY29tLyIsInJlZmVycmluZ19kb21haW4iOiJ3d3cuZ29vZ2xlLmNvbSIsInNlYXJjaF9lbmdpbmUiOiJnb29nbGUiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTQ4ODg4LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',}

    json_ = {
        'content': message,
        'tts': False,
    }

    r = requests.post(f'https://discord.com/api/v9/channels/{channelID}/messages', headers=headers, json=json_)
    print(r.text)


while True:
    do()
    count_down(count)