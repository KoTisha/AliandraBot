import json
import config
import requests

M = ''

def Head(r):
    M = r
    saveJson(M)
    inputHandler(M)

def inputHandler(M):
        chat_id = M['message']['chat']['id']
        if 'text' in M['message']:
            message = M['message']['text']
            sendMessage(chat_id, message)
        if 'sticker' in M['message']:
            sticker = M['message']['sticker']['file_id']
            sendSticker(chat_id, sticker)

def saveJson(data, filename='income.json'):
    with open('/home/KoTish/projects/Aliandra/debug/%s' % filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def sendMessage(chat_id, text='Ничо не поняла, но очень интересно :)'):
    url = config.URL + 'sendMessage'
    answer = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, json=answer)
    return r.json()

def sendSticker(chat_id, sticker):
    url = config.URL + 'sendSticker'
    answer = {'chat_id': chat_id, 'sticker': sticker}
    r = requests.post(url, json=answer)
    return r.json()
