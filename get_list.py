import json
import requests


def get_json_list(url, token, key):
    request = requests.get(url, headers = {key: token})
    request.raise_for_status()
    return request.json()

if __name__ == '__main__':
    twist_token = "1rj2vRtegS8Y60B3w3qNZm5T2Q0TN2NR"
    twist_moe_url = "https://twist.moe/api/anime/"
    api_key = "X-Access-Token"
    try:
        json_file = get_json_list(twist_moe_url, twist_token, api_key)
        with open('anime_list.json', 'w') as f:
            json.dump(json_file, f)
    except:
        pass
