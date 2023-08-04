from slack_sdk import WebClient, errors

def msg_bot(secret, slack_messege):  #slack bot massage

    slack_token = secret['SLACK_TOKEN'].replace("\'","")
    channel = secret['SLACK_CHANNEL'].replace("\'","")

    message = slack_messege     #message from slack bot
    try:
        client = WebClient(token=slack_token)
        client.chat_postMessage(channel=channel, text=message)
    except errors.SlackApiError as e:
        print(f"Error: {e}")
    