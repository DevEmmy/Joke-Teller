import requests

def joke():
    x = requests.get('https://icanhazdadjoke.com/slack')
    response = x.json()

    return response["attachments"][0]["text"]