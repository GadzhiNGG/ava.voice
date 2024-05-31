#ДИКАЯ БЕТА!!!!!!!
#ВСЕ НЕПРАВИЛЬНО!!!! НЕ ЮЗАТЬ ЭТОТ КОД!!!!!!!!

import json
import requests
from config.token import conf_token
def stt(speech):
    import json
    import requests

    headers = {"Authorization": conf_token}

    url = "https://api.edenai.run/v2/audio/speech_to_text_async"
    json_payload = {
        "providers": "openai",
        "language": "ru",
        "speech": f'{speech}',
    }

    response = requests.post(url, json=json_payload, headers=headers)

    result = json.loads(response.text)
    print(result)


def main():
    stt(speech="/Users/gadziaskarov/Desktop/пет проекты/ava.voice/1717175827.mp3")

if __name__ == '__main__':
    main()