import requests
import json


token = '642fed5a96d7e642fed5a96d81'


def shoot(power: str, colors: dict, angleHorizontal=0, angleVertical=45):
    url = 'http://api.datsart.dats.team/art/ballista/shoot'
    headers = {
            "Authorization": f"Bearer {token}",
            'Content-Length': '',
            "Content-Type": "multipart/form-data; boundary="
            "----WebKitFormBoundary7MA4YWxkTrZu0gW"
        }
    body = ('------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n'
            'Content-Disposition: form-data; name="angleHorizontal"\r\n'
            f'\r\n{angleHorizontal}\r\n'
            '------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n'
            'Content-Disposition: form-data; name="angleVertical"\r\n'
            f'\r\n{angleVertical}\r\n'
            '------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n'
            'Content-Disposition: form-data; name="power"\r\n'
            f'\r\n{power}\r\n'
            )
    body_colors = []
    for color in colors:
        s = (f'Content-Disposition: form-data; name="colors[{color}]"\r\n'
            f'\r\n{colors[color]}\r\n'
            '------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n'
        )
    body = f"{body}{''.join(body_colors)}"

    headers['Content-Length'] = str(len(body))
    print(body)
    ans = requests.post(url, headers=headers, data=body)
    if ans.status_code == 200:
        ans = json.loads(ans.text)
    else:
        print(ans.text)
    return ans
