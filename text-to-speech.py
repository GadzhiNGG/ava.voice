import json
import requests
import os
import time

from config.token import conf_token #сам токен, который нужно взять на сайте Eden AI
def tts(text): # функция самого произношения
    headers = {"Authorization": conf_token} #см. строку 6

    url = "https://api.edenai.run/v2/audio/text_to_speech" #ссылка откуда будем брать
    payload = {
            "providers": "openai", "language": "ru",
            "option": "MALE",
            "text": f'{text}'
    }

    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    x_time = int(time.time())

    # with open(f'/Users/gadziaskarov/Desktop/пет проекты/ava.voice/audios/{x_time}.json', 'w') as file:
    #     json.dump(result, file)

    audio_url = result.get('openai').get('audio_resource_url')
    r = requests.get(audio_url)

    with open(f'/Users/gadziaskarov/Desktop/пет проекты/ava.voice/audios/{x_time}.mp3', 'wb') as file:
        file.write(r.content)

def main():
    tts(text='Привет! Как твои дела?')


if __name__ == '__main__':
    main()