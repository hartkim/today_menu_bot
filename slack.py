
import slack_sdk

def Msg_bot(slack_messege):  #slack bot massage
    with open('secret','r') as f:
        secret = {l.split('=')[0]: l.split('=')[1].rstrip() for l in f.readlines()}

    token = secret['SLACK_TOKEN'].replace("\'","")
    channel = secret['SLACK_CHANNEL'].replace("\'","")

    slack_token = token   #slack bot token
    channel = channel     #chnnel for sending massege from slack bot
    message = slack_messege     #message from slack bot
    client = slack_sdk.WebClient(token=slack_token)
    client.chat_postMessage(channel=channel, text=message)