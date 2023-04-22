import requests
import json


token = '642fed5a96d7e642fed5a96d81'


def get_depot_info():
    '''
    Отчет об имеющемся кол-ве уникальных цветов и общем кол-ве краски
    '''
    url = 'http://api.datsart.dats.team/art/colors/info'
    headers = {
            "Authorization": f"Bearer {token}",
            'Content-Length': '',
            "Content-Type": "multipart/form-data; boundary="
            "----WebKitFormBoundary7MA4YWxkTrZu0gW"
        }
    body = '------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n'
    headers['Content-Length'] = str(len(body))
    ans = requests.post(url, headers=headers, data=body)
    if ans.status_code == 200:
        ans = json.loads(ans.text)
    else:
        print(ans)
        print(ans.text)
    return ans


def get_paint_remains(color):
    '''
    Запрос остатков краски
    '''
    url = 'http://api.datsart.dats.team/art/colors/amount'
    headers = {
            "Authorization": f"Bearer {token}",
            'Content-Type': 'application/x-www-form-urlencoded',
        }
    body = {'color': color}
    ans = requests.post(url, headers=headers, data=body)
    if ans.status_code == 200:
        ans = json.loads(ans.text)
    else:
        print(ans)
        print(ans.text)
    return ans


def get_all_paints_remains_list():
    url = 'http://api.datsart.dats.team/art/colors/list'
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


if __name__ == '__main__':
    print(get_all_paints_remains_list())