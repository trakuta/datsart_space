import requests
import json


token = '642fed5a96d7e642fed5a96d81'


def get_tick():
    url = 'http://api.datsart.dats.team/art/state/tick'
    headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "multipart/form-data; boundary="
            "----WebKitFormBoundary7MA4YWxkTrZu0gW"
        }
    body = '----WebKitFormBoundary7MA4YWxkTrZu0gW\r\n'
    headers['Content-Length'] = str(len(body))
    ans = requests.post(url, headers=headers, data=body)
    if ans.status_code == 200:
        ans = json.loads(ans.text)
    return ans


def get_queue(id_):
    url = 'http://api.datsart.dats.team/art/state/queue'
    headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "multipart/form-data; boundary="
            "----WebKitFormBoundary7MA4YWxkTrZu0gW"
    }
    body = ('------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n'
            'Content-Disposition: form-data; name="id"\r\n'
            f'\r\n{id_}\r\n'
            '------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n'
    )

    headers['Content-Length'] = str(len(body))
    ans = requests.post(url, headers=headers, data=body)
    if ans.status_code == 200:
        ans = json.loads(ans.text)
    return ans
